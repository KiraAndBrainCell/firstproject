#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    Test case
    ~~~
    This module contains a test case.

    :copyright: (c) 2016 by Pooja_Rundwal for Dell.
"""
from libs.product.omm import omm_step_functions
from libs.product.omm.omm_step_functions import Steps
from libs.product.omm.standard.base_class import TestBase
from libs.product.omm.standard import util
from libs.product.omm.standard.appium_handler import appium_handler
import time

obj_common = omm_step_functions.Common(Steps)
obj_omm = omm_step_functions.Omm_class(Steps)

appium_handler = appium_handler()


class ESG_TC_53800(TestBase):
 
    _group_ = "Test case"

    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)

    def setUp(self):
        print "Inside the set up function"
        self.driver_start_status, msg = obj_common.step_start_driver()


    def test_53800(self):
        """
        @testcase: ESG_TC_53800
        """
      
        step_0 = obj_omm.step_omm_login
        step_1 = obj_omm.step_add_idrac
        step_2 = obj_omm.step_verify_idrac_basic_inventory
        step_3 = obj_omm.step_delete_idrac

        if self.driver_start_status:
            self.run_steps(step_0,step_1,step_2,step_3, step_args=[self],
                       continue_on_fail=True)
        else:
            self.fail("Failed to start driver")

    def tearDown(self):
        print "Inside the tear down function"
        if self.driver_start_status:
            driver_stop_status, msg = obj_common.step_quit_driver()
            if not driver_stop_status:
                self.fail("Failed to stop driver")
