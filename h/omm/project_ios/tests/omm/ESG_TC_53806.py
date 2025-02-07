 #!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    Test case
    ~~~
    This module contains a test case.

    :copyright: (c) 2016 by Pooja_Rundwal for Dell.
"""
import time
from libs.product.omm import omm_step_functions
from libs.product.omm.omm_step_functions import Steps
from libs.product.omm.standard.base_class import TestBase
from libs.product.omm.standard import util
from libs.product.omm.standard.appium_handler import appium_handler

obj_common = omm_step_functions.Common(Steps)
obj_omm = omm_step_functions.Omm_class(Steps)

appium_handler = appium_handler()

class ESG_TC_53806(TestBase):
 
    _group_ = "Test case"

    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)

    def setUp(self):
        print "Inside the set up function"
        self.driver_start_status, msg = obj_common.step_start_driver()
 



    def test_ESG_TC_53806(self):
        """
        @testcase: ESG_TC_53806
        """
        
        step_0 = obj_omm.step_omm_login
        step_1 = obj_omm.step_perform_shutdown_using_winrm
        step_2 = obj_omm.sstep_add_idrac
        step_3 = obj_omm.step_open_power_options
        #step_4 = obj_omm.step_verify_offstate_enabled_controls
        step_5 = obj_omm.step_perform_power_on_action
     
        step_6 = obj_omm.step_open_power_options
        #step_7 = obj_omm.step_verify_onstate_enabled_controls
        step_8 = obj_omm.step_perform_shutdown_action
        step_9 = obj_omm.step_open_power_options
        step_10 = obj_omm.step_perform_power_on_action
        step_11 = obj_omm.step_open_power_options
        step_12 = obj_omm.step_perform_power_cycle_action
        step_13 = obj_omm.step_open_power_options
        step_14 = obj_omm.step_perform_shutdownos_action
        step_15 = obj_omm.step_delete_idrac

        if self.driver_start_status:
            self.run_steps(step_0,step_1,step_2,step_3,step_5,step_6,step_8,step_9,step_10,step_11,step_12,step_13,step_14,step_15,step_args=[self],
                            continue_on_fail=True)
        else:
            self.fail("Failed to start driver")

    def tearDown(self):
        print "Inside the tear down function"
        if self.driver_start_status:
            driver_stop_status, msg = obj_common.step_quit_driver()
            if not driver_stop_status:
                self.fail("Failed to stop driver")
    