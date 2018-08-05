"""
Owner : Nithya_V

Date created : 28/4/2016

Description:
    Various parameters which needs to be used in common across different
    common modules

"""
import os
import unicodedata

from libs.product.omm.standard import util

'#######################################'
'current directory'
'#######################################'

current_dir = os.getcwd()

'#######################################'
'Wait dictionary'
'#######################################'

# wait dictionary for using standard wait times across framework
waitDictionary = {'s': 3, 's+': 5, 'm': 10, 'm+': 20, 'l': 30, 'xl': 60, 'xxl': 300}

'#############################################################'
'global variables for which data will be assigned on run time'
'#############################################################'

'appium driver object. Value will be assigned on appium server start'
driver = None

'Object repository dictionary. Values will be loaded on first test case execution'
object_repository = {}

'Test case verification dictionary'
tc_verfn_dict = {}

'Android version of the device'
android_version = None

'Device id of android device connected to the system'
android_device_id = None

'#######################################'
'Config parameters'
'#######################################'

'Getting configuration dictionary by reading config.ini file'
conf_dict = util.get_config_params()

'platform of execution - android or ios'
platform = str(conf_dict['Open_Manage_mobile']['platform']).lower()

'Android build file name kept in inputs folder'
android_buildFile_name = conf_dict['Open_Manage_mobile']['android_build_filename']

'ios build file name kept in inputs folder'
ios_buildFile_name = conf_dict['Open_Manage_mobile']['ios_build_filename']

'password value as provided by the user in config.ini'
password = conf_dict['Open_Manage_mobile']['password']
'old password value should be set when password changed'
old_password = ''

'password hint as provided by the user in config.ini'
password_hint = conf_dict['Open_Manage_mobile']['password_hint']

'IOS Version number'
ios_version_number = conf_dict['Open_Manage_mobile']['ios_version_number']

'getting version number from config gile'
version_number = conf_dict['Information']['version']
'password value as provided by the user in config.ini'
new_password = conf_dict['Open_Manage_mobile']['new_password']

'getting uild number from config file'
build_number = conf_dict['Information']['build_id']
'IOS Build Number'
ios_build_number = conf_dict['Open_Manage_mobile']['ios_build_number']

'Android Version Number'
android_version_no = conf_dict['Open_Manage_mobile']['android_version_number']

'Android Build Number'
android_build_no = conf_dict['Open_Manage_mobile']['android_build_number']

'bootstrap port number'
bootstrapport = conf_dict['Open_Manage_mobile']['appium_bootstrapport']

'Chrome driver port number'
chromedriverport = conf_dict['Open_Manage_mobile']['appium_chromedriverport']

'Port number'
portnum = conf_dict['Open_Manage_mobile']['appium_portnum']

'Platform version for IOS device'
platform_version = None
#android_version_no = "2.0.0.15"

'device name'
raw_device_name = conf_dict['Open_Manage_mobile']['device_name']
#device_name = unicodedata.normalize('NFKD', conf_dict['Open_Manage_mobile']['device_name'])
print "raw device name is %s" % raw_device_name
#device_name = (unicode(raw_device_name, "utf8")).encode('utf8', 'replace')

device_name = raw_device_name
print "device_name in global vars is %s" % device_name

'ios bundle id'
bundleid = 'beta.dell.com'

'ios udid'
udid = None

'#######################################'
'device configurations'
'#######################################'

'Standard appium server address which we use for execution'
server_address = "http://127.0.0.1:%s/wd/hub" % portnum
print "Server address is %s" % server_address
'App package for OMM execution'
app_package = 'com.dell.omm'

'App activity for OMM execution'
app_activity = 'com.dell.omm.ui.OmmHomeActivity'

'#######################################'
'File paths'
'#######################################'

