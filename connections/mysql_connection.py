import os
import smtplib
import pymysql
import ssl
import traceback
import sys

def connection():
    try:
        conn = pymysql.connect(host=os.environ['host'],
                               # port = 3306,
                               user=os.environ['user'],
                               passwd=os.environ['passwd'],
                               db=os.environ['db'])
        return conn
    except Exception as err_msg: 
        for frame in traceback.extract_tb(sys.exc_info()[2]): 
            fname, lineno, fn, text = frame 
            print(f"Error in creating connection object for mysql {text} on line {lineno} with error as {err_msg} ")

