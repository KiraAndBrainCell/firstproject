#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    Test case
    ~~~
    This test case is for installation with Create Password 
    (need to be used for regression testing)

    :copyright: (c) 2016 by Ramanuja_das_pvk for Dell.
"""
from libs.product.omm import omm_step_functions
from libs.product.omm.omm_step_functions import Steps
from libs.product.omm.standard.base_class import TestBase
from libs.product.omm.standard import global_vars
import time

obj_common = omm_step_functions.Common(Steps)
obj_omm = omm_step_functions.Omm_class(Steps)


class ESG_TC_53798(TestBase):

    _group_ = "Test case"

    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)
        self.driver_start_status = False
        self.uninstall_app = False

   

        self.uninstall_app, msg = obj_common.step_uninstall_app()
        if self.uninstall_app:
            self.driver_start_status, msg = obj_common.step_start_driver(auto_accept_alerts=True)
        else:
            self.fail("Failed to un-install the app")

    def test_53798_1(self):
        """
        @testcase: 53798.1
        """

        
        step_1 = obj_omm.step_verify_end_user_license_agreement_text
        step_2 = obj_omm.step_accept_license
        step_3 = obj_omm.step_verify_Diagnostics_and_usage_screenname 
        step_4 = obj_omm.step_verify_Diagnostics_and_usage_text
        step_5 = obj_omm.step_accept_diagnostics_and_usage
        
       
        'To create password and login with verification of all possible dialogues.'
        step_6= obj_omm.step_create_pwd_login_with_all_validation
    
        
        step_7 = obj_omm.step_verify_try_demomode_screenname
        step_8 = obj_omm.step_verify_try_demomode_page_text
        step_9 = obj_omm.step_demo_continue_to_openManage_mobile
  
        'Verify home screen'
        step_10 = obj_omm.step_verify_omm_home_screen
   
        'Restart App'
        step_12 = obj_common.step_restart_app
        time.sleep(10)
        'login attempt with wrong password'
        step_13 = obj_omm.step_omm_login_negative
        step_14 = obj_omm.step_verify_dialogue_wrong_password
        'login attempt with correct password'
        step_15 = obj_omm.step_omm_login_wth_pasword
        'verify home screen'
        step_16 = obj_omm.step_verify_omm_home_screen
        'restart app'
        step_17 = obj_common.step_restart_app
        time.sleep(10)
        'forgot password option'
        step_18 = obj_omm.step_forgot_password
        'verify forgot password screen'
        step_19 = obj_omm.step_verify_forgotPassword_screen
        'login attempt with wrong password'
        step_20 = obj_omm.step_omm_forgotPassword_login_negative
        'Verify the pop up for wrong password'
        step_21 = obj_omm.step_verify_dialogue_wrong_password
        'login attempt with correct password'
        step_22 = obj_omm.step_omm_forgotPassword_login
        'verify home screen'
        step_23 = obj_omm.step_verify_omm_home_screen
 
        #change password at login screen is available only at android. so not applicable for ios [steps 23 to 31]. Need to handle the same with settings menu
        'restart app'
        step_24 = obj_common.step_restart_app
        'change Password steps'
        step_25 = obj_omm.step_login_click_change_password
        'verify change password screen'
        step_26 = obj_omm.step_verify_changePassword_screen
        'To change password and login with verification of all possible dialogues.'
        step_27 = obj_omm.step_login_change_pwd_change_with_all_validation
        
#         'change password'
#         'step_24 = obj_omm.step_change_password'
        'Verify home screen'
        step_28 = obj_omm.step_verify_omm_home_screen

        'restart app'
        step_29 = obj_common.step_restart_app
        'login attempt with old password'
        step_30 = obj_omm.step_omm_changePassword_login_old_password
        'Verify the pop up for wrong password'
        step_31 = obj_omm.step_verify_dialogue_wrong_password
        'login attempt with correct password'
        step_32 = obj_omm.step_omm_login_wth_pasword
        'verify home screen'
        step_33 = obj_omm.step_verify_omm_home_screen

        #'settings_>change password cases: START'
#         'navigate to main menu or home menu'
#         step_32 = obj_omm.step_navigate_mainMenu_settings_changePassword
#         'navigate to home-> settings menu'
#         step_33 = obj_common.step_verify_settings_changePassword_screen
# 
#         'TODO: also verify change password case methods & names which are available as forgot password; also check for ios ios reset & uninstall, auto accept alerts change in between to verify the popup messages'
# 
#         'To change password and login with verification of all possible dialogues.'
#         step_34 = obj_omm.step_settings_change_pwd_change_with_all_validation
#         'Verify home screen'
#         step_35 = obj_omm.step_verify_omm_home_screen
# 
#         'restart app'
#         step_36 = obj_common.step_restart_app
#         'login attempt with old password'
#         step_37 = obj_omm.step_omm_forgotPassword_login_old_password
#         'Verify the pop up for wrong password'
#         step_38 = obj_omm.step_verify_dialogue_wrong_password
#         'login attempt with correct password'
#         step_39 = obj_omm.step_omm_login
#         'verify home screen'
#         step_40 = obj_omm.step_verify_omm_home_screen

        #'settings_>change password cases: END'

        #change password ios messages:
        #case;title;message;button
        #empty currentpwd:Invalid Password;The password you entered does not match the current;OK
        #correct current pwd, empty new pwd;Invalid Password;The password must be at least 4 characters long.
        #correct current pwd, new pwd same as current pwd;Invalid Password;The new password must be different from your current password.
        #correct current pwd, valid new pwd, not matching confirm pwd;Invalid Password;The new password and the re-entered password does not match.
        #correct current pwd, valid new pwd, matching confirm pwd, empty hint;Invalid Password;Password hint is required.
        

        'reset the app as cleanup for test run'
        step_50 = obj_common.step_reset_app


        if self.uninstall_app and self.driver_start_status:
            if global_vars.platform == 'android':
                # android
                self.run_steps(step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_8, step_9, step_10, step_12,step_13, step_14, step_15, step_16, step_17,step_18, step_19, step_20, step_21, step_22, step_23, step_24, step_25, step_26, step_27, step_28, step_29, step_30, step_31, step_32, step_33, step_args=[self], continue_on_fail=True)
            else:
                # ios
                self.run_steps(step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_8, step_9, step_10, step_args=[self], continue_on_fail=True)
          
           # android
            #self.run_steps(step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_8, step_9, step_10, step_11,step_12,step_13, step_14, step_15, step_16, step_17,step_18, step_19, step_20, step_21, step_22, step_23, step_24, step_25, step_26, step_27, step_28, step_29, step_30, step_31, step_32, step_33, step_args=[self], continue_on_fail=True)
#           ios
#             self.run_steps(step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_8, step_9, step_10, step_11, step_12, step_13, step_14, step_15, step_16, step_17,step_18, step_19, step_20, step_21, step_args=[self], continue_on_fail=True)
            
#             self.run_steps(step_23, step_24, step_25, step_26, step_27, step_28, step_29, step_30, step_31, step_args=[self], continue_on_fail=False)
#             self.run_steps(step_13, step_14, step_32, step_33, step_34, step_35, step_36, step_37, step_38, step_39, step_40, step_args=[self], continue_on_fail=True)
            #self.run_steps(step_16, step_17,step_18, step_19, step_20, step_21, step_args=[self], continue_on_fail=False)
        else:
            self.fail("Failed to start driver")

    #def tearDown(self):
        #print "Inside the tear down function"
        #if self.uninstall_app and self.driver_start_status:
           # driver_stop_status, msg = obj_common.step_quit_driver()
            #if not driver_stop_status:
               # self.fail("Failed to stop driver")
    def tearDown(self):
        print "Inside the tear down function"
        if self.driver_start_status:
            driver_stop_status, msg = obj_common.step_quit_driver()
            if not driver_stop_status:
                self.fail("Failed to stop driver")
                      
