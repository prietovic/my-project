from selenium import webdriver  # hay que haber ejecutado `pip install selenium` para que funcione la importación
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\99GU3945\\workspaces\\test-lab\\chromedriver.exe')

driver.get("https://the-internet.herokuapp.com/tables")

filas = driver.find_elements(By.CSS_SELECTOR, "#table1 > tbody > tr")

max_due = 0
max_name = ""

for fila in filas:
    info_lista = fila.text.split()
    name = info_lista[0]
    due = float(info_lista[3][1:])
    if due > max_due:
        max_due = due
        max_name = name

print (max_name + '/n' + str(max_due))