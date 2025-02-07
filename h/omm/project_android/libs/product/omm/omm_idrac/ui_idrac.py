""""
This module contains all the modules related to adding idrac in omm
"""
import traceback
import time


from libs.product.omm.standard.ui_controls import ui_controls
from libs.product.omm.standard import global_vars
from libs.product.omm.standard import omm_lib
from libs.product.omm.omm_idrac import idrac_lib

'Creating objects'
ui_controls = ui_controls()

'Retrieving variables'
g = global_vars
get_obj_identifier = omm_lib.get_obj_identifier


def click_add_idrac():
    """
    This function is used for clicking idrac button

    Function Owner : Pooja_Rundwal

    Date created : 04/05/2016

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        if g.platform == 'ios':
            'Click on add idrac button'
            time.sleep(5)
          
            flag1 = ui_controls.button(get_obj_identifier('idrac_add_btn'))
            print 'idrac button clicked on lower bar'
         
            'Verify page name changes to iDRAC'
            #flag2 = ui_controls.label(get_obj_identifier('add_idrac_lbl'))
            flag2=ui_controls.button(get_obj_identifier('ntrk_opt'))
            print 'network option clicked'
            time.sleep(5)
            
            'Click Add device button'
           # if flag2:
                #time.sleep(5)
                #flag3 = ui_controls.button(get_obj_identifier('idrac_add_btn'))
                #print 'Add Icon (+) clicked'
                #time.sleep(5)
        else:
         
            'click on sixth idrac device'
            main_menu_items = ui_controls.ui_elements(get_obj_identifier('plus_btn') )
            main_menu_items[1].click()
            print 'plus button clicked'
            #flag1 = ui_controls.button(get_obj_identifier('idrac_add_btn'))
           
            time.sleep(4)
            flag2 = ui_controls.Click(get_obj_identifier('ntrk_opt'))
            print 'network option clicked'
            
            
            #'click on idrac element'
            #flag3 = ui_controls.Click(get_obj_identifier('idrac_element'))
            #print'idrac selected successfully'

            'Click Add OME drop down to display Add idrac option'
            #flag3 = ui_controls.button(get_obj_identifier('add_hosttype_lst'))
            time.sleep(5)
            'Select Add idrac option'
            #if flag3:
                #time.sleep(5)
                #flag4 = ui_controls.button(get_obj_identifier('add_addidrac_txtview'))
                #print 'Add iDRAC Selected'
                #time.sleep(5)

        status = False if not (flag2) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def enter_idrac_details(idrac_ip, idrac_username, idrac_password):
    """
    This function is used for entering idrac ip and credentials

    Function Owner : Pooja_Rundwal

    Date created : 04/05/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'Enter idrac ip and credentials'
        flag1 = ui_controls.text_box(get_obj_identifier('addIdrac_ipHostname_txt'),idrac_ip)
        flag2 = ui_controls.text_box(get_obj_identifier('addIdrac_username_txt'),idrac_username)
        flag3 = ui_controls.text_box(get_obj_identifier('addIdrac_password_txt'),idrac_password)
        ui_controls.hide_keyboard()
        time.sleep(5)

        'Click add button'
        flag4 = ui_controls.button(get_obj_identifier('addIdrac_add_btn'))
        print 'iDRAC details entered successfully'

        status = False if not (flag1 and flag2 and flag3 and flag4) else True
        time.sleep(5)
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


def accept_ssl_certificate():
    """
    This function is used for clicking accept button on SSL Certificate window

    Function Owner : Pooja_Rundwal

    Date created : 05/05/2016

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    
    
    msg, status = "", True

    try:
        if g.platform == 'ios':
            'Click on add idrac button'
            time.sleep(5)
          
            #flag1 = ui_controls.button(get_obj_identifier('idrac_add_btn'))
            #print 'idrac button clicked on lower bar'
         
            'Verify page name changes to iDRAC'
            #flag2 = ui_controls.label(get_obj_identifier('add_idrac_lbl'))
            flag2=ui_controls.button(get_obj_identifier('ntrk_opt'))
            print 'network option clicked'
            time.sleep(5)
            
            'Click Add device button'
           # if flag2:
                #time.sleep(5)
                #flag3 = ui_controls.button(get_obj_identifier('idrac_add_btn'))
                #print 'Add Icon (+) clicked'
                #time.sleep(5)
        else:
            
            'verify SSL certificate pop up window appears'
            element = ui_controls.ui_element(get_obj_identifier('addIdrac_certificate_win'))
            if(element is None):
                flag1 = False
            else:
                flag1 = True

            'Click accept button'
            flag2 = ui_controls.button(get_obj_identifier('certificate_accept_btn'))
            print 'SSL Certificate accepted'
            
            'Wait till idrac page loads completely'
           # flag3 = wait_till_page_loads('idrac_console_ip_lbl')
           
            #flag3 = wait_till_page_loads('mnu_btn')
         
           
           
           
           
        status = False if not (flag1 and flag2) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg
    #msg, status = "", True

    #try:
        #'verify SSL certificate pop up window appears'
        #element = ui_controls.ui_element(get_obj_identifier('addIdrac_certificate_win'))
        #if(element is None):
            #flag1 = False
        #else:
            #flag1 = True

        #'Click accept button'
       # flag2 = ui_controls.button(get_obj_identifier('certificate_accept_btn'))
        #print 'SSL Certificate accepted'

        
       # flag3 = wait_till_page_loads('idrac_console_ip_lbl')
        #time.sleep(15)

        #status = False if not (flag3) else True
    #except Exception as excp:
        #traceback.print_exc()
        #msg += str(excp)
        #status = False
    #return status, msg
def temporary():
    """
    This function is used for clicking accept button on SSL Certificate window

    Function Owner : Pooja_Rundwal

    Date created : 05/05/2016

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    
    
    msg, status = "", True

    try:
        if g.platform == 'ios':
            'Click on add idrac button'
            time.sleep(5)
          
            #flag1 = ui_controls.button(get_obj_identifier('idrac_add_btn'))
            #print 'idrac button clicked on lower bar'
         
            'Verify page name changes to iDRAC'
            #flag2 = ui_controls.label(get_obj_identifier('add_idrac_lbl'))
            flag2=ui_controls.button(get_obj_identifier('ntrk_opt'))
            print 'network option clicked'
            time.sleep(5)
           
        else:
            
            time.sleep(10)
            'Click accept button'
            flag1 = ui_controls.Click(get_obj_identifier('ntwrkdels'))
            print 'SSL Certificate accepted'
            time.sleep(10)
            'Wait till idrac page loads completely'
            flag2 = ui_controls.back_button()
         
           
           
           
           
        status = False if not (flag1 and flag2 ) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg    
