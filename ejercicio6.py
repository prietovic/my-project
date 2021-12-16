from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\fernando.prieto\\workspaces\\test-lab\\chromedriver.exe')

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

botonAdd = driver.find_element(By.CSS_SELECTOR,"#content > div > button")

for i in range(20):
    botonAdd.click()

# for i in range(20):
#     botonDelete = driver.find_element(By.CSS_SELECTOR, "#elements > button:nth-child(1)")
#     botonDelete.click()

deleteButtons = driver.find_elements(By.CSS_SELECTOR, "#elements > button")

while len(deleteButtons) > 0:
    deleteButtons[0].click()
    deleteButtons = driver.find_elements(By.CSS_SELECTOR, "#elements > button")