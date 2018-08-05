""""
This module contains all the modules related to idrac common functions
"""
import traceback
from winrm.protocol import Protocol
import collections
from libs.product.omm.standard import global_vars


def run_winrm_command(class_name, idrac_ip, idrac_userName, idrac_password,
                      windows_ip, windows_username, windows_password, instanceid = None):
    """
    This function is used for getting output of enumeration class as speciified

    Function Owner : Pooja_Rundwal

    Date created : 9/5/2016

    @param class_name : WSMan class name
    @param idrac_ip : (string) idrac ip of system
    @param idrac_userName : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip from which query will be executed
    @param windows_userName : (string) windows system user name
    @param windows_password : (string) windows system password
    @param instance_id : (string) instance id for fetching data specific to an instance. Optional

    @return command_output : (string) Command Output, None in case of any error
    @return no_of_instances : (string) number of instances returned 
    """
    try:
        'establish connection with windows system'
        p = Protocol(
             endpoint='http://' + windows_ip+':5985/wsman',
             transport='plaintext',
             username=windows_username,
             password=windows_password)
        shell_id = p.open_shell()

        if instanceid is not None:
            winrm_command = global_vars.winrm_get_command + \
                            class_name + '?__cimnamespace=root/dcim+InstanceID=' + instanceid + \
                            ' -u:' + idrac_userName + ' -p:' + idrac_password + ' -r:https://' + \
                            idrac_ip + '/wsman -SkipCNcheck -SkipCAcheck -encoding:utf-8 -a:basic'
        else:
            'execute winrm command on idrac ip'
            winrm_command = global_vars.winrm_enumerate_command + \
                            class_name + ' -u:' + idrac_userName + ' -p:' + idrac_password + \
                            ' -r:https://' + idrac_ip + '/wsman -SkipCNcheck -SkipCAcheck -encoding:utf-8 -a:basic'
        print "Winrm Command %s \n" % (winrm_command)
        command_id = p.run_command(shell_id, winrm_command)

        'get command output'
        command_output, command_error, command_status = p.get_command_output(shell_id, command_id)
        no_of_instances = command_output.count(class_name)

        print 'Command Output:' + str(command_output)
        p.cleanup_command(shell_id, command_id)
        p.close_shell(shell_id)

        return command_output, no_of_instances
    except:
        traceback.print_exc()
        return None, '0'


def run_powerstate_change_winrm_command(power_state, idrac_ip, idrac_userName, idrac_password,
                      windows_ip, windows_username, windows_password):
    """
    This function is used for getting output of enumeration class as speciified

    Function Owner : Pooja_Rundwal

    Date created : 9/5/2016

    @param powerstate : 2 - Power On , 8 - Graceful shutdown
    @param idrac_ip : (string) idrac ip of system
    @param idrac_userName : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip from which query will be executed
    @param windows_userName : (string) windows system user name
    @param windows_password : (string) windows system password
    @param instance_id : (string) instance id for fetching data specific to an instance. Optional

    @return command_output : (string) Command Output, None in case of any error
    @return no_of_instances : (string) number of instances returned 
    """
    try:
        'establish connection with windows system'
        p = Protocol(
             endpoint='http://' + windows_ip+':5985/wsman',
             transport='plaintext',
             username=windows_username,
             password=windows_password)
        shell_id = p.open_shell()

        'execute winrm command on idrac ip'
        winrm_command = global_vars.winrm_invoke_powerstate_command + ' @{PowerState="' + power_state + '"}' \
                         + ' -u:' + idrac_userName + ' -p:' + idrac_password + \
                        ' -r:https://' + idrac_ip + '/wsman -SkipCNcheck -SkipCAcheck -encoding:utf-8 -a:basic'
        print "Winrm Command %s \n" % (winrm_command)
        command_id = p.run_command(shell_id, winrm_command)

        'get command output'
        command_output, command_error, command_status = p.get_command_output(shell_id, command_id)

        print 'Command Output:' + str(command_output)
        p.cleanup_command(shell_id, command_id)
        p.close_shell(shell_id)

        return command_output
    except:
        traceback.print_exc()
        return None, '0'

def run_vncApplyAttribute_winrm_command(attribute_name, attribute_value, idrac_ip, idrac_userName, idrac_password,
                      windows_ip, windows_username, windows_password):
    """
    This function is used for getting output of enumeration class as speciified

    Function Owner : Nithya_V

    Date created : 6/9/2016

    @param attribute_name : VNC attribute name which needs to be changed
    @param attribute_value : VNC attribute value which needs to be applied
    @param idrac_ip : (string) idrac ip of system
    @param idrac_userName : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip from which query will be executed
    @param windows_userName : (string) windows system user name
    @param windows_password : (string) windows system password
    @param instance_id : (string) instance id for fetching data specific to an instance. Optional

    @return command_output : (string) Command Output, None in case of any error
    @return no_of_instances : (string) number of instances returned 
    """
    try:
        'establish connection with windows system'
        p = Protocol(
             endpoint='http://' + windows_ip+':5985/wsman',
             transport='plaintext',
             username=windows_username,
             password=windows_password)
        shell_id = p.open_shell()

        'execute winrm command on idrac ip'
        winrm_command = global_vars.winrm_apply_vnc_attributes_command + ' -u:' + idrac_userName + ' -p:' + idrac_password + \
                         ' -r:https://' + idrac_ip + '/wsman -SkipCNcheck -SkipCAcheck -encoding:utf-8 -a:basic @{Target="iDRAC.Embedded.1";AttributeName=%s;AttributeValue=%s}' % (attribute_name, attribute_value)
        print "Winrm Command %s \n" % (winrm_command)
        command_id = p.run_command(shell_id, 'ls')

        'get command output'
        command_output, command_error, command_status = p.get_command_output(shell_id, command_id)

        print 'Command Output:' + str(command_output)
        p.cleanup_command(shell_id, command_id)
        p.close_shell(shell_id)

        return command_output, 0
    except:
        traceback.print_exc()
        return None, '0'

