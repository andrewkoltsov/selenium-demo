# -*- coding: utf-8 -*-
'''
Created on 07.09.2012

@author: Андрей
'''
from selenium import webdriver

class Browser(object):

    @classmethod
    def getFF(cls):
        options = webdriver.FirefoxProfile('c:/selenium_ff_profile')
        driver = webdriver.Firefox(options)
        return driver
    
    @classmethod
    def getIE(cls):
        return webdriver.Ie()
    
    @classmethod
    def getGC(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=C:/Documents and Settings/akoltsov/Local Settings/Application Data/Google/Chrome/User Data/Default')
        driver = webdriver.Chrome(chrome_options=options)
        return driver