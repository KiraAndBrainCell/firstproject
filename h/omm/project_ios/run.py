#!/usr/bin/python2

__unittest = True

import os

run_dir = os.path.abspath(os.path.dirname(__file__))
current_dir = os.getcwd()

if __name__ == '__main__':
    os.chdir(run_dir)

import sys
import time
import logging
import ConfigParser

# several of the modules in core expect to be able to import themselves... :(
sys.path.insert(1, os.path.abspath('libs/core'))

# Path updates for third party packages that expect to import packages 
sys.path.append(os.path.abspath('libs/thirdparty'))

sys.path.append(os.path.abspath('libs'))
sys.path.append(os.path.abspath('tests/omc'))
sys.path.append(os.path.abspath('tests/omc/rest'))
sys.path.append(os.path.abspath('tests/omc/rest/discovery'))
sys.path.append(os.path.abspath('tests/omc/rest/events'))
sys.path.append(os.path.abspath('tests/omm'))

import dellunit
from dellunit import build_report_json, report
logtime = time.strftime("%Y%m%d_%H%M%S")


def logfolder():
    config = ConfigParser.RawConfigParser()
    config.read(sys.argv[1])
    log_folder = str(config.get('dellunit', 'logfolder'))
    return log_folder

if __name__ == '__main__':
    prog = None

    try:
        print "System arguments is %s" % sys.argv
        prog = dellunit.TestProgram(logtime)
        jsonfile = ('report_%s.json'%logtime if (prog.timestamp_report == 1) else 'report.json')
        htmlfile = ('report_%s.html'%logtime if (prog.timestamp_report == 1) else 'report.html')
        JSON_FILE = os.path.abspath(os.path.join(logfolder(), jsonfile))
        REPORT_FILE = os.path.abspath(os.path.join(logfolder(), htmlfile))
    except:
        sys.stdout == sys.__stdout__
        sys.stderr == sys.__stderr__
        logging.exception('Fatal error during test, skipping report generation')
        os.chdir(current_dir)
        sys.exit(1)

    logging.info('Generating the report.json file')
    logging.info('Building report files')
    build_report_json.write_data(JSON_FILE, info=prog.info, logtime=logtime, timestamp_report=prog.timestamp_report)

    logging.info('Creating the report.html file')
    report.render_report(JSON_FILE, REPORT_FILE)

    if prog.mail_users:
        logging.info('Sending emails...')
        report.render_email(JSON_FILE, prog.mail_server, prog.mail_users)

    os.chdir(current_dir)
