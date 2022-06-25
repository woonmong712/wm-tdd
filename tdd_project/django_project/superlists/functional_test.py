from selenium import webdriver

browser = webdriver.Firefox()
# browser.get('http://127.0.0.1:8000/')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
