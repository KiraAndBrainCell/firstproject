""""
This module contains all the modules related to omm common module
"""
from time import sleep
import traceback

from libs.product.omm.standard.appium_handler import appium_handler
from libs.product.omm.standard.ui_controls import ui_controls
from libs.product.omm.standard import global_vars
from libs.product.omm.standard import omm_lib
from libs.product.omm.standard import util

'Creating objects'
ui_controls = ui_controls()

'Retrieving variables'
g = global_vars
get_obj_identifier = omm_lib.get_obj_identifier


def accept_license():
    """
    This function is used for accepting license on a fresh installation

    Function Owner : Nagarjuna

    Date created : 21/11/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True

    try:
        sleep(5)
        if g.platform == 'android':
            sleep(3)
            'Click on license accept button'
            flag1 = ui_controls.button(get_obj_identifier('license_accept_btn'))
            
                    

            status = False if not (flag1) else True
        else:
           
            'Click on Agree button in EULA page for IOS'
            flag = ui_controls.button(get_obj_identifier('license_accept_btn'))
            status = flag

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg

def verify_eula_lables_and_text():
    """
    This function is used to verify EULA labels and EULA text

    Function Owner : Nagarjuna

    Date created : 21/11/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True

    try:
        sleep(5)
        if g.platform == 'android':

            'verify end user license agreement label'
            flag1,msg = pagelabel_element_textvalidation('EUL_agrement_labl','End User License Agreement')
            sleep(4)   
             
            'Read verification input data of EULA acknowledge text'
            text_to_verify = util.read_file(g.demomode_acknowldge_agrement_txt)
              
            'verify EULA acknowledge agreement text'
            flag2,msg = element_textvalidation('EULA_acknowledge_agrmrnt_text',text_to_verify)
            sleep(4)      
            
            'verify view the full EULA here label'
            flag3,msg = pagelabel_element_textvalidation('EULA_full_view','View the full EULA here')
            sleep(4)   
            'click view the full EULA element to expand end user license agreemnt '    
            flag4 = ui_controls.Click(get_obj_identifier('EULA_full_view'))            
        
            'Read verification input data of EULA text'
            text_to_verify = util.read_file(g.demomode_EULA_agrement_txt)

            'verify EULA  agreement text'
            flag5,msg = element_textvalidation('EULAagrement_text',text_to_verify)
            sleep(4)           

            status = False if not (flag1 and flag2 and flag3 and flag4 and flag5) else True
        else:
            sleep(5)
           
            'Verify EULA label in EULA screen of IOS'
            flag1 = ui_controls.ui_element(get_obj_identifier('EUL_agrement_labl'))
           
            flag2,msg = value_textvalidation('EUL_agrement_labl','End User License Agreement')
            sleep(4)   
             
            flag3 = ui_controls.ui_element(get_obj_identifier('EULA_acknowldge_agrmrnt_text'))
            sleep(4)      
            
            'verify view the full EULA here label'
            flag4 = ui_controls.ui_element(get_obj_identifier('EULA_full_view'))
            flag5,msg = label_textvalidation('EULA_full_view','View the full EULA here.')
            sleep(4)   
            'click view the full EULA element to expand end user license agreemnt '    
            flag6 = ui_controls.button(get_obj_identifier('EULA_full_view'))  
            print "clicked on view the full EULA here"          
        
            'Click on Agree button in EULA page for IOS'
            flag7 = ui_controls.button(get_obj_identifier('license_accept_btn'))
            print "clicked on licence button"
            status = False if not (flag1 and flag2 and  flag3 and flag4 and flag5 and flag6 and flag7) else True

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg


def verify_diagnostics_and_usage_screen_name():
    """
    This function is used for verify diagnostics and usage screen name

    Function Owner : Nagarjuna

    Date created : 21/11/2016

    @return True/False : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        sleep(10)
        if g.platform == 'android':

            'Verify screen name of diagnostics and usage page'
            sleep(3)
           
            flag1,msg = pagelabel_element_textvalidation('Diagnostics_usage_lbl','Diagnostics and Usage')
            
            
            flag = False if not (flag1) else True
            
        else:

            
            flag1,msg = label_textvalidation('Diagnostics_usage_lbl','Diagnostics and Usage')
          
            flag = False if not (flag1) else True
        if not flag:
            return False, msg
        else:
            print "License agreement screen name is displayed properly"
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        return False, msg
    return True, msg


def verify_diagnostics_and_usage_text():
    """
    This function is used for verify diagnostics and usage lable and text

    Function Owner : Nagarjuna

    Date created : 21/11/2016

    @return True/False : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        sleep(10)
        if g.platform == 'android':
            sleep(3)
            'verify end user license agreement label'
            flag1,msg = pagelabel_element_textvalidation('Diagnostics_usage_lbl','Diagnostics and Usage')
            sleep(4)      
            'Read verification input data'
            text_to_verify = util.read_file(g.demomode_Diagnostcs_nd_usage_txt)
            'verify end user license agreement label'
            flag2,msg = element_textvalidation('Diagnostics_usage_txt',text_to_verify)
            
            flag = False if not (flag1 and flag2) else True
        else:

            'verify end user license agreement label'
            #flag1,msg = element_textvalidation('Diagnostics_usage_lbl','Diagnostics and Usage')
            'Verify diagnostics usage text'
            flag1 = ui_controls.ui_element(get_obj_identifier('Diagnostics_usage_lbl'))
            'Verify diagnostics usage text'
            flag2 = ui_controls.ui_element(get_obj_identifier('Diagnostics_usage_txt'))
            
            sleep(4)      
            'Read verification input data'
            #text_to_verify = util.read_file(g.demomode_Diagnostcs_nd_usage_txt)
            #'verify end user license agreement label'
            #flag2,msg = element_textvalidation('Diagnostics_usage_txt',text_to_verify)
            flag = False if not (flag1 and flag2) else True
        if not flag:
            return False, msg
        else:
            print "License agreement screen name is displayed properly"
            
            
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        return False, msg
    return True, msg   

 
def accept_diagnostics_and_usage():
    """
    This function is used for accepting diagnostics and usage

    Function Owner : Nagarjuna

    Date created : 21/11/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True

    try:
        sleep(5)
        if g.platform == 'android':
            sleep(3)
            'Click on diagnostics and usage agree button'
            flag1 = ui_controls.button(get_obj_identifier('diagnostics_accept_btn'))

            status = False if not (flag1) else True
        else:
           
            'Click on Agree button in EULA page for IOS'
            flag = ui_controls.button(get_obj_identifier('diagnostics_accept_btn'))
            status = flag

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg


def verify_try_demomode_page_text():
    """
    This function is used for verify diagnostics and usage label and text

    Function Owner : Nagarjuna

    Date created : 21/11/2016

    @return True/False : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        sleep(10)
        if g.platform == 'android':

            'verify the text of demo mode label'
            flag1,msg = element_textvalidation('demomoe_lbl','Demo Mode')
            sleep(4)      
            'Read verification input data'
            text_to_verify = util.read_file(g.Try_demomode_txt)
            'verify the text of demo mode'
            flag2,msg = element_textvalidation('demo_demoVersion_textview',text_to_verify)
            
            flag = False if not (flag1 and flag2) else True
        else:

            'verify demo mode screen label'
            flag1 = ui_controls.ui_element(get_obj_identifier('demo_demoMode_textview'))

            'Verify for the text of demo mode'
            #flag2 = ui_controls.ui_element(get_obj_identifier('demo_demoVersion_textview'))
            flag = False if not (flag1) else True
        if not flag:
            return False, msg
        else:
            print "License agreement screen name is displayed properly"
            
            
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        return False, msg
    return True, msg 
  

