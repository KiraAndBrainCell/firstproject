""""
This module contains all the modules related to adding OME in omm
"""
import traceback
import time

from libs.product.omm.standard.ui_controls import ui_controls
from libs.product.omm.standard import global_vars
from libs.product.omm.standard import omm_lib
from libs.product.omm.omm_ome import ome_lib

'Creating objects'
ui_controls = ui_controls()

'Retrieving variables'
g = global_vars
get_obj_identifier = omm_lib.get_obj_identifier


def click_add_ome():
    """
    This function is used for clicking OME button

    Function Owner : Abdul_G_Shaik

    Date created : 06/09/2016

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        if g.platform == 'ios':
            'Click on add idrac button'
            time.sleep(5)
            flag1 = ui_controls.button(get_obj_identifier('add_ome_btn'))
            print 'OME button clicked on lower bar'

            #'Verify page name changes to OME'
            #flag2 = ui_controls.label(get_obj_identifier('add_ome_lbl'))
            #time.sleep(5)
            'Click Add device button'
            #if flag2:
                #time.sleep(5)
                #flag3 = ui_controls.button(get_obj_identifier('ome_add_btn'))
                #print 'Add Icon (+) clicked'
                #time.sleep(5)
        else:
            'Click on + button'
            time.sleep(5)
            flag1 = ui_controls.button(get_obj_identifier('ome_add_btn'))
            print 'plus button clicked'
            #flag2 =   ui_controls.button(get_obj_identifier('open_manage_esntials_elmnt'))
            #print 'OpenManage essentials element'
       

        status = False if not (flag1) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg
def eenter_ome_details(ome_ip, ome_username, ome_password):
    """
    This function is used for entering OME ip and credentials

    Function Owner : Abdul_G_Shaik

    Date created : 06/09/2016

    @@param ome_ip : (string) OME ip of system
    @param ome_userName : (string) OME user name
    @param ome_password : (string) OME password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'Click on + button'
        time.sleep(5)
        flag0 = ui_controls.button(get_obj_identifier('ome_add_btn'))
        print 'plus button clicked'
        
        'Enter OME application ip and credentials'
        flag1 = ui_controls.text_box(get_obj_identifier('addOme_ipHostname_txt'),ome_ip)
        flag2 = ui_controls.text_box(get_obj_identifier('addOme_username_txt'),ome_username)
        flag3 = ui_controls.text_box(get_obj_identifier('addOme_password_txt'),ome_password)
        ui_controls.hide_keyboard()
        time.sleep(5)
        'Click on + button'
       
        time.sleep(5)
        flag4 =ui_controls.Click(get_obj_identifier('addOme_add_btn'))
        print 'add ome button clicked'
        time.sleep(5)
        flag5 = ui_controls.Click(get_obj_identifier('addome_confirmation_yes_btn'))
        time.sleep(20)
        #flag6=ui_controls.Click(get_obj_identifier('save_btn'))
        time.sleep(5)   
        flag7=ui_controls.Click(get_obj_identifier('alert_ok_btn'))
        time.sleep(10)
        status = False if not (flag0 and flag1 and flag2 and flag3 and flag4 and flag5 and flag7) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def enter_ome_details(ome_ip, ome_username, ome_password):
    """
    This function is used for entering OME ip and credentials

    Function Owner : Abdul_G_Shaik

    Date created : 06/09/2016

    @@param ome_ip : (string) OME ip of system
    @param ome_userName : (string) OME user name
    @param ome_password : (string) OME password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        #flag0 = ui_controls.Click(get_obj_identifier('open_manage_esntials_elmnt'))
        #print 'openManage Essentials selected successfully'

        'Enter OME application ip and credentials'
        flag1 = ui_controls.text_box(get_obj_identifier('addOme_ipHostname_txt'),ome_ip)
        flag2 = ui_controls.text_box(get_obj_identifier('addOme_username_txt'),ome_username)
        flag3 = ui_controls.text_box(get_obj_identifier('addOme_password_txt'),ome_password)
        ui_controls.hide_keyboard()
        time.sleep(5)
        'Click add button'
        #flag4 = ui_controls.button(get_obj_identifier('addOme_add_btn'))
        print 'OME details entered successfully'
        #flag5 = ui_controls.Click(get_obj_identifier('yes_pop_up_btn'))
        #time.sleep(7)
        #flag6 = ui_controls.Click(get_obj_identifier('save_btn'))
        #time.sleep(5)
        #flag7 = ui_controls.Click(get_obj_identifier('yes_pop_up_btn'))
        #flag7 = ui_controls.Click(get_obj_identifier('Ok_bttn'))
        #time.sleep(15)

        status = False if not (flag1 and flag2 and flag3) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def accept_ssl_certificate():
    """
    This function is used for clicking accept button on SSL Certificate window

    Function Owner : Abdul_G_Shaik

    Date created : 06/09/2016

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'verify SSL certificate pop up window appears'
        element = ui_controls.ui_element(get_obj_identifier('addOme_certificate_win'))
        print 'alert is verified'
        if(element is None):
            flag1 = False
        else:
            flag1 = True

        'Click accept button'
        flag2 = ui_controls.button(get_obj_identifier('addOme_certificate_accept_btn'))
        time.sleep(5)
        #flag3 = ui_controls.button(get_obj_identifier('sve_opt'))
        
        
        

        status = False if not (flag1 and flag2) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg
