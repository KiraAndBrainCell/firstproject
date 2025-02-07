'''
Created on Oct 26, 2016

@author: lex
'''
import traceback
from libs.product.omm.standard.ui_controls import ui_controls
from libs.product.omm.standard import omm_lib
from libs.product.omm.standard import util
from libs.product.omm.standard import global_vars
from libs.product.omm.omm_idrac import ui_idrac
from libs.product.omm.omm_ome import ui_ome
from libs.product.omm.omm_generic import ui_generic
from time import sleep



'Creating objects'
ui_controls = ui_controls()

'Retrieving variables'
g = global_vars
get_obj_identifier = omm_lib.get_obj_identifier


def verify_demomode_first_ome_devices_text():
    """
    This function is used to verify demomode ome servers  devices text 

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            
            flag1 = duplicate_verify_first_ome_device_home_page_txt(ome_dvce_to_click="demomode_device_top_text",device_name='10.255.2.2',ome_device_name="ome_dvce_name",ome_device_home="ome_dvce_home",devices_elemnt="ome_dvce",
                                                                    devices_count="ome_dvce_count",device_crticl_elemnt="ome_dvce_crtical",
                                                                    dvce_warn_elmnt="ome_dvce_warng",dvce_hlth_elmnt="ome_dvce_hlthy",dvce_unknow_elmnt="ome_dvce_unkwn",
                                                                    alerts_elemnt="ome_alrt_txt",alrt_count="ome_alrt_count",alrt_crtical="ome_alrt_critical",alrt_warning="ome_alrt_wrning",
                                                                    alrt_helthy="ome_alrt_hlthy",alrt_info="ome_alrt_info",alrt_unknown="ome_alrt_unknwn",dynamic_file=g.dynamic_second_ome_device_homePage_txt,actul_file=g.second_ome_device_homePage_txt)
            
            flag2 = verify_first_ome_device_alerts()
            
            flag3 = verify_first_ome_device_devices(ntwrk_dvce='Network Devices',rac='RAC',servers='Servers')
        
            flag4 = click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Network Devices')
            flag5 = verify_first_ome_all_ntwrk_devices_homepage_txt(dynami_file=g.dynamic_first_ome_ntwrkdevice_homePage_txt,actual_file=g.first_ome_network_device_home_page_txt)
           
            flag6 = click_on_desired_element(elment_objt='Ome_devices',elmnt_name='RAC')
            
            flag7 = verify_first_ome_all_rac_devices_homepage_txt(dymanic_file=g.dynamic_first_ome_racDevice_homePage_txt,actual_file=g.first_ome_racDevice_homePage_txt)
         
            flag8 = click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Servers')
            
            flag9 = verify_first_ome_all_servers_devices_homepage_txt(dynamic_file=g.dynamic_first_ome_servers_homePage_txt,actual_file=g.first_ome_servers_homePage_txt)
            flag10= duplicate_verify_first_ome_device_home_page_txt(ome_dvce_to_click="demomode_device_top_text",device_name='10.255.2.1',ome_device_name="ome_dvce_name",ome_device_home="ome_dvce_home",devices_elemnt="ome_dvce",
                                                                    devices_count="ome_dvce_count",device_crticl_elemnt="ome_dvce_crtical",
                                                                    dvce_warn_elmnt="ome_dvce_warng",dvce_hlth_elmnt="ome_dvce_hlthy",dvce_unknow_elmnt="ome_dvce_unkwn",
                                                                    alerts_elemnt="ome_alrt_txt",alrt_count="ome_alrt_count",alrt_crtical="ome_alrt_critical",alrt_warning="ome_alrt_wrning",
                                                                    alrt_helthy="ome_alrt_hlthy",alrt_info="ome_alrt_info",alrt_unknown="ome_alrt_unknwn",dynamic_file=g.dynamic_first_ome_device_homePage_txt,actul_file=g.first_ome_device_homePage_txt)
            flag11 = verify_first_ome_device_alerts()
            
            flag12 = verify_first_ome_device_devices(ntwrk_dvce='Network Devices',rac='RAC',servers='Servers')
            #flag4 = verify_first_ome_netwrk_devices_count()
            flag13 =click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Network Devices')
            
            flag14 = verify_first_ome_all_ntwrk_devices_homepage_txt(dynami_file=g.dynamic_first_ome_ntwrkdevice_homePage_txt,actual_file=g.first_ome_network_device_home_page_txt)
            
            #flag15 = verify_first_ome_rac_devices_count()
            
            flag16=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='RAC')
            
            flag17 = verify_first_ome_all_rac_devices_homepage_txt(dymanic_file=g.dynamic_first_ome_racDevice_homePage_txt,actual_file=g.first_ome_racDevice_homePage_txt)
        #flag8 = verify_first_ome_servers_devices_count()
            flag18=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Servers')
            
            flag19 = verify_first_ome_all_servers_devices_homepage_txt(dynamic_file=g.dynamic_first_ome_servers_homePage_txt,actual_file=g.first_ome_servers_homePage_txt)
                  
                  

            status = False if not (flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8 and flag9 and flag10 and flag11 and flag12 and flag13 and flag14 and flag16 and flag17 and flag18 and flag19) else True
            
    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg
def vverify_demomode_first_ome_devices_text():
    """
    This function is used to verify demomode ome servers  devices text 

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            flag1 = duplicate_verify_first_ome_device_home_page_txt(ome_dvce_to_click="demomode_device_top_text",device_name='10.255.2.1',ome_device_name="ome_dvce_name",ome_device_home="ome_dvce_home",devices_elemnt="ome_dvce",
                                                                    devices_count="ome_dvce_count",device_crticl_elemnt="ome_dvce_crtical",
                                                                    dvce_warn_elmnt="ome_dvce_warng",dvce_hlth_elmnt="ome_dvce_hlthy",dvce_unknow_elmnt="ome_dvce_unkwn",
                                                                    alerts_elemnt="ome_alrt_txt",alrt_count="ome_alrt_count",alrt_crtical="ome_alrt_critical",alrt_warning="ome_alrt_wrning",
                                                                    alrt_helthy="ome_alrt_hlthy",alrt_info="ome_alrt_info",alrt_unknown="ome_alrt_unknwn",dynamic_file=g.dynamic_first_ome_device_homePage_txt,actul_file=g.first_ome_device_homePage_txt)
            #flag2 = verify_first_ome_device_alerts()
            
            flag3 = verify_first_ome_device_devices(ntwrk_dvce='Network Devices',rac='RAC',servers='Servers')
        #flag4 = verify_first_ome_netwrk_devices_count()
            flag16=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Network Devices')
            flag5 = verify_first_ome_all_ntwrk_devices_homepage_txt(dynami_file=g.dynamic_first_ome_ntwrkdevice_homePage_txt,actual_file=g.first_ome_network_device_home_page_txt)
            flag6 = verify_first_ome_rac_devices_count()
            flag17=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='RAC')
            
            flag7 = verify_first_ome_all_rac_devices_homepage_txt(dymanic_file=g.dynamic_first_ome_racDevice_homePage_txt,actual_file=g.first_ome_racDevice_homePage_txt)
        #flag8 = verify_first_ome_servers_devices_count()
            flag18=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Servers')
            
            flag9 = verify_first_ome_all_servers_devices_homepage_txt(dynamic_file=g.dynamic_first_ome_servers_homePage_txt,actual_file=g.first_ome_servers_homePage_txt)
            
        # flag10 = duplicate_verify_first_ome_device_home_page_txt(ome_dvce_to_click="demomode_device_top_text",device_name='10.255.2.2',ome_device_name="ome_dvce_name",ome_device_home="ome_dvce_home",devices_elemnt="ome_dvce",
                                                                    #devices_count="ome_dvce_count",device_crticl_elemnt="ome_dvce_crtical",
                                                                    #dvce_warn_elmnt="ome_dvce_warng",dvce_hlth_elmnt="ome_dvce_hlthy",dvce_unknow_elmnt="ome_dvce_unkwn",
                                                                    #alerts_elemnt="ome_alrt_txt",alrt_count="ome_alrt_count",alrt_crtical="ome_alrt_critical",alrt_warning="ome_alrt_wrning",
                                                                    #alrt_helthy="ome_alrt_hlthy",alrt_info="ome_alrt_info",alrt_unknown="ome_alrt_unknwn",dynamic_file=g.dynamic_second_ome_device_homePage_txt,actul_file=g.second_ome_device_homePage_txt)
            
            #flag19 = verify_first_ome_device_alerts()
            
            #flag2 = verify_first_ome_device_devices(ntwrk_dvce='Network Devices',rac='RAC',servers='Servers')
        
            #flag21=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Network Devices')
            #flag22 = verify_first_ome_all_ntwrk_devices_homepage_txt(dynami_file=g.dynamic_first_ome_ntwrkdevice_homePage_txt,actual_file=g.first_ome_network_device_home_page_txt)
           
            #flag23=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='RAC')
            
            #flag24 = verify_first_ome_all_rac_devices_homepage_txt(dymanic_file=g.dynamic_first_ome_racDevice_homePage_txt,actual_file=g.first_ome_racDevice_homePage_txt)
         
            #flag25=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Servers')
            
            #flag26= verify_first_ome_all_servers_devices_homepage_txt(dynamic_file=g.dynamic_first_ome_servers_homePage_txt,actual_file=g.first_ome_servers_homePage_txt)
                  
                  

            status = False if not (flag1 and flag3 and flag16 and flag5 and flag6 and flag17 and flag7 and flag18 and flag9) else True
            
    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_demomode_second_ome_devices_text():
    """
    This function is used to verify demomode ome servers  devices text 

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            flag1 = duplicate_verify_first_ome_device_home_page_txt(ome_dvce_to_click="demomode_device_top_text",device_name='10.255.2.2',ome_device_name="ome_dvce_name",
                                                                    ome_device_home="ome_dvce_home",devices_elemnt="ome_dvce",
                                                                    devices_count="ome_dvce_count",device_crticl_elemnt="ome_dvce_crtical",
                                                                    dvce_warn_elmnt="ome_dvce_warng",dvce_hlth_elmnt="ome_dvce_hlthy",dvce_unknow_elmnt="ome_dvce_unkwn",
                                                                    alerts_elemnt="ome_alrt_txt",alrt_count="ome_alrt_count",alrt_crtical="ome_alrt_critical",alrt_warning="ome_alrt_wrning",
                                                                    alrt_helthy="ome_alrt_hlthy",alrt_info="ome_alrt_info",alrt_unknown="ome_alrt_unknwn",dynamic_file=g.dynamic_second_ome_device_homePage_txt,actul_file=g.second_ome_device_homePage_txt )
            flag2 = verify_first_ome_device_alerts()
            
            flag3 = verify_first_ome_device_devices(ntwrk_dvce='Network Devices',rac='RAC',servers='Servers')
            
            flag4=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Network Devices')
            
            flag5 = verify_first_ome_all_ntwrk_devices_homepage_txt(dynami_file=g.dynamic_second_ome_ntwrkdevice_homePage_txt,actual_file=g.second_ome_network_device_home_page_txt)
          
            flag6=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='RAC')
            
            flag7 = verify_first_ome_all_rac_devices_homepage_txt(dymanic_file=g.dynamic_second_ome_racDevice_homePage_txt,actual_file=g.second_ome_racDevice_homePage_txt)
           
            flag8=click_on_desired_element(elment_objt='Ome_devices',elmnt_name='Servers')
            
            flag9 = verify_first_ome_all_servers_devices_homepage_txt(dynamic_file=g.dynamic_second_ome_servers_homePage_txt,actual_file=g.second_ome_servers_homePage_txt)
                  

          
            status = False if not (flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8 and flag9) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg



def verify_demomode_all_idrac_devices_text():
    """
    This function is used to verify demomode ome servers  devices text 

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            flag1= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.35.0.2',dynamic_file=g.dynamic_second_idrac_homepage_txt,actual_file=g.second_idrac_homepage_txt)
            flag2=verify_idrac_dvce_location_detaails(dynamic_file=g.dynamic_idrac_device_location_stus_txt,actual_file=g.idrac_device_location_txt)
            flag3= verify_idrac_dvce_hardwre_logs()
            flag4=verify_idrac_dvce_helath_status(dynamic_file=g.dynamic_idrac_device_helath_stus_txt,actual_file=g.idrac_health_stus_txt)
            flag5 = go_to_page_name('Home')
            flag6= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.35.0.1',dynamic_file=g.dynamic_first_idrac_homepage_txt,actual_file=g.first_idrac_homepage_txt)
            flag7=verify_idrac_dvce_location_detaails(dynamic_file=g.dynamic_idrac_device_location_stus_txt,actual_file=g.idrac_device_location_txt)
            flag8= verify_idrac_dvce_hardwre_logs()
            flag9=verify_idrac_dvce_helath_status(dynamic_file=g.dynamic_idrac_device_helath_stus_txt,actual_file=g.idrac_health_stus_txt)
            flag10 = go_to_page_name('Home')
            flag11= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.35.0.3',dynamic_file=g.dynamic_third_idrac_homepage_txt,actual_file=g.third_idrac_homepage_txt)
            flag12=verify_idrac_dvce_location_detaails(dynamic_file=g.dynamic_idrac_device_location_stus_txt,actual_file=g.idrac_device_location_txt)
            flag13= verify_idrac_dvce_hardwre_logs()
            flag14=verify_idrac_dvce_helath_status(dynamic_file=g.dynamic_idrac_device_helath_stus_txt,actual_file=g.idrac_health_stus_txt)
            flag15 = go_to_page_name('Home')
            flag16= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.40.0.1',dynamic_file=g.dynamic_fourth_idrac_homepage_txt,actual_file=g.fourth_idrac_homepage_txt)
            flag17=verify_idrac_dvce_location_detaails(dynamic_file=g.dynamic_fourth_idrac_location_stus_txt,actual_file=g.fourth_idrac_device_location_txt)
            flag18= verify_idrac_dvce_hardwre_logs()
            flag19=verify_idrac_dvce_helath_status(dynamic_file=g.dynamic_fourth_idrac_device_helath_stus_txt,actual_file=g.fourth_idrac_health_stus_txt)
            flag20 = go_to_page_name('Home')
            flag21= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.40.0.2',dynamic_file=g.dynamic_fifth_idrac_homepage_txt,actual_file=g.fifth_idrac_homepage_txt)
            flag22=verify_idrac_dvce_location_detaails(dynamic_file=g.dynamic_fourth_idrac_location_stus_txt,actual_file=g.fourth_idrac_device_location_txt)
            flag23= verify_idrac_dvce_hardwre_logs()
            flag24=verify_idrac_dvce_helath_status(dynamic_file=g.dynamic_fourth_idrac_device_helath_stus_txt,actual_file=g.fourth_idrac_health_stus_txt)
            flag25 = go_to_page_name('Home')
            flag26=verify_sixth_idrac_home_page_text()
            flag27= verify_idrac_dvce_hardwre_logs()
            flag28=verify_idrac_dvce_helath_status(dynamic_file=g.dynamic_idrac_device_helath_stus_txt,actual_file=g.idrac_health_stus_txt)
            flag29 = go_to_page_name('Home')
            
            
            
            
            
            flag30=verify_seventh_idrac_home_page_text()
            flag31=verify_idrac_dvce_location_detaails(dynamic_file=g.dynamic_idrac_device_location_stus_txt,actual_file=g.idrac_device_location_txt)
            flag32= verify_idrac_dvce_hardwre_logs()
            flag33=verify_idrac_dvce_helath_status(dynamic_file=g.dynamic_idrac_device_helath_stus_txt,actual_file=g.idrac_health_stus_txt)
            flag34 = go_to_page_name('Home')

            
            
            
            
            
            #flag26= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.35.0.1',dynamic_file=g.dynamic_sixth_idrac_homepage_txt,actual_file=g.sixth_idrac_homepage_txt)
            #flag27= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.35.0.1',dynamic_file=g.dynamic_seventh_idrac_homepage_txt,actual_file=g.seventh_idrac_homepage_txt)

            
            
            #flag5= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.35.0.1',dynamic_file=g.dynamic_first_idrac_homepage_txt,actual_file=g.first_idrac_homepage_txt)

          
           
            #flag6=verify_idrac_dvce_location_detaails()
            #flag7= verify_idrac_dvce_hardwre_logs()
            #flag8=verify_idrac_dvce_helath_status()
            #flag9 = go_to_page_name('Home')
            #flag10= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.35.0.1',dynamic_file=g.dynamic_first_idrac_homepage_txt,actual_file=g.first_idrac_homepage_txt)

          
            #flag0=duplicate_verify_first_idrac_home_page_text()
           
            
            
            
            
            #flag2 = verify_first_idrac_dvce_hardwre_logs()
            #flag3 = verify_first_idrac_dvce_firmware_dtls()
            #flag4 = verify_first_idrac_dvce_netwrk_dtls()
            #flag5 = verify_first_idrac_dvce_hardwre_inventory()
            #flag6 = verify_first_idrac_helath_status_element()
            #flag7 = verify_first_idrac_warranty_info_element()
            #flag8 = verify_first_idrac_dvce_location_dtls()
            #flag9 = verify_first_idrac_dvce_online_resoruces()
            #flag10 = verify_sixth_idrac_home_page_text()
            #flag11 = verify_sixth_idrac_dvce_hardwre_logs()
            #flag12 = verify_sixth_idrac_dvce_firmware_dtls()
            #flag13 = verify_sixth_idrac_dvce_netwrk_dtls()
            #flag14 = verify_sixth_idrac_helath_status_element()
            #flag15 = verify_sixth_idrac_warranty_info_element()
            #flag16 = verify_sixth_idrac_dvce_online_resoruces()

            status = False if not (flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8 and flag9 and flag10 and flag11 and flag12 and flag13 and flag14 and flag15 and flag16 and flag17 and flag18 and flag19 and flag20
                                   and flag21 and flag22 and flag23 and flag24 and flag25 and flag26 and flag27 and flag28 and flag29 and flag30 and flag31 and flag32 and flag33 and flag34) else True
            #status = False if not (flag1) else True
 
    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg

