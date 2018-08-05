""""
This module contains all the modules related to idrac common functions
"""
import pymssql
import traceback
import pyodbc

import collections
from libs.product.omm.standard import global_vars
from wsman.provider import winrm
from wsman.provider.remote import Remote
from wsman.transport.process import Subprocess

namespace = 'root/dcim'
uri = "http://schemas.dmtf.org"
#number_of_rows_db=0
number_of_rows_db=0
Currentindexinmultidimensionallist=-1
CounterforDBRowdatainlist=0
DBRowdatainlist=[]


def getEnumerated(classToBeEnumerated, idrac_ip, idrac_userName, idrac_password, \
                  rawOutput=True):
    """
    This function is used for getting output of enumeration class as speciified

    Function Owner : Nithya_V

    Date created : 9/5/2016

    @param classToBeEnumerated : (string) DCIM class for which data to be retrieved
    @param idrac_ip : (string) idrac ip of system for which data to be retrieved
    @param idrac_userName : (string) idrac user name of system for which data to be retrieved
    @param idrac_password : (string) idrac password of system for which data to be retrieved
    @param rawOutput : (string) output without parsing

    @return result : (string) Command Output, None in case of any error
    """
    try:
        remobj = Remote(idrac_ip, idrac_userName, idrac_password)
        print '\nENUMERATING THE CLASS '  +classToBeEnumerated+ "\n"
        winrmobj = winrm.WinRM(transport = Subprocess())
        result = winrmobj.enumerate(cim_class=classToBeEnumerated, \
                        cim_namespace=namespace, remote=remobj, raw=rawOutput, uri_host=uri)
        if result == None:
            print 'Enumeration Command Failed'
            return None
        else:
            if rawOutput == False:
                print 'Number of Instances returned : ', len(result)
            return result  
    except:
        traceback.print_exc()
        return None


def get_wsman_dict(classToBeEnumerated, idrac_ip, idrac_userName, idrac_password,\
                    rawOutput=True):
    """
    This function is used for getting output of enumeration class as a dictionary of
    attribute value pairs

    Function Owner : Nithya_V

    Date created : 9/5/2016

    @param classToBeEnumerated : (string) DCIM class for which data to be retrieved
    @param idrac_ip : (string) idrac ip of system for which data to be retrieved
    @param idrac_userName : (string) idrac user name of system for which data to be retrieved
    @param idrac_password : (string) idrac password of system for which data to be retrieved
    @param rawOutput : (string) output without parsing

    @return wsman_dict : (dictionary) Output as a dictionary
    """
    wsman_dict = {}
    try:
        cmdoutput = getEnumerated(classToBeEnumerated, idrac_ip, idrac_userName, \
                                  idrac_password, rawOutput=rawOutput)
        print cmdoutput
        for line in cmdoutput.split('\n'):
            if line.__contains__('</n1:') and line.__contains__('<n1:'):
                attribute = str(line.split('</n1:')[1]).replace(">", "").strip()
                value = str(line.split('</n1:')[0]).replace(attribute, "").replace("<n1:", "").replace(">","").strip()
                wsman_dict[attribute] = value
    except:
        traceback.print_exc()
    return wsman_dict 


def db_get_totalcount(table_name):
    """
    This function is used for getting database query results of total count of devices and events

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param table_name : (string) Database Table Name 

    @return rows : (string) Return the number of records available in DB for respective table
    """
    try:
        'establish DB Connection'
        cnxn = pyodbc.connect('DSN=MYSERVER;UID=administrator;PWD=Dell123')
        cursor = cnxn.cursor()
        
        'Form the SQL query and execute'
        sql_query = "select count(*) from OMEssentials.dbo."+table_name
        cursor.execute(sql_query)
        
        'Fetch the row'
        rows = cursor.fetchone()[0]
        print 'Command Output:' + str(rows)

        'Close the connection'
        cursor.close()

        return str(rows)
    except:
        traceback.print_exc()
        return None