def try_continue_to_openManage_mobile():
    """
   This function is used for selecting continue to openManage mobile

    Function Owner : Nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

            'Getting y_elem as destination element'
            y_elem = ui_controls.ui_element(get_obj_identifier('common_widget_scrollview'))

            'Getting x_elem as source element'
            x_elem = ui_controls.ui_element(get_obj_identifier('demo_tryDemoMode_btn'))

            'Scroll the element from x elem to y elem'
            flag1 = ui_controls.scroll_element(x_elem, y_elem)
            sleep(3)

            'Click on Continue to OMM button'
            flag2 = ui_controls.button(get_obj_identifier('demo_continueToOmm_btn'))

            status = False if not (flag1 and flag2) else True
        else:
            sleep(3)
            flag1=ui_controls.swipe_up()
            sleep(3)
            'Click on Continue to OMM button in IOS'
            flag2 = ui_controls.button(get_obj_identifier('demo_continueToOmm_btn'))
            sleep(4)
         
            status = False if not (flag1 and flag2) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg
    
  




 











































   
def demomode_accept_license():
    """
    This function is used for accepting license on a fresh installation

    Function Owner : Nithya_V

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
#     import genericfunctions
#     genericfunctions.accept_license_function()

    try:
        sleep(5)
        if g.platform == 'android':

            # agrment_lbl = ui_controls.text_view(get_obj_identifier('EUL_agrement_labl'))
            #if agrment_lbl.strip() =='End User License Agreement':   
                #print "End user License Agreement label is displaying properly"      
            #else:
                # print "End user License Agreement label is not displaying properly"
            'verify end user license agreement label'
            flag1,msg = element_textvalidation('EUL_agrement_labl','End User License Agreement')
            sleep(4)   
             

            #'get the text view of the Eula acknowledge agreement text'
            #Agrement_text_view = ui_controls.text_view(get_obj_identifier('EULA_acknowledge_agrmrnt_text'))

            'Read verification input data'
            text_to_verify = util.read_file(g.demomode_acknowldge_agrement_txt)
            #if not text_to_verify:
                #print "Unable to retrieve text to verify demo mode idrac device text input file"
                #return False, msg
            #if text_to_verify.strip() == Agrement_text_view.strip():
                #print "DemoMode Eula agreement acknowledgement  report verified sucessfully"
            #else:
                #print "DemoMode Eula agreement acknowledgement  report is not verified sucessfully"  
                
            'verify Eula acknowledge agreement text'
            flag2,msg = element_textvalidation('EULA_acknowledge_agrmrnt_text',text_to_verify)
            sleep(4)       
            'click on eula full view element'    
            flag3 = ui_controls.Click(get_obj_identifier('EULA_full_view'))            
            #'get the text view of the Eula whole agreement text'
            #Eula_text_view = ui_controls.text_view(get_obj_identifier('EULAagrement_text'))

            'Read verification input data'
            text_to_verify = util.read_file(g.demomode_EULA_agrement_txt)

            # if not text_to_verify:
                #print "Unable to retrieve text to verify demo mode idrac device text input file"
                #return False, msg
            # if text_to_verify.strip() == Eula_text_view.strip():
                #print "DemoMode Eula agreement  report verified sucessfully"
            #else:
                # print "DemoMode Eula agreement device report  verified unsucessfully"   
            'verify Eula acknowledge agreement text'
            flag3,msg = element_textvalidation('EULAagrement_text',text_to_verify)
            sleep(4)           

            'Click on license accept button'
            flag4 = ui_controls.button(get_obj_identifier('agree'))
            'verify diagnostics and usage label'
            #diagnotsic_usage_lbl = ui_controls.text_view(get_obj_identifier('Diagnostics_usage_lbl'))
            #if diagnotsic_usage_lbl.strip() =='Diagnostics and Usage':   
                #print "Diagnostics and Usage label is displaying properly"      
            #else:
                #print "Diagnostics and Usage label is not displaying properly"
            'verify end user license agreement label'
            flag5,msg = element_textvalidation('Diagnostics_usage_lbl','Diagnostics and Usage')
            sleep(4)      

            ''
            # Diagnostic_usge_txt_view = ui_controls.text_view(get_obj_identifier('Diagnostics_usage_txt'))
            #if not Diagnostic_usge_txt_view:
                #print "Unable to retrieve text of diagnostics and usage text from application"
                # return False, msg

            'Read verification input data'
            text_to_verify = util.read_file(g.demomode_Diagnostcs_nd_usage_txt)

            #if not text_to_verify:
                #print "Unable to retrieve text to verify demo mode diagnostics and usage text file"
                #return False, msg
            #if text_to_verify.strip() == Diagnostic_usge_txt_view .strip():
                # print "DemoMode Diagnostics and Usage report verified sucessfully"
            #else:
                #print "DemoMode Diagnostics and Usage report verified unsucessfully" 
             
            'verify end user license agreement label'
            flag6,msg = element_textvalidation('Diagnostics_usage_txt',text_to_verify)
            sleep(4) 
            flag7 = ui_controls.button(get_obj_identifier('agree'))

            status = False if not (flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7) else True
        else:
            'Click on Agree button in EULA page for IOS'
            flag = ui_controls.button(get_obj_identifier('a'))
            status = flag

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg




