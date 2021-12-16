from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\fernando.prieto\\workspaces\\test-lab\\chromedriver.exe')

try:
    driver.get("https://www3.animeflv.net/")
    link=driver.find_element(By.CSS_SELECTOR, "a[href*='one piece']*")
    link.click()