def pysmsql_db_get_totalcount(table_name):
    """
    This function is used for getting database query results of total count of devices and events

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param table_name : (string) Database Table Name 

    @return rows : (string) Return the number of records available in DB for respective table
    """
    try:
        'establish DB Connection'
        #cnxn = pyodbc.connect('DSN=MYSERVER;UID=sa;PWD=dell_123')
        #cursor = cnxn.cursor()
        conn = pymssql.connect("100.100.16.50","omm","Dell123$")
        cursor = conn.cursor()

        
        'Form the SQL query and execute'
        sql_query = "select count(*) from OMEssentials.dbo."+table_name
        cursor.execute(sql_query)
        
        'Fetch the row'
        rows = cursor.fetchone()[0]
        print 'Command Output:' + str(rows)

        'Close the connection'
        cursor.close()

        return str(rows)
    except:
        traceback.print_exc()
        return None        
    
def db_all_device_event_count(table_name, status):
    """
    This function is used for getting database query results of various type devices statuses and events severities

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param table_name : (string) Database Table Name 
    @param status : (string) Status code number

    @return rows : (string) Return the number of records available in DB for respective health status or event severity
    
    For Device Health Status:
        0 - None
        2 - Unknown
        4 - Normal
        8 - Warning
        16 - Critical
        32 - DefaultVM
        
        for Event Severity:
        1 - Unknown
        2 - Info
        4 - Normal
        8 - Warning
        16 - Critical
        32 - Irrecoverable
        100 - Interpreted
    """
    try:
        'establish DB Connection'
        cnxn = pyodbc.connect('DSN=MYSERVER;UID=sa;PWD=Dell1234')
        cursor = cnxn.cursor()
        
        'Form the SQL query and execute'
        if table_name == "Device":
            column_name = "DeviceGlobalStatus"
        elif table_name == "Event":
            column_name = "Severity"
        sql_query = "select count(*) from OMEssentials.dbo."+table_name+" where "+column_name+" = "+status
        cursor.execute(sql_query)  
        
        'Fetch the row'
        rows = cursor.fetchone()[0]
        print 'Command Output:' + str(rows)

        'Close the connection'
        cursor.close()

        return rows
    except:
        traceback.print_exc()
        return None


def convert_code_to_description(table_name, status):
    """
    This function will accept the status code and return the Health Status description
    This function will accept the status code and return the Event Severity description

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param table_name : (string) Database Table Name 
    @param status : (string) Status code number

    @return new_attribute_value : (string) New value after conversion
    """
    try:
        status = str(status)
        if table_name == "Device":
            if status == "0":
                return "None"
            elif status == "2":
                return "Unknown"
            elif status == "4":
                return "Healthy"
            elif status == "8":
                return "Warning"
            elif status == "16":
                return "Critical"
            elif status == "32":
                return "DefaultVM"
        elif table_name == "Event":
            if status == "1":
                return "Unknown"
            elif status == "2":
                return "Info"
            elif status == "4":
                return "Healthy"
            elif status == "8":
                return "Warning"
            elif status == "16":
                return "Critical"
            elif status == "32":
                return "Irrecoverable"
            elif status == "100":
                return "Interpreted"
    except:
        traceback.print_exc()
        return ''
def pysmsql_convert_code_to_description(table_name, status):
    """
    This function will accept the status code and return the Health Status description
    This function will accept the status code and return the Event Severity description

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param table_name : (string) Database Table Name 
    @param status : (string) Status code number

    @return new_attribute_value : (string) New value after conversion
    """
    try:
        status = str(status)
        if table_name == "Device":
            if status == "0":
                return "None"
            elif status == "2":
                return "Unknown"
            elif status == "4":
                return "Healthy"
            elif status == "8":
                return "Warning"
            elif status == "16":
                return "Critical"
            elif status == "32":
                return "DefaultVM"
        elif table_name == "Event":
            if status == "1":
                return "Unknown"
            elif status == "2":
                return "Info"
            elif status == "4":
                return "Healthy"
            elif status == "8":
                return "Warning"
            elif status == "16":
                return "Critical"
            elif status == "32":
                return "Irrecoverable"
            elif status == "100":
                return "Interpreted"
    except:
        traceback.print_exc()
        return ''    
    

