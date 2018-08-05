import traceback
from subprocess import Popen, PIPE
import ConfigParser
import datetime
import sys
import re
import csv
import os
import io
from os import path as ospath
from ConfigParser import SafeConfigParser

current_dir =  os.getcwd()

def get_config_params():
    """
    This function is used for getting the dictionary of
    config parameters available in config.ini

    @return my_config_parser_dict : (Dictionary) Config dictionary contains all
                                configuration parameters
    """
    ConfigFile = sys.argv[1]
    print "Config file is %s" % ConfigFile
    my_config_parser_dict = {}
    try:
        config = ConfigParser.RawConfigParser()
        config.read(ConfigFile)
        my_config_parser_dict = {s: dict(config.items(s)) for s in \
                                 config.sections()}
    except:
            traceback.print_exc()
    return my_config_parser_dict


def step(num):
    """
    This function is used for printing step in std out

    @param  num : (String) Step number/Step heading to be printed
    """
    try:
        print "#", "*" * 100
        print " " * 46, " STEP %s " % str(num)
        print "#", "*" * 100
    except:
        traceback.print_exc()


def title(titlestr):
    """
    This function is used for printing title in formatted way in std out

    @param  titlestr : (String) Title string to be printed in std out
    """
    try:
        print "#", "*" * 100
        print " " * 10, titlestr
        print "#", "*" * 100
    except:
        traceback.print_exc()


def pathJoin(a, *p):
    """
    This function is used for joining two or more folder to form the path

    @param  a : (String) base path
    @param  p : (String) one or more path which has to be appended
    """
    try:
        return ospath.join(a, *p)
    except:
        traceback.print_exc()


