import traceback
from libs.product.omm.standard import omm_lib
from libs.product.omm.standard import util
from libs.product.omm.standard import global_vars
from libs.product.omm.omm_idrac import ui_idrac
from libs.product.omm.omm_ome import ui_ome, ome_lib
from libs.product.omm.omm_generic import ui_generic
from libs.product.omm.omm_generic import demomode_functions
from libs.product.omm.standard import global_vars



from libs.product.omm.standard.appium_handler import appium_handler
from libs.product.omm.omm_ome.ome_lib import omedbdata

from libs.product.omm.standard.omm_lib import step_reset_android_app,\
    step_restart_android_app



appium_handler = appium_handler()
g = global_vars


class Steps():

    def __init__(self, *args, **kwargs):
        pass


class Common(Steps):

    # Created by Nithya V on 27/04/2016
    def step_start_driver(self, auto_accept_alerts=True):
        """
        Start the appium driver
        """
        status, msg = False, ""
        try:
            util.step("- Start the appium driver")
            flag, msg = appium_handler.start_driver(is_auto_accept_alerts = auto_accept_alerts)
            if flag:
                print "Appium driver has been started successfully"
                status = True
            else:
                print "Appium driver has not been started successfully"
        except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
        return status, msg
    def sstep_start_driver(self, auto_accept_alerts=False):
        """
        Start the appium driver
        """
        status, msg = False, ""
        try:
            util.step("- Start the appium driver")
            flag, msg = appium_handler.start_driver(is_auto_accept_alerts = auto_accept_alerts)
            if flag:
                print "Appium driver has been started successfully"
                status = True
            else:
                print "Appium driver has not been started successfully"
        except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
        return status, msg

    def step_quit_driver(self):
        """
        Quit driver and stop server/app
        """
        status, msg = False, ""
        try:
            util.step("- Quit appium driver and stop server/app")
            flag, msg = appium_handler.quit_driver()
            if flag:
                status = True
            else:
                print "Appium driver/server has not been terminated successfully"
        except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
        return status, msg

    def step_uninstall_app(self, ):
        """
        Uninstall app
        """
        flag, msg = False, ""
        try:
            util.step("- Uninstall OMM app")
            if global_vars.platform == 'android':
                flag = omm_lib.uninstall_android_omm_app()
            else:
                flag = omm_lib.uninstall_ios_omm_app()
        except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
        return flag, msg

    def step_startDriver(self, data, args):
        """
        To Start Driver
        """
        util.step("- To start driver")
        expectedResult = "User should be able to start driver successfully"
        if args[1]['startServer'] != False:
            flag, msg = appium_handler.start_driver()
        else:
            flag, msg = appium_handler.start_driver(startServer=False)
        pass_message = "Driver should be started successfully"
        fail_message = "Driver has not been started successfully- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_stopDriver(self, data, args):
        """
        To Start Driver
        """
        util.step("- To start driver")
        expectedResult = "User should be able to stop driver successfully"
        if args[1]['stopServer'] != False:
            flag, msg = appium_handler.quit_driver()
        else:
            flag, msg = appium_handler.quit_driver(stopServer=False)
        pass_message = "Driver should be stopped successfully"
        fail_message = "Driver has not been stopped successfully- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def step_restart_app(self, data, args):
        """
        Restart app
        """
        flag, msg = False, ""
        expectedResult = "App should be restarted successfully"
        pass_message = "App restarted successfully"
        fail_message = "App not restarted successfully- %s" % msg
        try:
            util.step("- Restart OMM app")
            if global_vars.platform == 'android':
                flag = omm_lib.step_restart_android_app()
            else:
                flag = omm_lib.step_restart_ios_app()
        except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag, msg
    def step_reset_app(self, data, args):
        """
        Reset app
        """
        flag, msg = False, ""
        try:
            util.step("- Reset OMM app")
            if global_vars.platform == 'android':
                flag = omm_lib.step_reset_android_app()
                
            else:
                flag = omm_lib.step_reset_ios_app()
        except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
        return flag, msg


