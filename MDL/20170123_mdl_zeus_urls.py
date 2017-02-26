#Filename: 20170121_mdl_zeus_urls.py
#Author: Rod Chubb


#Purpose: This script downloads the list of zeus urls provided 
#by mdl in csv format.

#Description: This script downloads the list of zeus urls provided
#by mdl in csv format. The file name is created with the date, in 
#YYYYMMDDHHMMSS format, prepended to "_mdl_zeus_urls.csv"

#Target URL: http://www.malwaredomainlist.com/zeuscsv.php

#Script usage is:
#"python 20170123_mdl_zeus_urls.py"


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
mdl_zeus_urls_filename_prefix = current_date_time() 
mdl_zeus_urls_filename_base = "_mdl_zeus_urls"
mdl_zeus_urls_filename_suffix = ".csv"
mdl_zeus_urls_filename_entire = mdl_zeus_urls_filename_prefix + mdl_zeus_urls_filename_base + mdl_zeus_urls_filename_suffix
target_url = "http://www.malwaredomainlist.com/zeuscsv.php"


#Script
mdl_zeus_urls_request = requests.get(target_url)
mdl_zeus_urls = mdl_zeus_urls_request.text
open(mdl_zeus_urls_filename_entire, "wb").write(mdl_zeus_urls)
