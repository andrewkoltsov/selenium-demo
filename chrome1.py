'''
Created on 02.08.2012

@author: avkoltsov
'''
from selenium import webdriver
from time import sleep

if __name__ == '__main__':
    driver = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=C:/Documents and Settings/akoltsov/Local Settings/Application Data/Google/Chrome/User Data/Default')
        driver = webdriver.Chrome(chrome_options=options);
        driver.get('https://www.google.com/reader/')
        sleep(3)
    finally:
        driver.quit()