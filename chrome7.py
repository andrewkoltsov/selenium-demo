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

                page.open_subscription(li)
                page.scroll_entries_down()
                entries = page.get_entries()
                
                entries.reverse()
                last_enrty_date = page.get_date(entries[0])
                print '%s (%s) %s' % (li.text, len(entries), last_enrty_date)
                                                 
    finally:
        driver.quit()