def aaccept_ssl_certificate():
    """
    This function is used for clicking accept button on SSL Certificate window

    Function Owner : Pooja_Rundwal

    Date created : 05/05/2016

    @return status : (bool)status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True

    try:
        'verify SSL certificate pop up window appears'
        element = ui_controls.ui_element(get_obj_identifier('addIdrac_certificate_win'))
        if(element is None):
            flag1 = False
        else:
            flag1 = True
        time.sleep(10)    

        'Click accept button'
        flag2 = ui_controls.button(get_obj_identifier('certificate_accept_btn'))
        print 'SSL Certificate accepted'
        
        
        'Wait till idrac page loads completely'
        flag3 = wait_till_page_loads('idrac_console_ip_lbl')

        status = False if not (flag1 and flag2 and flag3) else True
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
        time.sleep(4)
        'Check if page loaded'
        element = ui_controls.ui_element(get_obj_identifier(control_name))
      
        while (element is None ):
            time.sleep(15)
            counter = counter + 1
            element = ui_controls.ui_element(get_obj_identifier(control_name))
            'Exit if waited for 2 mins'
            if counter >50:
                status = False
                break
    except Exception as excp:
        print 'Waiting for inventory to load'
    return status
def idrac_wait_till_page_loads(control_name):
    """
    This function is used to wait till screen is loaded completely

    Function Owner : Pooja_Rundwal

    Date created : 05/05/2016

    @param control_name : (string) user defined name of the control from object repository.
    """
    counter, status = 0, True
    try:
        time.sleep(5)
        'Check if page loaded'
        element = ui_controls.ui_element(get_obj_identifier(control_name))
      
        while (element is None ):
            time.sleep(10)
            counter = counter + 1
            element = ui_controls.ui_element(get_obj_identifier(control_name))
            'Exit if waited for 2 mins'
            if counter >500:
                status = False
                break
    except Exception as excp:
        print 'Waiting for inventory to load'
    return status




def verify_idrac_basic_inventory(idrac_ip, idrac_username, idrac_password,
                                 windows_ip, windows_username, windows_password):                                 
    """
    This function verifies idrac basic inventory

    Function Owner : Pooja_Rundwal

    Date created : 18/05/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip from which query will be executed
    @param windows_username : (string) windows system user name
    @param windows_password : (string) windows system password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    
    msg, status = "", True
    attribute_value = ''
    try:
        time.sleep(10)
        'Verify Power Status'
        attribute_value = get_inventory(global_vars.powerManagementService_classname,'PowerState',
                                        idrac_ip, idrac_username, idrac_password,
                                        windows_ip, windows_username, windows_password)
        
        if g.platform == 'ios':
           
            flag1 = verify_inventory(attribute_value)
        else:
            flag1 = verify_inventory(attribute_value, 'idrac_powerstatus_txtView')

        'Verify Service Tag'
        attribute_value = get_inventory(global_vars.systemView_classname, 'ServiceTag',
                                        idrac_ip, idrac_username, idrac_password,
                                        windows_ip, windows_username, windows_password)
      
        if g.platform == 'ios':
           
            flag2 = verify_inventory(attribute_value)
        else:
            flag2 = verify_inventory(attribute_value, 'idrac_servicetag_txtView')

        'Verify Model'
        attribute_value = get_inventory(global_vars.systemView_classname, 'Model',
                                        idrac_ip, idrac_username, idrac_password,
                                        windows_ip, windows_username, windows_password)
      
        if g.platform == 'ios':
       
            flag3 = verify_inventory(attribute_value)
        else:
            flag3 = verify_inventory(attribute_value, 'idrac_devicemodel_txtView')
 
        'Verify CPU'
        attribute_value = get_inventory(global_vars.cpuView_classname, 'Model',
                                        idrac_ip, idrac_username, idrac_password,
                                        windows_ip, windows_username, windows_password)
   
        if g.platform == 'ios':
           
            flag4 = verify_inventory(attribute_value)
        else:
            flag4 = verify_inventory(attribute_value, 'idrac_cpuinfo_txtView')

        'Verify Memory'
        attribute_value = get_inventory(global_vars.memoryView_classname, 'Size',
                                        idrac_ip, idrac_username, idrac_password,
                                        windows_ip, windows_username, windows_password)
    
        if g.platform == 'ios':
          
            flag5 = verify_inventory(attribute_value)
        else:
            flag5 = verify_inventory(attribute_value, 'idrac_memoryinfo_txtView')
 
 
        'Verify OS Name'
        'Fetch OS name'
        os_name = get_inventory(global_vars.systemString_classname, 'CurrentValue',
                                idrac_ip, idrac_username, idrac_password,
                                windows_ip, windows_username, windows_password,
                                global_vars.osname_instanceid)

        'Fetch OS version'
        os_version = get_inventory(global_vars.systemString_classname, 'CurrentValue',
                                   idrac_ip, idrac_username, idrac_password,
                                   windows_ip, windows_username, windows_password,
                                   global_vars.osversion_instanceid)
     
        attribute_value = str(os_name) + ' - ' + str(os_version)
 
        if g.platform == 'ios':
           
            flag6 = verify_inventory(attribute_value)
        else:
            flag6 = verify_inventory(attribute_value, 'idrac_osinfo_txtView')
 
        'Verify hostname'
        attribute_value = get_inventory(global_vars.systemView_classname, 'HostName',
                                        idrac_ip, idrac_username, idrac_password,
                                        windows_ip, windows_username, windows_password)
        print attribute_value
        print attribute_value
        print attribute_value
        
        if g.platform == 'ios':
         
            flag7 = verify_inventory(attribute_value)
        else:
            flag7 = verify_inventory(attribute_value, 'idrac_hostname_txtView')
 
        'Verify IP address'
        if g.platform == 'ios':
         
            flag8 = verify_inventory(attribute_value)
        else:
            flag8 = verify_inventory(idrac_ip, 'idrac_ipaddress_txtView')
 
        'Verify LCD'
        attribute_value = get_inventory(global_vars.systemString_classname, 'CurrentValue',
                                        idrac_ip, idrac_username, idrac_password,
                                        windows_ip, windows_username, windows_password,
                                        global_vars.lcd_instanceid)
     
        if g.platform == 'ios':
            
            flag9 = verify_inventory(attribute_value)
        else:
            flag9 = True   #verify_inventory(attribute_value)

        'Verify IP at top screen'
        label_text = ui_controls.text_view(get_obj_identifier('idrac_console_ip_label'),label=True)

        if label_text.strip() == idrac_ip.strip():
            flag10 = True
        else:
            flag10 = False

        status = False if not (flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 \
                               and flag9 and flag10) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
    return status, msg


