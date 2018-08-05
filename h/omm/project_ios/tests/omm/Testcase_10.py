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

obj_common = omm_step_functions.Common(Steps)
obj_omm = omm_step_functions.Omm_class(Steps)


class Testcase_1000(TestBase):

    _group_ = "Test case"

    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)
        self.driver_start_status = False
        self.uninstall_app = False
        
        
    def setUp(self):
        print "Inside the set up function"
        self.uninstall_app,  msg = obj_common.step_uninstall_app()
        if self.uninstall_app:
            self.driver_start_status, msg = obj_common.step_start_driver()
        else:
            self.fail("Failed to un-install the app")
        
    def test_1000_1(self):
        """
        @testcase: 1000.1
        """
        
        'Verify license agreement screen and accept license'
        #step_1 = obj_omm.step_verify_license_agreement_screenname
        step_2 = obj_omm.step_accept_license
        
        'Verify share app Data screen and do not share'
        #step_3 = obj_omm.step_verify_share_appData_screenname
        step_4 = obj_omm.step_dont_share
        
        'Verify create password screen and create password'
        step_5 = obj_omm.step_verify_createPassword_screen
        step_6 = obj_omm.step_create_password
        
        'Verify demo mode screen and continue to OMM'
        step_7 = obj_omm.step_verify_demomode_screenname
        step_8 = obj_omm.step_trydemo_continue
        
        'Verify home screen'
        step_9 = obj_omm.step_verify_omm_home_screen

        'Navigate to About Screen and verify'
        step_10 = obj_omm.step_navigate_mainMenu
        step_11 = obj_omm.step_navigate_aboutScreen
        step_12 = obj_omm.step_verify_aboutScreen
        
        'Verify Version and Build number in about screen'
        step_13 = obj_omm.step_verify_versionBuildNumber
        
        if self.uninstall_app and self.driver_start_status:
            self.run_steps(step_2,step_4, step_5,step_6,step_7,
                         step_8, step_9, step_10, step_11,
                           step_12, step_13,
                           step_args=[self], continue_on_fail=False)
        else:
            self.fail("Failed to start driver")

    def tearDown(self):
        print "Inside the tear down function"
        if self.uninstall_app and self.driver_start_status:
            driver_stop_status, msg = obj_common.step_quit_driver()
            if not driver_stop_status:
                self.fail("Failed to stop driver")
