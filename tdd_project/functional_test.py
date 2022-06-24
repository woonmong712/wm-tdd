from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localholst:8000')

assert 'Django' in browser.title
