from selenium import webdriver
from dotenv import load_dotenv, find_dotenv
import os

# Loads environmental variables 
load_dotenv(find_dotenv())

# CHROME_PATH would be somthing like "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(executable_path=os.getenv('CHROME_PATH'))
