#!/usr/bin/python2

__unittest = True

import os
import re

#run_dir = os.path.abspath(os.path.dirname(__file__))
current_dir = os.getcwd()
import subprocess
import socket
import platform
from subprocess import Popen,PIPE

# if __name__ == '__main__':
#     os.chdir(run_dir)

import sys
import time
import logging

import os
import time
import threading
import ConfigParser

from shutil import copyfile
from libs.product.omm.standard import util
reload(sys)
sys.setdefaultencoding('utf8')


config = ConfigParser.RawConfigParser()
config.read('config.ini')
logs_folder = config.get('dellunit', 'logfolder')
apk_installer = config.get('Open_Manage_mobile', 'android_build_filename')
exePlatform = config.get('Open_Manage_mobile', 'platform')
os_type = str(platform.system())

if os_type =='Windows':
    portsInuse = util.listening_ports_list()



if __name__ == '__main__':
    prog = None

    try:
        # getting dictionary of devices and status to execute
        device_emulator_dict = util.get_emulator_device_info()

        deviceToexecute_list, testcase_ids = [], []

        # Creating the list of devices based on execution flag 'Yes'
        for device, devicedict in device_emulator_dict.iteritems():

            if str(devicedict['Execute']).lower() == 'yes':
            #if str(execute).lower() == 'yes':
                deviceToexecute_list.append(str(device))
                testcase_ids.append(str('(%s)' % devicedict['Testcases']))
        run_file_list, config_file_list, device_build_list, exe_files, exnfiles = [], [], [], [], []

        i = 1
        #port_num = 4723
        port_num = 4723
        bootstrap_port = 4725
        chromedriverport = 9516
        
        #port_num = util.checkPortInUse(port_num, portsInuse)

        'Create multiple run.py & config.inifiles with device_name appended to it'
        for device in deviceToexecute_list:
            run_file = 'run_%s.py' % device
            run_file_list.append(run_file)
            copyfile('run.py', run_file)
            print "Created run file for device - %s for execution" % device
 
            log_path = 'logs_%s' % device
            util.change_file(run_file, 'logs', log_path)
 
            config_file = 'config_%s.ini' % device
            config_file_list.append(config_file)
            copyfile('config.ini', config_file)
            print "Created config file for for device - %s for execution" % device
 
            'Copying build file name'
            if exePlatform.lower() == 'android':
 
                device_build = 'device_%d.apk' % i
                android_build_path = current_dir + '/inputs/omm/builds/android/' + apk_installer
                build_copy_file = current_dir + '/inputs/omm/builds/android/%s' % device_build
                copyfile(android_build_path, build_copy_file)
                device_build_list.append(build_copy_file)
                util.change_configfile(config_file, 'Open_Manage_mobile', 'android_build_filename', device_build)
            else:
                print "Error: Please enter the platform name properly"
            
            
            if os_type in ['Darwin']:
                exnfile = "runDevice_%s.sh" % i
                exe_file = current_dir + "/" +  exnfile
                
            elif str(platform.system()) == 'Windows': 

                port_num = util.checkPortInUse(port_num, portsInuse)
                bootstrap_port = util.checkPortInUse(bootstrap_port, portsInuse)
                
                exnfile = "runDevice_%s.bat" % i
                exe_file = current_dir + "/" + exnfile
            
            else:
                print "OS not supported for execution"
                
            
            exe_files.append(exe_file)
            exnfiles.append(exnfile)
            print "Exe files are %s" % exe_files
            if os.path.exists(exe_file):
                    os.remove(exe_file)
                
            print "Bat/sh file for the device is created"
            cmd = 'python \"%s\" \"%s\"' % (run_file, config_file)
            with open(exe_file, 'w') as f:
                #f.write('cls\n')
                #f.write('cd %s\n' % current_dir)
                if os_type in ['Darwin']:
                    f.write('cd "$(dirname "$0")"\n')
                f.write('python \"%s\" \"%s\"' % (str(run_file), str(config_file)))
            
            print "Editing config file for device with appium port number, boot strap port number, devicename, logfolder"
            util.change_configfile(config_file, 'Open_Manage_mobile', 'appium_portnum', str(port_num))
            util.change_configfile(config_file, 'Open_Manage_mobile', 'appium_bootstrapport', str(bootstrap_port))
            print "Edited bootstrap port number to %s" %  str(bootstrap_port)   
            util.change_configfile(config_file, 'Open_Manage_mobile', 'appium_chromedriverport', str(chromedriverport))
            
            util.change_configfile(config_file, 'Open_Manage_mobile', 'device_name', str(device))
            print "device name got edited successfully"
            util.change_configfile(config_file, 'dellunit', 'logfolder', 'logs/%s' % str(log_path))
            print "test case id is %s" % testcase_ids[i-1]
            util.change_configfile(config_file, 'dellunit', 'tests', testcase_ids[i-1])
            
            i = i + 1
 
            port_num = port_num + 10
 
            bootstrap_port = bootstrap_port + 10
            chromedriverport = chromedriverport + 10
            
            log_file = current_dir + "/logs/" + log_path
 
            if not os.path.exists(log_file):
                os.makedirs(log_file)
            print "Logs folder for the device is created"

        processlist = []
        for file in exnfiles:
            print "Execution for device started ..."
            if os_type == 'Windows' :
                p = subprocess.Popen(file, creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                print "Execution of file %s started in MAC system" % file
                #subprocess.Popen("chmod +x %s" % file, shell=True)
                p = subprocess.Popen("sh %s" % file, shell=True)
            time.sleep(3)
            processlist.append(p)
     
        for process in processlist:
            process.wait()

        print "All devices execution completed ....."
    finally:
        pass
        
 
        if config_file_list != []:
            for file in config_file_list:
                config_file = current_dir + "/" + file
                if os.path.exists(config_file):
                    os.remove(config_file)
                    print "Config file for each device is %s deleted" % config_file
        if run_file_list != []:
             for file in run_file_list:
                 runfile = current_dir + "/" + file
                 if os.path.exists(runfile):
                     os.remove(runfile)
                     print "Run file for each device is %s deleted" % runfile
        if exe_files != []:
             for file in exe_files:
                 if os.path.exists(file):
                     os.remove(file)
                     print "Bat/sh     file for each device is %s deleted" % file
        else:
            print "Bat file list is empty"
        if device_build_list != []:
            for file in device_build_list:
                 if os.path.exists(file):
                     os.remove(file)
                     print "Build file for each device is %s deleted" % runfile
        else:
            print "Build file list is empty"