def dnt_share_app():
    """
    This function is used for 'Do not share application' with developers

    Function Owner : Nithya_V

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:

        'Click on Do not share button'
        flag1 = ui_controls.button(get_obj_identifier('a'))
        #flag2 = ui_controls.button(get_obj_identifier('share_dontShare_btn'))
     
   

        status = False if not(flag1) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def create_pwd_login():
    """
    This function is used for creating password and login

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'Enter the password in Create password text box'
            flag1 = ui_controls.text_box(get_obj_identifier('login_createPassword_txt'), value=g.password)

            'Checks for the keyboard presence and hides it'
            flag2 = ui_controls.hide_keyboard()

            'Enter the confirm password in Confirm Password text box'
            flag3 = ui_controls.text_box(get_obj_identifier('login_confirmPassword_txt'), value=g.password)

            'Checks for the keyboard presence and hides it'
            flag4 = ui_controls.hide_keyboard()

            'Click on create password login button'
            flag5 = ui_controls.button(get_obj_identifier('login_createPasswordLogin_btn')) 

            status = False if not (flag1 and flag2 and flag3 and flag4 and flag5) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            'Setting values on Confirm Password text box in ios.'
            flag2 = ui_controls.setValue(get_obj_identifier('login_confirmPassword_txt'), g.password)

            'Setting values on Password Hint text box in ios.'
            #flag3 = ui_controls.setValue(get_obj_identifier('login_passwordHint_txt'), g.password_hint)

            'Click on Create Password button in IOS'
            flag4 = ui_controls.button(get_obj_identifier('login_createPasswordLogin_btn')) 
            sleep(10)

            status = False if not (flag1 and flag2 and flag4) else True


    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def demomode_create_pwd_login():
    """
    This function is used for creating password and login

    Function Owner : Nithya_V

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'Enter the password in Create password text box'
            flag1 = ui_controls.text_box(get_obj_identifier('login_createPassword_txt'), value=g.password)

            'Checks for the keyboard presence and hides it'
            flag2 = ui_controls.hide_keyboard()

            'Enter the confirm password in Confirm Password text box'
            flag3 = ui_controls.text_box(get_obj_identifier('login_confirmPassword_txt'), value=g.password)

            'Checks for the keyboard presence and hides it'
            flag4 = ui_controls.hide_keyboard()

            'Click on create password login button'
            flag5 = ui_controls.button(get_obj_identifier('login_createPasswordLogin_btn')) 

            status = False if not (flag1 and flag2 and flag3 and flag4  and flag5) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            'Setting values on Confirm Password text box in ios.'
            flag2 = ui_controls.setValue(get_obj_identifier('login_confirmPassword_txt'), g.password)

            'Setting values on Password Hint text box in ios.'
            flag3 = ui_controls.setValue(get_obj_identifier('login_passwordHint_txt'), g.password_hint)

            'Click on Create Password button in IOS'
            flag4 = ui_controls.button(get_obj_identifier('login_createPasswordLogin_btn')) 

            status = False if not (flag1 and flag2 and flag3 and flag4) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg



def try_demo_continue():
    """
   This function is used for selecting try demo mode or continue

    Function Owner : Nithya_V

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

            'Getting y_elem as destination element'
            y_elem = ui_controls.ui_element(get_obj_identifier('common_widget_scrollview'))

            'Getting x_elem as source element'
            x_elem = ui_controls.ui_element(get_obj_identifier('demo_tryDemoMode_btn'))

            'Scroll the element from x elem to y elem'
            flag1 = ui_controls.scroll_element(x_elem, y_elem)
            sleep(3)

            'Click on Continue to OMM button'
            flag2 = ui_controls.button(get_obj_identifier('demo_continueToOmm_btn'))

            status = False if not (flag1 and flag2) else True
        else:
            sleep(3)
            'Click on Continue to OMM button in IOS'
            flag1 = ui_controls.button(get_obj_identifier('demo_continueToOmm_btn'))
            sleep(5)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def try_demo_mode_now():
    """
   This function is used for selecting try demo mode or continue

    Function Owner : Nithya_V

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        sleep(10)
        if g.platform == 'android':

            'Getting y_elem as destination element'
            y_elem = ui_controls.ui_element(get_obj_identifier('common_widget_scrollview'))

            'Getting x_elem as source element'
            x_elem = ui_controls.ui_element(get_obj_identifier('demo_tryDemoMode_btn'))

            'Scroll the element from x elem to y elem'
            flag1 = ui_controls.scroll_element(x_elem, y_elem)
            sleep(3)

            'Click on Continue to OMM button'
            flag2 = ui_controls.button(get_obj_identifier('Try_demomode_now'))

            status = False if not (flag1 and flag2) else True
        else:
            'Click on Continue to OMM button in IOS'
            flag1 = ui_controls.button(get_obj_identifier('demo_continueToOmm_btn'))

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg






def demo_mode_try_now():

    """
    This function is used for selecting try demo mode continue

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
      
        if g.platform == 'android':
            'verify label text of try in demo mode'
            Try_demomode_lbl = ui_controls.text_view(get_obj_identifier('Try_demomode_lbl'))
            if Try_demomode_lbl.strip() == 'Demo Mode':
                print "Try demo mode page label is displaying properly"
            else:
                print "Try demo mode page label is not displaying properly"
            'get the text of try in demo mode page'
            Try_demomode_txt_view = ui_controls.text_view(get_obj_identifier('Try_demomode_txt'))
            'Read verification input text from try demo mode text file'
            text_to_verify = util.read_file(g.Try_demomode_txt)
            if not text_to_verify:
                print "Unable to retrieve text of try  demo mode  input text file"
                return False, msg
            if text_to_verify.strip() == Try_demomode_txt_view.strip():
                print "Try demo mode page text verified successfully"
            else:
                print "Try demo mode page text verified unsuccessfully"

            'Getting y_elem as destination element'
            y_elem = ui_controls.ui_element(get_obj_identifier('common_widget_scrollview'))
            'Getting x_elem as source element'
            x_elem = ui_controls.ui_element(get_obj_identifier('demo_tryDemoMode_btn'))
            'Scroll the element from x element to y element'
            flag1 = ui_controls.scroll_element(x_elem, y_elem)
            sleep(3)
            'Click on Continue to OMM button'
            flag2 = ui_controls.button(get_obj_identifier('demo_tryDemoMode_btn'))
            status = False if not (flag1 and flag2) else True
        else:
           
            sleep(3)
            flag1=ui_controls.swipe_up()
            'Click on Continue to OMM button in IOS'
            #flag1 = ui_controls.button(get_obj_identifier('demo_tryDemoMode_btn'))
            flag2 = ui_controls.button(get_obj_identifier(' '))
            status = False if not (flag1 and flag2) else True

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg



def omm_login():
    """
    This function is used for creating password and login

    Function Owner : Nithya_V

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            sleep(5)
            'Enters value in password text box based on the user inputs'
            flag1 = ui_controls.text_box(get_obj_identifier('login_enterPassword_txt'), value=g.password)
            sleep(3)
            'Clicks on the login button'
            flag2 = ui_controls.button(get_obj_identifier('login_createPasswordLogin_btn'))
        
            status = False if not (flag1 and flag2) else True
        else:    
            'Enters value in password text box based on the user inputs'
            flag1 = ui_controls.setValue(get_obj_identifier('login_enterPassword_txt'), value=g.password)

            'Clicks on the login button'
            flag2 = ui_controls.button(get_obj_identifier('login_btn'))
            
            status = False if not (flag1 and flag2) else True
        
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def verify_omm_license_agrmt_screenname():
    """
    This function is used for verifying the omm license screen name

    Function Owner : Nithya_V

    Date created : 5/05/2016

    @return True/False : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        sleep(10)
        if g.platform == 'android':
           

            'Verify screen name of License agreement page'

            flag1 = ui_controls.ui_element(get_obj_identifier('license_omm_textview'))
        else:
            sleep(10)
            #flag0 =ui_controls.updte_setngs()
            'Verify EULA label in EULA screen of IOS'
            flag1 = ui_controls.ui_element(get_obj_identifier('license_eula_lbl'))

            'Verify for Dell OMM label in EULA screen of IOS'
           # flag2 = ui_controls.ui_element(get_obj_identifier('license_forDellOmm_lbl'))
            flag = False if not (flag1) else True
        if not flag:
            return False, msg
        else:
            print "License agreement screen name is displayed properly"
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        return False, msg
    return True, msg


def verify_omm_license_agrmt():
    """
    This function is used for verifying the omm license page

    Function Owner : Nithya_V

    Date created : 5/05/2016

    @return True/False : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        if g.platform == 'android':
            'Read verification input data'
            text_to_verify = util.read_file(g.license_agrmt_input)
            if not text_to_verify:
                print "Unable to retrive text to verify license agreement input file"
                return False, msg

            'Getting text from License agreement page'
            text = ui_controls.text_view(get_obj_identifier('license_agreeText_textView'))
            if not text:
                print "Text retrieved from text view is empty"
                return False, msg
            'Comparing text retrieved from UI with verification input text'
            if text_to_verify.strip() == text.strip():
                print ("License agreement displayed in UI is matching with text to verify for license agreement") + \
                      ("Verification Text- %s" % text_to_verify) + \
                       ("############Text from UI is #########\n %s\n" % text)
            else:
                return False, msg
        else:
            print "IOS value and text does nto return entire license text. Hence cannot validate license text in IOS"
            return True, msg

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        return False, msg
    return True, msg


def verify_share_app_screen_name():
    """
    This function is used for verifying text in share app data screen name

    Function Owner : Nithya_V

    Date created : 5/05/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        if g.platform == 'android':
            'Verify screen name of Share App screen name'
            flag = ui_controls.ui_element(get_obj_identifier('share_appDataScreenName_textview'))
        else:
            text_heading = ui_controls.text_view(get_obj_identifier('share_appData_heading_textView'), value=True)
            if not text_heading:
                print "Text retrieved from text view is empty"
                return False, msg

            'Comparing text retrieved from UI with verification input '
            if g.shareApp_data_ios.strip() == text_heading.strip():
                print ("Share App data displayed in UI is matching with text to verify") + \
                      ("Verification Text- %s" % g.shareApp_data_ios) + \
                       ("############Text from UI is #########\n %s\n" % text_heading)
                flag = True
        if not flag:
            return False, msg
        else:
            print "Share app  screen name is displayed properly"
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        return False, msg
    return True, msg