def vverify_demomode_all_idrac_devices_text():
    """
    This function is used to verify demomode ome servers  devices text 

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            
            flag6= duplicate_verify_first_idrac_home_page_text(clikble_idrc_name='10.35.0.1',dynamic_file=g.dynamic_first_idrac_homepage_txt,actual_file=g.first_idrac_homepage_txt)
            flag7=verify_idrac_dvce_location_detaails(dynamic_file=g.dynamic_idrac_device_location_stus_txt,actual_file=g.idrac_device_location_txt)
            flag8= verify_idrac_dvce_hardwre_logs()
            flag9=verify_idrac_dvce_helath_status(dynamic_file=g.dynamic_idrac_device_helath_stus_txt,actual_file=g.idrac_health_stus_txt)
            flag10 = go_to_page_name('Home')

      
            status = False if not (flag6 and flag7 and flag8 and flag9 and flag10) else True
 
    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg









def exit_demomode_frm_all_pages():
    """
    This function is used to Exit demo mode option from every page

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
           
            flag1 = go_to_page_name("Settings") 
            sleep(3)
            'exit demo mode from home page'
            flag2 = exit_demomode("Exit Demo Mode")
            'enable demo mode'
            sleep(3)
            flag3 = enable_demomode()
            sleep(3)
            flag4 = go_to_page_name("Home")
            'exit demo mode '
            flag5 = exit_demomode("Exit Demo Mode")
            sleep(3)
            'enable demo mode'
            flag6 = enable_demomode()
            sleep(3)
            flag7 = go_to_page_name("Task Manager")
         
            sleep(3)
            'exit demo mode from home page'
            flag8 = exit_demomode("Exit Demo Mode")
            'enable demo mode'
            sleep(3)
            flag9 = enable_demomode()
            sleep(3)
            flag11 = go_to_page_name("App Log")
         
            sleep(3)
            'exit demo mode from home page'
            flag10 = exit_demomode("Exit Demo Mode")
            'enable demo mode'
            sleep(3)
            flag11 = enable_demomode()
            sleep(3)
            flag12 = go_to_page_name("Home")
            
           

            status = False if not ( flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7 and flag8 and flag9 and flag10 and flag11 and flag12) else True
    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_enable_demomode_from_settings():
    """
    This function is used for verifying enable demo mode option from setting

    Function Owner : nagarjuna

    Date created : 7/08/2016

    @return True/False : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

            flag1 = verify_enable_demomode_option()

            status = False if not (flag1) else True
            
        else:
            flag1 = verify_enable_demomode_option()

            status = False if not (flag1) else True   

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg





def try_demoo_continue():

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
            flag2 = ui_controls.button(get_obj_identifier('demo_tryDemoMode_btn'))
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







def verify_enable_demomode_option():

    """
    This function is used for verifying enable/disable  demo mode option
    from setting

    Function Owner : nagarjuna

    Date created : 7/08/2016

    @return True/False : (bool)status of execution.if successful
    True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'select the settings page from demo mode settings'
            flag1=go_to_page_name("Settings")

            'swipe down to visible enable demo mode toggle switch'
            flag2 = ui_controls.swipe_down()
            sleep(3)
            'verify the page label when demo mode is enabled'
            flag3,msg = ui_generic.pagelabel_element_textvalidation('DemoMode_enable_Bar_Tittle','DEMO MODE SETTINGS')
            'click on toggle switch to disable demo mode option'
            flag4 = ui_controls.Click(get_obj_identifier('DemoMode_Enable_disble_toggle_btn'))
            print "clicked on enable/disable demo mode toggle switch to disable demo mode"
            sleep(3)
            'verify the page label when demo mode is disabled'
            flag5,msg = ui_generic.pagelabel_element_textvalidation('setings_lbl','Settings')
            'click one toggle switch to enable'
            flag6 = ui_controls.Click(get_obj_identifier('DemoMode_Enable_disble_toggle_btn'))
            print 'clicked on enable/disable demo mode toggle switch to enable demo mode'
           
            sleep(4)
            'verify Enable Demo mode  pop up window appears'
            element = ui_controls.ui_element(get_obj_identifier('addOme_certificate_win'))
            print 'alert is verified'
            if(element is None):
                flag5 = False
            else:
                flag5 = True
                sleep(3)
            'accept the Popup'    
            flag7 = ui_controls.Click(get_obj_identifier('DemoModeEnable_Popup_ok_btn'))
            print'accepted enable demo mode pop up'

            flag8,msg = ui_generic.pagelabel_element_textvalidation('DemoMode_enable_Bar_Tittle','DEMO MODE SETTINGS')
            
            sleep(3)

            status = False if not (flag1 and flag2 and flag3 and flag4 and 
                                   flag5 and flag6 and flag7 and flag8) else True
        else:
            'click on omenu button in demo mode'
            flag1 = ui_controls.Click(get_obj_identifier('DemoMode_menu'))
            'click on settings option'
            flag2 = ui_controls.Click(get_obj_identifier('DemoMode_setting_option'))
            'verify page label when demo mode is enabled'
            'verify  bar title text when demo mode is enabled'
            flag3,msg = ui_generic.element_textvalidation('DemoMode_enable_Bar_Tittle','DEMO MODE')
            'click on toggle button to disable demo mode option'
            flag5 = ui_controls.Click(get_obj_identifier('DemoMode_Enable_disble_toggle_btn'))
            'verify  bar title text when demo mode is disabled'
            flag4,msg = ui_generic.element_textvalidation('DemoMode_Disable_bar_Tittle','Settings')
            sleep(3)
            'click on toggle button to enable DemoMode'
            flag5 = ui_controls.Click(get_obj_identifier('DemoMode_Enable_disble_toggle_btn'))    
            
            'accept a pop up by clicking on ok button'
            flag6 = ui_controls.Click(get_obj_identifier('DemoModeEnable_Popup_ok_btn'))
            sleep(3)
        
            flag7=ui_controls.back_button()
            
            
            
            
            
            status = False if not (flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag7) else True
                                       

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


