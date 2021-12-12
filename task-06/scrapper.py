from selenium import webdriver
from pathlib import Path

url='https://trends.google.com/trends/?geo=IN'

path=Path('C:/Users/rahul/Downloads/chromedriver')

driver=webdriver.Chrome(executable_path=path)
driver.get(url)

_check=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/ng-include/div/examples/div/div/div[2]/a[1]/trends-widget/ng-include/widget/div/div/div[1]/div[2]')

print(_check.text)
driver.close()