def verify_share_app_screen():
    """
    This function is used for verifying text in share app data screen

    Function Owner : Nithya_V

    Date created : 5/05/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        # verifying sub-heding only for android
        if g.platform == 'android':
            'Getting text of Share app Data heading from Share app Data screen'
            text_heading = ui_controls.text_view(get_obj_identifier('share_appData_heading_textView'))
            if not text_heading:
                print "Text retrieved from text view is empty"
                return False, msg

            'Comparing text retrieved from UI with verification input '
            if g.shareApp_data.strip() == text_heading.strip():
                print ("Share App data displayed in UI is matching with text to verify") + \
                      ("Verification Text- %s" % g.shareApp_data) + \
                       ("############Text from UI is #########\n %s\n" % text_heading)

        'Read verification input data'
        text_to_verify = util.read_file(g.shareAppData_input)

        if not text_to_verify:
            print "Unable to retrive text to verify share app Data input file"
            return False, msg

        if g.platform == 'android':
            'Getting text of Share app Data body from Share app Data screen'
            text_body = ui_controls.text_view(get_obj_identifier('share_appData_body_textView'))
        else:
            'Getting text of Share app Data body of IOS app Data Screen'
            text_body = ui_controls.text_view(get_obj_identifier('share_appData_body_textView'), value=True)
            text_to_verify = '%s\n\n%s'  % (g.shareApp_data, text_to_verify)
        if not text_body:
            print "Text retrieved from text view is empty"
            return False, msg
        print "Text to verify is %s\n" % text_to_verify

        'Comparing text retrieved from UI with verification input text'
        if text_to_verify.strip() == text_body.strip():
            print ("License agreement displayed in UI is matching with text to verify for license agreement") + \
                  ("Verification Text- %s" % text_to_verify) + \
                   ("############Text from UI is #########\n %s\n" % text_body)
        else:
            return False, msg

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        return False, msg
    return True, msg


def verify_createPassword_screen():

    """
    This function is used for verifying Create Password screen name

    Function Owner : Nithya_V

    Date created : 6/05/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        'Getting Create Password text_view object'
        flag = ui_controls.ui_element(get_obj_identifier('login_createPassword_textview'))

        if g.platform == 'ios':
            flag2 = ui_controls.ui_element(get_obj_identifier('login_createPassword_lbl'))
            flag = flag2
        if flag:
            print "Create Password Screen Name is displayed properly"
            return True, msg
        else:
            print "Create Password Screen Name is not displayed properly"

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return True, msg


def verify_try_demoMode_screenname():
    """
    This function is used for verifying demo mode screen name

    Function Owner : Nithya_V

    Date created : 6/05/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        sleep(3)
        'Getting Create Password text_view object'
        flag = ui_controls.ui_element(get_obj_identifier('demo_demoMode_textview'))

        if g.platform == 'ios':
            flag2,msg = label_textvalidation('demo_demoMode_textview','Demo Mode')
          
            flag = flag2
        if flag:
            print "Demo Mode Screen Name is displayed properly"
            return True, msg
        else:
            print "Demo Mode Screen Name is not displayed properly"

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return True, msg
   


def verify_demoMode_screen():
    """
    This function is used for verifying texts in Demo mode screen

    Function Owner : Nithya_V

    Date created : 6/05/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        'Getting text of Demo mode text view with details'
        if g.platform == 'android':
            text_demoversion = ui_controls.text_view(get_obj_identifier('demo_demoVersion_textview'))
        else:
            text_demoversion = ui_controls.text_view(get_obj_identifier('demo_demoVersion_textview'), value=True)
        if not text_demoversion:
            print "Text retrieved from text view is empty"
            return False, msg

        'Read verification input data'
        text_to_verify = util.read_file(g.DemoMode_input)
        print "text to verify is %s" % text_to_verify
        if not text_to_verify:
            print "Unable to retrive text to verify share app Data input file"
            return False, msg

        'Comparing text retrieved from UI with verification input text'
        if text_to_verify.strip() == text_demoversion.strip():
            print ("License agreement displayed in UI is matching with text to verify for license agreement") + \
                  ("Verification Text- %s" % text_to_verify) + \
                   ("############Text from UI is #########\n %s\n" % text_demoversion)
        else:
            return False, msg

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        return False, msg
    return True, msg


def verify_homeScreen():
    """
    This function is used for verifying home screen name

    Function Owner : Nithya_V

    Date created : 19/05/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        'Getting home page label for IOS - Open Manage Essentials'
        if g.platform == 'ios':
            text_view = ui_controls.text_view(get_obj_identifier('home_OME_lbl'), value=True)
            text_toverify = g.ios_homeScreen_label
        else:
            sleep(3)
            text_view = ui_controls.text_view(get_obj_identifier('home_OME_lbl'))
            text_toverify = g.android_homeScreen_label

            'Verifying whether home screen label is Open Manage Essentials for IOS'
            if text_view.strip() == text_toverify :
                print "Home Screen label is verified successfully"
            else:
                print "Home Screen label is not verified successfully"
                return False, msg
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return True, msg


def navigate_mainMenu():
    """
    This function is used for navigating to the main menu where various
    OMM options such as About, settings etc are available
 
    Function Owner : Nithya_V
 
    Date created : 19/05/2016
 
    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, flag = "", False
    try:  
        'Click on the main menu item in OMM home page'
        flag = ui_controls.button(get_obj_identifier('mnu_btn'))
        if flag:
            print "Main menu icon in home page is clicked"

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return flag, msg

def  nnavigate_mainMenu():
    """
    This internal function is used for creating password and login

    Function Owner : Ramanuja_das_pvk

    Date created : 20/09/2016

    @param  password   : (String) password
    @param  re_enter_password : (String) re-enter password
    @param  hint : (String) password hint

    @return status : (bool)status of execution.if successful True else False
    """
    if g.platform == 'android':
        'Enter the password in Create password text box'
        
        flag1 = ui_controls.hide_keyboard()

        'Enter password hint in Password Hint text box'
        #flag5 = ui_controls.text_box(get_obj_identifier('login_passwordHint_txt'), value=hint)

        'Checks for the keyboard presence and hides it'
        #flag6 = ui_controls.hide_keyboard()

      

        status = False if not ( flag1) else True
    else:
        'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
        flag1=ui_controls.Click(get_obj_identifier('mnu_btn'))

        status = False if not (flag1) else True
    return status



