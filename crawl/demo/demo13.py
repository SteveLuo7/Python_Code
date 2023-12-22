from lxml import etree
from selenium import webdriver
driver = webdriver.Chrome()
url = "https://www.huya.com/g/lol"
driver.get(url)
names = driver.find_elements_by_class_name("nick")

counts = driver.find_elements_by_class_name("js-num")

for name,count in zip(names,counts):
    print(name,":",count)

driver.quit()