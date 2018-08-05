#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
    Test case
    ~~~
    This module contains a test case.

    :copyright: (c) 2016 by Nithya_V for Dell.
"""

# from libs.product.omm import omm_step_functions
# from libs.product.omm.omm_step_functions import Steps
from libs.product.omc.standard.base_class import TestBase

from libs.product.omm import omm_lib
from libs.product.omm import idrac_lib


# obj_common = omm_step_functions.Common(Steps)
# obj_omm = omm_step_functions.Omm_class(Steps)


class Testcase_1101(TestBase):

    _group_ = "Test case"

    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)
        
    def setUp(self):
        print "Inside the set up function"
#         self.driver_start_status, msg = obj_common.step_start_driver()
#         print "self.driver_start_status is %s" % self.driver_start_status

    def test_1101_1(self):
        """
        @testcase: 1101.1
        """
#         abc = omm_lib.get_testcase_verification_details('Testcase_102')
#         print abc
#         result = idrac_lib.getEnumerated('DCIM_SystemView')
#         print "result is %s" % result
        #device_name, platform_ver = omm_lib.getIos_devicename_platformversion()
#         system_dict = idrac_lib.get_wsman_dict('DCIM_SystemView', '10.94.195.188', 'root', 'calvin')
#         print "dict is %s" % dict
        #print "device name %s & platform version is %s" % (device_name, platform_ver)
#         step_1 = obj_omm.step_omm_login
# 
#         if self.driver_start_status:
#             print "self.driver_start_status is %s" % self.driver_start_status
#             self.run_steps(step_1, step_args=[self],
#                            continue_on_fail=False)
#         else:
#             self.fail("Failed to start driver")

        #omm_lib.get_gennymotion_devices()
        devID = omm_lib.get_android_device_id()
        print "Device Id is %s" % devID

    def tearDown(self):
        print "inside tear down function"
#         print "self.driver_start_status is %s" % self.driver_start_status
#         if self.driver_start_status:
#             driver_stop_status, msg = obj_common.step_quit_driver()
#             if not driver_stop_status:
#                 self.fail("Failed to stop driver")