def navigate_aboutScreen():
    """
    This function is used for navigating to the About Screen
 
    Function Owner : Nithya_V
 
    Date created : 19/05/2016
 
    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, flag = "", False
    try:
        if g.platform == 'ios':
            'Click on the main menu item in OMM home page'
            flag = ui_controls.button(get_obj_identifier('mainMenu_about_lnk'))
            if flag:
                print "About link in main menu is clicked"
        else:
            main_menu_items = ui_controls.ui_elements(get_obj_identifier('mainMenu_title_textView'))
            for item in main_menu_items:
                print item.get_attribute('text')
                if item.get_attribute('text').strip() == g.aboutScreen_label:
                    item.click()
                    flag = True
                    print "About link in main menu has been clicked"
                    break
        sleep(3) 
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return flag, msg


def verify_aboutScreen():
    """
    This function is used for verifying the About Screen

    Function Owner : Nithya_V

    Date created : 19/05/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        'Getting about page label for IOS - About'
        if g.platform == 'ios':
            text_view = ui_controls.text_view(get_obj_identifier('mainMenu_about_lbl'), value=True)
        else:
            text_view = ui_controls.text_view(get_obj_identifier('mainMenu_about_lbl'))

            'Verifying whether about screen label is About for IOS'
            if text_view.strip() == g.aboutScreen_label :
                print "About Screen label is verified successfully"
            else:
                print "About Screen label is not verified successfully"
                return False, msg
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return True, msg


def verify_ios_versionNumber():
    """
    This function is used for verifying Version build number
 
    Function Owner : Nithya_V
 
    Date created : 19/05/2016
 
    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        'Getting Version number for IOS '
        if g.platform == 'ios':
            text_view = ui_controls.text_view(get_obj_identifier('about_versionNumber_lbl'), label=True)

            'Verifying whether Version number is matching with expected value IOS'
            if g.platform == 'ios' and text_view.strip() == g.version_number :
                print "Version number is verified successfully. Expected : %s. Actual : %s" % (g.version_number,text_view.strip())
            else:
                if g.platform == 'ios':
                    print "Version number is not verified successfully. Expected : %s. Actual : %s" % (g.version_number, text_view.strip())
                return False, msg
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return True, msg

def value_textvalidation(objectidentifier,validationtext):
    """
    This function is used to validate text returned by an ui element for test case validation purpose.

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'Here we will pass objectidentifier for required element'
        text_heading = ui_controls.text_view(get_obj_identifier(objectidentifier),value=True)
        print "Current text returned by UI is==>"+str(text_heading)

        'To check if it is returning empty value here'
        if not text_heading:
            print str(validationtext)+" text does not exist and it is returning empty value."
            return False, msg

        'Comparing text retrieved from UI with validation  text'
        if validationtext.strip() == text_heading.strip():
            print (str(validationtext)+" text has been found!!!")
        else:
            print("Sorry!!!text has been mismatched,it should be "+str(validationtext))
            print ("Text shown at UI is==>"+str(text_heading))
            return False, msg  

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg
def label_textvalidation(objectidentifier,validationtext):
    """
    This function is used to validate text returned by an ui element for test case validation purpose.

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'Here we will pass objectidentifier for required element'
        text_heading = ui_controls.text_view(get_obj_identifier(objectidentifier),label=True)
        print "Current text returned by UI is==>"+str(text_heading)

        'To check if it is returning empty value here'
        if not text_heading:
            print str(validationtext)+" text does not exist and it is returning empty value."
            return False, msg

        'Comparing text retrieved from UI with validation  text'
        if validationtext.strip() == text_heading.strip():
            print (str(validationtext)+" text has been found!!!")
        else:
            print("Sorry!!!text has been mismatched,it should be "+str(validationtext))
            print ("Text shown at UI is==>"+str(text_heading))
            return False, msg  

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg

def element_textvalidation(objectidentifier,validationtext):
    """
    This function is used to validate text returned by an ui element for test case validation purpose.

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'Here we will pass objectidentifier for required element'
        text_heading = ui_controls.text_view(get_obj_identifier(objectidentifier))
        print "Current text returned by UI is==>"+str(text_heading)

        'To check if it is returning empty value here'
        if not text_heading:
            print str(validationtext)+" text does not exist and it is returning empty value."
            return False, msg

        'Comparing text retrieved from UI with validation  text'
        if validationtext.strip() == text_heading.strip():
            print (str(validationtext)+" text has been found!!!")
        else:
            print("Sorry!!!text has been mismatched,it should be "+str(validationtext))
            print ("Text shown at UI is==>"+str(text_heading))
            return False, msg  

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg
def pagelabel_element_textvalidation(objectidentifier,validationtext):
    """
    This function is used to validate text returned by an ui element for test case validation purpose.

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'Here we will pass objectidentifier for required element'
        text_heading = ui_controls.text_view(get_obj_identifier(objectidentifier))
        print "label name returned by UI is==>"+str(text_heading)

        'To check if it is returning empty value here'
        if not text_heading:
            print str(validationtext)+" label does not exist and it is returning empty value."
            return False, msg

        'Comparing text retrieved from UI with validation  text'
        if validationtext.strip() == text_heading.strip():
            print (str(validationtext)+" labels has been matching!!!")
        else:
            print("Sorry!!!text has been mismatched,it should be "+str(validationtext))
            print ("label Text shown at UI is==>"+str(text_heading))
            return False, msg  

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg



def labels_validation(ele,actultext):
    """
    This function is used to validate text returned by an ui element for test case validation purpose.

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'Here we will pass objectidentifier for required element'
        text_heading = ui_controls.text_view(get_obj_identifier(ele))
        print "Current label returned by UI is==>"+str(text_heading)

        'To check if it is returning empty value here'
        if not text_heading:
            print str(actultext)+" label does not exist and it is returning empty value."
            return False, msg

        'Comparing text retrieved from UI with validation  text'
        if actultext.strip() == text_heading.strip():
            print (str(actultext)+" label has been found!!!")
        else:
            print("Sorry!!!lable has been mismatched,it should be "+str(actultext))
            print ("label shown at UI is==>"+str(text_heading))
            return False, msg  

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def verify_ios_buildNumber():
    """
    This function is used for verifying Build number
 
    Function Owner : Nithya_V
 
    Date created : 19/05/2016
 
    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        'Getting Build number for IOS '
        if g.platform == 'ios':
            text_view = ui_controls.text_view(get_obj_identifier('about_buildNumber_lbl'), label=True)

            'Verifying whether Build number is matching with expected value IOS'
        if g.platform == 'ios' and text_view.strip() == g.build_number :
            print "Build number for IOS is verified successfully. Expected : %s. Actual : %s" % (g.build_number, text_view.strip())
        else:
            if g.platform == 'ios':
                print "Build number is not verified successfully. Expected : %s. Actual : %s" % (g.build_number, text_view.strip())
            return False, msg
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return True, msg


def verify_Version_buildNumber():
    """
    This function is used for verifying Build number
 
    Function Owner : Nithya_V
 
    Date created : 19/05/2016
 
    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, flag = "", False
    try:
        'Getting Build number for IOS '
        if g.platform == 'ios':
            flag1, msg1 = verify_ios_versionNumber()
            msg += msg1
            flag2, msg2 = verify_ios_buildNumber()
            msg += msg2
            'go back'
            flag3=ui_controls.image(get_obj_identifier('about_back_btn'))
            print 'cliked on back button'
            flag = False if not (flag1 and flag2 and flag3) else True
        else:
            text_view = ui_controls.text_view(get_obj_identifier('about_buildVersion_lbl'))
           
            if text_view.strip() == g.android_version_no.strip():
              
                print "Version and Build number matched. Expected : %s. Actual : %s" % (g.android_version_no, text_view.strip())
                flag = True  
            else:
                
                print "Version and Build number does not match. Expected : %s. Actual : %s" % (g.android_version_no, text_view.strip())
            flag1=ui_controls.back_button()
            
            flag = False if not (flag1) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return flag, msg

