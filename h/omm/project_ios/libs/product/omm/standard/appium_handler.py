"""
This module for dealing all things related appium driver and server.
"""
import os
from appium import webdriver
import subprocess
from subprocess import Popen
import re
import time
import traceback
import platform

from libs.product.omm.standard import util
from libs.product.omm.standard import global_vars
from libs.product.omm.standard import omm_lib

omm_obj_repo_path = global_vars.obj_repo_path



class appium_handler():

    def __init__(self):

        'Initializing variables used in this class'
        self.driver = None
        self.app_process = None
        self.device_id = ""

        'Getting platform of execution. Android or ios'
        self.platform = global_vars.platform

        'Getting android attributes from global vars file'
        self.android_buildFile_name = global_vars.android_buildFile_name
        self.android_sdk_path = global_vars.apk_path + global_vars.android_buildFile_name
        self.app_package = global_vars.app_package
        self.app_activity = global_vars.app_activity
        self.server_address = global_vars.server_address

        'Fetch IOS attributes from global vars'
        self.ios_buildFile_name = global_vars.ios_buildFile_name
        self.ios_sdk_path = global_vars.ipa_path + global_vars.ios_buildFile_name

        'Fetch object repository only when it is empty. One time fetch in case of multiple executions'
        if global_vars.object_repository == {}:
            global_vars.object_repository = omm_lib.get_omm_obj_repository()

        'Fetch test case specific input'
        if global_vars.tc_verfn_dict == {}:
            global_vars.tc_verfn_dict = omm_lib.get_testcase_verification_dict()

        'Fetch android version only if value is None. This allows one time' 
        'fetching in case of multiple test case executions'

        if self.platform.lower() == "android":
            'Fetch android version only if value is None. This allows one time' 
            'fetching in case of multiple test case executions'

            if global_vars.android_version == None:
                global_vars.android_version = omm_lib.get_android_version()

            'Fetch android device id only if value is None. This allows one time'
            'fetching in case of multiple test case executions'

            if global_vars.android_device_id == None:
                global_vars.android_device_id = omm_lib.get_android_device_id()

        elif str(self.platform).lower() == "ios":
            if global_vars.udid == None:
                global_vars.udid = omm_lib.get_ios_udid()
                print "global vars udid is %s" % global_vars.udid

    def start_driver(self,is_auto_accept_alerts =False):
        """
        This function is used for starting appium driver

        Function Owner : Nithya_V

        Date created : 20/04/2016

        @param  install : (bool) True if installation is required

        @return flag : (bool)status of execution.if successful True else False
        """
        msg = ""
        try:
            platform = str(self.platform).lower()
            desired_caps = {}
            print "#####===== Platform is %s =========#####\n" % platform
            if not platform in ["android", "ios"]:
                return False, "Given Unsupported Platform : %s" % platform

            if platform == "android":
                desired_caps = {}
                desired_caps['platformName'] = 'Android'
                desired_caps['platformVersion'] = global_vars.android_version
                desired_caps['deviceName'] = global_vars.android_device_id
                desired_caps['udid'] = global_vars.android_device_id
                # desired_caps['udid'] = global_vars.android_device_id
                # desired_caps['udid']= '1b5f6849c4213f6d'
                desired_caps['unicodekeyboard'] = True
                desired_caps['resetkeyboard'] = True
#               desired_caps['autoAcceptAlerts'] = True
                desired_caps['autoAcceptAlerts'] = is_auto_accept_alerts

                # Returns abs path relative to this file and not cwd
                desired_caps['app'] = os.path.join(os.getcwd(),self.android_sdk_path)
                desired_caps['appPackage'] = global_vars.app_package
                desired_caps['appActivity'] = global_vars.app_activity

            elif platform == "ios":
                desired_caps['platformName'] = 'Ios'

                desired_caps['deviceName'] = 'iPhone'
                desired_caps['app'] = os.path.join(os.getcwd(), self.ios_sdk_path)

                desired_caps['bundleid'] = global_vars.bundleid
                desired_caps['udid'] = global_vars.udid

                desired_caps['unicodekeyboard'] = True
                desired_caps['resetkeyboard'] = True

                desired_caps['autoAcceptAlerts'] = is_auto_accept_alerts

            print "#####===== Desired Caps is %s =====#####\n" % desired_caps

            # starting the appium server
            status, msg = self.start_appium_server()
            if not status:
                print "Appium server has not been started successfully"
                return False, msg

            # initializing the driver
            driver = webdriver.Remote(self.server_address, desired_caps)
            self.driver = driver

            # passing driver variable to global vars module
            global_vars.driver = driver
            print "Driver started successfully"
        except Exception as excp:
            traceback.print_exc()
            msg += "\n%s" % str(excp)
            return False, msg
        return True, msg
    def start_appium_server(self):
        """
        This function is used for starting appium server

        Function Owner : Nithya_V

        Date created : 20/04/2016

        @return flag : (bool)status of execution.if successful True else False
        @return msg : (string) msg in case of any exception
        """
        msg = ""
        try:
            'Creating appium server log file dynamically on each execution'
            appium_svr_log_file = "appium_server_logs_%s.txt" % util.uniqueID()
            appium_log_file = global_vars.appium_log_file_path + appium_svr_log_file

            'Removing the file if same file exists'
            if os.path.exists(appium_log_file):
                os.remove(appium_log_file)
            print "Appium server logs has been saved to logs file - %s" % \
                re.search("appium_server_logs_\d+", appium_log_file, re.I).group(0).strip()

            'Checking whether system running on MAC OS (Darwin) or not'
            print "Platform for execution is %s" % str(platform.system())
            if str(platform.system()) in ['Darwin']:
                print "\n###### Platform for execution is %s ######\n" % str(platform.system())
                cmd, output = global_vars.ios_appServer_start_cmd + appium_svr_log_file, ""
                popen = Popen([cmd], 
                              shell=True,
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE
                              )
            elif str(platform.system()) == 'Windows': #Start appium if OS is windows'
                cmd, output = global_vars.android_appServer_start_cmd + appium_svr_log_file, ""
                popen = Popen(cmd, stdout=subprocess.PIPE)
            else:
                print "OS not supported for execution"
                return None, msg
            self.app_process = popen
            time.sleep(15)
            for line in iter(popen.stdout.readline, b""):
                output += str(line)
                if str(line).__contains__('Console LogLevel: debug'):
                    print "Appium server has started successfully\n"
                    break
                elif str(line).lower().__contains__('error'):
                    print "Error in starting appium server"
                    break
            return popen, output
        except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            return None, msg
        return True, msg

    def stop_appium_server(self):
        """
        This function is used for stopping appium server

        Function Owner : Nithya_V

        Date created : 20/04/2016

        @return flag : (bool)status of execution.if successful True else False
        """
        try:
            self.app_process.kill()
            print "Appium server has been terminated\n"
        except:
            traceback.print_exc()
            return False
        return True
        
    def quit_driver(self, stopServer=True):
        """
        This function is used for quiting appium driver

        Function Owner : Nithya_V

        Date created : 20/04/2016

        @return flag : (bool)status of execution.if successful True else False
        @return msg : (string) msg in case of any exception
        """
        msg = ""
        try:
            # closing the OMM app
            self.driver.close_app()

            # exiting the driver
            self.driver.quit()

            if stopServer:
                # stopping the appium server
                self.stop_appium_server()

                # setting the global variable to None
                global_vars.driver = None

        except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            return False, msg
        return True, msg