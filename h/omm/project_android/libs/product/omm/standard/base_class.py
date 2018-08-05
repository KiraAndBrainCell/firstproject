import traceback
from dellunit.case import DellTestCase
from libs.product.omm.standard import util
from libs.product.omm.standard import global_vars
from libs.product.omm.standard import ui_controls


class TestBase(DellTestCase):

    def __init__(self, *argv, **kwargs):
        DellTestCase.__init__(self, *argv, **kwargs)
        confdict = util.get_config_params()
        self.testcase_id = self._testMethodDoc.split(':')[1].strip()
        print 'test case id : ' + str(self.testcase_id)
        self.windows_ip = confdict['Open_Manage_mobile']['windows_ip']
        self.windows_username = confdict['Open_Manage_mobile']['windows_username']
        self.windows_password = confdict['Open_Manage_mobile']['windows_password']

    def create_step_msg(self, expectedResult, actualResult):
        """
            This function is used for creating step message by taking
            expected Result and actual Result message

            @param  expectedResult   : (String) Expected Result of the test
            @param  actualResult : (String) Actual Result of the test

            @return step_message : (String) step_message to be printed in
                                    report
        """
        step_message = ""
        try:
            step_message = ("<b>EXPECTED RESULT:</b><br/>%s<br/><br/><b>"
            "ACTUAL RESULT:</b><br/>%s<br/>" % (expectedResult, actualResult))
        except:
            traceback.print_exc()
        return step_message

    def set_pass_fail(self, flag, expectedResult, pass_message, fail_message):
        """
            This function is used for setting pass or fail and will be
            called in step_functions module

            @param  flag   : (Bool) Status of Execution - True or False
            @param  expectedResult : (String) Expected Result of the test
            @param  pass_message : (String) Message on test pass
            @param  fail_message : (String) Message on test fail
        """
        try:
            self.assertTrue(flag == True, pass_message)
            self.set_step_message(self.create_step_msg(expectedResult, pass_message))
        except:
#             if global_vars.driver != None:
#                ui_controls.capture_screenshot()
            self.logger.error("Fail:" + fail_message)
            self.fail(self.create_step_msg(expectedResult, fail_message))