def create_pwd_login_with_all_validation():
    """
    This function is used for creating password and login

    Function Owner : Ramanuja_das_pvk

    Date created : 20/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", False
    try:
        if g.platform =='android':
            "Empty values for all fields"
            status1 = create_pwd_login_internal('', '')
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            "validate"
            expected_dialogue_title = g.popup_title_error
            expected_dialogue_message = g.popup_message_password_blank
            verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

            "short password value"
            status2 = create_pwd_login_internal('1', '')
            "validate"
            expected_dialogue_title = g.popup_title_error
            expected_dialogue_message = g.popup_message_password_short
            verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

            "not matching passwords"
            status3 = create_pwd_login_internal(g.password, '')
            "validate"
            expected_dialogue_title = g.popup_title_error
            expected_dialogue_message = g.popup_message_password_do_not_match
            verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

        #"no hint"
        #status4 = create_pwd_login_internal(g.password, g. password, '')
        #"validate"
        #expected_dialogue_title = g.popup_title_error
        #expected_dialogue_message = g.popup_message_password_hint
        # verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

        #"hint same as password"
        #status5 = create_pwd_login_internal(g.password, g.password)
        #"validate"
        #expected_dialogue_title = g.popup_title_error
        #expected_dialogue_message = g.popup_message_password_hint_same_as_passsword
        #verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

            "Values from global_vars g"
            status6 = create_pwd_login_internal(g.password, g.password)

            status = status1 and status2 and status3 and status6
            
        else:    
            "Empty values for all fields"
            status1 = create_pwd_login_internal('', '')
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            "validate"
            expected_dialogue_title = g.ios_popup_title_error
            expected_dialogue_message = g.ios_popup_message_password_blank
            verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

            "short password value"
            status2 = create_pwd_login_internal('1', '')
            "validate"
            expected_dialogue_title = g.ios_popup_title_error
            expected_dialogue_message = g.ios_popup_message_password_short
            verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

            "not matching passwords"
            status3 = create_pwd_login_internal(g.password, '')
            "validate"
            expected_dialogue_title = g.ios_popup_title_error
            expected_dialogue_message = g.ios_popup_message_password_do_not_match
            verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

        #"no hint"
        #status4 = create_pwd_login_internal(g.password, g. password, '')
        #"validate"
        #expected_dialogue_title = g.popup_title_error
        #expected_dialogue_message = g.popup_message_password_hint
        # verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

        #"hint same as password"
        #status5 = create_pwd_login_internal(g.password, g.password)
        #"validate"
        #expected_dialogue_title = g.popup_title_error
        #expected_dialogue_message = g.popup_message_password_hint_same_as_passsword
        #verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

            "Values from global_vars g"
            status6 = create_pwd_login_internal(g.password, g.password)

            status = status1 and status2 and status3 and status6

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg
def login_change_pwd_change():
    """
    This function is used for changing password at login

    Function Owner : Ramanuja_das_pvk

    Date created : 20/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'Enter the current password in Current password text box'
            flag0 = ui_controls.text_box(get_obj_identifier('login_changePwd_enter_currentOmmPassword_txt'), value=g.password)

            'Enter the password in Create new password text box'
            flag1 = ui_controls.text_box(get_obj_identifier('login_changePwd_createNewPassword_txt'), value=g.new_password)

            'Checks for the keyboard presence and hides it'
            flag2 = ui_controls.hide_keyboard()

            'Enter the confirm new password in Confirm Password text box'
            flag3 = ui_controls.text_box(get_obj_identifier('login_changePwd_confirmNewPassword_txt'), value=g.new_password)

            'Checks for the keyboard presence and hides it'
            flag4 = ui_controls.hide_keyboard()

            'Enter password hint in Password Hint text box'
            flag5 = ui_controls.text_box(get_obj_identifier('login_changePwd_passwordHint_txt'), value=g.new_password_hint)

            'Checks for the keyboard presence and hides it'
            flag6 = ui_controls.hide_keyboard()

            'Click on change password change button'
            flag7 = ui_controls.button(get_obj_identifier('resetOMM_changePassword_change_btn'))

            status = False if not (flag0 and flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7) else True
        else:
            'Enter the current password in Current password text box'
            flag0 = ui_controls.text_box(get_obj_identifier('login_changePwd_enter_currentOmmPassword_txt'), value=g.password)

            'Setting values on Create new Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_changePwd_createNewPassword_txt'), g.new_password)

            'Setting values on Confirm new Password text box in ios.'
            flag2 = ui_controls.setValue(get_obj_identifier('login_changePwd_confirmNewPassword_txt'), g.new_password)

            'Setting values on Password Hint text box in ios.'
            flag3 = ui_controls.setValue(get_obj_identifier('login_changePwd_passwordHint_txt'), g.new_password_hint)

            'Click on Change Password change button in IOS'
            flag4 = ui_controls.button(get_obj_identifier('resetOMM_changePassword_change_btn'))

            status = False if not (flag0 and flag1 and flag2 and flag3 and flag4) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def login_click_change_pwd():
    """
    This function is used for clicking 'Change Password' button at Login screen

    Function Owner : Ramanuja_das_pvk

    Date created : 20/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        sleep(3)
        'Click on change password'
        flag = ui_controls.button(get_obj_identifier('login_changePassword_btn'))

        status = False if not flag else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg





def create_pwd_login_internal(password, re_enter_password):
    """
    This internal function is used for creating password and login

    Function Owner : Ramanuja_das_pvk

    Date created : 20/09/2016

    @param  password   : (String) password
    @param  re_enter_password : (String) re-enter password
    @param  hint : (String) password hint

    @return status : (bool)status of execution.if successful True else False
    """
    if g.platform == 'android':
        'Enter the password in Create password text box'
        flag1 = ui_controls.text_box(get_obj_identifier('login_createPassword_txt'), value=password)

        'Checks for the keyboard presence and hides it'
        flag2 = ui_controls.hide_keyboard()

        'Enter the confirm password in Confirm Password text box'
        flag3 = ui_controls.text_box(get_obj_identifier('login_confirmPassword_txt'), value=re_enter_password)

        'Checks for the keyboard presence and hides it'
        flag4 = ui_controls.hide_keyboard()

        'Enter password hint in Password Hint text box'
        #flag5 = ui_controls.text_box(get_obj_identifier('login_passwordHint_txt'), value=hint)

        'Checks for the keyboard presence and hides it'
        #flag6 = ui_controls.hide_keyboard()

        'Click on create password login button'
        flag7 = ui_controls.button(get_obj_identifier('login_createPasswordLogin_btn'))

        status = False if not (flag1 and flag2 and flag3 and flag4 and flag7) else True
    else:
        'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
        flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), password)

        'Setting values on Confirm Password text box in ios.'
        flag2 = ui_controls.setValue(get_obj_identifier('login_confirmPassword_txt'), password)

        'Setting values on Password Hint text box in ios.'
        # flag3 = ui_controls.setValue(get_obj_identifier('login_passwordHint_txt'), hint)

        'Click on Create Password button in IOS'
        flag4 = ui_controls.button(get_obj_identifier('login_createPasswordLogin_btn'))

        status = False if not (flag1 and flag2 and flag3 and flag4) else True
    return status


def login_change_pwd_change_with_all_validation():
    """
    This function is used for changing password and login

    Function Owner : Ramanuja_das_pvk

    Date created : 20/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", False
    try:
        "Empty values for all fields"
        status1 = login_change_pwd_change_internal('', '', '')
        "validate"
        expected_dialogue_title = g.popup_title_error
        expected_dialogue_message = g.popup_message_password_incorrect
        verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')
 
        "Correct current password, & Empty values for all other fields"
        status2 = login_change_pwd_change_internal(g.password, '', '')
        "validate"
        expected_dialogue_title = g.popup_title_error
        expected_dialogue_message = g.popup_message_password_blank
        verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')
 
        "Correct current password, & short new password value"
        status3 = login_change_pwd_change_internal(g.password, '1', '')
        "validate"
        expected_dialogue_title = g.popup_title_error
        expected_dialogue_message = g.popup_message_password_short
        verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')
 
        "Correct current password, & not matching new passwords"
        status4 = login_change_pwd_change_internal(g.password, g.new_password, '')
        "validate"
        expected_dialogue_title = g.popup_title_error
        expected_dialogue_message = g.popup_message_password_do_not_match
        verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')
 
        #"Correct current password, & matching correct new password & no hint"
        #status5 = login_change_pwd_change_internal(g.password, g.new_password, g.new_password)
        #"validate"
        #expected_dialogue_title = g.popup_title_error
        #expected_dialogue_message = g.popup_message_password_hint
        #verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')
 
        #"Correct current password, & hint same as new password"
        #status6 = login_change_pwd_change_internal(g.password, g.new_password, g.new_password)
       # "validate"
       # expected_dialogue_title = g.popup_title_error
       # expected_dialogue_message = g.popup_message_password_hint_same_as_passsword
        #verify_dialogue(title=expected_dialogue_title, message=expected_dialogue_message, name_of_control_to_click='popup_default_button')

        "Values from global_vars g"
        status7 = login_change_pwd_change_internal(g.password, g.new_password, g.new_password)
        if status7 is True:
            #print 'old_password: ' + g.old_password
            print 'password: ' + g.password
            #print 'password_hint: ' + g.password_hint
            print 'new_password: ' + g.new_password
            #print 'new_password_hint: ' + g.new_password_hint

            #g.old_password = g.password
            g.password = g.new_password
            #g.password_hint = g.new_password_hint

            print '*****global vars updated*****'
            #print 'old_password: ' + g.old_password
            print 'password: ' + g.password
           # print 'password_hint: ' + g.password_hint
            print 'new_password: ' + g.new_password
            #print 'new_password_hint: ' + g.new_password_hint
        else:
            g.old_password = ''

        status = status1 and status2 and status3 and status4 and status7

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def login_change_pwd_change_internal(current_password, new_password, re_enter_new_password):
    """
    This internal function is used for changing password and login

    Function Owner : Ramanuja_das_pvk

    Date created : 20/09/2016

    @param  current_password   : (String) current_password
    @param  new_password       : (String) new_password
    @param  re_enter_password : (String) re-enter password
    @param  new_password_hint : (String) new_password_hint

    @return status : (bool)status of execution.if successful True else False
    """
    status = False
    if g.platform == 'android':
        'Enter the current password in Current password text box'
        flag0 = ui_controls.text_box(get_obj_identifier('login_changePassword_enter_currentOmmPassword_txt'), value=current_password)
        sleep(3)

        'Enter the password in Create new password text box'
        flag1 = ui_controls.text_box(get_obj_identifier('login_changePassword_createNewPassword_txt'), value=new_password)
        sleep(3)

        'Checks for the keyboard presence and hides it'
        flag2 = ui_controls.hide_keyboard()
        sleep(3)

        'Enter the confirm new password in Confirm Password text box'
        flag3 = ui_controls.text_box(get_obj_identifier('login_changePassword_confirmNewPassword_txt'), value=re_enter_new_password)
        sleep(3)

        'Checks for the keyboard presence and hides it'
        flag4 = ui_controls.hide_keyboard()
        sleep(3)

        #'Enter password new_password_hint in Password Hint text box'
        #flag5 = ui_controls.text_box(get_obj_identifier('login_changePassword_passwordHint_txt'), value=new_password_hint)

        'Checks for the keyboard presence and hides it'
        flag6 = ui_controls.hide_keyboard()
        sleep(3)
        'Click on change password -> change button'
        flag7 = ui_controls.button(get_obj_identifier('login_changePassword_change_btn'))

        status = False if not (flag0 and flag1 and flag2 and flag3 and flag4  and flag6 and flag7) else True
    else:
        'Enter the current password in Current password text box'
        flag0 = ui_controls.text_box(get_obj_identifier('login_changePassword_enter_currentOmmPassword_txt'), value=current_password)

        'Setting values on Create new Password text box in ios. Using set value as send_keys failing here'
        flag1 = ui_controls.setValue(get_obj_identifier('login_changePassword_createNewPassword_txt'), value=new_password)

        'Setting values on Confirm new Password text box in ios.'
        flag2 = ui_controls.setValue(get_obj_identifier('login_changePassword_confirmNewPassword_txt'), value=re_enter_new_password)

        #'Setting values on Password Hint text box in ios.'
        #flag3 = ui_controls.setValue(get_obj_identifier('login_changePassword_passwordHint_txt'), value=new_password_hint)

        'Click on Change password -> change button in IOS'
        flag4 = ui_controls.button(get_obj_identifier('login_changePassword_change_btn'))

        status = False if not (flag0 and flag1 and flag2 and flag4) else True

    return status