def get_inventory(class_name, attribute_name, idrac_ip, idrac_username, idrac_password,
                        windows_ip, windows_username, windows_password, instanceid=None):
    """
    This function gets idrac basic inventory based on winrm command

    Function Owner : Pooja_Rundwal

    Date created : 18/05/2016

    @param class_name : (string) WSMan class name
    @param attribute_name : (string) Attribute name to fetch data
    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip from which query will be executed
    @param windows_username : (string) windows system user name
    @param windows_password : (string) windows system password
    @param instance_id : (string) instance id for fetching data specific to an instance

    @return attribute_value : (string) Attribute value fetched from winrm
    """
    attribute_value = ''
    try:
        'Fetch details'
        wsman_dict, no_of_instances = idrac_lib.get_wsman_dict(class_name, idrac_ip, idrac_username,
                                    idrac_password, windows_ip, windows_username, windows_password, instanceid)

        'Fetch ServiceTag, Model, Hostname'
        if wsman_dict != {} and no_of_instances == 1:
            'Fetch attribute value'
            attribute_value = wsman_dict[attribute_name]
            if class_name == global_vars.powerManagementService_classname:
                'Fetch Power Status'
                attribute_value = idrac_lib.power_status_mapping(attribute_value)

        'Fetch CPU and Memory'
        if wsman_dict != {} and no_of_instances > 1:
            if class_name == 'DCIM_CPUView' and attribute_name == 'Model':
                if g.platform == 'ios':
                    attribute_value = str(no_of_instances).strip() + ' x ' + str(wsman_dict['Model1'] +
                                            ' (' + wsman_dict['NumberOfProcessorCores1'] + ' Cores)')
                else:
                    attribute_value = str(no_of_instances).strip() + 'X ' + str(wsman_dict['Model1'] +
                                            ' (' + wsman_dict['NumberOfProcessorCores1'] + ' Cores)')
            elif class_name == 'DCIM_MemoryView' and attribute_name == 'Size':
                attribute_value = 0
                for index in range(no_of_instances):
                    attribute_value = attribute_value + float(wsman_dict['Size' + str(index+1)])
                'Convert to GB'
                attribute_value = idrac_lib.convert_byte_to_gb(attribute_value)
    except:
        traceback.print_exc()
        attribute_value = ''
    return attribute_value


