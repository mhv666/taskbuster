# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
 
class NewVisitorTest(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.browser.implicitly_wait(3)   
    def test_it_worked(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.driver.title)
    def tearDown(self):
        self.driver.close()

 
if __name__ == '__main__':
    unittest.main()