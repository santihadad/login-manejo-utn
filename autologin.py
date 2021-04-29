from selenium import webdriver
from getpass import getpass
import time

username = "72586@industrial.frc.utn.edu.ar"
password = "p@nd@461"

driver = webdriver.Edge('C:\\WebDriver\\msedgedriver.exe')
driver.get('https://uv.frc.utn.edu.ar/login/index.php')

usuario_web = driver.find_element_by_id("username")
contraseña_web = driver.find_element_by_id("password")

usuario_web.send_keys(username)
contraseña_web.send_keys(password)

login_button = driver.find_element_by_id("loginbtn")
login_button.submit()

driver.implicitly_wait(10)
entrar_aula_manejo = driver.find_element_by_link_text("2021-5D1-1-547 2021-5D1(1) Manejo de Materiales y Distribución de Plantas")
entrar_aula_manejo.click()

driver.implicitly_wait(10)
asistencia = driver.find_element_by_link_text("Asistencia")
asistencia.click()

#Colocar presente
driver.implicitly_wait(10)
enviar_asistencia = driver.find_element_by_link_text("Enviar asistencia")
enviar_asistencia.click()

#Radio Button
presente = driver.find_element_by_xpath("//*[@id='id_status_17749']")
presente.click()

#Guardar cambios y cerrar todo
guardar_cambios = driver.find_element_by_xpath("//*[@id='id_submitbutton']")
guardar_cambios.click()
time.sleep(3)
driver.close()