def omedbdata1(omedbip,sqluser,sqlpwd,query):
    #print "inside omedbdata(omedbip,sqluser,sqlpwd,dbname,query) function"
    #msg, status = "", True
    #global number_of_rows_db
    #try:
        #number_of_rows_db=0
        #conn = pymssql.connect(omedbip,sqluser,sqlpwd,dbname)
        #cursor = conn.cursor()
        #cursor.execute(query)
        #row = cursor.fetchone()
        #while row:
            #number_of_rows_db+=1
            #print row
            #row = cursor.fetchone()        
        #print "Number of rows in database is==>"+str(number_of_rows_db)
        #number_of_rows_db=0
        #conn.close()
        #status = True
    #except Exception as excp:
        #traceback.print_exc()
        #msg += str(excp)
        #status = False
    #return status, msg
    msg, status = "", True
    global number_of_rows_db
    global Currentindexinmultidimensionallist
    global CounterforDBRowdatainlist
    try:
        conn = pymssql.connect(omedbip,sqluser,sqlpwd)
        cursor = conn.cursor()        
        cursor.execute(query)
        row = cursor.fetchone()
        while row:
            DBRowdatainlist.append(row)
            number_of_rows_db+=1 
            row = cursor.fetchone()
            
        number_of_rows_db=0
        conn.close()
        #we will read the DB result from DBRowdatainlist and store it to multidimensional list to return by function as final result.
        for item in DBRowdatainlist:
            CounterforDBRowdatainlist+=1
            Currentindexinmultidimensionallist+=1
            if CounterforDBRowdatainlist==1:
                w, h =len(item),len(DBRowdatainlist)
                Matrix = [[0 for x in range(w)] for y in range(h)]
                for column in range(w):
                    Matrix[Currentindexinmultidimensionallist][column]=str(item[column])
            else:
                for column in range(w):
                    Matrix[Currentindexinmultidimensionallist][column]=str(item[column])
                    
    except Exception as excp:
        msg += str(excp)
        status = False
    return status, msg,Matrix
    

def omedbdata(omedbip,sqluser,sqlpwd,dbname,query):
    print "insdie omedbdata(omedbip,sqluser,sqlpwd,dbname,query) function"
    global number_of_rows_db
    conn = pymssql.connect(omedbip,sqluser,sqlpwd,dbname)
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    while row:
        number_of_rows_db+=1
        print row
        row = cursor.fetchone()
    print "Number of rows in database is==>"+str(number_of_rows_db)
    number_of_rows_db=0
    conn.close()
        
    
    
    

        

    
def pysmsql_db_all_device_event_count(table_name, status):
    """
    This function is used for getting database query results of various type devices statuses and events severities

    Function Owner : Abdul_G_Shaik

    Date created : 06/15/2016

    @param table_name : (string) Database Table Name 
    @param status : (string) Status code number

    @return rows : (string) Return the number of records available in DB for respective health status or event severity
    
    For Device Health Status:
        0 - None
        2 - Unknown
        4 - Normal
        8 - Warning
        16 - Critical
        32 - DefaultVM
        
        for Event Severity:
        1 - Unknown
        2 - Info
        4 - Normal
        8 - Warning
        16 - Critical
        32 - Irrecoverable
        100 - Interpreted
    """
    try:
        'establish DB Connection'
        #cnxn = pyodbc.connect('DSN=MYSERVER;UID=sa;PWD=dell_123')
        #cursor = cnxn.cursor()
        conn = pymssql.connect("100.100.16.50","omm","Dell123$")
        cursor = conn.cursor()
        
        'Form the SQL query and execute'
        if table_name == "Device":
            column_name = "DeviceGlobalStatus"
        elif table_name == "Event":
            column_name = "Severity"
        sql_query = "select count(*) from OMEssentials.dbo."+table_name+" where "+column_name+" = "+status
        cursor.execute(sql_query)  
        
        'Fetch the row'
        rows = cursor.fetchone()[0]
        print 'Command Output:' + str(rows)

        'Close the connection'
        cursor.close()

        return rows
    except:
        traceback.print_exc()
        return None
    
    
    
    
    