def jaff_a():
    """
    This function is used for selecting the Alert Subscription option

    Function Owner : Abdul_G_Shaik

    Date created : 06/10/2016

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
  
    msg, status = "", True
    try:
  
        if g.platform == 'android':

            'Click on + button'
            time.sleep(5)
            flag1 =ui_controls.Click(get_obj_identifier('addOme_add_btn'))
            print 'add ome button clicked'
            flag2 = ui_controls.Click(get_obj_identifier('addome_confirmation_yes_btn'))
         
            
            time.sleep(5)
            flag6=ui_controls.Click(get_obj_identifier('save_btn'))
            time.sleep(5)
            flag7 =ui_controls.Click(get_obj_identifier('alert_ok_btn'))
            flag = False if not (flag1 and flag2 and flag6 and flag7) else True
        else:

            'Click on add idrac button'
            time.sleep(5)
            flag1 = ui_controls.Click(get_obj_identifier('sve_opt'))
        
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

    

def alert_subscription():
    """
    This function is used for selecting the Alert Subscription option

    Function Owner : Abdul_G_Shaik

    Date created : 06/10/2016

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'verify Alert Subscription pop up window appears'
        element = ui_controls.ui_element(get_obj_identifier('alert_subscription_lbl'))
        if(element is None):
            flag1 = False
        else:
            flag1 = True
        if g.platform == 'ios':
            'Click skip button'
            flag2 = ui_controls.button(get_obj_identifier('alert_subscription_skip_btn'))
            time.sleep(10)
        else:
            'Click OK button'
            flag2 = ui_controls.button(get_obj_identifier('alert_subscription_ok_btn'))
            time.sleep(10)

        status = False if not (flag1 and flag2) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def add_ome_app(ome_ip, ome_username, ome_password):
    """
    This function is used for adding OME application

    Function Owner : Abdul_G_Shaik

    Date created : 06/14/2016

    @@param ome_ip : (string) OME ip of system
    @param ome_userName : (string) OME user name
    @param ome_password : (string) OME password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    try:
        'Select option to add OME'
        flag1 = click_add_ome()

        'Enter OME details'
        flag2 = enter_ome_details(ome_ip, ome_username, ome_password)

        flag3= jaff_a()
        time.sleep(10)
        'wait for alert subscription label'
        #flag4 = wait_till_page_loads('ome_consle_lbl')
        'click on save '
        
        #flag4 = navigate_home()
        'Alert Subscription page'
        #flag5 = alert_subscription()
        #flag5= ui_controls.Click(get_obj_identifier('ome_console_ip_lbl'))

        status = False if not (flag1 and flag2 and flag3) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def verify_ome_details(device_health, event_severity):
    """
    This function verifies OME devices health and event severity details

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param device_health : (array) list of all device health statuses in Database
    @param event_severity : (array) list of all event severity statuses in Database

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    attribute_value = ''
    try:   
        'Verify Count of Devices'
        attribute_value = ome_lib.db_get_totalcount("Device")
        flag1 = verify_total_count(attribute_value)

        'Verify Count of Events'
        attribute_value = ome_lib.db_get_totalcount("Event")
        flag2 = verify_total_count(attribute_value)

        'Verify devices count based upon health statuses'
        flag3 = verify_all_status_count(device_health, "Device")

        'Verify events count based upon severity'
        flag4 = verify_all_status_count(event_severity, "Event")

        status = False if not (flag1 and flag2 and flag3 and flag4) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def verify_pysmsql_ome_details(device_health, event_severity):
    """
    This function verifies OME devices health and event severity details

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param device_health : (array) list of all device health statuses in Database
    @param event_severity : (array) list of all event severity statuses in Database

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    attribute_value = ''
    try:   
        'Verify Count of Devices'
        
        attribute_value= ome_lib.pysmsql_db_get_totalcount("Device")
        
        
        flag1 = pysmsql_verify_total_count(attribute_value)

        'Verify Count of Events'
        attribute_value = ome_lib.pysmsql_db_get_totalcount("Event")
        
        flag2 = pysmsql_verify_total_count(attribute_value)

        'Verify devices count based upon health statuses'
        flag3 = pysmsql_verify_all_status_count(device_health, "Device")

        'Verify events count based upon severity'
        flag4 = pysmsql_verify_all_status_count(event_severity, "Event")

        status = False if not (flag1 and flag2 and flag3 and flag4) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def verify_total_count(attribute_value):
    """
    This function verifies if the object (total device count and total event count) is present on screen

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param attribute_value : (string) Attribute value fetched from Database

    @return flag : (bool) status of execution.if successful True else False
    """
    flag = True
    try:
        'Verify Attribute value exists on screen'
        if g.platform == 'ios':
            element = g.driver.find_element_by_name(str(attribute_value)).find_element_by_name(str(attribute_value))
            print "Element with name %s is found\n" % (str(attribute_value))
            control_value = element.get_attribute('value')
            print 'Control Value:' + str(control_value)
        else:
            element = g.driver.find_element_by_name(attribute_value)
            print "Element with name %s is  found\n" % (str(attribute_value))
            control_value = element.get_attribute('text')
            print 'Control Value:' + str(control_value)

        'Check control value matches attribute value'
        if control_value.strip() == attribute_value.strip():
            print "Control value %s is same as attribute value %s \n" % (control_value, attribute_value)
            flag = True
        else:
            print "Control value %s is not same as attribute value %s \n" % (control_value, attribute_value)
            flag = False

    except:
        print "Element with name %s not found\n" % (str(attribute_value))
        traceback.print_exc()
        flag = False
    return flag
def pysmsql_verify_total_count(attribute_value):
    """
    This function verifies if the object (total device count and total event count) is present on screen

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param attribute_value : (string) Attribute value fetched from Database

    @return flag : (bool) status of execution.if successful True else False
    """
    flag = True
    try:
        time.sleep(3)
        'Verify Attribute value exists on screen'
        if g.platform == 'ios':
            element = g.driver.find_element_by_name(str(attribute_value)).find_element_by_name(str(attribute_value))
            print "Element with name %s is found\n" % (str(attribute_value))
            control_value = element.get_attribute('value')
            print 'Control Value:' + str(control_value)
        else:
            time.sleep(3)
            element = g.driver.find_element_by_name(str(attribute_value))
        
            print "Element with name %s is  found\n" % (str(attribute_value))
            control_value = element.get_attribute('text')
            print 'Control Value:' + str(control_value)
            time.sleep(3)

        'Check control value matches attribute value'
        if control_value.strip() == attribute_value.strip():
            print "Control value %s is same as attribute value %s \n" % (control_value, attribute_value)
            flag = True
        else:
            print "Control value %s is not same as attribute value %s \n" % (control_value, attribute_value)
            flag = False

    except:
        print "Element with name %s not found\n" % (str(attribute_value))
        traceback.print_exc()
        flag = False
    return flag
def ppysmsql_verify_total_count(attribute_value):
    """
    This function verifies if the object (total device count and total event count) is present on screen

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param attribute_value : (string) Attribute value fetched from Database

    @return flag : (bool) status of execution.if successful True else False
    """
    flag = True
    try:
        'Verify Attribute value exists on screen'
        if g.platform == 'ios':
            element = g.driver.find_element_by_name("com.dell.omm:id/device_count").find_element_by_name("com.dell.omm:id/device_count")
            #print "Element with name %s is found\n" % (str(attribute_value))
            #control_value = element.get_attribute('value')
            #print 'Control Value:' + str(control_value)
        else:
            #element = g.driver.find_element_by_id("com.dell.omm:id/device_count")
           
            Try_demomode_lbl = ui_controls.text_view(get_obj_identifier('dvce_cnt'))
            print   Try_demomode_lbl
        
            #print "Element with name %s is  found\n" % (str(attribute_value))
            control_value = Try_demomode_lbl
            print 'Control Value:' + str(control_value)

        'Check control value matches attribute value'
        if control_value.strip() == attribute_value.strip():
            print "Control value %s is same as attribute value %s \n" % (control_value, attribute_value)
            flag = True
        else:
            print "Control value %s is not same as attribute value %s \n" % (control_value, attribute_value)
            flag = False

    except:
        print "Element with name %s not found\n" % (str(attribute_value))
        traceback.print_exc()
        flag = False
    return flag

def verify_all_status_count(health, table_name):
    """
    This function extract the database details of various device and event statuses

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param health : (array) list of all device health statuses and event severities in Database
    @param table_name : (string) table name of either Device or Event

    @return flag : (bool) status of execution.if successful True else False
    """
    flag = True
    try:
        time.sleep(3)
        'Get the Database values of all types of statuses/severities'
        list_health = health.split(",")
        for status in list_health:
            db_result = ome_lib.db_all_device_event_count(table_name, status.strip())
            print "DB RESULT is: ", db_result
            if db_result != 0:
                'Convert the database code into description'
                description = str(ome_lib.convert_code_to_description(table_name, status.strip()))
                db_result_string = str(db_result)
                time.sleep(3)

                'Form the object to search in UI'
                attribute_value = db_result_string+" "+description
                time.sleep(3)

                'Verify Attribute value exists on screen'
                element = g.driver.find_element_by_name(attribute_value)
                print "Element with name %s is found\n" % (str(attribute_value))

                if g.platform == 'ios':
                    control_value = element.get_attribute('value')
                    print 'Control Value:' + str(control_value)
                else:
                    control_value = element.get_attribute('value')
                    print 'Control Value:' + str(control_value)

                'Check control value matches attribute value'
                if control_value.strip() == attribute_value.strip():
                    print "Control value %s is same as attribute value %s \n" % (control_value, attribute_value)
                    flag = True
                else:
                    print "Control value %s is not same as attribute value %s \n" % (control_value, attribute_value)
                    flag = False
            else:
                'No records found in DB'
                print "No records founds with health status of %s \n" % status
    except:
        print "Could not get the values and compare in UI \n" % table_name
        traceback.print_exc()
        flag = False
    return flag
def pysmsql_verify_all_status_count(health, table_name):
    """
    This function extract the database details of various device and event statuses

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param health : (array) list of all device health statuses and event severities in Database
    @param table_name : (string) table name of either Device or Event

    @return flag : (bool) status of execution.if successful True else False
    """
    flag = True
    try:
        time.sleep(5)
        'Get the Database values of all types of statuses/severities'
        list_health = health.split(",")
        for status in list_health:
            db_result = ome_lib.pysmsql_db_all_device_event_count(table_name, status.strip())
            print "DB RESULT is: ", str(db_result)
            if db_result != 0:
                'Convert the database code into description'
                description = str(ome_lib.pysmsql_convert_code_to_description(table_name, status.strip()))
                
                
                db_result_string = str(db_result)

                'Form the object to search in UI'
                attribute_value = db_result_string+" "+description
                
                

                'Verify Attribute value exists on screen'
                element = g.driver.find_element_by_name(attribute_value)
                print "Element with name %s is found\n" % (str(attribute_value))

                if g.platform == 'ios':
                    control_value = element.get_attribute('value')
                    print 'Control Value:' + str(control_value)
                else:
                    control_value = element.get_attribute('text')
                    print 'Control Value:' + str(control_value)

                'Check control value matches attribute value'
                if control_value.strip() == attribute_value.strip():
                    print "Control value %s is same as attribute value %s \n" % (control_value, attribute_value)
                    flag = True
                else:
                    print "Control value %s is not same as attribute value %s \n" % (control_value, attribute_value)
                    flag = False
            else:
                'No records found in DB'
                print "No records founds with health status of %s \n" % status
    except:
        print "Could not get the values and compare in UI \n" % table_name
        traceback.print_exc()
        flag = False
    return flag



def navigate_home():
    """
    This function is used to navigate to home screen

    Function Owner : Pooja_Rundwal

    Date created : 08/06/2016

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    try:
        'Click main menu from the top bar'
        time.sleep(5)
        flag1 = ui_controls.image(get_obj_identifier('mnu_btn'))

        'Select Home Option'
        if flag1:
            menu_list = ui_controls.ui_elements(get_obj_identifier('omm_menu_options'))
            for menu in menu_list:
                if menu.get_attribute('text').encode("ascii", "ignore").strip() == 'Home':
                    menu.click()
                    time.sleep(5)
                    flag2 = True
                    break
        status = False if not (flag1 and flag2) else True
    except Exception as excp:
        traceback.print_exc()
        status = False
        msg += str(excp)
    return status, msg


