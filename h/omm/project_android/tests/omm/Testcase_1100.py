#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    Test case
    ~~~
    This test case is for installation with verification of screen names and
    text in each of the screens

    :copyright: (c) 2016 by Nithya_V for Dell.
"""
from libs.product.omm import omm_step_functions
from libs.product.omm.omm_step_functions import Steps
from libs.product.omm.standard.base_class import TestBase
#from libs.product.omm.standard import omm_lib


obj_common = omm_step_functions.Common(Steps)
obj_omm = omm_step_functions.Omm_class(Steps)


class Testcase_1100(TestBase):

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
        
    def test_1100_1(self):
        """
        @testcase: 1100.1
        """
        step_1  =  obj_omm.step_omm_login
       
        step_10 = obj_omm.step_perform_shutdown_using_winrm
        step_11 = obj_omm.step_add_idrac
        step_12 = obj_omm.step_open_power_options
        step_13 = obj_omm.step_verify_offstate_enabled_controls
        step_14 = obj_omm.step_perform_power_on_action
        step_15 = obj_omm.step_open_power_options
        step_16 = obj_omm.step_verify_onstate_enabled_controls
        step_17 = obj_omm.step_perform_shutdown_action
        step_18 = obj_omm.step_open_power_options
        step_19 = obj_omm.step_perform_power_on_action
        step_20 = obj_omm.step_open_power_options
        step_21 = obj_omm.step_perform_power_cycle_action
        step_22 = obj_omm.step_open_power_options
        step_23 = obj_omm.step_perform_shutdownos_action
        step_24 = obj_omm.step_delete_idrac

    
        
        if self.uninstall_app and self.driver_start_status:
            self.run_steps(step_1,step_10,step_11,step_12,step_13,step_14,step_15,step_16,step_17,step_18,step_19,step_20,step_21,step_22,step_23,step_24, step_args=[self],
                           continue_on_fail= True)
        else:
            self.fail("Failed to start driver")

    def tearDown(self):
        print "Inside the tear down function"
        if self.uninstall_app and self.driver_start_status:
            driver_stop_status, msg = obj_common.step_quit_driver()
            if not driver_stop_status:
                self.fail("Failed to stop driver")
