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
import path
import pandas as pd

from driver_builder import DriverBuilder

prefs = {"download.default_directory" : os.getcwd(), 
         "download.prompt_for_download" : False
};

# Stored variables
url = "https://www.onlinedatagenerator.com/"


driver_builder = DriverBuilder()
download_path = path.dirname(path.realpath(__file__))
expected_download = path.join(download_path, "ExportCSV.csv")

# clean downloaded file
try:
   remove(expected_download)
except OSError:
   pass

assert (not path.isfile(expected_download))

driver = driver_builder.get_driver(download_path, headless=True)

# Open website
driver.get(url) 

# Insert username/password
driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/div/div/div/div[2]/div/div[2]/form/div[2]/div[3]/p/button').click()

self.wait_until_file_exists(expected_download, 30)
driver.close()

assert (path.isfile(expected_download))

print("done")

print(os.getcwd())
print(os.listdir())
df = pd.read_csv(os.getcwd()+'ExportCSV.csv')
print(len(df))

def wait_until_file_exists(self, actual_file, wait_time_in_seconds=5):
    waits = 0
    while not path.isfile(actual_file) and waits < wait_time_in_seconds:
        print("sleeping...." + str(waits))
        sleep(.5)  # make sure file completes downloading
        waits += .5