def runCommand(cmd, inparam=None, shell=True):
    """
    This function is used to run any shell command

    @param  cmd : (String) Command to be executed
    @param  inparam : (String) in parameters if any
    @param  shell : (String) True or False
    """
    result, error = "", ""
    try:
        process = Popen(cmd, shell=shell, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        if (inparam != None):
            result, error = process.communicate(inparam)
        else:
            result, error = process.communicate()
        print "result %s, error is %s" % (result, error)
    except:
        traceback.print_exc()
    print "result %s, error is %s" % (result, error)
    return result, error


def ordered(obj):
    """
    This function is used to return dictionary or list in sorted form

    Function Owner : Nithya_V

    Date created : 2/17/2016

    @param  obj : (String) Dictionary /List which has to be sorted
    """
    try:
        if isinstance(obj, dict):
            return sorted((k, ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(ordered(x) for x in obj)
        else:
            return obj
    except:
        traceback.print_exc()
        return None


def uniqueID():
    """
    This function is used to generate unique ID which can be used to generate
    unique name such as connection profile name, discovery task name etc

    Function Owner : Nithya_V

    Date created : 2/17/2016

    @param  c_datetime : (String) Returns current datatime formatted as a
                            unique ID
    """
    c_datetime = ""
    try:
        #c_datetime = datetime.datetime.now().strftime("%Y%m%d%I%M%S")
          c_datetime = datetime.datetime.now().strftime("%Y%m%d%I%M")
    except:
        traceback.print_exc()
    return c_datetime


def pathExists(filename, directory="."):
    """
    This function is used to verify if path exists

    @param  filename : (String) File name to be verified
    @param  directory : (String) current directory
    """
    try:
        fullpath = ospath.join(directory, filename)
        if (ospath.exists(fullpath)):
            return True
        else:
            return False
    except:
        traceback.print_exc()
        return False


def read_file(file_name):
    """
    This function is used to verify read the data from the file

    @param  filename : (String) File name from which data to be read

    @return file_data : (string) data read from the file. None if it is empty
    """
    file_data = None
    try:
        file_object = open(file_name, "r+")
        file_data = str(file_object.read())
        file_object.close()
    except:
        traceback.print_exc()
    return file_data


def listening_ports_list():
    """
    This function is used to getting listening ports list

    Function Owner : Nithya_V

    Date created : 6/10/2016

    @return  portsInuse : (list) List of ports which is in use
    """
    portsInuse = []
    try:
        netstat, error = runCommand('netstat -a')
        for net in netstat.split('\n'):
            if net.__contains__('LISTENING'):
                usedaddrgroup = (re.search("\d+.\d+.\d+.\d+:\d+", net, re.I))
                if not usedaddrgroup:
                    usedaddrgroup = (re.search("]:\d+", net, re.I))
                usedaddr = usedaddrgroup.group(0).strip()
                usedport = usedaddr.split(":")[1]
                portsInuse.append(usedport)
        print "Ports in use is %s" % portsInuse
    except:
        traceback.print_exc()
    return portsInuse


def checkPortInUse(port, portsInuse=None):
    """
    This function is used for checking port is in use.
    If in use, will return an unused port number

    Function Owner : Nithya_V

    Date created : 2/17/2016

    @param  port : (int) port number
    @param  portsInuse : (list) If not none, retrieves ports which are not in use

    @return  portforuse : (int) Port which is unused
    """

    portforuse = None
    try:
        if portsInuse == None:
            portsInuse = listening_ports_list()

        if str(port) in portsInuse:
            newport = port + 1
            print "Port %s is in use. Incrementing port by 1" % port
            portforuse = checkPortInUse(newport, portsInuse)
        else:
            print "Port %s not in use" % port
            portforuse = port
    except:
        traceback.print_exc()
    return portforuse


def get_emulator_device_info():
    """
    This function is used to getting emulator device dictionary

    Function Owner : Nithya_V

    Date created : 6/10/2016

    @return  device_emulator_dict : (dict) Emulator dictionary
    """
    device_emulator_dict = {}
    'Path in which emulator device csv is stored'
    emulator_device_csv = current_dir + "/inputs/omm/omm_emulator_execution.csv"
    try:
        # reading omm_emulator_execution.csv and converting to a dictionary
        emulator_device_obj = open(emulator_device_csv, "rb")
        emultr_dev_reader = csv.reader(emulator_device_obj)
        for row in emultr_dev_reader:
            for col in row:
                if str(row[0]).strip() != 'Device Name':
                    print "Col is %s" % col
                    print "Row is %s" % row
                    device_emulator_dict[row[0]] = {'Execute' : row[1], 'Testcases' : row[2].split('#')[1]}
                    break
        print "Device dictionary is %s" % device_emulator_dict
    except:
        print "Unable to retrieve Device execution details ..."
        traceback.print_exc()
    return device_emulator_dict


def change_file(file_name, old_value, new_value):
    """
    This function is used to change an old value to new value

    Function Owner : Nithya_V

    Date created : 6/10/2016

    @param  file_name : (string) File name of file to be changed
    @param  old_value : (string) value which has to be changed
    @param  new_value : (string) new value to be added

    @return  status : (string) True if successful, False otherwise  
    """
    status = False
    try:
        with open(file_name) as f:
            file_str = f.read()
    
        file_str = file_str.replace(old_value, new_value )
    
        with open(file_name, "w") as f:
            f.write(file_str)
        status = True
    except:
        traceback.print_exc()
    return status


def change_configfile(file_name, section, key, value):
    """
    This function is used to change an old value to new value

    Function Owner : Nithya_V

    Date created : 6/10/2016

    @param  file_name : (string) File name of file to be changed
    @param  section : (string) section in config.ini where change has to be made
    @param  key : (string) key to be changed
    @param  value : (string) value to be added

    @return  status : (string) True if successful, False otherwise  
    """
    status = False
    try:
        config = SafeConfigParser()
        config.read(file_name)

        config.set(section, key, value)
        with io.open(file_name, 'wb') as configfile:
            config.write(configfile)
        status = True
    except:
        traceback.print_exc()
    return status


def open_file(file_name):
    """
    This function is used to verify read the data from the file

    @param  filename : (String) File name from which data to be read

    @return file_data : (string) data read from the file. None if it is empty
    """
    file_data = None
    try:
        file_object = open(file_name, "w")
        file_object.close()
    except:
        traceback.print_exc()
    return file_data


def write_file(file_name, text):

    """
    This function is used to verify read the data from the file

    @param  filename : (String) File name from which data to be read

    @return file_data : (string) data read from the file. None if it is empty
    """
    file_data = None
    try:
        file_object = open(file_name, "a+")
        file_object.write("{0}{1}".format(str(text), os.linesep))
        #file_data = str(file_object.read())
        file_object.close()
    except:
        traceback.print_exc()
    return file_data
