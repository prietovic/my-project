from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\fernando.prieto\\workspaces\\test-lab\\chromedriver.exe')

driver.get("https://www3.animeflv.net/")
link = driver.find_elements_by_css_selector("a[href*='one piece']*")
link.click()


