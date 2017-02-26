#Filename: 20170121_mdl_delisted.py
#Author: Rod Chubb


#Purpose: This script downloads delisted sites, sites which are 
#offline or have been cleaned, from mdl in txt format.

#Description: This script downloads delisted sites, sites which
#are offline or have been cleaned, from mdl in txt format. The 
#file name is created with the date, in YYYYMMDDHHMMSS format,
#prepended to "_mdl_delisted.txt"

#Target URL: http://www.malwaredomainlist.com/hostslist/delisted.txt

#Script usage is:
#"python 20170123_mdl_delisted.py"


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
mdl_delisted_filename_prefix = current_date_time() 
mdl_delisted_filename_base = "_mdl_delisted"
mdl_delisted_filename_suffix = ".txt"
mdl_delisted_filename_entire = mdl_delisted_filename_prefix + mdl_delisted_filename_base + mdl_delisted_filename_suffix
target_url = "http://www.malwaredomainlist.com/hostslist/delisted.txt"


#Script
mdl_delisted_request = requests.get(target_url)
mdl_delisted = mdl_delisted_request.text
open(mdl_delisted_filename_entire, "wb").write(mdl_delisted)