def go_to_main_page_and_child_page(main_page_name_one,child_page_name):

    """
    This function is used to get home page in demo mode

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
              
                'click on menu to get drop down menu options'
                flag1 = ui_controls.button(get_obj_identifier('test_demomode_menu'))
                print"clicked on main menu button to get"+str(main_page_name_one.strip())
                sleep(4)
                'click on drop down home option to get home page'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('test_demomode_menu_options'))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == main_page_name_one.strip():
                        item.click()
                        print "clicked on main option, name is==>"+str(main_page_name_one.strip())
                    if item.get_attribute('text').strip() == child_page_name.strip() : 
                        item.click()  
                        print "clicked option page, page name is==>"+str(child_page_name.strip())
                        break

                    status = False if not (flag1) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg
def go_to_page_name(page_name):

    """
    This function is used to get any page from demo mode menu

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
               
                'click on menu to get drop down menu options'
                flag1 = ui_controls.button(get_obj_identifier('test_demomode_menu'))
                sleep(3)
                print"clicked on main menu button to get option " +str(page_name.strip())
                sleep(4)
                'get all drop down option from demo mode menu button and get the desired page'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('test_demomode_menu_options'))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == page_name.strip() : 
                        item.click()  
                        print "clicked on page, page name is==>"+str(page_name.strip())
                        break
                sleep(3)    

                status = False if not (flag1) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def click_on_desired_element(elment_objt=None,elmnt_name=None):

    """
    This function is used to get any page from demo mode menu

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
               
                sleep(3)
                'get all drop down option from demo mode menu button and get the desired page'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier(elment_objt))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == elmnt_name.strip() : 
                        item.click()  
                        print "clicked on page, page name is==>"+str(elmnt_name.strip())
                        break

                    status = False if not ( ) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg



def exit_demomode(exit_demo_mode_name):

    """
    This function is used exit from demo mode

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag1 : (bool)status of execution.if successful True else False

    @return msg: (string) exception string in case of any error

    """

    msg, status = "", True

    try:

        if g.platform == 'android':

            'Click on the demo mode main menu button to get exit demo mode option '
            flag1 = ui_controls.button(get_obj_identifier('test_demomode_menu'))
            print "clicked on main menu button to get option"+str(exit_demo_mode_name.strip())
            
            flag2 = ui_controls.Click(get_obj_identifier('exit_demomode'))       
            sleep(3)
            'click on pop up ok button to exit demo mode'
            flag3= ui_controls.Click(get_obj_identifier('DemoModeEnable_Popup_ok_btn1'))
            print "accepted pop up button to exit demo mode"
            'verify wether demo mode setting label is displaying or not'
          

            status = False if not (flag1 and flag2 and flag3) else True
        else:
            'click on omenu button in demo mode'
            flag1 = ui_controls.Click(get_obj_identifier('DemoMode_menu'))
            flag2 = ui_controls.Click(get_obj_identifier('exit_dmo_mode'))

            flag3 = ui_controls.Click(get_obj_identifier('yes_btn'))
            status = False if not (flag1 and flag2 and flag3) else True
            
    except Exception as excp:

            traceback.print_exc()

            msg += str(excp)

            status = False

    return status, msg


def enable_demomode():

    """
    This function is used to enable demo mode from settings in demo mode

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'Click on the main menu to get drop down menu options'
            flag1 = ui_controls.Click(get_obj_identifier('test_demomode_menu'))
            print "clicked on main menu button to get setting page"
            sleep(3)
            'click on settings from drop down menu options'
            main_menu_items = ui_controls.ui_elements(get_obj_identifier('test_demomode_menu_options'))
            for item in main_menu_items:
                if item.get_attribute('text').strip() == "Settings":
                    item.click()
                    flag1 = True
                    print "clicked settings option to get setting page"
                    break
            sleep(3)
            flag2 = ui_controls.swipe_down()
            'click on toggle button to enable demo mode option'
            flag3 = ui_controls.Click(get_obj_identifier('DemoMode_Enable_disble_toggle_btn')) 
            print "clicked on enable/disable  demo mode toggle switch to enable demo mode"
            sleep(3) 
            'accept enable demo mode popup'
            flag4 = ui_controls.Click(get_obj_identifier('DemoModeEnable_Popup_ok_btn'))
            print "accepted enable demo mode pop up button"
            'verify wether demo mode setting label is displaying or not'
          
            status = False if not (flag1 and flag2 and flag3 and flag4) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def demomode_tskmnger_page():

    """
    This function is used to get taskmangaer page

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'click on menu to get menu options'
            flag1 = ui_controls.button(get_obj_identifier('test_demomode_menu'))
            sleep(4)
            'click on task manager from drop down menu options'
            main_menu_items = ui_controls.ui_elements(get_obj_identifier('test_demomode_menu_options'))
            for item in main_menu_items:
                if item.get_attribute('text').strip() == "Task Manager":
                    item.click()
                    print "clicked on task manger option to get task manager page"
                    break

            status = False if not (flag1) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def demomode_settings_page():

    """
    This function is used to get demo mode settings page

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'click on menu to get drop down menu options'
            flag1 = ui_controls.button(get_obj_identifier('test_demomode_menu'))
            sleep(4)
            'click on menu to get home menu drop down option'
            main_menu_items = ui_controls.ui_elements(get_obj_identifier('test_demomode_menu_options'))
            for item in main_menu_items:
                if item.get_attribute('text').strip() == "Settings":
                    item.click()
                    print "cliked to settings option to get setings page"
                    break

            status = False if not (flag1) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def demomode_log_page():

    """
    This function is used to get demo mode settings page

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'click on menu to get menu options'
            flag1 = ui_controls.button(get_obj_identifier('test_demomode_menu'))
            sleep(4)
            'click on log option from drop down menu options'
            main_menu_items = ui_controls.ui_elements(get_obj_identifier('test_demomode_menu_options'))
            for item in main_menu_items:
                if item.get_attribute('text').strip() == "Log":
                    item.click()
                    print "clicked on log to get log page "
                    break

            status = False if not (flag1) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def demomode_about_page():

    """
    This function is used to get demo mode settings page

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'click on menu to get menu options'
            flag1 = ui_controls.button(get_obj_identifier('test_demomode_menu'))
            sleep(4)
            'click on about option from drop down menu options'
            main_menu_items = ui_controls.ui_elements(get_obj_identifier('test_demomode_menu_options'))
            for item in main_menu_items:
                if item.get_attribute('text').strip() == "About":
                    item.click()
                    print "clicked on about option to get about page "
                    break

            status = False if not (flag1) else True
        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def demomode_idrac_home_page():

    """
    This function is used to get demo mode Home page

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            'click on any one of idrac device to get idrac device home page'
            main_menu_items = ui_controls.ui_elements(get_obj_identifier('DemoMode_devices_textview'))
            for item in main_menu_items:
                if item.get_attribute('text').strip() == "RAC1":
                    item.click()
                    print "clicked on i drac device in demo mode"
                    break

            status = False if not () else True

        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'), g.password)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def demomode_ome_home_page():

    """
    This function is used to get demo mode Home page

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

            'click on any one of ome device device to get ome  device home page'
            main_menu_items = ui_controls.ui_elements(get_obj_identifier('DemoMode_devices_textview'))
            for item in main_menu_items:
                if item.get_attribute('text').strip() == "HOME":
                    item.click()
                    print "clicked on ome device in demo mode"
                    break
 
            status = False if not () else True

        else:
            'Setting values on Create Password text box in ios. Using set value as send_keys failing here'
            flag1 = ui_controls.setValue(get_obj_identifier('login_createPassword_txt'),g.password)

            status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_first_ome_device_home_page_txt():

    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                sleep(3)
                'get all the element text view in home page'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('demomode_device_top_text'))
                'click on first ome device'
                main_menu_items[0].click()
                dict = []

                'get the text view of ome device tag'
                ome_device = ui_controls.text_view(get_obj_identifier('ome_dvce_name'))
                dict.append(ome_device)
                'get the text view of ome device home tag'
                home_txt = ui_controls.text_view(get_obj_identifier('ome_dvce_home'))
                dict.append(home_txt)
                'get the text of critical element from devices'
                critical_txt = ui_controls.text_view(get_obj_identifier('ome_dvce_crtical'))
                dict.append(critical_txt)
                'get the text view of warning element from devices'
                warning_txt = ui_controls.text_view(get_obj_identifier('ome_dvce_warng'))
                dict.append(warning_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier('ome_dvce_hlthy'))
                dict.append(hlthy_txt)
                'get the text view of unknown element from devices'
                unkwn_txt = ui_controls.text_view(get_obj_identifier('ome_dvce_unkwn'))
                dict.append(unkwn_txt)
                'get the text view of ome devices count'
                ome_dvce_count = ui_controls.text_view(get_obj_identifier('ome_dvce_count'))
                dict.append(ome_dvce_count)
                'get the text view of devices from devices'
                devices_txt = ui_controls.text_view(get_obj_identifier('ome_dvce'))
                dict.append(devices_txt)
                'change to native context before going to swipe'
                flag1 = ui_controls.switch_to_context()
                'swipe down '
                flag2 = ui_controls.swipe_down()
                sleep(3)
                'get the text view of alert count element from alerts'
                ome_alrt_count = ui_controls.text_view(get_obj_identifier('ome_alrt_count'))
                dict.append(ome_alrt_count)
                'get the text view of alerts element from alerts'
                alerts_txt = ui_controls.text_view(get_obj_identifier('ome_alrt_txt'))
                dict.append(alerts_txt)
                'get the text view of critical element from alerts'
                alrt_criticl_txt = ui_controls.text_view(get_obj_identifier('ome_alrt_critical'))
                dict.append(alrt_criticl_txt)
                'get the text view of warning element from alerts'
                alrt_warn_txt = ui_controls.text_view(get_obj_identifier('ome_alrt_wrning'))
                dict.append(alrt_warn_txt)
                'get the text view of healthy element from alerts'
                alrt_hlthy_txt = ui_controls.text_view(get_obj_identifier('ome_alrt_hlthy'))
                dict.append(alrt_hlthy_txt)
                'get the text view of info element from alerts'
                alrt_info_txt = ui_controls.text_view(get_obj_identifier('ome_alrt_info'))
                dict.append(alrt_info_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier('ome_alrt_unknwn'))
                dict.append(alrt_unkwn_txt)

                'create a new text file for demo mode idrac and ome devices ' 
                util.open_file(g.dynamic_first_ome_device_homePage_txt)
                'write a text file'
                for txt in dict:
                    util.write_file(g.dynamic_first_ome_device_homePage_txt, txt)
                'read the demo mode devices text file'
                actual_text = util.read_file(g.dynamic_first_ome_device_homePage_txt)

                text_to_verify = util.read_file(g.first_ome_device_homePage_txt)
                if not text_to_verify:
                        print "Unable to retrieve text to verify first ome device home page elements text "

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():   
                        print " first Ome device  home page  text verified sucessfully"

                else:
                        print "first ome device home page text verified unsucessfully"

                status = False if not (flag1 and flag2) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def duplicate_verify_first_ome_device_home_page_txt(ome_dvce_to_click=None,device_name=None,ome_device_name=None,ome_device_home=None,devices_elemnt=None,devices_count=None,device_crticl_elemnt=None,
                                                    dvce_warn_elmnt=None,dvce_hlth_elmnt=None,dvce_unknow_elmnt=None,alerts_elemnt=None,alrt_count=None,alrt_crtical=None,
                                                    alrt_warning=None,alrt_helthy=None,alrt_info=None,alrt_unknown=None,dynamic_file=None,actul_file=None):

    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                sleep(3)
               
                main_menu_items = ui_controls.ui_elements(get_obj_identifier(ome_dvce_to_click))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == device_name.strip() : 
                        item.click()  
                        print "clicked on ome device , ome  name is==>"+str(device_name.strip())
                        break

                dict = []

                'get the text view of ome device tag'
                ome_device = ui_controls.text_view(get_obj_identifier(ome_device_name))
                dict.append(ome_device)
                'get the text view of ome device home tag'
                home_txt = ui_controls.text_view(get_obj_identifier(ome_device_home))
                dict.append(home_txt)
                'get the text of critical element from devices'
                critical_txt = ui_controls.text_view(get_obj_identifier(devices_elemnt))
                dict.append(critical_txt)
                'get the text view of warning element from devices'
                warning_txt = ui_controls.text_view(get_obj_identifier(devices_count))
                dict.append(warning_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(device_crticl_elemnt))
                dict.append(hlthy_txt)
                sleep(3)
                'get the text view of unknown element from devices'
                unkwn_txt = ui_controls.text_view(get_obj_identifier(dvce_warn_elmnt ))
                dict.append(unkwn_txt)
                'get the text view of ome devices count'
                ome_dvce_count = ui_controls.text_view(get_obj_identifier(dvce_hlth_elmnt ))
                dict.append(ome_dvce_count)
                'get the text view of devices from devices'
                devices_txt = ui_controls.text_view(get_obj_identifier(dvce_unknow_elmnt ))
                dict.append(devices_txt)
                'change to native context before going to swipe'
                #flag1 = ui_controls.switch_to_context()
                sleep(2)
                'swipe down '
                flag1 = ui_controls.swipe_down()
                sleep(3)
                'get the text view of alert count element from alerts'
                ome_alrt_count = ui_controls.text_view(get_obj_identifier(alerts_elemnt))
                dict.append(ome_alrt_count)
                'get the text view of alert count element from alerts'
                ome_alrt_count = ui_controls.text_view(get_obj_identifier(alrt_count))
                dict.append(ome_alrt_count)
                'get the text view of alerts element from alerts'
                alerts_txt = ui_controls.text_view(get_obj_identifier(alrt_crtical))
                dict.append(alerts_txt)
                'get the text view of critical element from alerts'
                alrt_criticl_txt = ui_controls.text_view(get_obj_identifier(alrt_warning))
                dict.append(alrt_criticl_txt)
                'get the text view of warning element from alerts'
                alrt_warn_txt = ui_controls.text_view(get_obj_identifier(alrt_helthy))
                dict.append(alrt_warn_txt)
                'get the text view of healthy element from alerts'
                alrt_hlthy_txt = ui_controls.text_view(get_obj_identifier(alrt_info))
                dict.append(alrt_hlthy_txt)
                sleep(3)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(alrt_unknown))
                dict.append(alrt_unkwn_txt)

                'create a new text file for demo mode idrac and ome devices ' 
                util.open_file(dynamic_file)
                'write a text file'
                for txt in dict:
                    util.write_file(dynamic_file,txt)
                    print txt
                'read the demo mode devices text file'
                actual_text = util.read_file(dynamic_file)

                text_to_verify = util.read_file(actul_file)
                if not text_to_verify:
                        print "Unable to retrieve text to verify first ome device home page elements text "

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():   
                        print "  Ome device  home page  text verified successfully,ome device name is"+str(device_name.strip())

                else:
                        print " ome device home page text verified unsuccessfully,ome device name is"+str(device_name.strip())
                sleep(2)

                status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg




