from selenium import webdriver
from time import sleep

ruta_driver = "/home/jose/Descargas/chromedriver_linux64/chromedriver" #Ruta al driver de Chrome
driver = webdriver.Chrome(ruta_driver)

driver.get("https://myablecity.herokuapp.com/")
driver.find_element_by_xpath('//*[@id="invitado"]').click()
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/button[1]').click()
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/button/img').click()

sleep(2)
list_e = [elemen for elemen in driver.find_elements_by_class_name('tamanio')]
list_w = [words.text for words in list_e]
print(list_w)