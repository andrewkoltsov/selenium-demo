'''
Created on 02.08.2012

@author: avkoltsov
'''
from browser import Browser
from google_reader_page import GoogleReaderPage

from time import sleep

if __name__ == '__main__':
    driver = None
    try:
        driver = Browser.getFF()
        page = GoogleReaderPage(driver)
        page.open_page()
        
        sleep(3)
    finally:
        driver.quit()