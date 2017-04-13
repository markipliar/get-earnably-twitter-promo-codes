from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path=r'/home/hang/Documents/geckodriver')

browser.get('http://www.google.com')