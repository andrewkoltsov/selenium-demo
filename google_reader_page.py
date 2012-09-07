'''
Created on 03.08.2012

@author: avkoltsov
'''
from google_reader_selectors import GoogleReaderSelectors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime

WAIT_FOR_SUBSCRIPTION_LOAD = 3

class GoogleReaderPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        
    def open_page(self):
        self.driver.get('https://www.google.com/reader/')
        
    def get_element(self, locator):
        '''
        throws exception if element not found
        '''
        selector_type , selector = locator.split('=', 1)
        
        element = None
        
        if 'id' == selector_type:
            element = self.driver.find_element(by=By.ID, value=selector)
        elif 'xpath' == selector_type:
            element = self.driver.find_element(by=By.XPATH, value=selector)
        elif 'link_text' == selector_type:
            element = self.driver.find_element(by=By.LINK_TEXT, value=selector)
        elif 'partial_link_text' == selector_type:
            element = self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=selector)
        elif 'name' == selector_type:
            element = self.driver.find_element(by=By.NAME, value=selector)
        elif 'tag' == selector_type:
            element = self.driver.find_element(by=By.TAG_NAME, value=selector)
        elif 'class' == selector_type:
            element = self.driver.find_element(by=By.CLASS_NAME, value=selector)
        elif 'css' == selector_type:
            element = self.driver.find_element(by=By.CSS_SELECTOR, value=selector)
        
        return element
        
    def get_elements(self, locator):
        selector_type , selector = locator.split('=', 1)
        
        elements = []
        
        if 'id' == selector_type:
            elements = self.driver.find_elements(by=By.ID, value=selector)
        elif 'xpath' == selector_type:
            elements = self.driver.find_elements(by=By.XPATH, value=selector)
        elif 'link_text' == selector_type:
            elements = self.driver.find_elements(by=By.LINK_TEXT, value=selector)
        elif 'partial_link_text' == selector_type:
            elements = self.driver.find_elements(by=By.PARTIAL_LINK_TEXT, value=selector)
        elif 'name' == selector_type:
            elements = self.driver.find_elements(by=By.NAME, value=selector)
        elif 'tag' == selector_type:
            elements = self.driver.find_elements(by=By.TAG_NAME, value=selector)
        elif 'class' == selector_type:
            elements = self.driver.find_elements(by=By.CLASS_NAME, value=selector)
        elif 'css' == selector_type:
            elements = self.driver.find_elements(by=By.CSS_SELECTOR, value=selector)
            
        return elements 
    
    def get_subscriptions(self):
        return self.get_elements(GoogleReaderSelectors.subscriptions)
    
    def get_entries(self):
        return self.get_elements(GoogleReaderSelectors.entries)
    
    def open_subscription(self, webelement):
        webelement.click()
        webelement.click()
        self.wait_spinner_is_visible()
        
    def scroll_entries_down(self):
        last = self.get_entries()[-1]
        while True:
            body = self.get_element('tag=body')
            body.send_keys(Keys.PAGE_DOWN)
            self.wait_spinner_is_visible()
            new_last =  self.get_entries()[-1]
            if last._id == new_last._id:
                break
            last = new_last
            
    def get_date(self, entry):
        date_as_str = entry.find_element_by_class_name('entry-date').text
        entry_date = None
        
        try:
            entry_date = datetime.strptime(date_as_str, '%d.%m.%Y').date()
        except:
            entry_date = datetime.now().date()
        
        return entry_date
        
        
    def wait_spinner_is_visible(self, time_to_wait = WAIT_FOR_SUBSCRIPTION_LOAD):
        try:
            WebDriverWait(self.driver, time_to_wait).\
                until(lambda x: self.get_element(GoogleReaderSelectors.spinner).is_displayed(),
                      'subscrption load too long, more then %s seconds' % time_to_wait)
            WebDriverWait(self.driver, time_to_wait).\
                until(lambda x: not self.get_element(GoogleReaderSelectors.spinner).is_displayed(),
                      'subscrption load too long, more then %s seconds' % time_to_wait)
        except:
            pass
