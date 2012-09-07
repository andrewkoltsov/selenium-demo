'''
Created on 02.08.2012

@author: avkoltsov
'''
from browser import Browser
from time import sleep

if __name__ == '__main__':
    driver = None
    try:
        driver = Browser.getFF()
        driver.get('https://www.google.com/reader/')
        sleep(3)
    finally:
        driver.quit()