def delete_ome(ome_ip):
    """
    This function is used to delete OME ip

    Function Owner : Abdul_G_Shaik

    Date created : 23/06/2016

    @param ome_ip : (string) OME ip to be deleted

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
  
    msg, status = "", True
    try:
  
        if g.platform == 'android':

            'Navigate to home screen'
            time.sleep(15)
            flag1 = navigate_home()

            'Select OME checkbox'
            flag2 = ui_controls.Click(get_obj_identifier('ome_select_chk'))
            print 'OME Selected'
           
            flag3 =ui_controls.button(get_obj_identifier('ome_delete_btn'))
          
            flag4 =ui_controls.button(get_obj_identifier('confirmdelete_yes_btn'))
            
            flag = False if not (flag1 and flag2 and flag3 and flag4) else True
        else:

            time.sleep(15)
            'Select configuration button'
            flag1 = ui_controls.button(get_obj_identifier('device_configuration_btn'))

            time.sleep(10)
            ' Select Edit Connection'
            flag2 = ui_controls.button(get_obj_identifier('omeconfiguration_editconnection_txtView'))

            'Click delete button'
            flag3 = ui_controls.button(get_obj_identifier('ome_delete_btn'))
            print 'Delete button clicked'
            time.sleep(5)

            'Click yes button on popup'
            #flag4 = ui_controls.button(get_obj_identifier('confirmdelete_yes_btn'))
            flag = False if not (flag1 and flag2 and flag3) else True
        if not flag:
            return False, msg
        else:
            print "License agreement screen name is displayed properly"
            
            
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        return False, msg
    return True, msg   


def ddelete_ome():
    """
    This function is used to delete OME ip

    Function Owner : Abdul_G_Shaik

    Date created : 23/06/2016

    @param ome_ip : (string) OME ip to be deleted

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'Navigate to home screen'
            time.sleep(15)
            flag1 = navigate_home()

            'Select OME checkbox'
            flag2 = ui_controls.Click(get_obj_identifier('ome_select_chk'))
            print 'OME Selected'
           
            flag3 =ui_controls.button(get_obj_identifier('ome_delete_btn'))
          
            flag4 =ui_controls.button(get_obj_identifier('confirmdelete_yes_btn'))
            
        else:
            time.sleep(15)
            'Select configuration button'
            flag1 = ui_controls.button(get_obj_identifier('device_configuration_btn'))

            time.sleep(10)
            ' Select Edit Connection'
            flag2 = ui_controls.button(get_obj_identifier('omeconfiguration_editconnection_txtView'))

            'Click delete button'
            flag3 = ui_controls.button(get_obj_identifier('ome_delete_btn'))
            print 'Delete button clicked'
            time.sleep(5)

        status = False if not (flag1 and flag2 and flag3 and flag4) else True
    except Exception as excp:
        traceback.print_exc()
        status = False
        msg += str(excp)
    return status, msg