def verify_inventory(attribute_value, element_name=None):
    """
    This function verifies idrac basic inventory based on winrm output data

    Function Owner : Pooja_Rundwal

    Date created : 18/05/2016

    @param attribute_value : (string) Attribute value fetched from winrm
    @param element_name : (string) Element name given in object repository file. Optional

    @return flag : (bool) status of execution.if successful True else False
    """
    flag = True
    try:
        'Verify Attribute value exists on screen'
        if attribute_value != '' and element_name is None:
            if g.platform == 'ios':
                element = g.driver.find_element_by_name(attribute_value)
                print "Element with name %s is found\n" % (str(attribute_value))
                #control_value = element.get_attribute('label').encode("ascii", "ignore")
                control_value = element.get_attribute('value').encode("ascii", "ignore")
                print 'Control Value:' + str(control_value)
        elif attribute_value != "" and element_name is not None:
            if g.platform == 'android':
                element = ui_controls.ui_element(get_obj_identifier(element_name))
                if element is None:
                    print "Element with name %s is not found\n" % (str(attribute_value))
                    control_value = ''
                else:
                    control_value = element.get_attribute('text').encode("ascii", "ignore")
                    print "Element with name %s is  found\n" % (str(attribute_value))
                    print 'Control Value:' + str(control_value)
        else:
            flag = False

        'Check control value matches attribute value'
        if control_value.strip() == attribute_value.strip():
            print "Control value %s is same as attribute value %s" % (control_value, attribute_value)
            flag = True
        else:
            print "Control value %s is not same as attribute value %s" % (control_value, attribute_value)
            flag = False
    except:
        print "Element with name %s not found\n" % (str(attribute_value))
        traceback.print_exc()
        flag = False
    return flag


def launchVirtualConsole():
    """
    This function is used for launching virtual console

    Function Owner : Nithya_V

    Date created : 11/08/2016

    @return flag : (bool) status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True

    try:

        if g.platform == 'android':
    
            'Click on More options button in iDRAC home page'
            
            flag1 = ui_controls.Click(get_obj_identifier('action_dsktop_lbl'))
            
            #'Click on Launch Virtual Console in the More options menu'
            #flag2 = ui_controls.button(get_obj_identifier('home_launchVC_lnk'))
    
            status = False if not (flag1) else True
        
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg


def virtualConsoleAlertHandle():
    """
    This function is used for verifying & pressing YES or NO in Virtual Console alert

    Function Owner : Nithya_V

    Date created : 12/08/2016

    @return flag : (bool) status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True

    try:

        if g.platform == 'android':
            
            time.sleep(5)
            
            'Getting Alert Title label in VNC'
            vnc_alertTitle = ui_controls.text_view(get_obj_identifier('vnc_alertTitle_lbl'))
            
            if vnc_alertTitle == 'Unable to launch VNC':
                print "VNC alert title is verified successfully"
            else:
                print "VNC Alert title is not matching. Expected : Unable to launch VNC. Actual : " % vnc_alertTitle
                return False
            
            print "VNC Alert Title is %s" % vnc_alertTitle
            
            'Click on Yes in VNC Alert button'
            flag1 = ui_controls.button(get_obj_identifier('vnc_alertYes_btn'))
    
            status = False if not (flag1) else True

        
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg


def installAndroidApp():
    """
    This function is used for installing android app

    Function Owner : Nithya_V

    Date created : 12/08/2016

    @return flag : (bool) status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True

    try:

        if g.platform == 'android':
            
            'Click on Launch Virtual Console in the More options menu'
            flag1 = ui_controls.button(get_obj_identifier('bVNC_Install_btn'))
            
            'Click on bVNC accept button'
            flag2 = ui_controls.button(get_obj_identifier('bVNC_accept_btn'))
            
            for i in range(0,5):
            
                'Verify presence of bVNC un-install button to ensure completion of installation'
                element = ui_controls.ui_element(get_obj_identifier('bVNC_uninstall_btn'))
            
                if element != None :
                    print "App has been successfully installed"
                    break
                else:
                    time.sleep(10)
            status = False if not (flag1 and flag2) else True
        
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg

def configure_LaunchVirtualConsole(secureTunnel=False):
    """
    This function is used for verifying & pressing YES or NO in Virtual Console alert

    Function Owner : Nithya_V

    Date created : 12/08/2016

    @return flag : (bool) status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True

    try:

        if g.platform == 'android':
            time.sleep(15)
            
            'Enter password in password field'
            flag1 = ui_controls.text_box(get_obj_identifier('lVC_password_txt'), value='calvin')
            
            if not secureTunnel:
                'De-select the Use Secure Tunnel check box'
                flag2 = ui_controls.check_box(get_obj_identifier('lVC_secureTunnel_chk'), plainChkUnchk=True)
                if not flag2:
                    return False, msg

            'Click on launch Virtual Console button'
            flag3 = ui_controls.button(get_obj_identifier('lVC_launch_btn'))
            
            status = False if not (flag1 and flag3) else True
        
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg

def verifylaunchVNCalert():
    """
    This function is used for verifying launch VNC alert title to establish handshake

    Function Owner : Nithya_V

    Date created : 12/08/2016

    @return flag : (bool) status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, flag1, flag2, status = "", True, True, False

    try:

        if g.platform == 'android':
            
            for i in range(0,5):
            
                'Getting Alert Title label in VNC'
                vncHandshakeTitle = ui_controls.text_view(get_obj_identifier('vnc_handshakeAlertTitle_lbl'))
                
                if vncHandshakeTitle.__contains__('Connecting'):
                    print "VNC establish handshake alert title is verified successfully"
                    flag1 = True
                else:
                    print "VNC establish handshake alert title is not matching. Expected : Unable to launch VNC. Actual : " % vncHandshakeTitle
                
                'Getting message body of Establishing handshake in VNC'
                vncMessageBody = ui_controls.text_view(get_obj_identifier('vnc_establishHandShake_lbl'))
                
                if vncMessageBody.__contains__('Establishing handshake.'):
                    print "VNC establish handshake alert body message is verified successfully"
                    flag2 = True
                else:
                    print "VNC establish handshake alert body message is not matching. Expected : Unable to launch VNC. Actual : " % vncMessageBody
                
                if flag1 and flag2:
                    status = True
                    break
                else:
                    time.sleep(5)
        
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg

def verifyVNCViewer():
    """
    This function is used for verify VNC Viewer canvas

    Function Owner : Nithya_V

    Date created : 12/08/2016

    @return flag : (bool) status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", False

    try:

        if g.platform == 'android':
            
            for i in range(0,10):
            
                'Getting Alert Title label in VNC'
                vncCanvas = ui_controls.ui_element(get_obj_identifier('vnc_canvas_img'))
                 
                if vncCanvas != None :
                    status = True
                    break
                else:
                    time.sleep(5)

            time.sleep(5)
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False

    return status, msg


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
                if menu.get_attribute('text').encode("ascii", "ignore").strip() =='Home':
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


def delete_idrac(idrac_ip):
    """
    This function is used to delete idrac ip

    Function Owner : Pooja_Rundwal

    Date created : 08/06/2016

    @param idrac_ip : (string) iDRAC ip to be deleted

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    #msg, status = "", True
   # try:
       # if g.platform == 'android':
            #'Navigate to home screen'
           # time.sleep(15)
            #flag1 = navigate_home()
            #'click on idrc check box option'
           # flag2= ui_controls.Click(get_obj_identifier('idrac_chk_box'))
            #print 'iDRAC check box Selected'
            #flag3 =ui_controls.button(get_obj_identifier('ome_delete_btn'))
            #print 'deleted '
          
            #flag4 =ui_controls.button(get_obj_identifier('confirmdelete_yes_btn'))
        #else:
            #time.sleep(15)
            #'Select configuration button'
            #flag1 = ui_controls.button(get_obj_identifier('device_configuration_btn'))
            #flag0 = ui_controls.button(get_obj_identifier('idrac_ip'))
            #flag1 = ui_controls.button(get_obj_identifier('more_options_btn'))
            

            #time.sleep(10)
            #' Select Edit Connection'
            #flag2 = ui_controls.button(get_obj_identifier('idracconfiguration_editconnection_txtView'))

            #'Click delete button'
            #flag3 = ui_controls.button(get_obj_identifier('idrac_delete_btn'))
            #print 'Delete button clicked'
            #time.sleep(5)

        
        #time.sleep(5)
        
        #status = False if not (flag1 and flag2 and flag3 and flag4) else True
    #except Exception as excp:
        #traceback.print_exc()
        #status = False
       # msg += str(excp)
    #return status, msg
    msg, status = "", True
    try:
  
        if g.platform == 'android':

            'Navigate to home screen'
            time.sleep(15)
            flag1 = navigate_home()
            'click on idrc check box option'
            flag2= ui_controls.Click(get_obj_identifier('idrac_chk_box'))
            print 'iDRAC check box Selected'
            flag3 =ui_controls.button(get_obj_identifier('ome_delete_btn'))
            print 'deleted '
          
            flag4 =ui_controls.button(get_obj_identifier('confirmdelete_yes_btn'))
            
            flag = False if not (flag1 and flag2 and flag3 and flag4) else True
        else:

            time.sleep(15)
            #'Select configuration button'
            #flag1 = ui_controls.button(get_obj_identifier('device_configuration_btn'))
            #flag0 = ui_controls.button(get_obj_identifier('idrac_ip'))
            flag1 = ui_controls.button(get_obj_identifier('more_options_btn'))
            

            time.sleep(10)
            ' Select Edit Connection'
            flag2 = ui_controls.button(get_obj_identifier('idracconfiguration_editconnection_txtView'))

            'Click delete button'
            flag3 = ui_controls.button(get_obj_identifier('idrac_delete_btn'))
            print 'Delete button clicked'
            time.sleep(5)

        
        #time.sleep(5)
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
def select_idrc_options():
    """
    This function is used for navigating to Power options screen

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param power_option : (string) Power option to be selected. Valid values: power_on, power_cycle, shutdown

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
   
    msg, status = "", True

    try:
        if g.platform == 'ios':
            #time.sleep(10)
            'Select configuration button'
            flag1 = ui_controls.button(get_obj_identifier('more_options_btn'))

            time.sleep(10)
            flag2 = ui_controls.Click(get_obj_identifier('device_configure'))        
            'Select Power Options'
            flag2 = ui_controls.button(get_obj_identifier('idracconfiguration_poweroptions_txtView'))

            'Wait till power options page loads completely'
            flag3 = wait_till_page_loads('poweroptions_poweron_rdb')
            time.sleep(5)

               
        else:
         
            'Select configuration button'
            flag1 = ui_controls.back_button()
            
            time.sleep(10)
            items = ui_controls.ui_elements(get_obj_identifier('addedidrac_ip_txtView'))  
            items.click()  
           

        status = False if not (flag1 and flag2 and flag3) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg


 