def verify_first_ome_device_alerts():

    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
            
                flag0= ui_controls.Click(get_obj_identifier('ome_alrt_txt'))
                'verify Alerts label'
                flag1= element_textvalidation('alrt_lbl','Alerts')
                sleep(4)   
                'click on alert text element'
                flag2 = select_ome_device_alert_name('All Alerts')
                sleep(3)
                'click on spinner view'
                flag3 = select_ome_device_alert_name('All Internal Alerts')
                sleep(3)
                'click on all alerts '
                flag4 = select_ome_device_alert_name('Critical Alerts')
                sleep(3)
                'click on spinner view '
                flag5 = select_ome_device_alert_name('Normal Alerts')
                sleep(3)
                'click on all internal alerts'
                flag6 = select_ome_device_alert_name('Unknown Alerts')
                sleep(7)
                'click on spinner view'
                #flag7 = select_ome_device_alert_name('Warning Alerts')
                flag7= ui_controls.button(get_obj_identifier('more_options_btn'))
                sleep(3)
                flag8 = ui_controls.button(get_obj_identifier('refresh_btn'))
                sleep(4)
                flag8 = ui_controls.back_button()
                sleep(3)
               

                status = False if not (flag0 and flag1 and flag2 and flag3 and flag4 and flag5 and flag6 and flag8) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg
def verify_idrac_dvce_hardwre_logs(clik_hrdrelogs_name='hardwre_logs_elmnt'):

    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
           
                flag0= ui_controls.Click(get_obj_identifier(clik_hrdrelogs_name))
                sleep(3)
                flag1= element_textvalidation('hardwre_logs_lbl','Hardware Log')
                
             
                
                sleep(4)   
                'click on alert text element'
                flag2=select_idrac_dvce_hrdwre_logs(drop_down_spiner='Alerts_spiner_view',selectble_alert_name='System Event Log',Alerts_top_txt='Hrdware_log_alrts_element')
                #flag2 = select_ome_device_alert_name('System Event Log')
                sleep(3)
                'click on spinner view'
                flag3=select_idrac_dvce_hrdwre_logs(drop_down_spiner='Alerts_spiner_view',selectble_alert_name='Lifecycle Log',Alerts_top_txt='life_cycle_log')
                sleep(15)
                
                flag4 = ui_controls.back_button()
                sleep(3)
               

                status = False if not (flag0 and flag1 and flag2 and flag3 and flag4 ) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg



def verify_idrac_dvce_helath_status(clik_hlth_ststus_elmnt='hlth_status_elemnt',hlth_stus_proprty='helth_stus_proprty',hlth_stus_vle='helth_stus_vle',hlth_stus_tmp='helth_stus_tmp',
                                    hlth_stus_pwr_one='helth_stus_pwr_one',hlth_stus_stroge='helth_stus_stroge',
                                    hlth_stus_btry='helth_stus_btry',hlth_stus_fan='helth_stus_fan',hlth_stus_intruson='helth_stus_intruson',
                                    hlth_stus_pwr_two='helth_stus_pwr_two',hlth_stus_remoble_flash='helth_stus_remoble_flash',
                                    hlth_stus_tempar='helth_stus_tempar',hlth_stus_vol='helth_stus_vol',dynamic_file=None,actual_file=None):

    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                sleep(3)
                'get the text view of healthy element from devices'
                flag0 = ui_controls.Click(get_obj_identifier(clik_hlth_ststus_elmnt))

                dict = []
              
                sleep(3)
                flag1= element_textvalidation('health_sts_lbl','Health Status')
                sleep(3)
            
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_proprty))
                dict.append(hlthy_txt)
                sleep(3)
                'get the text view of unknown element from devices'
                unkwn_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_vle))
                dict.append(unkwn_txt)
                'get the text view of ome devices count'
                ome_dvce_count = ui_controls.text_view(get_obj_identifier(hlth_stus_tmp))
                dict.append(ome_dvce_count)
                sleep(3)
                'get the text view of devices from devices'
                devices_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_pwr_one))
                dict.append(devices_txt)
                'change to native context before going to swipe'
                #flag1 = ui_controls.switch_to_context()
                'swipe down '
                sleep(3)
                flag2 = ui_controls.swipe_down()
                
                'get the text view of alerts element from alerts'
                alerts_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_stroge))
                dict.append(alerts_txt)
                'get the text view of critical element from alerts'
                alrt_criticl_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_btry))
                dict.append(alrt_criticl_txt)
                'get the text view of warning element from alerts'
                alrt_warn_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_fan))
                dict.append(alrt_warn_txt)
                'get the text view of healthy element from alerts'
                alrt_hlthy_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_intruson))
                dict.append(alrt_hlthy_txt)
                sleep(3)
                'get the text view of healthy element from alerts'
                hlth_power = ui_controls.text_view(get_obj_identifier(hlth_stus_pwr_two))
                dict.append(hlth_power)
                'get the text view of healthy element from alerts'
                hlth_flash = ui_controls.text_view(get_obj_identifier(hlth_stus_remoble_flash))
                dict.append(hlth_flash)
                sleep(3)
                'get the text view of healthy element from alerts'
                hlthy_tmp = ui_controls.text_view(get_obj_identifier(hlth_stus_tempar))
                dict.append(hlthy_tmp)
                'get the text view of healthy element from alerts'
                hlth_voltge = ui_controls.text_view(get_obj_identifier(hlth_stus_vol))
                dict.append(hlth_voltge)
                sleep(3)

                'create a new text file for demo mode idrac and ome devices ' 
               
                util.open_file(dynamic_file)
                'write a text file'
                for txt in dict:
                  
                    util.write_file(dynamic_file,txt)
                    print txt
                'read the demo mode devices text file'
                actual_text = util.read_file(dynamic_file)

                text_to_verify = util.read_file(actual_file)
                if not text_to_verify:
                        print "Unable to retrieve text to verify first ome device home page elements text "

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():   
                        print " idrac device health status  text verified successfully"

                else:
                        print "idrac device health status text verified unsuccessfully"
                sleep(3)
                flag3 = ui_controls.back_button() 
                       

                status = False if not (flag0 and flag1 and flag2 and flag3) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_idrac_dvce_location_detaails(loction_elmnt='location_details_elmnt',loction_proprty='location_proprty',loction_vle='location_vle',loction_data_cntr='location_data_cntr',
                                    loction_room='location_room',loction_aisle='location_aisle',
                                    loction_rac='location_rac',loction_slot='location_slot',loction_data_vle='location_data_vle',loction_room_vle='location_room_vle',loction_aisle_vle='location_aisle_vle',
                                    loction_rac_vle='location_rac_vle',loction_slot_vle='location_rac_vle',dynamic_file=None,actual_file=None):

    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                sleep(3)
                
                flag0 = ui_controls.Click(get_obj_identifier(loction_elmnt))
                sleep(3)
                dict = []
               
                flag1= element_textvalidation('location_info_lbl','Location Information')
            
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(loction_proprty))
                dict.append(hlthy_txt)
                'get the text view of unknown element from devices'
                unkwn_txt = ui_controls.text_view(get_obj_identifier(loction_vle))
                dict.append(unkwn_txt)
                'get the text view of ome devices count'
                ome_dvce_count = ui_controls.text_view(get_obj_identifier(loction_data_cntr))
                dict.append(ome_dvce_count)
                sleep(3)
                'get the text view of devices from devices'
                devices_txt = ui_controls.text_view(get_obj_identifier(loction_room))
                dict.append(devices_txt)
                'change to native context before going to swipe'
                #flag1 = ui_controls.switch_to_context()
            
              
                
                'get the text view of alerts element from alerts'
                alerts_txt = ui_controls.text_view(get_obj_identifier(loction_aisle))
                dict.append(alerts_txt)
                'get the text view of critical element from alerts'
                alrt_criticl_txt = ui_controls.text_view(get_obj_identifier(loction_rac))
                dict.append(alrt_criticl_txt)
                'get the text view of warning element from alerts'
                alrt_warn_txt = ui_controls.text_view(get_obj_identifier(loction_slot))
                dict.append(alrt_warn_txt)
                sleep(3)
                'get the text view of healthy element from alerts'
                alrt_hlthy_txt = ui_controls.text_view(get_obj_identifier(loction_data_vle))
                dict.append(alrt_hlthy_txt)
                'get the text view of healthy element from alerts'
                hlth_power = ui_controls.text_view(get_obj_identifier(loction_room_vle))
                dict.append(hlth_power)
                sleep(3)
                'get the text view of healthy element from alerts'
                hlth_flash = ui_controls.text_view(get_obj_identifier(loction_aisle_vle))
                dict.append(hlth_flash)
                'get the text view of healthy element from alerts'
                hlthy_tmp = ui_controls.text_view(get_obj_identifier(loction_rac_vle))
                dict.append(hlthy_tmp)
                'get the text view of healthy element from alerts'
                hlth_voltge = ui_controls.text_view(get_obj_identifier(loction_slot_vle))
                dict.append(hlth_voltge)
                sleep(3)

                util.open_file(dynamic_file)
                'write a text file'
                for txt in dict:
                    
                    util.write_file(dynamic_file,txt)
                    print txt
                'read the demo mode devices text file'
                actual_text = util.read_file(dynamic_file)

                text_to_verify = util.read_file(actual_file)
                if not text_to_verify:
                        print "Unable to retrieve text to verify first ome device home page elements text "

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():   
                        print " idrac device location details  text verified successfully"

                else:
                        print "idrac device location details text verified unsuccessfully"
                sleep(3)        
                flag3 = ui_controls.back_button() 
                 
            

                status = False if not (flag0 and flag1 and flag3) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg






def select_ome_device_alert_name(clickble_alert_name):

    """
    This function is used to select ome alerts drop down list

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                
                'click on menu to get drop down menu options'
                flag1 = ui_controls.Click(get_obj_identifier('Alerts_spiner_view'))
                print"clicked on alert drop down to get=> " +str(clickble_alert_name.strip())
                sleep(4)
                'get all drop down option from demo mode menu button and get the desired page'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('Alerts_spiner_view'))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == clickble_alert_name.strip() : 
                        item.click()  
                        print "clicked on alert, alert name is==>"+str(clickble_alert_name.strip())
                        break
                sleep(3)    
                if  ui_controls.isdisplayed(get_obj_identifier('Alerts_top_txt'))  :
                        print "alerts which are displaying=> " +str(clickble_alert_name.strip())
               
                else :
                        print "alerts which are not displaying " +str(clickble_alert_name.strip())
                 
                status = False if not (flag1) else True

               

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg



def select_idrac_dvce_hrdwre_logs(drop_down_spiner=None,selectble_alert_name=None,Alerts_top_txt=None):

    """
    This function is used to select ome alerts drop down list

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                
                'click on menu to get drop down menu options'
                flag1 = ui_controls.Click(get_obj_identifier(drop_down_spiner))
                print"clicked on alert drop down to get=> " +str(selectble_alert_name.strip())
                sleep(4)
                'get all drop down option from demo mode menu button and get the desired page'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier(drop_down_spiner))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == selectble_alert_name.strip() : 
                        item.click()  
                        print "clicked on alert, alert name is==>"+str(selectble_alert_name.strip())
                        break
                    
                if  ui_controls.isdisplayed(get_obj_identifier(Alerts_top_txt))  :
                        print "alerts which are displaying=> " +str(selectble_alert_name.strip())
               
                else :
                        print "alerts which are not displaying " +str(selectble_alert_name.strip())
                 
                status = False if not (flag1) else True

               

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg



def verify_first_ome_device_devices(ntwrk_dvce=None,rac=None,servers=None):

    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                sleep(3)
                #flag1 = ui_controls.back_button()
                'click on device image'
                flag2 = ui_controls.button(get_obj_identifier('ome_dvce'))
                print "clicked on devices"
                sleep(3)
                'verify Alerts label'
                flag3 = element_textvalidation('all_dvce_labl','All Devices')
                'get all drop down option from demo mode menu button and get the desired page'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('Ome_devices'))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == ntwrk_dvce.strip() : 
                      
                        print " verified successfully==>"+str(ntwrk_dvce.strip())
                    if item.get_attribute('text').strip() == rac.strip() : 
                       
                        print "verified successfully==>"+str(rac.strip())
                    if item.get_attribute('text').strip() == servers.strip() : 
                        
                        print "verified successfully==>"+str(servers.strip())        
                        
               
                status = False if not (flag2 and flag3) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_all_ome_and_idrac__devices_txt(elment=None,first_ome=None,second_ome=None,first_idrc=None,
                                          second_idrc=None,third_idrc=None,fourth_idrc=None,fifth_idrc=None,
                                          six_idrc=None,sevnth_idrc=None):

    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                sleep(3)
               
                
                'get all drop down option from demo mode menu button and get the desired page'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier(elment))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == first_ome.strip() : 
                      
                        print " verified successfully==>"+str(first_ome.strip())
                    if item.get_attribute('text').strip() == second_ome.strip() : 
                       
                        print "verified successfully==>"+str(second_ome.strip())
                    if item.get_attribute('text').strip() == first_idrc.strip() : 
                        
                        print "verified successfully==>"+str(first_idrc.strip())  
                    if item.get_attribute('text').strip() == second_idrc.strip() : 
                      
                        print " verified successfully==>"+str(second_idrc.strip())
                    if item.get_attribute('text').strip() == third_idrc.strip() : 
                     
                        print "verified successfully==>"+str(third_idrc.strip())
                        
                    flag2=ui_controls.swipe_down()
                    sleep(6)     
                    if item.get_attribute('text').strip() == fourth_idrc.strip() : 
                        
                        print "verified successfully==>"+str(fourth_idrc.strip())   
                    if item.get_attribute('text').strip() == fifth_idrc.strip() : 
                      
                        print " verified successfully==>"+str(fifth_idrc.strip())
                    if item.get_attribute('text').strip() == six_idrc.strip() : 
                       
                        print "verified successfully==>"+str(six_idrc.strip())
                    if item.get_attribute('text').strip() == sevnth_idrc.strip() : 
                        
                        print "verified successfully==>"+str(sevnth_idrc.strip())   
                    
                    
                status = False if not (flag2) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg





def verify_first_ome_netwrk_devices_count():

    """
    This function is used to get all the text of demo mode first ome network devices

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

             
                'click on any one of idrac device to get idrac device home page'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('Ome_devices'))
                for item in main_menu_items:
                    if item.get_attribute('text').strip() == "Network Devices":
                        item.click()
                        print "clicked on network devices"
                        break

                dict=[]
                'get all network devices top element text and append to list class'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('ntwrk_dvce_top_txt'))
                if not main_menu_items:
                    print "Unable to retrieve text to verify  first ome device, top element text of network devices elements"

                'append the getting text in list'
                for item in main_menu_items:
                    txt = item.get_attribute('text')
                    dict.append(txt)
                'get the all network devices bottom text and append the list class'  
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('ntwrk_dvce_btom_txt'))
                if not main_menu_items:
                    print "Unable to retrive text to verify demomode first ome device ,bottom element text of network devices elements"

                'append the getting text to list class'
                for item in main_menu_items:
                    txt = item.get_attribute('text')
                    dict.append(txt)

                'create a new text file for demo mode idrac and ome devices ' 
                util.open_file(g.dynamic_first_ome_ntwrk_devices_txt)
                for txt in dict:
                    util.write_file(g.dynamic_first_ome_ntwrk_devices_txt, txt)

                'read the demo mode devices text file'
                actual_text = util.read_file(g.dynamic_first_ome_ntwrk_devices_txt) 
                'Read verification input data'
                text_to_verify = util.read_file(g.first_ome_ntwrk_devices_txt)
                if not text_to_verify:
                    print "Unable to retrieve text to verify first ome device network devices text file"
                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():

                    print " Demo mode first ome device  network devices text verified sucessfully"

                else:
                    print "Demo Mode first ome device  network devices text verified unsucessfully"    

                status = False if not () else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_first_ome_all_ntwrk_devices_homepage_txt(dynami_file=None,actual_file=None):

    """
    This function is used to get all the text of demo mode first ome network  device home page text

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
               
                'get the all network devices bottom text and append the list class'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('ntwrk_dvce_top_txt'))
                'click on first network device'
                count_inner = 0
                while count_inner < (len(main_menu_items)):
                    main_menu_items[count_inner].click()
                    print "verifying details of network device , network device number is ==>"+str(count_inner)
                   
                    dict1=[]
                    'get the text view of network device element '
                    ntwrk_dvce = ui_controls.text_view(get_obj_identifier('ntrwk_dvce_dvce_tag'))
                    dict1.append(ntwrk_dvce)
                    'get the text view of power state tag element '
                    pwr_state = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_pwr_state_tag'))
                    dict1.append(pwr_state)
                    'get the text view of service tag element '
                    servce_tag = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_srvce_tag'))
                    dict1.append(servce_tag)
                    'get the text view of device type element '
                    dvce_type = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_dvce_type_tag'))
                    dict1.append(dvce_type)
                    sleep(3)
                    'get the text view of device model element'
                    dvce_model = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_dvce_model_tag'))
                    dict1.append(dvce_model)
                    sleep(3) 
                    'get the text view of ip adress model '
                    ip_adres = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_ipAdres_tag'))
                    dict1.append(ip_adres)
                    'get the text view of power value element'
                    pwer_value = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_pwr_value'))
                    dict1.append(pwer_value)
                    'get the text view of service value element'
                    srvce_value = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_srvce_tag_value'))
                    dict1.append(srvce_value)
                    'get the text view of device model value element'
                    dvce_type_vlue = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_deviceType_value'))
                    dict1.append(dvce_type_vlue)
                    dvce_model_vlue = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_model_vle'))
                    dict1.append(dvce_model_vlue)
                    'get the text view of ip adress value elment'
                    ipAdres_value = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_ipAdres_value'))
                    dict1.append(ipAdres_value)
                    sleep(3) 
                    'get the text view of software details element'
                    softwre_dtls = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_software_dtls_elmnt'))
                    dict1.append(softwre_dtls)
                    'get the text view of alerts element'
                    alrts = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_alrts_elmnt'))
                    dict1.append(alrts)
                    'get the text view of warranty element'
                    warrnty = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_warrnty_elmnt'))
                    dict1.append(warrnty)
                    sleep(3)
                    'get the text view of online resources'
                    online_resource = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_online_resrce_element'))
                    dict1.append(online_resource)
                    'create a new text file for demo mode idrac and ome devices ' 
                    util.open_file(dynami_file)
                    for txt in dict1:
                        util.write_file(dynami_file,txt)  

                    actual_text = util.read_file(dynami_file)   
                    text_to_verify = util.read_file(actual_file)
                    if not text_to_verify:
                        print "Unable to retrieve text to verify first ome device  ntwrk devices page elements text "

                    'Comparing text retrieved from UI with verification input text'
                    if text_to_verify.strip() == actual_text.strip():
                        print  "successfully verified text of network device, network device number is  ==>"+str(count_inner)

                    else:
                        print "unsuccessfully verified text of network device, network device number is  ==>"+str(count_inner)

                    'go back'
                    flag1 = ui_controls.back_button()
                    sleep(3) 
                    
                    count_inner += 1
                flag2 = ui_controls.back_button()
                'go back'
                sleep(3)
                    

                status = False if not (flag1 and flag2) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_first_ome_rac_devices_count():

    """
    This function is used to get all the text of demo mode first ome RAC devices

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                'click on network devices element'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('Ome_devices') )
                main_menu_items[1].click()
                dict=[]    
                'get all network devices top element text and append to list class'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('ntwrk_dvce_top_txt'))
                if not main_menu_items:
                    print "Unable to retrieve text to verify  first ome device, top element text of network devices elements"

                'append the getting text in list'
                for item in main_menu_items:
                    txt = item.get_attribute('text')
                    dict.append(txt)
                'get the all network devices bottom text and append the list class'  
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('ntwrk_dvce_btom_txt'))
                if not main_menu_items:
                    print "Unable to retrive text to verify demomode first ome device ,bottom element text of network devices elements"

                'append the getting text to list class'
                for item in main_menu_items:
                    txt = item.get_attribute('text')
                    dict.append(txt)

                'create a new text file for demo mode idrac and ome devices ' 
                util.open_file(g.dynamic_first_RAC_ntwrk_devices_txt)
                for txt in dict:
                    util.write_file(g.dynamic_first_RAC_ntwrk_devices_txt, txt)

                'read the demo mode devices text file'
                actual_text = util.read_file(g.dynamic_first_RAC_ntwrk_devices_txt)  
                'Read verification input data'
                text_to_verify = util.read_file((g.first_ome_RAC_devices_txt))
                if not text_to_verify:
                    print "Unable to retrive text to verify first ome device network devices text file"

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():

                    print " demo mode first ome device  RAC devices text verified successfully"

                else:
                    print "Demo Mode first ome device  RAC devices text verified unsuccessfully" 

                status = False if not () else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_first_ome_all_rac_devices_homepage_txt(dymanic_file=None,actual_file=None):

    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                'get the all network devices bottom text and append the list class'  
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('ntwrk_dvce_top_txt'))
                'click on first rac device'
                count_inner = 0
                while count_inner < (len(main_menu_items)):
                    main_menu_items[count_inner].click()
                    print "verifying details of RAC device , rac device number is ==>"+str(count_inner)
                    dict2 = []
                    'get the text view rac device element'
                    rac_dvce = ui_controls.text_view(get_obj_identifier('rac_device_dvce_elment'))
                    dict2.append(rac_dvce)
                    'get the text view of power state element'
                    pwr_state = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_pwr_state_tag'))
                    dict2.append(pwr_state)
                    'get the text view of service tag element'
                    servce_tag = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_srvce_tag'))
                    dict2.append(servce_tag)
                    'get the text view of device type element'
                    dvce_type = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_dvce_type_tag'))
                    dict2.append(dvce_type)
                    'get the text view of device model element'
                    dvce_model = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_dvce_model_tag'))
                    dict2.append(dvce_model)
                    'get the text view of ip adress element'
                    ip_adres = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_ipAdres_tag'))
                    dict2.append(ip_adres)
                    'get the text view of power value element'
                    pwer_value = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_pwr_value'))
                    dict2.append(pwer_value)
                    'get the text view of service value element'
                    srvce_value = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_srvce_tag_value'))
                    dict2.append(srvce_value)
                    'get the text view of device model element'
                    dvce_model = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_deviceType_value'))
                    dict2.append(dvce_model)
                    'get the text view of ip adress value element'
                    ipAdres_value = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_ipAdres_value'))
                    dict2.append(ipAdres_value)
                    'get the text view of software details element'
                    softwre_dtls = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_software_dtls_elmnt'))
                    dict2.append(softwre_dtls)
                    'get the text view of alerts element'
                    alrts = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_alrts_elmnt'))
                    dict2.append(alrts)
                    'get the text view of warranty element'
                    warrnty = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_warrnty_elmnt'))
                    dict2.append(warrnty)
                    'get the text view of online resources element'
                    online_resource = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_online_resrce_element'))
                    dict2.append(online_resource)
                    'create a new text file for demo mode idrac and ome devices ' 
                    util.open_file(dymanic_file)
                    for txt in dict2:
                        util.write_file(dymanic_file,txt)  

                    actual_text = util.read_file(dymanic_file)   
                    text_to_verify = util.read_file(actual_file)
                    if not text_to_verify:
                        print "Unable to retrieve text to verify first ome device  network devices page elements text "
                    'Comparing text retrieved from UI with verification input text'
                    if text_to_verify.strip() == actual_text.strip():
                        print "successfully verified text of RAC device, rac device number is  ==>"+str(count_inner)
                    else:
                        print "unsuccessfully verified text of RAC device, rac device number is  ==>"+str(count_inner)
                    'go back'
                    flag1 = ui_controls.back_button()
                    sleep(3)
                    'go back'
                    sleep(3)
                    count_inner += 1
                flag2 = ui_controls.back_button()

                status = False if not (flag1 and flag2) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_first_ome_servers_devices_count():

    """
    This function is used to get all the text of demo mode first ome servers devices

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                'click on servers device element'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('Ome_devices'))
                main_menu_items[2].click()
                dict=[]
                'get all network devices top element text and append to list class'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('ntwrk_dvce_top_txt'))
                if not main_menu_items:
                    print "Unable to retrieve text to verify  first ome device, top element text of network devices elements"
                'append the getting text in list'
                for item in main_menu_items:
                    txt = item.get_attribute('text')
                    dict.append(txt)
                'get the all network devices bottom text and append the list class'  
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('ntwrk_dvce_btom_txt'))
                if not main_menu_items:
                    print "Unable to retrive text to verify demomode first ome device ,bottom element text of network devices elements"

                'append the getting text to list class'
                for item in main_menu_items:
                    txt = item.get_attribute('text')
                    dict.append(txt)

                'create a new text file for demo mode idrac and ome devices ' 
                util.open_file(g.dynamic_first_ome_servers_devices_txt)
                for txt in dict:
                    util.write_file(g.dynamic_first_ome_servers_devices_txt, txt)

                'read the demo mode devices text file'
                actual_text = util.read_file(g.dynamic_first_ome_servers_devices_txt) 
                'Read verification input data'
                text_to_verify = util.read_file((g.first_ome_servers_devices_txt))
                if not text_to_verify:
                    print "Unable to retrieve text to verify first ome device network devices text file"

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():

                    print " Demo mode first ome device  servers devices text verified sucessfully"

                else:
                    print "Demo Mode first ome device  servers devices text verified unsucessfully"    

                status = False if not () else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_first_ome_all_servers_devices_homepage_txt(dynamic_file=None,actual_file=None):

    """
    This function is used to get all the text of demo mode first ome servers home page text

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                'get the all network devices bottom text and append the list class'  
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('ntwrk_dvce_top_txt'))
                'click on first servers device element'
                count_inner = 0
                while count_inner < (len(main_menu_items)-1):
                    main_menu_items[count_inner].click()
                    print "verifying details of servers device , servers device number is ==>"+str(count_inner)
                    dict3=[]
                    'get the text view of server device tag element'
                    server_dvce = ui_controls.text_view(get_obj_identifier('servr_device_dvce_elment'))
                    dict3.append(server_dvce)
                    'get the text view of power state tag element'
                    pwr_state = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_pwr_state_tag'))
                    dict3.append(pwr_state)
                    'get the text view of service tag element'
                    servce_tag = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_srvce_tag'))
                    dict3.append(servce_tag)
                    sleep(3)
                    'get the text view of device type element'
                    dvce_type = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_dvce_type_tag'))
                    dict3.append(dvce_type)
                    'get the text view of device model element'
                    dvce_model = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_dvce_model_tag'))
                    dict3.append(dvce_model)
                    'get the text view of device model value element'
                    dvce_model_value = ui_controls.text_view(get_obj_identifier('rac_dvce_model_value_tag'))
                    dict3.append(dvce_model_value)
                    sleep(3)
                    'get the text view of cpu tag element'
                    cpu_tag = ui_controls.text_view(get_obj_identifier('rac_device_cpu_tag'))
                    dict3.append(cpu_tag)
                    'get the text view of cpu value tag element'
                    cpu_vlue_tag = ui_controls.text_view(get_obj_identifier('rac_cpu_value_tag'))
                    dict3.append(cpu_vlue_tag)
                    'get the text view of memory tag elment'
                    memory_tag = ui_controls.text_view(get_obj_identifier('rac_device_memry_tag'))
                    dict3.append(memory_tag)
                    'get the text view of memory value element'
                    memry_vlue_tag = ui_controls.text_view(get_obj_identifier('rac_memry_value_tag'))
                    dict3.append(memry_vlue_tag)
                    'get the text view of os tag element'
                    os_tag = ui_controls.text_view(get_obj_identifier('rac_device_os_tag'))
                    dict3.append(os_tag)
                    sleep(3)
                    'get the text view of os value tag element'
                    os_vlue_tag = ui_controls.text_view(get_obj_identifier('rac_os_value_tag'))
                    dict3.append(os_vlue_tag)
                    'get the text view ip address tag element'
                    ip_adres = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_ipAdres_tag'))
                    dict3.append(ip_adres)
                    'get the text view of ip address value element'
                    ip_adres_value = ui_controls.text_view(get_obj_identifier('rac_ipadres_value_tag'))
                    dict3.append(ip_adres_value)
                    
                    'swipe down to till last element'
                    flag2 = ui_controls.swipe_down()
                    sleep(3)
                    'get the text view power value element'
                    pwer_value = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_pwr_value'))
                    dict3.append(pwer_value)
                    'get the text view of service value element'
                    srvce_value = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_srvce_tag_value'))
                    dict3.append(srvce_value)
                    'get the text view of device model element'
                    dvce_model = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_deviceType_value'))
                    dict3.append(dvce_model)
                    'get the text view of software details element'
                    softwre_dtls = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_software_dtls_elmnt'))
                    dict3.append(softwre_dtls)
                    'get the text view of alerts element'
                    alrts = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_alrts_elmnt'))
                    dict3.append(alrts)
                    sleep(3)
                    'get the text view of warranty element'
                    warrnty = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_warrnty_elmnt'))
                    dict3.append(warrnty)
                    'get the text view of online resources elment'
                    online_resource = ui_controls.text_view(get_obj_identifier('ntwrk_dvce_online_resrce_element'))
                    dict3.append(online_resource)
                    'create a new text file for demo mode idrac and ome devices ' 
                    util.open_file(dynamic_file)
                    for txt in dict3:
                        util.write_file(dynamic_file,txt)  
                    'read the text input file'
                    actual_text = util.read_file(dynamic_file)   
                    text_to_verify = util.read_file(actual_file)
                    if not text_to_verify:
                        print "Unable to retrieve text to verify  network devices  text "
                    'Comparing text retrieved from UI with verification input text'
                    if text_to_verify.strip() == actual_text.strip():   
                        print "successfully verified text of Servers device, server device number is  ==>"+str(count_inner)

                    else:
                        print "unsuccessfully verified text of Servers device, server device device number is  ==>"+str(count_inner)

                    'go back'
                    flag3 = ui_controls.back_button()
                    sleep(3)
                    'go back'
                    sleep(3)
                    count_inner += 1
                flag4 = ui_controls.back_button()
                'click on menu'
                flag5 = ui_controls.Click(get_obj_identifier('test_demomode_menu')) 
                sleep(3)
                'click on home option'
                flag6 = ui_controls.Click(get_obj_identifier('DemoMode_Home_option'))
                sleep(3)

                status = False if not (flag2 and flag3 and flag4 and flag5 and flag6) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def verify_sixth_idrac_home_page_text():
    """
    This function is used to get all the text of demo mode devices

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                
                flag1=duplicate_verify_sixth_idrac_home_page_text(clikble_idrc_name='192.168.0.110',Hostname_Tag='idrac_Hostname_Tag',quick_sync='idrac_quick_sync',quk_sync_vle='idrac_quk_sync_vle',
                                                          dynamic_file=g.dynamic_sixth_idracdvce_homepage_txt,actual_file=g.sixth_idrac_device_hmepage_txt)


                status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg
def verify_seventh_idrac_home_page_text():
    """
    This function is used to get all the text of demo mode devices

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                flag1=duplicate_verify_sevnth_idrac_home_page_text(clikble_idrc_name='10.11.50.1',
                                                                  hrdware_invntry_elmnt='hrdwre_invntry_elmnt',location_detals_elmnt='location_details_elmnt',
                                                                  dynamic_file=g.dynamic_sevnth_idracdvce_hmepage_txt,actual_file=g.sevnth_idrac_device_hmepage_txt)


                status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def duplicate_verify_first_idrac_home_page_text(powr_state_tag='Idrac_powerState',idrac_devices='demomode_device_top_text',clikble_idrc_name=None,
                                                                  powr_state_vlue='idrac_powerstatus_vlue',srvice_tag='idrac_servce_tag',
                                                                  dvceModel_Tag='idrac_dvceModel_Tag',Memory_tag='idrac_Memory_tag',os_Tag='idrac_os_Tag',
                                                                  Hostname_Tag='idrac_Hostname_Tag',ip_adres_Tag='idrac_ip_adres_Tag',pwr_state_value='idrac_pwr_stte_value',mdel_value='model_vlue',
                                                                  memory_value='idrac_memory_value',os_value='idrac_os_value',host_value='idrac_host_value',
                                                                  ipadres_value='idrac_ipadres_value',hrdwre_logs_elmnt='hardwre_logs_elmnt',
                                                                  frmware_elmnt='firmware_elmnt',ntwork_details='ntwrk_details',hrdware_invntry_elmnt='hrdwre_invntry_elmnt',
                                                                  hlth_stus_elemnt='hlth_status_elemnt',waranty_info_elmnt='warnty_info_elmnt',location_detals_elmnt='location_details_elmnt',
                                                                  online_resource_elmnt='online_resource_elmnt',dynamic_file=None,actual_file=None):
                                            
    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                sleep(2)
                main_menu_items = ui_controls.ui_elements(get_obj_identifier(idrac_devices))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == clikble_idrc_name.strip() : 
                        item.click()  
                        print "clicked on ome device , ome  name is==>"+str(clikble_idrc_name.strip())
                        break

                
                dict = []

              
                'get the text view of ome device home tag'
                home_txt = ui_controls.text_view(get_obj_identifier(powr_state_tag))
                dict.append(home_txt)
                'get the text of critical element from devices'
                critical_txt = ui_controls.text_view(get_obj_identifier(powr_state_vlue))
                dict.append(critical_txt)
                'get the text view of warning element from devices'
                warning_txt = ui_controls.text_view(get_obj_identifier(srvice_tag))
                dict.append(warning_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(ipadres_value))
                dict.append(hlthy_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(dvceModel_Tag))
                dict.append(hlthy_txt)
                sleep(3)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(Memory_tag))
                dict.append(hlthy_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(ipadres_value))
                dict.append(hlthy_txt)
                'get the text view of unknown element from devices'
                unkwn_txt = ui_controls.text_view(get_obj_identifier(os_Tag))
                dict.append(unkwn_txt)
                'get the text view of ome devices count'
                ome_dvce_count = ui_controls.text_view(get_obj_identifier(Hostname_Tag))
                dict.append(ome_dvce_count)
                'get the text view of devices from devices'
                devices_txt = ui_controls.text_view(get_obj_identifier(ip_adres_Tag))
                dict.append(devices_txt)
                
                'swipe down '
                flag1 = ui_controls.swipe_down()
                sleep(3)
                
                'get the text view of alerts element from alerts'
                alerts_txt = ui_controls.text_view(get_obj_identifier(memory_value))
                dict.append(alerts_txt)
                'get the text view of critical element from alerts'
                alrt_criticl_txt = ui_controls.text_view(get_obj_identifier(os_value))
                dict.append(alrt_criticl_txt)
                'get the text view of warning element from alerts'
                alrt_warn_txt = ui_controls.text_view(get_obj_identifier(host_value))
                dict.append(alrt_warn_txt)
                sleep(3)
                'get the text view of healthy element from alerts'
                alrt_hlthy_txt = ui_controls.text_view(get_obj_identifier(ipadres_value))
                dict.append(alrt_hlthy_txt)
                
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(hrdwre_logs_elmnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(frmware_elmnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(ntwork_details))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(hrdware_invntry_elmnt))
                dict.append(alrt_unkwn_txt)
                sleep(3)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_elemnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(waranty_info_elmnt))
                dict.append(alrt_unkwn_txt)
                sleep(3)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(location_detals_elmnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(online_resource_elmnt))
                dict.append(alrt_unkwn_txt)
                
                sleep(3)
                'create a new text file for demo mode idrac and ome devices ' 
              
                util.open_file(dynamic_file)
                'write a text file'
                for txt in dict:
                  
                    util.write_file(dynamic_file,txt)
                    print txt
                'read the demo mode devices text file'
                actual_text = util.read_file(dynamic_file)

                text_to_verify = util.read_file(actual_file)
                if not text_to_verify:
                        print "Unable to retrieve text to verify first ome device home page elements text "

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():   
                        print " idrac device  home page  text verified successfully, idrac device is ==>"+str(clikble_idrc_name.strip())

                else:
                        print "idrac device device home page text verified unsuccessfully, idrac device is==>"+str(clikble_idrc_name.strip())
                sleep(3)        

                status = False if not (flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


def duplicate_verify_sixth_idrac_home_page_text(powr_state_tag='Idrac_powerState',idrac_devices='demomode_device_top_text',clikble_idrc_name=None,
                                                                  powr_state_vlue='idrac_powerstatus_vlue',srvice_tag='idrac_servce_tag',
                                                                  dvceModel_Tag='idrac_dvceModel_Tag',Memory_tag='idrac_Memory_tag',os_Tag='idrac_os_Tag',
                                                                  Hostname_Tag=None,ip_adres_Tag='idrac_ip_adres_Tag',pwr_state_value='idrac_pwr_stte_value',mdel_value='model_vlue',
                                                                  memory_value='idrac_memory_value',os_value='idrac_os_value',host_value='idrac_host_value',
                                                                  ipadres_value='idrac_ipadres_value',quick_sync=None,quk_sync_vle=None,hrdwre_logs_elmnt='hardwre_logs_elmnt',
                                                                  frmware_elmnt='firmware_elmnt',ntwork_details='ntwrk_details',
                                                                  hlth_stus_elemnt='hlth_status_elemnt',waranty_info_elmnt='warnty_info_elmnt',
                                                                  online_resource_elmnt='online_resource_elmnt',dynamic_file=None,actual_file=None):

                                                             
    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                  
                sleep(3)
                flag0=ui_controls.swipe_down()
                sleep(2)
                main_menu_items = ui_controls.ui_elements(get_obj_identifier(idrac_devices))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == clikble_idrc_name.strip() : 
                        item.click()  
                        print "clicked on ome device , ome  name is==>"+str(clikble_idrc_name.strip())
                        break

               
                dict = []
                
               
                'get the text view of ome device home tag'
                home_txt = ui_controls.text_view(get_obj_identifier(powr_state_tag))
                dict.append(home_txt)
                'get the text of critical element from devices'
                critical_txt = ui_controls.text_view(get_obj_identifier(powr_state_vlue))
                dict.append(critical_txt)
                'get the text view of warning element from devices'
                warning_txt = ui_controls.text_view(get_obj_identifier(srvice_tag))
                dict.append(warning_txt)
                sleep(3)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(ipadres_value))
                dict.append(hlthy_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(dvceModel_Tag))
                dict.append(hlthy_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(Memory_tag))
                dict.append(hlthy_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(ipadres_value))
                dict.append(hlthy_txt)
                sleep(3)
                'get the text view of unknown element from devices'
                unkwn_txt = ui_controls.text_view(get_obj_identifier(os_Tag))
                dict.append(unkwn_txt)
                'get the text view of ome devices count'
                ome_dvce_count = ui_controls.text_view(get_obj_identifier(Hostname_Tag))
                dict.append(ome_dvce_count)
                'get the text view of devices from devices'
                devices_txt = ui_controls.text_view(get_obj_identifier(ip_adres_Tag))
                dict.append(devices_txt)
                'change to native context before going to swipe'
                #flag1 = ui_controls.switch_to_context()
                'swipe down '
                flag1 = ui_controls.swipe_down()
                sleep(3)
                'get the text view of alert count element from alerts'
                #ome_alrt_count = ui_controls.text_view(get_obj_identifier(pwr_state_value))
                #dict.append(ome_alrt_count)
                'get the text view of alert count element from alerts'
                #ome_alrt_count = ui_controls.text_view(get_obj_identifier(model_value))
                #dict.append(ome_alrt_count)
                'get the text view of alerts element from alerts'
                alerts_txt = ui_controls.text_view(get_obj_identifier(memory_value))
                dict.append(alerts_txt)
                'get the text view of critical element from alerts'
                alrt_criticl_txt = ui_controls.text_view(get_obj_identifier(os_value))
                dict.append(alrt_criticl_txt)
                'get the text view of warning element from alerts'
                alrt_warn_txt = ui_controls.text_view(get_obj_identifier(host_value))
                dict.append(alrt_warn_txt)
                sleep(3)
                'get the text view of healthy element from alerts'
                alrt_hlthy_txt = ui_controls.text_view(get_obj_identifier(ipadres_value))
                dict.append(alrt_hlthy_txt)
                
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(hrdwre_logs_elmnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(frmware_elmnt))
                dict.append(alrt_unkwn_txt)
                sleep(3)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(ntwork_details))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                #alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(hrdware_invntry_elmnt))
                #dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_elemnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(waranty_info_elmnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                #alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(location_detals_elmnt))
                #dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(online_resource_elmnt))
                dict.append(alrt_unkwn_txt)
                sleep(3)
                'get the text view of unknown element from alerts'
                quck_sync = ui_controls.text_view(get_obj_identifier(quick_sync))
                dict.append(quck_sync)
                'get the text view of unknown element from alerts'
                quick_sync_vle = ui_controls.text_view(get_obj_identifier(quk_sync_vle))
                dict.append(quick_sync_vle)
               
                sleep(3)
              
              
                util.open_file(dynamic_file)
                'write a text file'
                for txt in dict:
                 
                    util.write_file(dynamic_file,txt)
                    print txt
                'read the demo mode devices text file'
                actual_text = util.read_file(dynamic_file)

                text_to_verify = util.read_file(actual_file)
                if not text_to_verify:
                        print "Unable to retrieve text to verify first ome device home page elements text "

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():   
                        print " idrac device  home page  text verified successfully, idrac device is ==>"+str(clikble_idrc_name.strip())

                else:
                        print "idrac device device home page text verified unsuccessfully, idrac device is==>"+str(clikble_idrc_name.strip())
                sleep(3)        

                status = False if not (flag0 and flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg
def duplicate_verify_sevnth_idrac_home_page_text(powr_state_tag='Idrac_powerState',idrac_devices='demomode_device_top_text',clikble_idrc_name=None,
                                                                  powr_state_vlue='idrac_powerstatus_vlue',srvice_tag='idrac_servce_tag',
                                                                  dvceModel_Tag='idrac_dvceModel_Tag',Memory_tag='idrac_Memory_tag',os_Tag='idrac_os_Tag',
                                                                  ip_adres_Tag='idrac_ip_adres_Tag',pwr_state_value='idrac_pwr_stte_value',mdel_value='model_vlue',
                                                                  memory_value='idrac_memory_value',os_value='idrac_os_value',
                                                                  ipadres_value='idrac_ipadres_value',hrdwre_logs_elmnt='hardwre_logs_elmnt',
                                                                  frmware_elmnt='firmware_elmnt',ntwork_details='ntwrk_details',hrdware_invntry_elmnt=None,
                                                                  hlth_stus_elemnt='hlth_status_elemnt',waranty_info_elmnt='warnty_info_elmnt',location_detals_elmnt=None,
                                                                  online_resource_elmnt='online_resource_elmnt',dynamic_file=None,actual_file=None):

                                                            
    """
    This function is used to get all the text of demo mode first ome  device

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                  
                sleep(3)
                flag0=ui_controls.swipe_down()
                sleep(1)
                main_menu_items = ui_controls.ui_elements(get_obj_identifier(idrac_devices))
                for item in main_menu_items:

                    if item.get_attribute('text').strip() == clikble_idrc_name.strip() : 
                        item.click()  
                        print "clicked on ome device , ome  name is==>"+str(clikble_idrc_name.strip())
                        break

                dict = []
               
                'get the text view of ome device home tag'
                home_txt = ui_controls.text_view(get_obj_identifier(powr_state_tag))
                dict.append(home_txt)
                'get the text of critical element from devices'
                critical_txt = ui_controls.text_view(get_obj_identifier(powr_state_vlue))
                dict.append(critical_txt)
                'get the text view of warning element from devices'
                warning_txt = ui_controls.text_view(get_obj_identifier(srvice_tag))
                dict.append(warning_txt)
                sleep(3)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(ipadres_value))
                dict.append(hlthy_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(dvceModel_Tag))
                dict.append(hlthy_txt)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(Memory_tag))
                dict.append(hlthy_txt)
                sleep(3)
                'get the text view of healthy element from devices'
                hlthy_txt = ui_controls.text_view(get_obj_identifier(ipadres_value))
                dict.append(hlthy_txt)
                'get the text view of unknown element from devices'
                unkwn_txt = ui_controls.text_view(get_obj_identifier(os_Tag))
                dict.append(unkwn_txt)
                'get the text view of ome devices count'
                sleep(3)
                'get the text view of devices from devices'
                devices_txt = ui_controls.text_view(get_obj_identifier(ip_adres_Tag))
                dict.append(devices_txt)
               
                'swipe down '
                flag1 = ui_controls.swipe_down()
                sleep(3)
               
                'get the text view of alerts element from alerts'
                alerts_txt = ui_controls.text_view(get_obj_identifier(memory_value))
                dict.append(alerts_txt)
                'get the text view of critical element from alerts'
                alrt_criticl_txt = ui_controls.text_view(get_obj_identifier(os_value))
                dict.append(alrt_criticl_txt)
                
                'get the text view of healthy element from alerts'
                alrt_hlthy_txt = ui_controls.text_view(get_obj_identifier(ipadres_value))
                dict.append(alrt_hlthy_txt)
                
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(hrdwre_logs_elmnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(frmware_elmnt))
                dict.append(alrt_unkwn_txt)
                sleep(3)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(ntwork_details))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(hrdware_invntry_elmnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(hlth_stus_elemnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(waranty_info_elmnt))
                dict.append(alrt_unkwn_txt)
                sleep(3)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(location_detals_elmnt))
                dict.append(alrt_unkwn_txt)
                'get the text view of unknown element from alerts'
                alrt_unkwn_txt = ui_controls.text_view(get_obj_identifier(online_resource_elmnt))
                dict.append(alrt_unkwn_txt)
                sleep(3) 
                util.open_file(dynamic_file)
                'write a text file'
                for txt in dict:
                   
                    util.write_file(dynamic_file,txt)
                    print txt
                'read the demo mode devices text file'
                actual_text = util.read_file(dynamic_file)

                text_to_verify = util.read_file(actual_file)
                if not text_to_verify:
                        print "Unable to retrieve text to verify first ome device home page elements text "

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():   
                        print " idrac device  home page  text verified successfully, idrac device is ==>"+str(clikble_idrc_name.strip())

                else:
                        print "idrac device device home page text verified unsuccessfully, idrac device is==>"+str(clikble_idrc_name.strip())
                sleep(3)        

                status = False if not (flag0 and flag1) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg




