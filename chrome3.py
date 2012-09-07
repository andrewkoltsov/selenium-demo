'''
Created on 02.08.2012

@author: avkoltsov
'''
from selenium import webdriver

from google_reader_page import GoogleReaderPage

if __name__ == '__main__':
    driver = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=C:/Documents and Settings/akoltsov/Local Settings/Application Data/Google/Chrome/User Data/Default')
        driver = webdriver.Chrome(chrome_options=options);
        
        page = GoogleReaderPage(driver)
        page.open_page()
        
        lis = page.get_subscriptions()
        for li in lis:
            if  li.is_displayed():
                print li.text
    finally:
        driver.quit()