def open_power_options():
    """
    This function is used for navigating to Power options screen

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param power_option : (string) Power option to be selected. Valid values: power_on, power_cycle, shutdown

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
   # msg, status = "", True
    #try:
        #time.sleep(10)
        #'Select configuration button'
        #flag1 = ui_controls.button(get_obj_identifier('more_options_btn'))

        #time.sleep(10)
       # flag2 = ui_controls.Click(get_obj_identifier('device_configure'))        
        #'Select Power Options'
       # flag2 = ui_controls.button(get_obj_identifier('idracconfiguration_poweroptions_txtView'))

        #'Wait till power options page loads completely'
        #flag3 = wait_till_page_loads('poweroptions_poweron_rdb')
        #time.sleep(5)

        #status = False if not (flag1 and  flag2 and flag3) else True
    #except Exception as excp:
        #traceback.print_exc()
       # status = False
        #msg += str(excp)
    #return status, msg
    msg, status = "", True

    try:
        if g.platform == 'ios':
            time.sleep(10)
            'Select configuration button'
            flag1 = ui_controls.button(get_obj_identifier('more_options_btn'))

            time.sleep(10)
            flag2 = ui_controls.Click(get_obj_identifier('device_configure'))        
            'Select Power Options'
            flag2 = ui_controls.button(get_obj_identifier('idracconfiguration_poweroptions_txtView'))

            'Wait till power options page loads completely'
            flag3 = wait_till_page_loads('poweroptions_poweron_rdb')
            time.sleep(5)

               
        else:
            'Select configuration button'
            #flag0 = ui_controls.back_button()
            
            time.sleep(15)
            #items = ui_controls.ui_elements(get_obj_identifier('addedidrac_ip_txtView'))  
            #items.click()  
           

            'Select configuration button'
            flag1 = ui_controls.button(get_obj_identifier('more_options_btn'))

            time.sleep(10)
            flag2 = ui_controls.Click(get_obj_identifier('device_configure'))        
            'Select Power Options'
            flag3 = ui_controls.button(get_obj_identifier('idracconfiguration_poweroptions_txtView'))
            

            
            flag4 = wait_till_page_loads('poweroptions_poweron_rdb')

        status = False if not (flag1 and flag2 and flag3 and flag4) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg




def select_power_option(power_option):
    """
    This function is used for selecting power option

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param power_option : (string) Power option to be selected.
                        Valid values: power_on, power_cycle, shutdown, shutdown_os

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    try:
        if power_option.lower() == 'power_on':
            if g.platform == 'android':
                flag1 = ui_controls.check_box(get_obj_identifier('poweroptions_poweron_rdb'))
            else:
                flag1 = ui_controls.button(get_obj_identifier('poweroptions_poweron_rdb'))
        elif power_option.lower() == 'power_cycle':
            if g.platform == 'android':
                flag1 = ui_controls.check_box(get_obj_identifier('poweroptions_powercycle_rdb'))
            else:
                flag1 = ui_controls.button(get_obj_identifier('poweroptions_powercycle_rdb'))
        elif power_option.lower() == 'shutdown':
            if g.platform == 'android':
                flag1 = ui_controls.check_box(get_obj_identifier('poweroptions_shutdown_rdb'))
                flag2 = ui_controls.check_box(get_obj_identifier('poweroptions_shutdownos_chk'), 'uncheck')
            else:
                flag1 = ui_controls.button(get_obj_identifier('poweroptions_shutdown_rdb'))
                value = ui_controls.ui_element(get_obj_identifier('poweroptions_shutdownos_chk')).get_attribute('value')
                if str(value) == '0':
                    flag2 = True
            flag1 = flag1 and flag2
        elif power_option.lower() == 'shutdown_os':
            if g.platform == 'android':
                flag1 = ui_controls.check_box(get_obj_identifier('poweroptions_shutdown_rdb'))
                flag2 = ui_controls.check_box(get_obj_identifier('poweroptions_shutdownos_chk'))
            else:
                flag1 = ui_controls.button(get_obj_identifier('poweroptions_shutdown_rdb'))
                flag2 = ui_controls.button(get_obj_identifier('poweroptions_shutdownos_chk'))
                value = ui_controls.ui_element(get_obj_identifier('poweroptions_shutdownos_chk')).get_attribute('value')
                if str(value) == '1':
                    flag2 = True
                else:
                    flag2 = False
            flag1 = flag1 and flag2
        else:
            print'Incorrect power option given. Please give correct power option.'
            msg += 'Incorrect power option given. Please give correct power option.'
            return False, msg
        print 'Power Option Selected : %s \n' %(power_option)
        'Click Submit button'
        flag2 = ui_controls.button(get_obj_identifier('poweroptions_submit_btn'))

        'Click yes button on popup'
        flag3 = ui_controls.button(get_obj_identifier('confirmdelete_yes_btn'))
        time.sleep(10)
        if g.platform == 'ios':
            ui_controls.button(get_obj_identifier('alert_ok_btn'))
        time.sleep(30)
        status = False if not (flag1 and flag2 and flag3) else True
    except Exception as excp:
        traceback.print_exc()
        status = False
        msg += str(excp)
    return status, msg


