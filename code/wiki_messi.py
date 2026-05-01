from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


Url = "https://fr.wikipedia.org"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(Url)
time.sleep(2)
search = driver.find_element(By.NAME, "search")
search.send_keys("Lionel Messi")
search.send_keys(Keys.RETURN)
time.sleep(2)
table_clubs = driver.find_elements(By.CSS_SELECTOR, "table.fstats")

for table in table_clubs:
	table = table.text
	print(table)


time.sleep(40)