def aadd_ome_wizard():
    """
    This function is used for clicking idrac button

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'Click on Plus button to launch Add OME wizard'
        time.sleep(5)
        ui_controls.Click(get_obj_identifier('ome_add_btn'))
        print 'plus button clicked Successfully'

        'Check for the existence of Add OME text'
        text_heading = ui_controls.text_view(get_obj_identifier('add_txt'))
        print "Current text value is==>"+str(text_heading)

        'To check if it is returning empty value here'
        if not text_heading:
            print "Add OME text does not exist and it is returning empty value."
            return False, msg

        'Comparing text retrieved from UI with Add OME text'
        if "Add".strip() == text_heading.strip():
            print ("Add OME text has been found!!!")
        else:
            print("Sorry!!!text has been mismatched,it should be Add OME")
            return False, msg

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def add_ome_wizard():
    """
    This function is used for clicking idrac button

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        if  g.platform == 'android':
            'Click on Plus button to launch Add OME wizard'
            time.sleep(5)
            ui_controls.Click(get_obj_identifier('ome_add_btn'))
            print 'plus button clicked Successfully'
                
            'Check for the existence of Add OME text'
            text_heading = ui_controls.text_view(get_obj_identifier('add_txt'))
            print "Current text value is==>"+str(text_heading)

            'To check if it is returning empty value here'
            if not text_heading:
                print "Add OME text does not exist and it is returning empty value."
            return False, msg

            'Comparing text retrieved from UI with Add OME text'
            if "Add".strip() == text_heading.strip():
                print ("Add OME text has been found!!!")
            else: 
                print("Sorry!!!text has been mismatched,it should be Add OME")
            return False, msg
                 
               
        else:
                'Click on Plus button to launch Add OME wizard'
                time.sleep(5)
                ui_controls.Click(get_obj_identifier('ome_add_btn'))
                print 'plus button clicked Successfully'

                'Check for the existence of Add OME text'
                text_heading = ui_controls.text_view(get_obj_identifier('add_txt'))
                print "Current text value is==>"+str(text_heading)

                'To check if it is returning empty value here'
                if not text_heading:
                    print "Add OME text does not exist and it is returning empty value."
                return False, msg

                'Comparing text retrieved from UI with Add OME text'
                if "Add OME".strip() == text_heading.strip():
                    print ("Add OME text has been found!!!")
                else: 
                    print("Sorry!!!text has been mismatched,it should be Add OME")
                    return False, msg
         
             
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def select_device_and_create_powertask():
    """
    This function is used to select a target MN to create the power task under OME from OMM.

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        time.sleep(10)
        'Click on Devices pie chart to navigate under ALl Devices'
        flag1 = ui_controls.button(get_obj_identifier('devices_health_piechart'))
        time.sleep(40)

        'Select RAC group and click on it during power task creation'

        flag2 = ui_controls.Click_MultipleUIElements_Selectpassedelement(get_obj_identifier('device_type_rac_powertask'),Elementnameforselection='RAC',elementidentifier='device_type_rac_powertask',elementname='RAC')
        time.sleep(40)

        'select the passed target device for power task creation'
        flag3 = ui_controls.Click_MultipleUIElements_Selectpassedelement(get_obj_identifier('powertask_target_mn'),Elementnameforselection='idrac',elementidentifier='powertask_target_mn',elementname='idrac8')
        time.sleep(5)
        'click on power option menu'
     
        flag4 = ui_controls.Click(get_obj_identifier('more_options_btn'))
        'Click on power button for navigating to power options page(reboot page)'
        time.sleep(5)
        flag5 = ui_controls.Click(get_obj_identifier('powertask_power_btn'))
        time.sleep(5)

        flag6 = ui_controls.text_box(get_obj_identifier('powertask_username_txt'),'administrator')
        time.sleep(3)
        flag7 = ui_controls.text_box(get_obj_identifier('powertask_password_txt'),'Lexington123')
        ui_controls.hide_keyboard()
        time.sleep(5)

        'click on Enable All check box'
        flag8 = ui_controls.check_box(get_obj_identifier('powertask_enableall_checkbox'))
        time.sleep(5)

        'select appropriate power task for creation as per test case requirement'
        flag9 = ui_controls.check_box(get_obj_identifier('powertask_radio_poweron'))
        time.sleep(5)

        'Click on submit for creating the task under OME for same device'
        flag10 = ui_controls.Click(get_obj_identifier('powertask_submit_btn'))
        time.sleep(5)

        'Click on Yes button from confirm operation window'
        flag11 = ui_controls.Click(get_obj_identifier('powertask_confirmoperation_yes_btn'))
        time.sleep(5)

        #'Click on Task manager button to monitor task status under Task manager window'
        #flag11 = ui_controls.Click(get_obj_identifier('powertask_taskmgr_taskmanager_btn'))
        #time.sleep(5)
        'click on task manager on power task pop up'
        flag12 = ui_controls.Click(get_obj_identifier('taskmngr_btn'))

        'Here we will verify if Task Manager window has been launched successfully or not'
        flag13,msg = element_textvalidation('taskmanager_window','Task Manager')
        time.sleep(4)

        'Check for task name under Task Manager window'
        flag14,msg = element_textvalidation('powertask_name_taskmanager','Power On of idrac')


        status = False if not (flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8 and flag9 and flag10 and flag11 and flag12 and flag13 and flag14) else True

        print status

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg
def hi_select_device_and_create_powertask():
    """
    This function is used to select a target MN to create the power task under OME from OMM.

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        

        #flag1 =ui_controls.hi_Click_MultipleUIElements_Selectpassedelement(get_obj_identifier('demomode_device_name'),Elementnameforselection='192.168.0.11',elementidentifier='demomode_device_name',elementname='192.168.0.11')
        flag2=ui_controls.hi_Click_MultipleUIElements_Selectpassedelement(get_obj_identifier('demomode_device_name'),Elementnameforselection='10.11.50.1',elementidentifier='demomode_device_name',elementname='10.11.50.1')
        
        status = False if not (flag2) else True

        print status

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg
def duplicate_select_device_and_create_powertask():
    """
    This function is used to select a target MN to create the power task under OME from OMM.

    Function Owner : Sudhish_Singh

    Date created : 

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        

        flag1 = ui_controls.hi_Click_MultipleUIElements_Selectpassedelement(get_obj_identifier('demomode_device_name'),Elementnameforselection='192.168.0.110',elementidentifier='demomode_device_name',elementname='192.168.0.110')
        

      


        status = False if not (flag1) else True

        print status

    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg
def wait_till_page_loads(control_name):
    """
    This function is used to wait till screen is loaded completely

    Function Owner : Pooja_Rundwal

    Date created : 05/05/2016

    @param control_name : (string) user defined name of the control from object repository.
    """
    counter, status = 0, True
    try:
        'Check if page loaded'
        element = ui_controls.ui_element(get_obj_identifier(control_name))
        while (element is None ):

            counter = counter + 1
            element = ui_controls.ui_element(get_obj_identifier(control_name))
            'Exit if waited for 2 mins'
            if counter >25:
                status = False
                break
    except Exception as excp:
        print 'Waiting for inventory to load'
    return status




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
        'Here we will pass object identifier for required element'
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


def Click_MultipleUIElements_Selectpassedelement(self, identifier, tag_name=None,Elementnameforselection=None,elementidentifier=None,elementname=None):

        """
        This function is used to select an specific element once ui page is returning multiple elements with same resource id.
        Function Owner : Sudhish_Singh
        Date created :
        @param  identifier: (string) object identifier.
        @param  tag_name=None: (string) tag name.
        @param  Elementnameforselection: (string) element name which need to select from multiple elements.        
        @return status : (bool)status of execution.if successful True else False
        """
        global Uipagescrollcount
        global CurrentElementidentifierforselection
        global CurrentElementnameforselection

        Uipagescrollcount = Uipagescrollcount+1
        print "Function call count==>"+str(Uipagescrollcount)
        if Uipagescrollcount == 1:
            CurrentElementidentifierforselection = elementidentifier
            CurrentElementnameforselection = elementname

        print "Click_MultipleUIElements_Selectpassedelement identifier===>"+str(CurrentElementidentifierforselection)
        print "Click_MultipleUIElements_Selectpassedelement Name===>"+str(CurrentElementnameforselection)
        msg, status = True

        try:

            elements = []
            # getting the button element
            elements = self.ui_elements(identifier, tag_name)

            print "printing elements from Click_MultipleUIElements function"
            print elements

            for Currentelementtext in elements:
                print Currentelementtext.text

            print "Passed element name for selection is==>"+str(Elementnameforselection)

            for el in elements:
                if el.text.strip() == Elementnameforselection.strip():
                    print "Current element is==>"+str(el.text)
                    print "Passed element is==>"+str(Elementnameforselection)
                    print "Congratulation!!!Required element has been found successfully,now we can select and click on it"
                    print "Reseting global count variable Uipagescrollcount"
                    Uipagescrollcount=0
                    status = True
                    el.click()
                    break
                else:
                    print "Current element is==>"+str(el.text)
                    print "Passed element is==>"+str(Elementnameforselection)
                    print "Passed element has not been found till now trying for more."
                    status = False
                    continue

            'if element passed for selection doesnot exist on ui at all then return the proper message for failure'
            if status == False:

                print CurrentElementidentifierforselection
                print CurrentElementnameforselection
                self.swipe_down()
                if Uipagescrollcount==50:
                    print "Reached max count 50 can not scroll more"
                    print "Sorry!!!Traversed through entire ui element but not finding passed element for selection,passed element is==>"+str(Elementnameforselection)
                    print "Reseting global count variable Uipagescrollcount"
                    Uipagescrollcount=0
                    print "global count variable Uipagescrollcount value after final reset is====>"+str(Uipagescrollcount)
                else:
                    self.Click_MultipleUIElements_Selectpassedelement(get_obj_identifier(CurrentElementidentifierforselection),Elementnameforselection=CurrentElementnameforselection) 
   
        except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
        return status, msg
