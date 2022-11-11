from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv, find_dotenv
import os

# Loads the environmental variables 
load_dotenv(find_dotenv())

# Specifies the port that will be set on the command line
opts = Options()
opts.add_experimental_option("debuggerAddress", "localhost:9250")

# This is the path where crome driver has been downloaded and installed from https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(os.getenv('CHROME_DRIVER_PATH'), chrome_options=opts)
driver.get("http://gmail.com")
