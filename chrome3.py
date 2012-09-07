'''
Created on 02.08.2012

@author: avkoltsov
'''
from browser import Browser
from google_reader_page import GoogleReaderPage

if __name__ == '__main__':
    driver = None
    try:
        driver = Browser.getFF()
        page = GoogleReaderPage(driver)
        page.open_page()
        
        lis = page.get_subscriptions()
        for li in lis:
            if  li.is_displayed():
                print li.text
    finally:
        driver.quit()