'Input file path in which test case input such as devices details etc will be stored'
tc_input_file_path = current_dir + "/inputs/omm/omm_tc_info.xml"
demomode_acknowldge_agrement_txt =  current_dir + "/inputs/omm/verification_inputs/demomode_EULA_acknowledge_agrement.txt"
demomode_EULA_agrement_txt = current_dir + "/inputs/omm/verification_inputs/demomode_EULA_agrement.txt"
demomode_Diagnostcs_nd_usage_txt= current_dir + "/inputs/omm/verification_inputs/demomode_diagnostics_usage.txt"
Try_demomode_txt = current_dir + "/inputs/omm/verification_inputs/Try_demomode.txt"

'Path of license agreement verification input file'
license_agrmt_input = current_dir + "/inputs/omm/verification_inputs/LicenseAgreement.txt"
shareAppData_input = current_dir + "/inputs/omm/verification_inputs/ShareAppData.txt"
DemoMode_input = current_dir + "/inputs/omm/verification_inputs/DemoMode.txt"
demomode_acknowldge_agrement_txt =  current_dir + "/inputs/omm/verification_inputs/demomode_EULA_acknowledge_agrement.txt"
demomode_EULA_agrement_txt = current_dir + "/inputs/omm/verification_inputs/demomode_EULA_agrement.txt"
demomode_Diagnostcs_nd_usage_txt= current_dir + "/inputs/omm/verification_inputs/demomode_diagnostics_usage.txt"
Try_demomode_txt = current_dir + "/inputs/omm/verification_inputs/Try_demomode.txt"
first_ome_ntwrk_devices_txt = current_dir + "/inputs/omm/verification_inputs/first_ome_netwrkdevices.txt"
fourth_idrac_health_stus_txt=current_dir + "/inputs/omm/verification_inputs/fourth_idrac_dvce_helth_stus_txt"



first_ome_servers_devices_txt = current_dir + "/inputs/omm/verification_inputs/first_ome_Servers_devices.txt"
demomode_ome_network_device_txt = current_dir + "/inputs/omm/verification_inputs/demomode_netwrkdevices.txt"
second_ome_network_device_home_page_txt = current_dir + "/inputs/omm/verification_inputs/_ome_ntwrk_device_page_elmnts.txt"
first_ome_RAC_devices_txt =  current_dir + "/inputs/omm/verification_inputs/first_ome_RAC_devices.txt"
demomode_ome_first_RAC_device_txt = current_dir + "/inputs/omm/verification_inputs/demomode_ome_first_RAC_device.txt"
demomode_ome_servers_devices_txt = current_dir + "/inputs/omm/verification_inputs/demomode_ome_servers_devices.txt"
demomode_ome_first_servers_device_txt = current_dir + "/inputs/omm/verification_inputs/demomode_ome_first_server_devices.txt"
demomode_first_idrac_homepage_txt =  current_dir + "/inputs/omm/verification_inputs/first_idrac_homepage.txt"
demomode_idrac_hrd_invtry_cpu_dtls = current_dir + "/inputs/omm/verification_inputs/demomode_idrac_hardware_inventary_cpu_dtls.txt"
demomode_idrac_hardware_inventary_memory_dtls = current_dir + "/inputs/omm/verification_inputs/demomode_idrac_hardware_inventary_memory_dtls.txt"


first_ome_device_homePage_txt = current_dir + "/inputs/omm/verification_inputs/first_omedevice_homepage_txt"

second_ome_device_homePage_txt = current_dir + "/inputs/omm/verification_inputs/second_omedevice_homepage_txt"
second_ome_network_device_home_page_txt=  current_dir + "/inputs/omm/verification_inputs/second_ome_ntwrkdevice_homepage_txt"

first_ome_network_device_home_page_txt = current_dir + "/inputs/omm/verification_inputs/first_ome_ntwrkdevice_homepage_txt"
first_ome_racDevice_homePage_txt =  current_dir + "/inputs/omm/verification_inputs/first_ome_rackdevice_homepage_txt"
second_ome_racDevice_homePage_txt= current_dir + "/inputs/omm/verification_inputs/second_ome_rackdevice_homepage_txt"

first_ome_servers_homePage_txt = current_dir + "/inputs/omm/verification_inputs/first_ome_serversdevice_homepage_txt"
second_ome_servers_homePage_txt = current_dir + "/inputs/omm/verification_inputs/second_ome_serversdevice_homepage_txt"