def verify_control_enable(control_name, isenable=True):
    """
    This function is used to verify power options are enabled/disabled based on current power state

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param control_name : (string) user defined name for power option given in object repository
    @param isenable: (string) True if enable, False if disable. Default is True

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    try:
        'check if control is enable or not'
        time.sleep(5)
        flag1 = ui_controls.ui_element(get_obj_identifier(control_name)).is_enabled()
        if flag1 == isenable:
            status = True
            print 'Control %s is in %s state, Expected state is %s \n' % (control_name, str(flag1), 'True')
        else:
            status = False
            print 'Control %s is in %s state, Expected state is %s\n' % (control_name, str(flag1), 'False')
    except Exception as excp:
        traceback.print_exc()
        status = False
        msg += str(excp)
    return status, msg


def verify_power_state_winrm(idrac_ip, idrac_username, idrac_password,
                                 windows_ip, windows_username, windows_password, expected_state):
    """
    This function is used to verify current power state

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip
    @param windows_username : (string) windows system user name
    @param windows_password : (string) windows system password
    @param expected_state : (string) Expected state of power

    @return flag : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, flag = "", True
    try:
        'Get current power status value'
        attribute_value = get_inventory(global_vars.powerManagementService_classname,'PowerState',
                                        idrac_ip, idrac_username, idrac_password,
                                        windows_ip, windows_username, windows_password)

        'Verify power state'
        if expected_state.lower().strip() == attribute_value.lower().strip():
            print "Expected value %s is same as attribute value %s" % (expected_state, attribute_value)
            flag = True
        else:
            print "Expected value %s is not same as attribute value %s" % (expected_state, attribute_value)
            flag = False

    except Exception as excp:
        traceback.print_exc()
        flag = False
        msg += str(excp)
    return flag, msg


def perform_shutdown_using_winrm(idrac_ip, idrac_username, idrac_password,
                                 windows_ip, windows_username, windows_password):
    """
    This function is used to perform shutdown action using winrm command

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip
    @param windows_username : (string) windows system user name
    @param windows_password : (string) windows system password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    command_output, flag, msg = "", True, ""
    try:
        'Get current power status value'
        attribute_value = get_inventory(global_vars.powerManagementService_classname,'PowerState',
                                        idrac_ip, idrac_username, idrac_password,
                                        windows_ip, windows_username, windows_password)

        if attribute_value.lower() == 'on':
            command_output = idrac_lib.run_powerstate_change_winrm_command("8", idrac_ip, idrac_username, idrac_password,
                                                                      windows_ip, windows_username, windows_password)
            if "ReturnValue = 0" not in command_output:
                flag = False
            print 'Shutdown performed'
        else:
            print 'System is already in power off state'
        time.sleep(10)
    except Exception as excp:
        traceback.print_exc()
        flag = False
        msg += str(excp)
    return flag, msg


def verify_offstate_enabled_controls():
    """
    This function is used to verify which options are enabled when current power status is off

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    try:
     
        'Check controls enable/disable'
        flag1, msg = verify_control_enable('poweroptions_poweron_rdb', True)
        flag2, msg = verify_control_enable('poweroptions_powercycle_rdb', False)
        flag3, msg = verify_control_enable('poweroptions_shutdown_rdb',False)
        flag4, msg = verify_control_enable('poweroptions_shutdownos_chk', False)
        time.sleep(5)
        status = False if not (flag1 and flag2 and flag3 and flag4) else True
    except Exception as excp:
        traceback.print_exc()
        status = False
        msg += str(excp)
    return status, msg