class Omm_class(Steps):
    #created by nagarjuna on 21/11/2016
    def step_verify_end_user_license_agreement_text(self, data, args):
        
        """
        verify end user license agreement text
        """
        util.step("-Verify EULA text")
        expectedResult = "EULA label and text should be verified successfully"
        flag, msg =ui_generic.verify_eula_lables_and_text()
        pass_message = "EULA label and text is verified successfully"
        fail_message = " EULA label and text verified unsuccessfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag 
    # Created by Nithya V on 6/5/2016
    def step_verify_license_agreement_screenname(self, data, args):
        """
        Verify license agreement screen name
        """
        util.step("- Verify License agreement screen name")
        expectedResult = "License agreement screen name should be correct"
        flag, msg = ui_generic.verify_omm_license_agrmt_screenname()
        pass_message = "License agreement screen name is verified successfully"
        fail_message = "License agreement screen name is not verified successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    # Created by Nithya V on 27/04/2016
    def step_accept_license(self, data, args):
        
        """
        Accept the license agreement
        """
        util.step("- Accept the license")
        expectedResult = "User should be able to accept the license successfully"
        flag, msg =ui_generic.accept_license()
        pass_message = "License has been accepted successfully"
        fail_message = "License has not been accepted successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    
    # Created by nagarjuna  on 21/11/2016
    def step_verify_Diagnostics_and_usage_screenname(self, data, args):
        """
        Verify diagnostics and usage screen name
        """
        util.step("- Verify diagnostics and usage screen name")
        expectedResult = "diagnostics and usage screen name should be displayed properly"
        flag, msg = ui_generic.verify_diagnostics_and_usage_screen_name()
        pass_message = "diagnostics and usage screen name is verified successfully"
        fail_message = "diagnostics and usage screen name is verified unsuccessfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    
    # Created by nagarjuna  on 21/11/2016
    def step_verify_Diagnostics_and_usage_text(self, data, args):
        """
        Verify diagnostics and usage label and text
        """
        util.step("- Verify diagnostics and usage label and text")
        expectedResult = "diagnostics and usage text should be verified successfully"
        flag, msg = ui_generic.verify_diagnostics_and_usage_text()
        pass_message = "diagnostics and usage text is verified successfully"
        fail_message = "diagnostics and usage text is verified unsuccessfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    # Created by Nagarjuna V on 21/11/2016
    def step_accept_diagnostics_and_usage(self, data, args):
        
        """
        Accept the diagnostics and usage
        """
        util.step("- Accept the diagnostics and usage")
        expectedResult = "User should be able to accept the diagnostics and usage"
        flag, msg =ui_generic.accept_diagnostics_and_usage()
        pass_message = "diagnostics and usage has been accepted successfully"
        fail_message = "diagnostics and usage has not been accepted successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    # Created by Nithya V on 6/5/2016
    def step_verify_createPassword_screenname(self, data, args):
        """
        Verify Create Password screen Name
        """
        util.step("- Verify Create Password screen Name")
        expectedResult = "Verify the screen name of Create Password screen"
        flag, msg = ui_generic.verify_createPassword_screen()
        pass_message = "Create Password screen name is displayed properly"
        fail_message = "Create Password screen name is not displayed properly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    # Created by Nagarjuna  on 27/04/2016
    def step_create_login_password(self, data, args):
        """
        Create password before login
        """
        util.step("- Create password before login")
        expectedResult = "User should be able to create password successfully"
        flag, msg = ui_generic.create_pwd_login()
        pass_message = "Create password has been selected successfully"
        fail_message = "Create password has not been selected successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    # Created by nagarjuna  on 21/11/2016
    def step_verify_try_demomode_page_text(self, data, args):
        """
        Verify try demo mode page text
        """
        util.step("- Verify try demo mode page text")
        expectedResult = "try demo mode page text should verified successfully"
        flag, msg = ui_generic.verify_try_demomode_page_text()
        pass_message = "try demo mode page text is verified successfully"
        fail_message = "try demo mode page text is verified unsuccessfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nagarjuna on 21/11/2016
    def step_demo_continue_to_openManage_mobile(self, data, args):
        """
        selecting to continue openManage mobile
        """
        util.step("- Try demo mode and continue (to omm)")
        expectedResult = "User should be able continue by selecting Continue to OMM option"
        flag, msg = ui_generic.try_continue_to_openManage_mobile()
        pass_message = "Try demo mode Continue to OMM has been selected successfully"
        fail_message = "Try demo mode Continue to OMM has not been selected successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def omeadd(self, data, args):
        #flag, msg=ome_lib.omedbdata1("10.94.13.76","sa","Dell1234", "omessentials","SELECT * FROM [dbo].[Device]")
        """
        Accept the license agreement
        """
        util.step("- db conection")
        expectedResult = "User should be able to accept the license successfully"
        #flag, msg = ome_lib.omedbdata1("10.94.13.76","sa","Dell1234", "omessentials","SELECT * FROM [dbo].[Device]")
        flag, msg,DBResultmatrix = ome_lib.omedbdata1("10.94.15.28","sa","Dell1234","SELECT * FROM [OMEssentials].[dbo].[Device]")
        print DBResultmatrix
        pass_message = "License has been accepted successfully"
        fail_message = "License has not been accepted successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

   
    # Created by Nithya V on 27/04/2016
    def step_dont_share(self, data, args):
        """
        Do not share the app with developers
        """
        util.step("- Do not share the app")
        expectedResult = "User should be able to select Dont share successfully"
        flag, msg = ui_generic.dnt_share_app()
        pass_message = "Do not share the app has been selected successfully"
        fail_message = "Do not share the app  has not been selected successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

   

    # Created by Nithya V on 27/04/2016
    def step_trydemo_continue(self, data, args):
        """
        Try demo mode and continue
        """
        util.step("- Try demo mode and continue (to omm)")
        expectedResult = "User should be able continue by selecting Continue to OMM option"
        flag, msg = ui_generic.try_demo_continue()
        pass_message = "Try demo mode Continue to OMM has been selected successfully"
        fail_message = "Try demo mode Continue to OMM has not been selected successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nithya V on 27/04/2016
    def step_omm_login(self, data, args):
        """
        Logging in to OMM
        """
        util.step("- Logging in to OMM")
        expectedResult = "User should be able log in to OMM"
        flag, msg = ui_generic.omm_login()
        pass_message = "OMM login is successful"
        fail_message = "OMM login is not successful - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

   

    # Created by Nithya V on 6/5/2016
    def step_verify_license_agreement(self, data, args):
        """
        Verify license agreement text displayed in License page
        """
        util.step("- Verify License agreement text")
        expectedResult = "Text displayed in UI should match with input verification data"
        flag, msg = ui_generic.verify_omm_license_agrmt()
        pass_message = "Text displayed in UI match with input verification data"
        fail_message = "Text displayed in UI does not match with input verification data - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nithya V on 6/5/2016
    def step_verify_share_appData_screenname(self, data, args):
        """
        Verify share app data screen name
        """
        util.step("- Verify app data screen name")
        expectedResult = "App Data screen name should be proper"
        flag, msg = ui_generic.verify_share_app_screen_name()
        pass_message = "App Data screen name is verified successfully"
        fail_message = "App Data screen name is not verified successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nithya V on 6/5/2016
    def step_verify_share_appData(self, data, args):
        """
        Verify Share App data text displayed in Share App Data screen
        """
        util.step("- Verify Share App data text displayed")
        expectedResult = "Text displayed in UI should match with input verification data"
        flag, msg = ui_generic.verify_share_app_screen()
        pass_message = "Text displayed in UI match with input verification data"
        fail_message = "Text displayed in UI does not match with input verification data - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    

    # Created by Nithya V on 6/5/2016
    def step_verify_try_demomode_screenname(self, data, args):
        """
        Verify demo mode screen name
        """
        util.step("- Verify demo mode screen name")
        expectedResult = "Demo mode screen name should be proper"
        flag, msg = ui_generic.verify_try_demoMode_screenname()
        pass_message = "Demo mode screen name is verified successfully"
        fail_message = "Demo mode screen name is not verified successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nithya V on 6/5/2016
    def step_verify_demoMode_screen(self, data, args):
        """
        Verify Demo mode screen
        """
        util.step("- Verify Demo Mode screen")
        expectedResult = "Screen name of Demo Mode screen should be proper"
        flag, msg = ui_generic.verify_demoMode_screen()
        pass_message = "Demo mode screen name is displayed properly"
        fail_message = "Demo mode screen name is not displayed properly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nithya V on 19/5/2016
    def step_verify_omm_home_screen(self, data, args):
        """
        Verify OMM home screen
        """
        util.step("- Verify OMM home screen")
        expectedResult = "OMM home screen should be proper"
        flag, msg = ui_generic.verify_homeScreen()
        pass_message = "OMM home screen is displayed properly"
        fail_message = "OMM home screen is not displayed properly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nithya V on 19/5/2016
    def step_navigate_mainMenu(self, data, args):
        """
        Navigate to OMM main menu
        """
        util.step("- Navigate to Main Menu")
        expectedResult = "User should be able to navigate to main menu"
        flag, msg = ui_generic.navigate_mainMenu()
        pass_message = "Main menu is displayed properly"
        fail_message = "Main menu is not displayed properly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nithya V on 19/5/2016
    def step_navigate_aboutScreen(self, data, args):
        """
        Navigate to about Screen
        """
        util.step("- Navigate to About Screen")
        expectedResult = "User should be able to navigate to about screen"
        flag, msg = ui_generic.navigate_aboutScreen()
        pass_message = "User is navigated to about Screen"
        fail_message = "User is not navigated to about screen - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nithya V on 19/5/2016
    def step_verify_aboutScreen(self, data, args):
        """
        Verify about Screen
        """
        util.step("- Verify About Screen")
        expectedResult = "About Screen should be displayed properly"
        flag, msg = ui_generic.verify_aboutScreen()
        pass_message = "About Screen is displayed properly"
        fail_message = "About Screen is not displayed properly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    # Created by Nithya V on 19/5/2016
    def step_verify_versionBuildNumber(self, data, args):
        """
        Verify Version and Build Number
        """
        util.step("- Verify Version and Build Number")
        expectedResult = "Version and Build Number should be correct"
        flag, msg = ui_generic.verify_Version_buildNumber()
        pass_message = "Version and Build Number is correct"
        fail_message = "Version and Build Number are incorrect - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_launchVirtualConsole(self, data, args):
        """
        To launch Virtual Console
        """
        util.step("- To launch Virtual Console")
        expectedResult = "Virtual Console should be launched successfully"
        flag, msg = ui_idrac.launchVirtualConsole()
        pass_message = "Virtual Console is launched successfully"
        fail_message = "Virtual Console has not been launched successfully- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_virtualConsoleAlertHandle(self, data, args):
        """
        To verify Virtual Console launch Alert & click on YES
        """
        util.step("- To verify Virtual Console Alert")
        expectedResult = "Virtual Console alert should be verified successfully & closed"
        flag, msg = ui_idrac.virtualConsoleAlertHandle()
        pass_message = "Virtual Console alert is verified successfully"
        fail_message = "Virtual Console alert has not been launched successfully- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_install_bvnc_app(self, data, args):
        """
        To install bvnc app 
        """
        util.step("- To install bVNC app")
        expectedResult = "To install bVNC app successfully"
        flag, msg = ui_idrac.installAndroidApp()
        pass_message = "bVNC app is installed successfully"
        fail_message = "bVNC app has not been installed successfully- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_configureLaunchVirtualConsole(self, data, args):
        """
        To configure Virtual Console launch 
        """
        util.step("- To configure Virtual Console launch")
        expectedResult = "To configure Virtual Console launch"
        flag, msg = ui_idrac.configure_LaunchVirtualConsole()
        pass_message = "Virtual Console settings is configured successfully"
        fail_message = "Virtual Console settings is not configured successfully- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_verifylaunchVNCAlert(self, data, args):
        """
        To verify vnc alert pop up on vnc launch
        """
        util.step("- To verify vnc alert pop up")
        expectedResult = "To VNC alert pop up on vnc launch should verified successfully"
        flag, msg = ui_idrac.verifylaunchVNCalert()
        pass_message = "VNC alert pop up on VNC launch is verified successfully"
        fail_message = "VNC alert pop up on VNC launch is not verified successfully- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_verifyVNCViewer(self, data, args):
        """
        To verify VNC Viewer
        """
        util.step("- To verify VNC Viewer is launched successfully")
        expectedResult = "VNC Viewer launch should be verified successfully"
        flag, msg = ui_idrac.verifyVNCViewer()
        pass_message = "VNC Viewer is launched successfully"
        fail_message = "VNC Viewer is not launched successfully- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_add_idrac(self, data, args):
        """
        Enter idrac ip and credentials
        """
        util.step("- add iDRAC")
        expectedResult = "User should be to able to add iDRAC successfully"
        idrac_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_ip']
        idrac_username = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_username']
        idrac_password = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_password']
        flag, msg = ui_idrac.add_idrac(idrac_ip, idrac_username, idrac_password)
        pass_message = "iDRAC added successfully"
        fail_message = "iDRAC not added successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def sstep_add_idrac(self, data, args):
        """
        Enter idrac ip and credentials
        """
        util.step("- add iDRAC")
        expectedResult = "User should be to able to add iDRAC successfully"
        idrac_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_ip']
        idrac_username = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_username']
        idrac_password = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_password']
        flag, msg = ui_idrac.add_idrac(idrac_ip, idrac_username, idrac_password)
        pass_message = "iDRAC added successfully"
        fail_message = "iDRAC not added successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def step_verify_idrac_basic_inventory(self, data, args):
        """
        Verify iDRAC Basic Inventory
        """
        util.step("- Verify Basic Inventory")
        expectedResult = "Basic Inventory should be displayed correctly"
        windows_ip = args[0].windows_ip
        windows_username = args[0].windows_username
        windows_password = args[0].windows_password
        idrac_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_ip']
        idrac_username = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_username']
        idrac_password = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_password']
        flag, msg = ui_idrac.verify_idrac_basic_inventory(idrac_ip, idrac_username,
                                    idrac_password, windows_ip, windows_username, windows_password)
        pass_message = "Basic Inventory displayed correctly"
        fail_message = "Basic Inventory not displayed correctly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_delete_idrac(self, data, args):
        """
        Delete iDRAC
        """
        util.step("- Delete idrac")
        expectedResult = "User should be able to delete iDRAC"
        idrac_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_ip']
        flag, msg = ui_idrac.delete_idrac(idrac_ip)
        pass_message = "iDRAC deleted successfully"
        fail_message = "iDRAC not deleted - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_open_power_options(self, data, args):
        """
        Navigate to Power Options screen
        """
        util.step("- Navigate to Power Options screen")
        expectedResult = "User should be able to navigate to Power Options Screen"
        flag, msg = ui_idrac.open_power_options()
        pass_message = "Power Options screen opened successfully"
        fail_message = "Power Options screen not opened successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_perform_power_on_action(self, data, args):
        """
        Perform power on action
        """
        util.step("- Perform power on action")
        expectedResult = "User should be able to perform power on action"
        windows_ip = args[0].windows_ip
        windows_username = args[0].windows_username
        windows_password = args[0].windows_password
        idrac_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_ip']
        idrac_username = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_username']
        idrac_password = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_password']
        flag, msg = ui_idrac.perform_power_on_action(idrac_ip, idrac_username,
                                                    idrac_password, windows_ip, windows_username, windows_password)
        pass_message = "Power on action performed successfully"
        fail_message = "Power on action not performed successfully - %s" % msg
        print 'Flag inside step'
        print flag
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_perform_shutdown_action(self, data, args):
        """
        Perform shutdown action
        """
        util.step("- Perform shutdown action")
        expectedResult = "User should be able to perform shutdown action"
        windows_ip = args[0].windows_ip
        windows_username = args[0].windows_username
        windows_password = args[0].windows_password
        idrac_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_ip']
        idrac_username = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_username']
        idrac_password = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_password']
        flag, msg = ui_idrac.perform_shutdown_action(idrac_ip, idrac_username,
                                                    idrac_password, windows_ip, windows_username, windows_password)
        pass_message = "Shutdown action performed successfully"
        fail_message = "Shutdown action not performed successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_perform_power_cycle_action(self, data, args):
        """
        Perform power cycle action
        """
        util.step("- Perform power cycle action")
        expectedResult = "User should be able to Perform power cycle action"
        windows_ip = args[0].windows_ip
        windows_username = args[0].windows_username
        windows_password = args[0].windows_password
        idrac_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_ip']
        idrac_username = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_username']
        idrac_password = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_password']
        flag, msg = ui_idrac.perform_power_cycle_action(idrac_ip, idrac_username, idrac_password,
                                                     windows_ip, windows_username, windows_password)
        pass_message = "Power cycle action performed successfully"
        fail_message = "Power cycle action not performed successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_perform_shutdownos_action(self, data, args):
        """
        Perform shutdown with shutdown os first action
        """
        util.step("- Perform shutdown with shutdown os first action")
        expectedResult = "User should be able to perform shutdown with shutdown os first action"
        windows_ip = args[0].windows_ip
        windows_username = args[0].windows_username
        windows_password = args[0].windows_password
        idrac_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_ip']
        idrac_username = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_username']
        idrac_password = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_password']
        flag, msg = ui_idrac.perform_shutdown_os_action(idrac_ip, idrac_username, idrac_password,
                                                     windows_ip, windows_username, windows_password)
        pass_message = "Shutdown with OS action performed successfully"
        fail_message = "Shutdown with OS action not performed successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_perform_shutdown_using_winrm(self, data, args):
        """
        Perform shutdown using winrm
        """
        util.step("- Perform shutdown using winrm")
        expectedResult = "User should be able to perform shutdown using winrm"
        windows_ip = args[0].windows_ip
        windows_username = args[0].windows_username
        windows_password = args[0].windows_password
        idrac_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_ip']
        idrac_username = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_username']
        idrac_password = global_vars.tc_verfn_dict[args[0].testcase_id]['idrac_password']
        flag, msg = ui_idrac.perform_shutdown_using_winrm(idrac_ip, idrac_username, idrac_password,
                                                    windows_ip, windows_username, windows_password)
        pass_message = "Shutdown performed successfully"
        fail_message = "Shutdown not performed successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_verify_offstate_enabled_controls(self, data, args):
        """
        Verify which controls are enabled/disabled when power state is off
        """
        util.step("- Verify which controls are enabled/disabled when power state is off")
        expectedResult = "Only Power on option should be enabled"
        flag, msg = ui_idrac.verify_offstate_enabled_controls()
        pass_message = "Only Power on option is enabled"
        fail_message = "Only power on option is not enabled - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_verify_onstate_enabled_controls(self, data, args):
        """
        Verify which controls are enabled/disabled when power state is on
        """
        util.step("- Verify which controls are enabled/disabled when power state is on")
        expectedResult = "Only Power on option should be disabled"
        flag, msg = ui_idrac.verify_onstate_enabled_controls()
        pass_message = "Only Power on option is disabled"
        fail_message = "Only power on option is not disabled - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_add_ome(self, data, args):
        """
        Click 'OME' button and then add OME application. Enter OME application ip and credentials
        """
        util.step("- Click 'OME' button and add 'OpenManage Essentials")
        expectedResult = "User should be able to click 'OME' button and add OME Application"
        ome_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_ip']
        ome_username = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_username']
        ome_password = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_password']
        flag, msg = ui_ome.add_ome_app(ome_ip, ome_username, ome_password)
        pass_message = "OME application is successfully added"
        fail_message = "OME application is not added successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def step_add_ome_device(self, data, args):
        """
        Click 'OME' button and then add OME application. Enter OME application ip and credentials
        """
        util.step("- Click 'OME' button and add 'OpenManage Essentials")
        expectedResult = "User should be able to click 'OME' button and add OME Application"
        ome_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_ip']
        ome_username = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_username']
        ome_password = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_password']
        flag, msg = ui_ome.add_ome_device(ome_ip, ome_username, ome_password)
        pass_message = "OME application is successfully added"
        fail_message = "OME application is not added successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_verify_pysmsql_ome_details(self, data, args):
        """
        Verify OME devices health and event severity details
        """
        util.step("- Verify OME devices health and event severity details")
        expectedResult = "OME health and event details should be displayed correctly"
        device_health = global_vars.tc_verfn_dict[args[0].testcase_id]['device_health']
        event_severity = global_vars.tc_verfn_dict[args[0].testcase_id]['event_severity']
        flag, msg = ui_ome.verify_pysmsql_ome_details(device_health, event_severity)
        pass_message = "OME health and event details displayed correctly"
        fail_message = "OME health and event details not displayed correctly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    
    def step_verify_ome_details(self, data, args):
        """
        Verify OME devices health and event severity details
        """
        util.step("- Verify OME devices health and event severity details")
        expectedResult = "OME health and event details should be displayed correctly"
        device_health = global_vars.tc_verfn_dict[args[0].testcase_id]['device_health']
        event_severity = global_vars.tc_verfn_dict[args[0].testcase_id]['event_severity']
        flag, msg = ui_ome.verify_ome_details(device_health, event_severity)
        pass_message = "OME health and event details displayed correctly"
        fail_message = "OME health and event details not displayed correctly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_delete_ome(self, data, args):
        """
        Delete OME
        """
        util.step("- Delete OME")
        expectedResult = "User should be able to delete OME"
        ome_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_ip']
        flag, msg = ui_ome.delete_ome(ome_ip)
        pass_message = "OME deleted successfully"
        fail_message = "OME not deleted - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def sstep_delete_ome(self, data, args):
        """
        Delete OME
        """
        util.step("- Delete OME")
        expectedResult = "User should be able to delete OME"
      
        flag, msg = ui_ome.ddelete_ome()
        pass_message = "OME deleted successfully"
        fail_message = "OME not deleted - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag


    def demomode_step_accept_license(self, data, args):
        """
        Accept the license agreement
        """
        util.step("- Accept the license")
        expectedResult = "User should be able to accept the license successfully"
        flag, msg = ui_generic.demomode_accept_license()
        pass_message = "License has been accepted successfully"
        fail_message = "License has not been accepted successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag


    def demomode_exit_from_all_pages(self, data, args):
        """
        verify exit demo mode from settings
        """
        util.step("exit demo mode")
        expectedResult = "should exit from demo mode"
        flag, msg = demomode_functions.exit_demomode_frm_all_pages()
        pass_message = "successfully exited from exit demo mode"
        fail_message = "unsuccessfully exited from exit demo mode  %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def vr_exit_demo_mode(self, data, args):
        """
        verify exit demo mode from settings
        """
        util.step("exit demo mode")
        expectedResult = "should exit from demo mode"
        flag, msg = demomode_functions.verify_demo_mode_all_devices()
        pass_message = "successfully exited from exit demo mode"
        fail_message = "unsuccessfully exited from exit demo mode  %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    
    def step_verify_enable_demomode_option_from_settings(self, data, args):
        """
        verify DemoMode enable /disable toggle switch from settings
        """
        util.step("- Verify DemoMode enable/ disable toggle switch from settings")
        expectedResult = "DemoMode enable toggle switch should be enable/disable"
        flag, msg = demomode_functions.verify_enable_demomode_from_settings()
        pass_message = "successfully verified DemoMode enable toggle switch from settings "
        fail_message = "unsuccessfully verified DemoMode enable toggle switch from settings  %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_trydemo_mode_now(self, data, args):
        """
        Try demo mode and continue
        """
        util.step("- Try demo mode and continue (to omm)")
        expectedResult = "User should be able continue by selecting Continue to OMM option"
        flag, msg = ui_generic.try_demo_mode_now()
        pass_message = "Try demo mode Continue to OMM has been selected successfully"
        fail_message = "Try demo mode Continue to OMM has not been selected successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_verify_demomode_devices_text(self, data, args):
        """

        verify demo mode ome and i drac devices text
        """
        util.step("- Verify ome and i drac devices text")
        expectedResult = "ome and idrac devices text should verifed correct"
        #flag, msg = demomode_functions.verify_demomode_ome_and_idrac_devices_text()
        flag,msg = demomode_functions.duplicate_verify_demomode_ome_and_idrac_devices_text()
        #flag, msg = demomode_functions.duplicate_verify_demomode_ome_and_idrac_devices_text(first_ome="10.255.2.1",second_ome="10.255.2.2",first_idrac="10.35.0.1",second_idrac="10.35.0.2",thrd_idrac="10.35.0.3",forth_idrac="10.40.0.1",fifth_idrac="10.40.0.2",six_idrac="192.168.0.110",sevnth_idrac="10.11.50.1")
        pass_message = "Devices text is displayed properly"
        fail_message = "Devices text is not displayed properly  %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_vrify_first_ome_devices_txt(self, data, args):
        """
        verify demo mode ome  device text
        """
        util.step("verify  ome devices text ")
        expectedResult = "DemoMode ome device text should be verified sucessfully"
        flag, msg = demomode_functions.verify_demomode_first_ome_devices_text()
        pass_message = "successfully verified demo mode ome devices text"
        fail_message = "unsuccessfully verified demo mode ome devices text %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    
    def step_vrify_second_ome_devices_txt(self, data, args):
        """
        verify demo mode ome  device text
        """
        util.step("verify  ome devices text ")
        expectedResult = "DemoMode ome device text should be verified sucessfully"
        flag, msg = demomode_functions.verify_demomode_second_ome_devices_text()
        pass_message = "successfully verified demo mode ome devices text"
        fail_message = "unsuccessfully verified demo mode ome devices text %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    
    
    
    
    
    
    
    def step_omm_login_wth_pasword(self, data, args):
        """
        Logging in to OMM
        """
        util.step("- Logging in to OMM")
        expectedResult = "User should be able log in to OMM"
        #flag, msg = ui_generic.omm_login()#commenting this & passing g.password as parameter because, even though g.password is updated still old value is considered in case of optional parameter with change password case
        flag, msg = ui_generic.omm_login_with_password(g.password)
        pass_message = "OMM login is successful"
        fail_message = "OMM login is not successful - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    
    def step_verify_first_idrac_devices_text(self, data, args):
        """

        verify demo mode idrac devices text
        """
        util.step("- Verify  idrac devices home page text")
        expectedResult = " all idrac devices text should be verifed sucessfully "
        flag, msg = demomode_functions.verify_demomode_all_idrac_devices_text()
        pass_message = "  idrac device text is  verifed properly"
        fail_message = "  idrac device text is  not verifed properly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_AddOMEWizardLaunch(self, data, args):
        """
        To Validate Add OME wizard has been launched successfully
        """
        util.step("- To Validate Add OME wizard has been launched successfully")
        expectedResult = "Add OME wizard must be launch successfully"
        flag, msg = ui_ome.aadd_ome_wizard()
        pass_message = "Add OME wizard has been launched successfully"
        fail_message = "Add OME wizard has not been launch successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_EnterOMEdetailsAndAdd(self, data, args):
        """
        To validate OME must be added successfully after entering all required correct details
        """
        util.step("- To validate OME must be added successfully after entering all required correct details")
        expectedResult = "OME must be add successfully after entering all required correct details"
        flag, msg = ui_ome.eenter_ome_details("100.100.16.50","administrator","Lexington123")
        pass_message = "OME has been added successfully after entering all required correct details"
        fail_message = " OME has not been added successfully- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def  sstep_EnterOMEdetailsAndAdd(self, data, args):
        """
        Click 'OME' button and then add OME application. Enter OME application ip and credentials
        """
        util.step("- Click 'OME' button and add 'OpenManage Essentials")
        expectedResult = "User should be able to click 'OME' button and add OME Application"
        ome_ip = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_ip']
        ome_username = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_username']
        ome_password = global_vars.tc_verfn_dict[args[0].testcase_id]['ome_password']
        flag, msg = ui_ome.eenter_ome_details(ome_ip, ome_username, ome_password)
        pass_message = "OME application is successfully added"
        fail_message = "OME application is not added successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag


    def step_SelectDeviceAndCreatePowerTask(self, data, args):
        """
        To validate power task has been created successfully under OME for same device after selecting a proper device under OMM and passing required parameters for power task creation. 
        """
        util.step("- To validate power task has been created successfully under OME for same device after selecting a proper device under OMM and passing required parameters for power task creation.")
        expectedResult = "Power task must be create successfully under OME for same device after selecting a proper device under OMM and passing required parameters for power task creation."
        flag, msg = ui_ome.select_device_and_create_powertask()
        pass_message = "Power task has been created successfully under OME for selected device "
        fail_message = " Power task has not been create successfully under OME for selected device- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def hi_step_SelectDeviceAndCreatePowerTask(self, data, args):
        """
        To validate power task has been created successfully under OME for same device after selecting a proper device under OMM and passing required parameters for power task creation. 
        """
        util.step("- To validate power task has been created successfully under OME for same device after selecting a proper device under OMM and passing required parameters for power task creation.")
        expectedResult = "Power task must be create successfully under OME for same device after selecting a proper device under OMM and passing required parameters for power task creation."
        flag, msg = ui_ome.hi_select_device_and_create_powertask()
        pass_message = "Power task has been created successfully under OME for selected device "
        fail_message = " Power task has not been create successfully under OME for selected device- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def duplicate_step_SelectDeviceAndCreatePowerTask(self, data, args):
        """
        To validate power task has been created successfully under OME for same device after selecting a proper device under OMM and passing required parameters for power task creation. 
        """
        util.step("- To validate power task has been created successfully under OME for same device after selecting a proper device under OMM and passing required parameters for power task creation.")
        expectedResult = "Power task must be create successfully under OME for same device after selecting a proper device under OMM and passing required parameters for power task creation."
        flag, msg = ui_ome.duplicate_select_device_and_create_powertask()
        pass_message = "Power task has been created successfully under OME for selected device "
        fail_message = " Power task has not been create successfully under OME for selected device- %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def step_demomode_create_password(self, data, args):
        """
        Create password before login
        """
        util.step("- Create password before login")
        expectedResult = "User should be able to create password successfully"
        flag, msg = ui_generic.demomode_create_pwd_login()
        pass_message = "Create password has been selected successfully"
        fail_message = "Create password has not been selected successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    
    def step_demo_mode_try_now(self, data, args):
        """
        Try demo mode and continue
        """
        util.step("- Try demo mode and continue (to omm)")
        expectedResult = "User should be able continue by selecting Continue to OMM option"
        flag, msg = ui_generic.demo_mode_try_now()
        pass_message = "Try demo mode Continue to OMM has been selected successfully"
        fail_message = "Try demo mode Continue to OMM has not been selected successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def step_create_pwd_login_with_all_validation(self, data, args):
        """
        Create password before login with all validations
        """
        util.step("- Create password before login with all validations")
        expectedResult = "User should be able to create password successfully for valid scenarios"
        flag, msg = ui_generic.create_pwd_login_with_all_validation()
        pass_message = "Create password has been selected successfully"
        fail_message = "Create password has not been selected successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def step_omm_login_negative(self, data, args):
        """
        Logging in to OMM with invalid password(s)
        """
        util.step("- Logging in to OMM with invalid password(s)")
        expectedResult = "User should not be able log in to OMM with invalid credential(s)"
        flag, msg = ui_generic.omm_login_with_password(password=g.password + '_1')
        pass_message = "OMM login with wrong password is unsuccessful - %s" % msg
        fail_message = "OMM login with wrong password is successful - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def step_verify_dialogue_wrong_password(self, data, args):
        """
        #Verifying Wrong password dialogue in OMM with invalid password(s)
        #"""
        util.step("- Verifying Wrong password dialogue in OMM with invalid password(s)")
        expectedResult = "Wrong password pop up should appear"
        expected_dialogue_title = g.ios_wrong_passwrd_error
        expected_dialogue_message = g.ios_wrong_password_message
        flag, msg = ui_generic.verify_wrong_popup_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')
        pass_message = "Expected Dialogue verified successfully"
        fail_message = "Expected Dialogue is not verified successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    #def step_verify_dialogue_wrong_password(self, data, args):
        #"""
        #Verifying Wrong password dialogue in OMM with invalid password(s)
        #"""
        #util.step("- Verifying Wrong password dialogue in OMM with invalid password(s)")
        #expectedResult = "Wrong password pop up should appear"
        #flag, msg = ui_generic.verify_dialogue_with_wrong_password()
       # pass_message = "Expected Dialogue verified successfully"
        #fail_message = "Expected Dialogue is not verified successfully - %s" % msg
        #args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        #return flag    
     # Created by Ramanuja_das_pvk on 27/09/2016
    def step_omm_forgotPassword_login_negative(self, data, args):
        """
        Logging in to OMM with Forgot Password Screen with invalid password(s)
        """
        util.step("- Forgot Password Screen Logging in to OMM with invalid password(s)")
        expectedResult = "User should not be able log in to OMM with Forgot Password Screen with invalid credential(s)"
        flag, msg = ui_generic.omm_forgot_password_login(password=g.password + '_1')
        pass_message = "OMM Forgot Password Screen login with wrong password is unsuccessful - %s" % msg
        fail_message = "OMM Forgot Password Screen login with wrong password is successful - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)

        return flag

    def step_omm_forgotPassword_login(self, data, args):
        """
        Logging in to OMM with Forgot Password Screen with valid password(s)
        """
        util.step("- Forgot Password Screen Logging in to OMM with valid password(s)")
        expectedResult = "User should not be able log in to OMM with Forgot Password Screen with valid credential(s)"
        flag, msg = ui_generic.omm_forgot_password_login(password=g.password)
        pass_message = "OMM Forgot Password Screen login is successful - %s" % msg
        fail_message = "OMM Forgot Password Screen login is un successful - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)

        return flag
    def step_login_click_change_password(self, data, args):
        """
        Click on Change password at login
        """
        util.step("- Click on hange password at login")
        expectedResult = "User should be moved to change password screen successfully"
        flag, msg = ui_generic.login_click_change_pwd()
        pass_message = "Click Change password is completed successfully"
        fail_message = "Click Change password is not completed successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag 
    def step_verify_changePassword_screen(self, data, args):
        """
        Verify change password screen
        """
        util.step("- Verify change password screen is present")
        expectedResult = " screen name should be proper"
        flag, msg = ui_generic.verify_changePassword_screen()
        pass_message = "Change Password screen is verified successfully"
        fail_message = "Change Password screen is not verified successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    # Created by Ramanuja_das_pvk on 27/08/2016
    def step_login_change_pwd_change_with_all_validation(self, data, args):
        """
        Change password at login with all validations
        """
        util.step("- Change password at login with all validations")
        expectedResult = "User should be able to Change password successfully for valid scenarios"
        flag, msg = ui_generic.login_change_pwd_change_with_all_validation()
        pass_message = "Change password is completed successfully"
        fail_message = "Change password is not completed successfully - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag

    def step_omm_changePassword_login_old_password(self, data, args):
        """
        Logging in to OMM with Forgot Password Screen with invalid password(s)
        """
        util.step("- Forgot Password Screen Logging in to OMM with old password(s)")
        expectedResult = "User should not be able log in to OMM with Forgot Password Screen with old credential(s)"
#         flag, msg = ui_generic.omm_forgot_password_login(password=g.old_password)
        flag, msg = ui_generic.omm_login_with_password(password=g.old_password)
        pass_message = "OMM Forgot Password Screen login with old password is unsuccessful - %s" % msg
        fail_message = "OMM Forgot Password Screen login with old password is successful - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)

        return flag
    def step_forgot_password(self, data, args):
        """
        Forgot Password option selection in OMM
        """
        util.step("- Forgot Password in OMM")
        expectedResult = "User should be able to GO to Forgot Password screen in OMM"
        flag, msg = ui_generic.omm_forgot_password()
        pass_message = "Forgot Password option selection is successful"
        fail_message = "Forgot Password option selection is not successful - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
    def step_verify_forgotPassword_screen(self, data, args):
        """
        Verify Forgot Password screen
        """
        util.step("- Verify Forgot Password screen")
        expectedResult = "Verify the screen name of Forgot Password screen"
        flag, msg = ui_generic.verify_forgotPassword_screen()
        pass_message = "Forgot Password screen name is displayed properly"
        fail_message = "Forgot Password screen name is not displayed properly - %s" % msg
        args[0].set_pass_fail(flag, expectedResult, pass_message, fail_message)
        return flag
