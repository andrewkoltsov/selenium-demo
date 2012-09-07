'''
Created on 02.08.2012

@author: avkoltsov
'''
from browser import Browser
from datetime import date
from google_reader_page import GoogleReaderPage


if __name__ == '__main__':
    driver = None
    articles_to_read = []
    earliest_date = date.today()
    try:
#       
        driver = Browser.getFF()
                
        page = GoogleReaderPage(driver)
        page.open_page()
        
        lis = page.get_subscriptions()
        for li in lis:
            if  li.is_displayed():
                
                page.open_subscription(li)
                page.scroll_entries_down()
                entries = page.get_entries()
                
                entries.reverse()
                early_enrty_date = page.get_date(entries[0])
                print '%s (%s) %s' % (li.text, len(entries), early_enrty_date)
                 
                if early_enrty_date < earliest_date:
                    earliest_date = early_enrty_date
                    articles_to_read = []
                
                if early_enrty_date == earliest_date:
                    for entry in entries:
                        enrty_date = page.get_date(entry)
                        if enrty_date == early_enrty_date:                                    
                            articles_to_read.append(entry.text)
                        else:
                            break
    finally:
        driver.quit()
        print '=' * 80
        for article in articles_to_read:
            print article