from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/brave'
browser = webdriver.Chrome(options=options)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
