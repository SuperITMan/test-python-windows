from time import sleep 
from datetime import datetime 
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import glob
import os
import pandas as pd

prefs = {"download.default_directory" : os.getcwd(), 
         "download.prompt_for_download" : False
};

# Stored variables
url = "https://www.onlinedatagenerator.com/"

#Setting chrome web driver
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs);
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Open website
driver.get(url) 

# Insert username/password
driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/div/div/div/div[2]/div/div[2]/form/div[2]/div[3]/p/button').click()

#sleep(5)
print(os.getcwd())
print(os.listdir())
df = pd.read_csv('D:\\a\\automated-uploads\\automated-uploads\\test-folder\\ExportCSV.csv')
print(len(df))