'''
def create_pwd_login():
    """
    This function is used for creating password and login

    Function Owner : Nithya_V

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'Enter the password in Create password text box'
            flag1 = ui_controls.text_box(get_obj_identifier('login_createPassword_txt'), value=g.password)

            'Checks for the keyboard presence and hides it'
            flag2 = ui_controls.hide_keyboard()

            'Enter the confirm password in Confirm Password text box'
            flag3 = ui_controls.text_box(get_obj_identifier('login_confirmPassword_txt'), value=g.password)

            'Checks for the keyboard presence and hides it'
            flag4 = ui_controls.hide_keyboard()

            'Click on create password login button'
            flag5 = ui_controls.button(get_obj_identifier('login_createPasswordLogin_btn')) 

            status = False if not (flag1 and flag2 and flag3 and flag4  and flag5) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            'Setting values on Confirm Password text box in ios.'
            flag2 = ui_controls.setValue(get_obj_identifier('login_confirmPassword_txt'), g.password)

            'Setting values on Password Hint text box in ios.'
            flag3 = ui_controls.setValue(get_obj_identifier('login_passwordHint_txt'), g.password_hint)

            'Click on Create Password button in IOS'
            flag4 = ui_controls.button(get_obj_identifier('login_createPasswordLogin_btn')) 

            status = False if not (flag1 and flag2 and flag3 and flag4) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg
'''











'''
def try_demo_mode_now():

    """
    This function is used for selecting try demo mode continue

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        sleep(10)
        if g.platform == 'android':
            'verify label text of try in demo mode'
            Try_demomode_lbl = ui_controls.text_view(get_obj_identifier('Try_demomode_lbl'))
            if Try_demomode_lbl.strip() == 'Demo Mode':
                print "Try demo mode page label is displaying properly"
            else:
                print "Try demo mode page label is not displaying properly"
            'get the text of try in demo mode page'
            Try_demomode_txt_view = ui_controls.text_view(get_obj_identifier('Try_demomode_txt'))
            'Read verification input text from try demo mode text file'
            text_to_verify = util.read_file(g.Try_demomode_txt)
            if not text_to_verify:
                print "Unable to retrieve text of try  demo mode  input text file"
                return False, msg
            if text_to_verify.strip() == Try_demomode_txt_view.strip():
                print "Try demo mode page text verified successfully"
            else:
                print "Try demo mode page text verified unsuccessfully"

            'Getting y_elem as destination element'
            y_elem = ui_controls.ui_element(get_obj_identifier('common_widget_scrollview'))
            'Getting x_elem as source element'
            x_elem = ui_controls.ui_element(get_obj_identifier('demo_tryDemoMode_btn'))
            'Scroll the element from x element to y element'
            flag1 = ui_controls.scroll_element(x_elem, y_elem)
            sleep(3)
            'Click on Continue to OMM button'
            flag2 = ui_controls.button(get_obj_identifier('demo_continueToOmm_btn'))
            status = False if not (flag1 and flag2) else True
        else:
            'Click on Continue to OMM button in IOS'
            flag1 = ui_controls.button(get_obj_identifier('demo_continueToOmm_btn'))
            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg
'''