first_idrac_homepage_txt= current_dir + "/inputs/omm/verification_inputs/first_idrac_dvce_homepage_txt"
idrac_device_location_txt=current_dir + "/inputs/omm/verification_inputs/idrac_dvce_location_info_txt"
idrac_health_stus_txt = current_dir + "/inputs/omm/verification_inputs/idrac_dvce_helth_stus_txt"
second_idrac_homepage_txt = current_dir + "/inputs/omm/verification_inputs/second_idrac_dvce_homepage_txt"
third_idrac_homepage_txt  = current_dir + "/inputs/omm/verification_inputs/third_idrac_dvce_homepage_txt"
fourth_idrac_homepage_txt=  current_dir + "/inputs/omm/verification_inputs/fourth_idrac_dvce_homepage_txt"
fourth_idrac_device_location_txt=current_dir + "/inputs/omm/verification_inputs/fourth_idrac_location_info_txt"
sixth_idrac_device_hmepage_txt=current_dir + "/inputs/omm/verification_inputs/six_idracevice_homepage_txt"
sevnth_idrac_device_hmepage_txt= current_dir + "/inputs/omm/verification_inputs/sevnth_idracevice_homepage_txt"
fifth_idrac_homepage_txt=current_dir + "/inputs/omm/verification_inputs/fifth_idrac_dvce_helth_stus_txt"






dynamic_sevnth_idracdvce_hmepage_txt= current_dir + "/inputs/omm/dynamic_txt_files/sevnth_idracevice_homepage_txt"
dynamic_sixth_idracdvce_homepage_txt= current_dir + "/inputs/omm/dynamic_txt_files/six_idracevice_homepage_txt"
dynamic_first_ome_device_homePage_txt= current_dir + "/inputs/omm/dynamic_txt_files/first_omedevice_homepage_txt"
dynamic_second_ome_device_homePage_txt= current_dir + "/inputs/omm/dynamic_txt_files/second_omedevice_homepage_txt"

dynamic_first_ome_ntwrkdevice_homePage_txt = current_dir + "/inputs/omm/dynamic_txt_files/first_ome_ntwrkdevice_homepage_txt"
dynamic_second_ome_ntwrkdevice_homePage_txt= current_dir + "/inputs/omm/dynamic_txt_files/second_ome_ntwrkdevice_homepage_txt"


dynamic_first_ome_racDevice_homePage_txt= current_dir + "/inputs/omm/dynamic_txt_files/first_ome_rackdevice_homepage_txt"
dynamic_second_ome_racDevice_homePage_txt= current_dir + "/inputs/omm/dynamic_txt_files/second_ome_rackdevice_homepage_txt"



dynamic_first_ome_servers_homePage_txt = current_dir + "/inputs/omm/dynamic_txt_files/first_ome_serversdevice_homepage_txt"
dynamic_second_ome_servers_homePage_txt = current_dir + "/inputs/omm/dynamic_txt_files/second_ome_serversdevice_homepage_txt"
dynamic_first_idrac_homepage_txt= current_dir + "/inputs/omm/dynamic_txt_files/first_idrac_dvce_homepage_txt"

dynamic_idrac_device_location_stus_txt= current_dir + "/inputs/omm/dynamic_txt_files/idrac_dvce_location_info_txt"
dynamic_idrac_device_helath_stus_txt=current_dir + "/inputs/omm/dynamic_txt_files/idrac_dvce_helth_stus_txt"
dynamic_fourth_idrac_device_helath_stus_txt= current_dir + "/inputs/omm/dynamic_txt_files/fourth_idrac_dvce_helth_stus_txt"
dynamic_fifth_idrac_homepage_txt=  current_dir + "/inputs/omm/dynamic_txt_files/fifth_idrac_dvce_helth_stus_txt"

dynamic_second_idrac_homepage_txt=current_dir + "/inputs/omm/dynamic_txt_files/second_idrac_dvce_homepage_txt"

