#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    Test case
    ~~~
    This test case is for installation with verification of only screen names 
    (need to be used for BVT testing)

    :copyright: (c) 2016 by Nithya_V for Dell.
"""
from libs.product.omm import omm_step_functions
from libs.product.omm.omm_step_functions import Steps
from libs.product.omm.standard.base_class import TestBase
from libs.product.omm.standard import omm_lib
from libs.product.omm.omm_idrac import ui_idrac
from libs.product.omm.standard.ui_controls import ui_controls
from libs.product.omm.omm_idrac import idrac_lib
from libs.product.omm.standard import omm_lib
from libs.product.omm.standard import global_vars

import time

obj_common = omm_step_functions.Common(Steps)
obj_omm = omm_step_functions.Omm_class(Steps)
ui_controls = ui_controls()



class Testcase_1200(TestBase):

    _group_ = "Test case"

    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)
        self.driver_start_status = False
        self.uninstall_app = False
        
        
    def setUp(self):
        print "Inside the set up function"

        self.driver_start_status, msg = obj_common.step_start_driver()
        if self.driver_start_status:
            omm_lib.uninstall_app('com.iiordanov.freebVNC')
        else:
            self.fail("Driver has not been started successfully")

        
    def test_1200_1(self):
        """
        @testcase: Testcase_1200
        """
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        '####################################################################################'
        '####################################################################################'
        '***************************Work Flow when VNC is enabled & bvnc is not installed'
        '####################################################################################'
        '####################################################################################'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        
        '#####################################################################################'
        'Add code below to Enable VNC & set password & set SSLEncryptionBitLength to Disabled '
        '#####################################################################################'
#         idrac_lib.apply_vnc_attributes('Enable', 1, idrac_ip, idrac_userName, idrac_password,
#                         windows_ip, windows_username, windows_password)
#          idrac_lib.apply_vnc_attributes('Password', 'calvin', idrac_ip, idrac_userName, idrac_password,
#                        windows_ip, windows_username, windows_password)
#         idrac_lib.apply_vnc_attributes('SSLEncryptionBitLength', 'Disabled', idrac_ip, idrac_userName, idrac_password,
#                       windows_ip, windows_username, windows_password)
        '#####################################################################################'
        'Verify license agreement screen and accept license'
        #step_1 = obj_omm.step_verify_license_agreement_screenname
        #step_15 = obj_omm.step_accept_license
        
        'Verify share app Data screen and do not share'
        #step_3 = obj_omm.step_verify_share_appData_screenname
        #step_16 = obj_omm.step_dont_share
        
        'Verify create password screen and create password'
        #step_5 = obj_omm.step_verify_createPassword_screen
        #step_17 = obj_omm.step_create_password
        
        'Verify demo mode screen and continue to OMM'
        #step_7 = obj_omm.step_verify_demomode_screenname
        #step_18 = obj_omm.step_trydemo_continue
       
        step_0 = obj_omm.step_add_idrac      
        'To launch Virtual Console from iDRAC home page'
        time.sleep(8)
        step_1 = obj_omm.step_launchVirtualConsole
        
        'To verify Virtual Console Alert message'
        step_2 = obj_omm.step_virtualConsoleAlertHandle
        
        'To install bvnc app'
        step_3 = obj_omm.step_install_bvnc_app
        
        'Stop the driver'
        step_4 = obj_common.step_stopDriver
        
        'Start driver to start app again'
        step_5 = obj_common.step_startDriver
    
           
        'Launch Virtual console after bvnc install'
        step_6 = obj_omm.step_launchVirtualConsole
        
        'Configure virtual console settings after bvnc install'
        step_7 = obj_omm.step_configureLaunchVirtualConsole
        
        'Verify the Alert on launching VNC'
        step_8 = obj_omm.step_verifylaunchVNCAlert
        
        'Verifying VNC Viewer'
        step_9 = obj_omm.step_verifyVNCViewer
        
        'Stop the driver'
        step_10 = obj_common.step_stopDriver
        
        'Start the driver again to launch bvnc for second time'
        step_11 = obj_common.step_startDriver

        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        '####################################################################################'
        '####################################################################################'
        '***************************Work flow when vnc is already installed'
        '####################################################################################'
        '####################################################################################'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'


        'Launch Virtual Console after bvnc install & after establishing handshake'
        step_12 = obj_omm.step_launchVirtualConsole
        
        'Configure vnc settings after establishing handshake'
        step_13 = obj_omm.step_configureLaunchVirtualConsole
        
        'View VNC Viewer after establishing hand shake'
        step_14 = obj_omm.step_verifyVNCViewer

         
#         'Flow when VNC is disabled'
#         '##### Code to disable VNC to be added ####'
#         idrac_lib.apply_vnc_attributes('Enable', 0, idrac_ip, idrac_userName, idrac_password,
#                       windows_ip, windows_username, windows_password)
#          
#         'Flow when encryption is set to 128-bit or higher '
#         idrac_lib.apply_vnc_attributes('SSLEncryptionBitLength', '128-bit or higher', idrac_ip, idrac_userName, idrac_password,
#                       windows_ip, windows_username, windows_password)
         
#         'Flow when encryption is set to 168-bit or higher'
#         idrac_lib.apply_vnc_attributes('SSLEncryptionBitLength', '168-bit or higher', idrac_ip, idrac_userName, idrac_password,
#                       windows_ip, windows_username, windows_password)
#         
#         'Flow when encryption is set to 256-bit or higher'
#         idrac_lib.apply_vnc_attributes('SSLEncryptionBitLength', '256-bit or higher', idrac_ip, idrac_userName, idrac_password,
#                       windows_ip, windows_username, windows_password)
#         
#         'Flow when encryption is set to AutoNegotiation'
#         idrac_lib.apply_vnc_attributes('SSLEncryptionBitLength', 'Auto Negotiate', idrac_ip, idrac_userName, idrac_password,
#                       windows_ip, windows_username, windows_password)
        
        if self.driver_start_status:
            
            testcase_parameters = {'startServer': False, 'stopServer': False}
            '#####################################################################################'
            'Add merged code to  login to OMM & navigate to the specific idrac page'
            '#####################################################################################'
            time.sleep(15)
            ui_controls.text_box('id=com.dell.omm:id/enter_password_enter_id', value='Dell')
            ui_controls.button('id=com.dell.omm:id/login_button_id')
            ui_controls.button('id=com.dell.omm:id/top_text')
            time.sleep(50)
            '#####################################################################################'
            
            'Execute steps to launch VNC & install bvnc'
            self.run_steps(step_0,step_1,step_2,step_3, step_4, step_5,
                           step_args=[self, testcase_parameters], continue_on_fail=True)

            '#####################################################################################'
            'Add merged code to  login to OMM & navigate to the specific idrac page'
            '#####################################################################################'        
            time.sleep(5)
            ui_controls.text_box('id=com.dell.omm:id/enter_password_enter_id', value='Dell')
            ui_controls.button('id=com.dell.omm:id/login_button_id')
            ui_controls.button('id=com.dell.omm:id/top_text')
            time.sleep(50)
            '#####################################################################################' 
            
            'Execute steps to launch VNC Viewer'
            self.run_steps(step_6, step_7, step_8, step_9, step_10, step_11,
                           step_args=[self, testcase_parameters], continue_on_fail=False)
 
 
            '#####################################################################################'
            'Add merged code to  login to OMM & navigate to the specific idrac page'
            '#####################################################################################'  
            ui_controls.text_box('id=com.dell.omm:id/enter_password_enter_id', value='Dell')
            ui_controls.button('id=com.dell.omm:id/login_button_id')
            ui_controls.button('id=com.dell.omm:id/top_text')
            time.sleep(45)
            '#####################################################################################'  
 
             
            'Execute steps to launch VNC Viewer when bvnc is already installed'
            self.run_steps(step_12, step_13, step_14,
                           step_args=[self, testcase_parameters], continue_on_fail=False)
            
        else:
            self.fail("Failed to start driver")       
        

    def tearDown(self):
        
        print "Inside the tear down function"
        driver_stop_status, msg = obj_common.step_quit_driver()
        if not driver_stop_status:
            self.fail("Failed to stop driver")

