from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome('C:\\Users\\fernando.prieto\\workspaces\\test-lab\\chromedriver.exe')
driver = webdriver.Chrome('C:\\Users\\99GU3945\\workspaces\\test-lab\\chromedriver.exe')

try:
    driver.maximize_window()

    driver.get("https://www.eltiempo.es/madrid.html")

    texto_temperatura = driver.find_element(By.CSS_SELECTOR,".c-tib-text")

    temperatura = int(texto_temperatura.text[:-1])

    assert 0 < temperatura < 2

except Exception:
    driver.save_screenshot("temp/Screenshot.png")
    raise
finally:
    driver.quit()