def apply_vnc_attributes(attribute, attribute_value, idrac_ip, idrac_userName, idrac_password,
                      windows_ip, windows_username, windows_password):
    """
    This function is used for applying vnc attributes

    Function Owner : Nithya_V

    Date created : 6/9/2016

    @param attribute_name : VNC attribute name which needs to be changed
    @param attribute_value : VNC attribute value which needs to be applied
    @param idrac_ip : (string) idrac ip of system
    @param idrac_userName : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip from which query will be executed
    @param windows_userName : (string) windows system user name
    @param windows_password : (string) windows system password
    @param instance_id : (string) instance id for fetching data specific to an instance. Optional

    @return command_output : (string) Command Output, None in case of any error
    @return no_of_instances : (string) number of instances returned 
    """
    output, instance_no = "", 0

    try:
        # attribute dictionary of all vnc settings
        attribute_dict = {'password': 'VNCServer.1#Password', 'ActiveSessions':'VNCServer.1#ActiveSessions', 'MaxSessions': 'VNCServer.1#MaxSessions',
                          'Port': 'VNCServer.1#Port','Timeout':'VNCServer.1#Timeout','Enable': 'VNCServer.1#Enable',
                           'LowerEncryptionBitLength': 'VNCServer.1#LowerEncryptionBitLength', 'SSLEncryptionBitLength': 'VNCServer.1#SSLEncryptionBitLength'}
        output, instance_no = run_vncApplyAttribute_winrm_command(attribute_dict[attribute], attribute_value, idrac_ip, idrac_userName, idrac_password,
                      windows_ip, windows_username, windows_password)
    except:
        traceback.print_exc()

    return output, instance_no


def get_wsman_dict(class_name, idrac_ip, idrac_userName, idrac_password,
                   windows_ip, windows_username, windows_password, instanceid = None):
    """
    This function is used for getting output of enumeration class as a dictionary of
    attribute value pairs

    Function Owner : Pooja_Rundwal

    Date created : 19/5/2016

    @param class_name : (string) DCIM class for which data to be retrieved
    @param idrac_ip : (string) idrac ip of system for which data to be retrieved
    @param idrac_userName : (string) idrac user name
    @param idrac_password : (string) idrac password
    @param windows_ip : (string) windows system ip
    @param windows_userName : (string) windows system user name
    @param windows_password : (string) windows system password
    @param instance_id : (string) instance id for fetching data specific to an instance. Optional

    @return wsman_dict : (dictionary) Output as a dictionary
    @return no_of_instances : (string) number of instances returned
    """
    wsman_dict = collections.OrderedDict()
    count = 0
    try:
        cmdoutput, no_of_instances = run_winrm_command(class_name, idrac_ip, idrac_userName, idrac_password,
                                                    windows_ip, windows_username, windows_password, instanceid )

        if cmdoutput is not None and no_of_instances == 1:
            'store winrm output in dictionary'
            for line in cmdoutput.split('\n'):
                if line.__contains__('='):
                    attribute = line.split('=')[0].strip()
                    value = line.split('=')[1].strip()
                else:
                    attribute = line.strip()
                    value = ''
                wsman_dict[attribute] = value
        elif cmdoutput is not None and no_of_instances > 1:
            for line in cmdoutput.split('\n'):
                if line.__contains__(class_name):
                    count = count + 1
                if line.__contains__('='):
                    attribute = line.split('=')[0].strip() + str(count)
                    value = line.split('=')[1].strip()
                else:
                    attribute = line.strip() + str(count)
                    value = ''
                wsman_dict[attribute] = value
        else:
            wsman_dict = {}
        print 'Dictionary:' + str(wsman_dict)
    except:
        traceback.print_exc()
    return wsman_dict, no_of_instances


def convert_byte_to_gb(attribute_value):
    """
    This function converts value from byte to GB

    Function Owner : Pooja_Rundwal

    Date created : 23/5/2016

    @param attribute_value : (string) value to be converted to GB

    @return new_attribute_value : (string) New value after conversion
    """
    try:
        attribute_value = int(attribute_value) / 1024
        new_attribute_value = str(attribute_value) + ' GB'
        return new_attribute_value
    except:
        traceback.print_exc()
        return ''


def power_status_mapping(attribute_value):
    """
    This function converts power status value fetched using Winrm to value displayed in console
    2 : On , 13 : Off

    Function Owner : Pooja_Rundwal

    Date created : 23/5/2016

    @param attribute_value : (string) value to be converted as per mapping

    @return new_attribute_value : (string) New value after conversion
    """
    try:
        if attribute_value == '2':
            if global_vars.platform == 'ios':
                new_attribute_value = 'On'
            else:
                new_attribute_value = 'ON'
        else:
            if global_vars.platform == 'ios':
                new_attribute_value = 'Off'
            else:
                new_attribute_value = 'OFF'
        return new_attribute_value
    except:
        traceback.print_exc()
        return ''
