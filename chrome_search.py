from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
search = input('Search :')
search_string = search.replace(' ', '+') 
driver.get("https://stackoverflow.com/search?q=" + search_string)
# driver.find_element_by_class_name('yuRUbf').click()
input('press any key to exit')
driver.quit()