def verify_onstate_enabled_controls():
    """
    This function is used to verify which options are enabled when current power status is on

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    try:
        'Check controls enable/disable'
        flag1, msg = verify_control_enable('poweroptions_poweron_rdb', False)
        flag2, msg = verify_control_enable('poweroptions_powercycle_rdb', True)
        flag3, msg = verify_control_enable('poweroptions_shutdown_rdb', True)
        flag4, msg = verify_control_enable('poweroptions_shutdownos_chk', True)
        time.sleep(5)
        status = False if not (flag1 and flag2 and flag3 and flag4) else True
    except Exception as excp:
        traceback.print_exc()
        status = False
        msg += str(excp)
    return status, msg


def perform_power_on_action(idrac_ip, idrac_username, idrac_password,
                                 windows_ip, windows_username, windows_password):
    """
    This function is used to perform and verify power on action

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip
    @param windows_username : (string) windows system user name
    @param windows_password : (string) windows system password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, flag = "", True
    try:
        'Perform power on action'
        flag, msg = select_power_option('power_on')
        if flag:
            flag, msg = verify_power_state_winrm(idrac_ip, idrac_username, idrac_password,
                                     windows_ip, windows_username, windows_password, 'on')
        time.sleep(5)    

        if g.platform == 'android':
            'Navigate back to previous screen'
            g.driver.back()
            'Navigate back to previous screen'
            g.driver.back()
        time.sleep(10)
    except Exception as excp:
        traceback.print_exc()
        flag = False
        msg += str(excp)
    return flag, msg


def perform_shutdown_action(idrac_ip, idrac_username, idrac_password,
                                 windows_ip, windows_username, windows_password):
    """
    This function is used to perform and verify shutdown action

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip
    @param windows_username : (string) windows system user name
    @param windows_password : (string) windows system password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, flag = "", True
    try:
        'Perform shutdown action'
        flag, msg = select_power_option('shutdown')
        if flag:
            flag, msg = verify_power_state_winrm(idrac_ip, idrac_username, idrac_password,
                                            windows_ip, windows_username, windows_password, 'off')
        time.sleep(5)    

        if g.platform == 'android':
            'Navigate back to previous screen'
            g.driver.back()
            'Navigate back to previous screen'
            g.driver.back()
    except Exception as excp:
        traceback.print_exc()
        flag = False
        msg += str(excp)
    return flag, msg


def perform_power_cycle_action(idrac_ip, idrac_username, idrac_password,
                                 windows_ip, windows_username, windows_password):
    """
    This function is used to perform and verify power cycle action

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip
    @param windows_username : (string) windows system user name
    @param windows_password : (string) windows system password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, flag = "", True
    try:
        'Perform power cycle action'
        flag, msg = select_power_option('power_cycle')
        if flag:
            flag, msg = verify_power_state_winrm(idrac_ip, idrac_username, idrac_password,
                                            windows_ip, windows_username, windows_password, 'on')
        time.sleep(5) 
        if g.platform == 'android':
            'Navigate back to previous screen'
            g.driver.back()
            'Navigate back to previous screen'
            g.driver.back()
    except Exception as excp:
        traceback.print_exc()
        flag = False
        msg += str(excp)
    return flag, msg


def perform_shutdown_os_action(idrac_ip, idrac_username, idrac_password,
                                 windows_ip, windows_username, windows_password):
    """
    This function is used to perform and verify shutdown action

    Function Owner : Pooja_Rundwal

    Date created : 10/06/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip
    @param windows_username : (string) windows system user name
    @param windows_password : (string) windows system password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, flag = "", True
    try:
        'Perform shutdown os action'
        flag, msg = select_power_option('shutdown_os')
        if flag:
            flag, msg = verify_power_state_winrm(idrac_ip, idrac_username, idrac_password,
                                            windows_ip, windows_username, windows_password, 'off')
        time.sleep(5)    

        if g.platform == 'android':
            'Navigate back to previous screen'
            g.driver.back()
            'Navigate back to previous screen'
            g.driver.back()
    except Exception as excp:
        traceback.print_exc()
        flag = False
        msg += str(excp)
    return flag, msg
def aadd_idrac(idrac_ip, idrac_username, idrac_password):
    """
    This function is used for adding idrac in OMM

    Function Owner : Pooja_Rundwal

    Date created : 04/05/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    try:
        'Select option to add idrac'
        flag1 = click_add_idrac()

        'Enter idrac details'
        flag2 = enter_idrac_details(idrac_ip, idrac_username, idrac_password)

        'Accept SSL certificate and wait till idrac page loads completely'
        flag3 = aaccept_ssl_certificate()

        status = False if not (flag1 and flag2 and flag3) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg

def add_idrac(idrac_ip, idrac_username, idrac_password):
    """
    This function is used for adding idrac in OMM

    Function Owner : Pooja_Rundwal

    Date created : 04/05/2016

    @param idrac_ip : (string) idrac ip of system
    @param idrac_username : (string) idrac user name
    @param idrac_password : (string) idrac password

    @return status : (bool) status of execution.if successful True else False
    @return msg : (string) step message in case of exception
    """
    msg, status = "", True
    try:
        'Select option to add idrac'
        flag1 = click_add_idrac()

        'Enter idrac details'
        flag2 = enter_idrac_details(idrac_ip, idrac_username, idrac_password)

        'Accept SSL certificate and wait till idrac page loads completely'
        flag3 = accept_ssl_certificate()
        flag4 = idrac_wait_till_page_loads('add_lbl')
        flag5 = idrac_wait_till_page_loads('ome_consle_lbl')
        flag6 =idrac_wait_till_page_loads('addedidrac_ip_txtView')
        #flag4=temporary()

        status = False if not (flag1 and flag2 and flag3 and flag4 and flag5 and flag6) else True
    except Exception as excp:
        traceback.print_exc()
        msg += str(excp)
        status = False
    return status, msg

