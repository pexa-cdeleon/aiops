#!/usr/bin/env python3

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

print("Hello Python")