def dduplicate_verify_first_idrac_home_page_text():
    """
    This function is used to get all the text of demo mode devices

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                sleep(2)
                flag1 = ui_controls.swipe_Down()
                'click on elements in first idrac device '
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('demomode_device_top_text') )
                main_menu_items[-6].click()
                dict=[]
                'get the text view of ome device tag'
                idrac_device = ui_controls.ui_elements(get_obj_identifier('idrac_device_tag') )
                print idrac_device[-1].get_attribute("text")
                dict.append(idrac_device[-1].get_attribute("text"))
             
                'get the text view of power state tag '
                pwr_state_tag = ui_controls.text_view(get_obj_identifier('Idrac_powerState'))
                dict.append(pwr_state_tag)
                'get the text view of service tag'
                srvce_tag = ui_controls.text_view(get_obj_identifier('idrac_servce_tag'))
                dict.append(srvce_tag)
                'get the text view of device model tag'
                dvce_model_tag = ui_controls.text_view(get_obj_identifier('idrac_dvceModel_Tag'))
                dict.append(dvce_model_tag)
                'get the text view of memory tag'
                memry_tag = ui_controls.text_view(get_obj_identifier('idrac_Memory_tag'))
                dict.append(memry_tag)
                'get the text view of os tag'
                os_tag = ui_controls.text_view(get_obj_identifier('idrac_os_Tag'))
                dict.append(os_tag)
                'get the text view of host name tag'
                hst_name_tag = ui_controls.text_view(get_obj_identifier('idrac_Hostname_Tag'))
                dict.append(hst_name_tag)
                'get the text view of ip adress tag'
                ipadres_tag = ui_controls.text_view(get_obj_identifier('idrac_ip_adres_Tag'))
                dict.append(ipadres_tag)
                'get the text view of power state value'
                pwr_state_vlue = ui_controls.text_view(get_obj_identifier('idrac_pwr_stte_value'))
                dict.append(pwr_state_vlue)
                
                'switch to native context'
                flag2 = ui_controls.switch_to_context()
                'swipe down to till last element'
                flag3 = ui_controls.swipe_down()
                sleep(3)
                'get the text view of device model value'
                dvce_model_vlue = ui_controls.text_view(get_obj_identifier('model_vlue'))
                dict.append(dvce_model_vlue)
                'get the text view of cpu value tag'
                'get the text view of memory value'
                memry_vlue = ui_controls.text_view(get_obj_identifier('idrac_memory_value'))
                dict.append(memry_vlue)
                'get the text view of os value'
                os_vlue = ui_controls.text_view(get_obj_identifier('idrac_os_value'))
                dict.append(os_vlue)
                'get the text view of host name value'
                hstname_vlue = ui_controls.text_view(get_obj_identifier('idrac_host_value'))
                dict.append(hstname_vlue)
                'get the text view of ip adress value'
                ipadres_vlue = ui_controls.text_view(get_obj_identifier('idrac_ipadres_value'))
                dict.append(ipadres_vlue)
                'get the text view of elements'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('DemoMode_devices_textview') )
                for txt in main_menu_items[-9:-1]:
                    teext = txt.get_attribute("text") 
                    dict.append(teext)
                'create a new text file for demo mode first idrac  device home page text ' 
                util.open_file(g.dynamic_first_idrac_device_homePage_txt)
                'write a text file'
                for txt in dict:
                    util.write_file(g.dynamic_first_idrac_device_homePage_txt, txt)
                'read the dynamic demo mode first idrac device home page text file'
                actual_text = util.read_file(g.dynamic_first_idrac_device_homePage_txt)
                'read first idrac device home page input text file' 
                text_to_verify = util.read_file(g.first_idrac_device_homePage_txt)
                if not text_to_verify:
                        print "Unable to retrieve text to verify first idrac device home page input text file "
                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():   
                        print " demo mode idrac device home page text verified successfully"

                else:
                        print "demo mode  idrac device home page text verified unsuccessfully"

                status = False if not (flag1 and flag2 and flag3) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg





def verify_first_idrac_dvce_hardwre_logs():

    """
    This function is used to get all the text of demo mode devices

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                'click on hardware logs element'
                flag1 = ui_controls.Click(get_obj_identifier('idrac_hardwre_logs_elmnt'))
                sleep(3)
                flag2 = ui_controls.Click(get_obj_identifier('SystmEvntLog_spiner_view'))
                sleep(3)
                flag3 = ui_controls.Click(get_obj_identifier('system_evnt_log'))
                sleep(3)
                flag4 = ui_controls.Click(get_obj_identifier('SystmEvntLog_spiner_view'))
                sleep(3)
                flag5 = ui_controls.Click(get_obj_identifier('lificycle_log'))
                sleep(3)
                'validate wether spinner view all alerts text displaying ro not'
                if ui_controls.isDisplayed(get_obj_identifier('SystmEvntLog_spiner_view')):
                    print 'System event log spinner view is displaying'
                else:
                    print 'System event log spinner view is not displaying'
                ''
                if ui_controls.isDisplayed(get_obj_identifier('Hrdware_log_alrts_element')):
                    print 'hardware log alerts is displaying properly'
                else:
                    print 'hardware log alerts is not displaying properly'
                'go back'
                flag3 = ui_controls.back_button()
                sleep(3)

                status = False if not (flag1 and flag2 and flag3 and flag4 and flag5) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg








def verify_first_idrac_helath_status_element():

    """
    This function is used to verify the first idrac device health status element

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':

                sleep(3)
                'click on health status element'
                flag1 = ui_controls.Click(get_obj_identifier('idrac_health_stus_elmnt'))
                sleep(3)
                'create a new text file for demo mode first idrac  device network details element text ' 
                util.open_file(g.dynamic_first_idrac_dvce_hlth_status_txt)

                'get the the text view of all health status element'
                main_menu_items = ui_controls.ui_elements(get_obj_identifier('DemoMode_devices_textview') )
                for txt in main_menu_items[-15:-1]:
                    util.write_file(g.dynamic_first_idrac_dvce_hlth_status_txt, txt.get_attribute("text"))
                'read the dynamic demo mode first idrac device network details text file'
                actual_text = util.read_file(g.dynamic_first_idrac_dvce_hlth_status_txt)
                'Read verification input data'
                text_to_verify = util.read_file(g.first_idrac_dvce_hlth_status_txt)
                if not text_to_verify:
                    print "Unable to retrive text of first idrac device health status of input text file"

                'Comparing text retrieved from UI with verification input text'
                if text_to_verify.strip() == actual_text.strip():
                    print " demo mode first idrac device health status text verified successfully"
                else:
                    print " demo mode first idrac device health status text verified unsuccessfully"
                'go back'
                flag2 = ui_controls.back_button()
                sleep(3)

                status = False if not (flag1 and flag2) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg








def verify_first_idrac_dvce_online_resoruces():

    """
    This function is used to verify the first idrac device health status element

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                sleep(3)
                'click on online resource element'
                flag1 = ui_controls.Click(get_obj_identifier('idrac_online_resrce_elemnt'))
                sleep(3)
                if ui_controls.isDisplayed(get_obj_identifier('Ok_bttn')):
                    flag2 = ui_controls.Click(get_obj_identifier('Ok_bttn'))
                if ui_controls.isDisplayed(get_obj_identifier('Add_btn')):
                    flag3 = ui_controls.Click(get_obj_identifier('Add_btn')) 
                sleep(3)
                'go back'
                flag4 = ui_controls.back_button()
                # flag16 = ui_controls.Click(get_obj_identifier('idrac_ntwrk_detals_elmnt'))
                sleep(6)
                # flag17 = ui_controls.back_button()
                'click on menu' 
                flag5 = ui_controls.Click(get_obj_identifier('test_demomode_menu')) 
                sleep(3) 
                'click on home option'
                flag6 = ui_controls.Click(get_obj_identifier('DemoMode_Home_option'))   
                sleep(3)

                status = False if not (flag1 and flag2 and flag2 and flag3 and flag4 and flag5 and flag6) else True

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


def verify_sixth_idrac_dvce_online_resoruces():

    """
    This function is used to verify the sixth idrac device online resources
    element

    Function Owner : nagarjuna

    Date created : 20/04/2016

    @return flag : (bool)status of execution.if successful True else False
    @return msg: (string) exception string in case of any error
    """
    msg, status = "", True
    try:
        if g.platform == 'android':
                sleep(5)
                'click on online resource element'
                flag1 = ui_controls.Click(get_obj_identifier('idrac_online_resrce_elemnt'))
                sleep(3)
                if ui_controls.isDisplayed(get_obj_identifier('Ok_bttn')):
                    flag2 = ui_controls.Click(get_obj_identifier('Ok_bttn'))
                if ui_controls.isDisplayed(get_obj_identifier('Add_btn')):
                    flag3 = ui_controls.Click(get_obj_identifier('Add_btn')) 
                sleep(3)
                'go back'
                flag2 = ui_controls.back_button()
                # flag16=ui_controls.Click(get_obj_identifier('idrac_ntwrk_detals_elmnt'))
                sleep(6)
                # flag17=ui_controls.back_button()
                'click on menu' 
                flag3 = ui_controls.Click(get_obj_identifier('test_demomode_menu')) 
                sleep(3)
                'click on home option'
                flag4 = ui_controls.Click(get_obj_identifier('DemoMode_Home_option'))
                sleep(3)

                status = False if not (flag1 and flag2 and
                                       flag2 and flag3 and flag4) else True

    except Exception as excp:
            traceback.print_exc()
            msg += str(excp)
            status = False
    return status, msg


