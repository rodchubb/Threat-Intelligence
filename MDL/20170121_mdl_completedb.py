#Filename: 20170121_mdl_completedb.py
#Author: Rod Chubb


#Purpose: This script downloads the complete database from mdl
#in csv format.

#Description: This script downloads the complete database from
#mdl in csv format. The file name is created with the date, in
#YYYYMMDD prepended to 'mdl_completedb.csv'

#Target URL: http://www.malwaredomainlist.com/mdlcsv.php

#Script usage is:
#"python 20170121_mdl_completedb.py"


#Imports
import datetime
import requests
import sys


#utf-8
reload(sys)
sys.setdefaultencoding('utf-8')


#Functions
def current_date_time():
    current_date_time_object = datetime.datetime.now()
    current_date_time_string = current_date_time_object.strftime("%Y%m%d%H%M%S")
    return current_date_time_string


#Constants
mdl_completedb_filename_prefix = current_date_time() 
mdl_completedb_filename_base = "_mdl_completedb"
mdl_completedb_filename_suffix = ".csv"
mdl_completedb_filename_entire = mdl_completedb_filename_prefix + mdl_completedb_filename_base + mdl_completedb_filename_suffix
target_url = "http://www.malwaredomainlist.com/mdlcsv.php"


#Script
mdl_completedb_request = requests.get(target_url)
mdl_completedb = mdl_completedb_request.text
open(mdl_completedb_filename_entire, "wb").write(mdl_completedb)