dynamic_third_idrac_homepage_txt= current_dir + "/inputs/omm/dynamic_txt_files/third_idrac_dvce_homepage_txt"
dynamic_fourth_idrac_homepage_txt= current_dir + "/inputs/omm/dynamic_txt_files/fourth_idrac_dvce_homepage_txt"
dynamic_fourth_idrac_location_stus_txt= current_dir + "/inputs/omm/dynamic_txt_files/fourth_idrac_location_info_txt"
fourth_idrac_device_location_txt= current_dir + "/inputs/omm/dynamic_txt_files/fourth_idrac_location_info_txt"











'File path in which appium server logs will be redirected and saved'
appium_log_file_path = current_dir + "/logs/"

'Path in which object repository with ui object details are stored'
obj_repo_path = current_dir + "/inputs/omm/omm_object_repository.csv"

'Path in which android build for execution has been saved'
apk_path = current_dir + "/inputs/omm/builds/android/"

'Path in which ios build for execution has been saved'
ipa_path = current_dir + "/inputs/omm/builds/ios/"

'Path in which screenshots on failure will be captured'
screenshot_path = current_dir + "/logs/screenshots/"

'Path of license agreement verification input file'
license_agrmt_input = current_dir + "/inputs/omm/verification_inputs/LicenseAgreement.txt"
shareAppData_input = current_dir + "/inputs/omm/verification_inputs/ShareAppData.txt"
DemoMode_input = current_dir + "/inputs/omm/verification_inputs/DemoMode.txt"
'#######################################'
'Verification texts'
'#######################################'
shareApp_data = "You can help Dell improve this app by sharing anonymous use data."
shareApp_data_ios = "Anonymous Analytics and Usage"
shareApp_data_android = "You can help Dell improve this app by sharing anonymous use data."
ios_homeScreen_label = 'OpenManage Essentials'
aboutScreen_label = 'About'
android_homeScreen_label = 'OpenManage Mobile'

'password hint value will be having this text as predecessor in ios'
password_hint_text_predecessor_ios = 'Password Hint: '

popup_title_invalidPassword_ios = 'Invalid Password'
popup_title_wrongPassword_ios = 'Wrong Password'

popup_title_error = 'Error'
ios_wrong_passwrd_error ='Wrong Password'
ios_wrong_password_message ='You entered the wrong password. Please try again.'
ios_popup_title_error = 'Invalid Password'
popup_message_password_incorrect = 'The password entered is incorrect.'
popup_message_password_incorrect_ios = 'You entered the wrong password. Please try again.'
popup_message_password_blank ='Password cannot be blank.'
ios_popup_message_password_blank ='The password must be at least 4 characters long.'
popup_message_password_short = 'Password too short.please enter mimimum 4 characters '
ios_popup_message_password_short = 'The password must be at least 4 characters long.'
popup_message_password_short_ios = 'The password must be at least 4 characters long.'
popup_message_password_do_not_match = 'Password do not match.'
popup_message_password_do_not_match = 'Password do not match.'
ios_popup_message_password_do_not_match = 'The new password and the re-entered password does not match.'
popup_message_password_do_not_match_ios = 'The new password and the re-entered password does not match.'
popup_message_password_hint = 'Password hint.'
popup_message_password_hint_ios = 'Password hint is required.'
popup_message_password_hint_same_as_passsword = 'Password cannot be the same as the hint.'
popup_message_password_hint_same_as_passsword_ios = 'The new password cannot match the password hint.'
popup_message_new_password_same_as_current_password = 'New Password cannot be the same as current password.'


popup_title_skip_password_confirmation = r'Warning'
popup_message_incorrect_password = r'Without a password, OMM cannot prevent unauthorized usave. Continue?'

popup_title_reset_confirmation1 = r'Are you sure?'
popup_title_reset_confirmation2 = r'Confirm Reset'
popup_message_reset_confirmation1 = r'This will delete all your existing data. Are you you want to proceed?'
popup_message_reset_confirmation2 = r'Changes cannot be undone.'

'#######################################'
'Commands'
'#######################################'

