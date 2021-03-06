#!/usr/bin/env python
#Filename: 20170123_abuse.ch_ransomwaretracker.py
#Author: Rod Chubb


#Purpose: This script downloads the ransomeware feed published by 
#abuse.ch in csv format.

#Description: This script downloads the ransomware feed published by
#abuse.ch in csv format. The file name is created with the date, in 
#YYYYMMDDHHMMSS format, prepended to "_abuse.ch_ransomwaretracker"

#Target URL: http://ransomwaretracker.abuse.ch/feeds/csv/

#Script Usage:
#"python 20170123_abuse.ch_ransomwaretracker.py"


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
abuse_ch_ransomwaretracker_filename_prefix = current_date_time()
abuse_ch_ransomwaretracker_filename_base = "_abuse_ch_ransomwaretracker"
abuse_ch_ransomwaretracker_filename_suffix = ".csv"
abuse_ch_ransomwaretracker_filename_entire = abuse_ch_ransomwaretracker_filename_prefix + abuse_ch_ransomwaretracker_filename_base + abuse_ch_ransomwaretracker_filename_suffix
target_url = "http://ransomwaretracker.abuse.ch/feeds/csv/"


#Script
abuse_ch_ransomwaretracker_request = requests.get(target_url)
abuse_ch_ransomwaretracker = abuse_ch_ransomwaretracker_request.text
open(abuse_ch_ransomwaretracker_filename_entire, "wb").write(abuse_ch_ransomwaretracker)