def omm_login_with_password(password=g.password):
    """
    This function is used for creating password and login

    Function Owner : Ramanuja_das_pvk

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        sleep(5)
#        
 
        'Enters value in password text box based on the user inputs'
        flag1 = ui_controls.text_box(get_obj_identifier('login_enterPassword_txt'), value=password)
        sleep(3)
        'Clicks on the login button'
        flag2 = ui_controls.button(get_obj_identifier('login_login_btn'))
        status = False if not (flag1 and flag2) else True
    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg



def omm_forgot_password_login(password=g.password):
    """
    This function is used for creating password and login

    Function Owner : Nithya_V

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        sleep(5)
        'Enters value in password text box based on the user inputs'
        flag1 = ui_controls.text_box(get_obj_identifier('login_forgotPwd_enterPassword_txt'), value=password)

        'Clicks on the login button'
        flag2 = ui_controls.button(get_obj_identifier('login_forgotPasswordLogin_btn'))
        status = False if not (flag1 and flag2) else True
    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def omm_forgot_password():
    """
    This function is used for selecting Forgot Password option at login screen

    Function Owner : Ramanuja_das_pvk

    Date created : 20/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        sleep(5)
        'Click Forgot Password button'
        flag = ui_controls.button(get_obj_identifier('enterPwd_forgotPwd'))
        status = flag
    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg














def verify_changePassword_screen():
    """
    This function is used for verifying Change Password screen

    Function Owner : Ramanuja_das_pvk

    Date created : 6/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        flag = False

        'Getting Change Password text_view object'
        if g.platform == 'ios':
            'Feature Not available for change password from login screen'
            flag = ui_controls.ui_element(get_obj_identifier('login_changePwd_text_view'))
        else:
            flag = ui_controls.ui_element(get_obj_identifier('login_changePassword_text_view'))

        if flag:
            print "Change Password Screen Name is displayed properly"
            return True, msg
        else:
            print "Change Password Screen Name is not displayed properly"

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return True, msg


def verify_setting_changePassword_screen():
    """
    This function is used for verifying Settings -> Change Password screen

    Function Owner : Ramanuja_das_pvk

    Date created : 26/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
#         'Getting Settings -> Change Password text_view object'
#         flag = ui_controls.ui_element(get_obj_identifier('login_changePwd_text_view'))

        flag = False

        if g.platform == 'ios':
            flag = ui_controls.ui_element(get_obj_identifier('settings_changePassword_lbl'))
        else:
            flag = ui_controls.ui_element(get_obj_identifier('settings_changePassword_lbl'))
        
        if flag:
            print "Settings -> Change Password Screen Name is displayed properly"
            return True, msg
        else:
            print "Settings -> Change Password Screen Name is not displayed properly"

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return True, msg


def verify_forgotPassword_screen():

    """
    This function is used for verifying Forgot Password screen & Password Hint

    Function Owner : Ramanuja_das_pvk

    Date created : 6/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    flag, msg = False, ""
    try:
        flag1,flag2 = False, False
        if g.platform == 'ios':
            flag1 = ui_controls.text_view(get_obj_identifier('login_forgotPassword_lbl'), value=True)
        else:
            'Getting Forgot Password text_view object'
            sleep(5)
            #flag1 = ui_controls.ui_element(get_obj_identifier('EUL_agrement_labl'))
            flag1 = ui_controls.ui_element(get_obj_identifier('login_forgotPwd_enterPassword_txt'))

        if flag1 is not None:
            print "Forgot Password Screen Name is displayed properly"
            flag = True
        else:
            print "Forgot Password Screen Name is not displayed properly"
        
       # password_hint = ''

        #if g.platform == 'ios':
           # flag2 = ui_controls.text_view(get_obj_identifier('forgotPwd_hint'), label = True)
            #password_hint = g.password_hint_text_predecessor_ios +g.password_hint
        #else:
            #'verify password hint'
            #flag2 = ui_controls.text_view(get_obj_identifier('forgotPwd_err_msg'))
            #password_hint = g.popup_message_password_incorrect

        #if flag2 is not None and flag2.lower() == password_hint.lower():
            #print "Forgot Password pop up error message is displayed properly"
            #flag = flag and True
       # else:
            #print "Forgot Password pop up error message is not displayed properly"
        
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return flag, msg









def navigate_mainMenu_settings():
    """
    This function is used for navigating to settings in the app. Home->Settings.

    Function Owner : Ramanuja_das_pvk

    Date created : 19/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, flag = "", False
    try:
        'click on home main menu button'
        flag1 = navigate_mainMenu()

        'Click on the settings item in the list generated from OMM home page -> main menu'
        flag2 = ui_controls.button(get_obj_identifier('home_mainMenu_settings_lnk'))
        flag = flag1 and flag2

        if flag:
            print "settings in the home page -> main menu button is clicked"

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return flag, msg


def navigate_mainMenu_settings_changePassword():
    """
    This function is used for navigating to Change Password page from settings in the app. Home->Settings.

    Function Owner : Ramanuja_das_pvk

    Date created : 19/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, flag = "", False
    try:
        'click on home main menu button -> settings'
        flag1 = navigate_mainMenu_settings()

        'Click on the change password in the OMM home page -> main menu -> settings'
        flag2 = ui_controls.button(get_obj_identifier('settings_changePassword_lbl'))
        flag = flag1 and flag2

        if flag:
            print "change password in the home page -> main menu -> settings is clicked"

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return flag, msg








def verify_settings_screen():
    """
    This function is used for verifying the Settings Screen

    Function Owner : Ramanuja_das_pvk

    Date created : 19/09/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg = ""
    try:
        if g.platform == 'ios':
            'Getting about page label for IOS - Settings'
            text_view = ui_controls.text_view(get_obj_identifier('mainMenu_settings_lbl'), value=True)
        else:
            'Getting about page label for Android - Settings'
            text_view = ui_controls.text_view(get_obj_identifier('mainMenu_settings_lbl'))

            'Verifying whether about screen label is About for IOS'
            if text_view.strip() == g.aboutScreen_label :
                print "About Screen label is verified successfully"
            else:
                print "About Screen label is not verified successfully"
                return False, msg
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return True, msg










def verify_dialogue(title, message, name_of_control_to_click='popup_default_button'):
    """
    Verify the dialogue pop up
    """
    msg, flag = "", False
    try:
        sleep(3)
        popup = ui_controls.ui_element(get_obj_identifier('popup'))
        flag1, flag2, flag3, flag4 = False, False, False, False

        if popup is not None:
            flag1 = True
            title_actual = ui_controls.text_view(get_obj_identifier('popup_title'))
            sleep(3)
            message_actual = ui_controls.text_view(get_obj_identifier('popup_message'))
            if title_actual.lower() == title.lower():
                flag2 = True
                print 'pop up title matched'
            if message_actual.lower() == message.lower():
                flag3 = True
                print 'pop up message matched'
            sleep(3)    
            flag4 = ui_controls.button(get_obj_identifier(name_of_control_to_click))
            flag = flag1 and flag2 and flag3 and flag4
        else:
            print 'pop up not available'
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return flag, msg