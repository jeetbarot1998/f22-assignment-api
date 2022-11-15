# Q3
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import requests as req
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Method 1: Using selenium to open the page and scrap data.

# Selenium Webdriver configuration
url = "https://www.iplt20.com/stats/2021/most-runs"
CHROMEDRIVER_PATH = './chromedriver_107.exe'

options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
driver.get(url)

headers = driver.find_elements_by_xpath('//table/tbody/tr/th')

mat_value = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[3]')
Inns = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[4]')
NO = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[5]')
Runs = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[6]')
HS = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[7]')
Avg = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[8]')
BF = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[9]')
SR = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[10]')
hundred = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[11]')
fifty = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[12]')
fours = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[13]')
sixes = driver.find_elements_by_xpath('//div[@id="battingTAB"]/table/tbody/tr/td[14]')

final_data_set = []

for each_val in range(len(mat_value)):
    each_entry = {
        'Mat': mat_value[each_val].text,
        'Inns': Inns[each_val].text,
        'NO': NO[each_val].text,
        'Runs': Runs[each_val].text,
        'HS': HS[each_val].text,
        'Avg': Avg[each_val].text,
        'BF': BF[each_val].text,
        'SR': SR[each_val].text,
        'hundred': hundred[each_val].text,
        'fifty': fifty[each_val].text,
        'fours': fours[each_val].text,
        'sixes': sixes[each_val].text
    }
    final_data_set.append(each_entry)

data_frame = pd.DataFrame(final_data_set)
print(data_frame)
data_frame.to_excel('ipl_scraped_data.xlsx', index=False)


# Method 2:
# I looked up in network tabs and found an external api call which is used to populate the table.
# Using Request Module to perform "GET" on the same URL to fetch the data
# URL: https://ipl-stats-sports-mechanic.s3.ap-south-1.amazonaws.com/ipl/feeds/stats/60-toprunsscorers.js?callback=ontoprunsscorers&_=1668094754381
data = req.get('https://ipl-stats-sports-mechanic.s3.ap-south-1.amazonaws.com/ipl/feeds/stats/60-toprunsscorers.js?callback=ontoprunsscorers&_=1668094754381')
d = data.text.replace('(','').replace(')','').replace('ontoprunsscorers','').replace(';','')
d = json.loads(d)

final_data_set = []
for each_val in d['toprunsscorers']:
    try:

        each_entry = {
            # "StrikerName" : each_val["StrikerName"],
            'Mat': each_val["Innings"],
            'Inns': each_val["Innings"],
            'NO': each_val["NotOuts"],
            'Runs': each_val["TotalRuns"],
            'HS': each_val["HighestScore"],
            'Avg': each_val["BattingAverage"],
            'BF': each_val["Balls"],
            'SR': each_val["StrikeRate"],
            'hundred': each_val["Centuries"],
            'fifty': each_val["FiftyPlusRuns"],
            'fours': each_val["Fours"],
            'sixes': each_val["Sixes"]
        }
        final_data_set.append(each_entry)
    except Exception as err:
        print('error at ',err)

data_frame = pd.DataFrame(final_data_set)
print(data_frame)
data_frame.to_excel('ipl_scraped_data_direct.xlsx', index=False)