'Command to get deviced id of android devices connected to the Management Station'
android_deviceID_cmd = 'adb devices -l'

'Command to get android version of the device connected'
android_version_cmd = 'adb -s device_id shell getprop ro.build.version.release'

'Command to start appium server'
android_appServer_start_cmd =  ('"' + 'C:/Program Files (x86)/Appium/node.exe' + '" ' + '"') + \
                'C:/Program Files (x86)/Appium/node_modules/appium/bin/Appium.js' + \
                ('"' + ' --address 127.0.0.1 --chromedriver-port %s --bootstrap-port %s' % (chromedriverport, bootstrapport )) + \
                (' --selendroid-port 8082 --no-reset --local-timezone --port %s --log ' % portnum) + appium_log_file_path

and_get_installed_packs_cmd = 'adb -s device_id shell pm list packages'
android_uninstall_cmd = 'adb -s device_id uninstall ' + app_package
android_app_uninstall_cmd = 'adb -s device_id uninstall '

ios_appServer_start_cmd = ('Node /Applications/appium.app/Contents/Resources/node_modules/appium/bin/appium.js') + \
                         (' --address 127.0.0.1 --port %s --chromedriver-port %s --bootstrap-port %s' % (portnum, chromedriverport, bootstrapport)) +\
                         (' --selendroid-port 8082 --no-reset --local-timezone --log ') + appium_log_file_path

'IOS command for getting UDID'
ios_udid_cmd = 'system_profiler SPUSBDataType | sed -n \'/iPhone/,/Serial/p\' | grep "Serial Number:" | awk -F ": " \'{print $2}\''

devicetype = (conf_dict['Open_Manage_mobile']['device_type']).lower()

'IOS command for getting platform version and device name'
ios_devName_platformver_cmd = 'instruments -s devices'

'IOS command for uninstalling app'
ios_uninstall_cmd = 'ideviceinstaller -u udid -U %s' % bundleid

'Genny motion command to get device list'
gennymotion_cmd = 'genyshell.exe -c "devices list"'

'Genny motion command for mac system'
mac_gennymotion_cmd = 'genyshell -c "devices list"'

'winrm command'
winrm_enumerate_command = 'winrm e http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/root/dcim/'

winrm_get_command = 'winrm g http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/root/dcim/'

winrm_invoke_powerstate_command = 'winrm i RequestPowerStateChange cimv2/root/dcim/DCIM_CSPowerManagementService?SystemCreationClassName=DCIM_SPComputerSystem+SystemName=systemmc+CreationClassName=DCIM_CSPowerManagementService+Name=pwrmgtsvc:1'

winrm_apply_vnc_attributes_command = 'winrm i ApplyAttributes http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/root/dcim/DCIM_iDRACCardService?__cimnamespace=root/dcim+SystemCreationClassName=DCIM_ComputerSystem+SystemName=DCIM:ComputerSystem+CreationClassName=DCIM_iDRACCardService+Name=DCIM:iDRACCardService'
'#######################################'
'WSMAN class names'
'#######################################'
systemView_classname = 'DCIM_SystemView'

cpuView_classname = 'DCIM_CPUView'

memoryView_classname ='DCIM_MemoryView'

powersupplyView_classname = 'DCIM_PowerSupplyView'

powerManagementService_classname = 'DCIM_CSAssociatedPowerManagementService'

systemString_classname = 'DCIM_SystemString'

lcd_instanceid = 'System.Embedded.1#LCD.1#CurrentDisplay'

osname_instanceid = 'System.Embedded.1#ServerOS.1#OSName'

osversion_instanceid = 'System.Embedded.1#ServerOS.1#OSVersion'

'#######################################'
'Verification texts'
'#######################################'
shareApp_data = "You can help Dell improve this app by sharing anonymous use data."
shareApp_data_ios = "Anonymous Analytics and Usage"
shareApp_data_android = "You can help Dell improve this app by sharing anonymous use data."
ios_homeScreen_label = 'OpenManage Essentials'
aboutScreen_label = 'About'
android_homeScreen_label = 'OpenManage Mobile'

