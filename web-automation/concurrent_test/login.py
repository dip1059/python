from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import constants as consts
import time

def do_login(driver: webdriver.Chrome or webdriver.Firefox, url = consts.BASE_URL+'login'):
  driver.get(url)
  time.sleep(consts.COMMON_SLEEP_SEC)

  txtEmail=driver.find_element(By.XPATH,"//input[@id='email']")
  txtPassword=driver.find_element(By.XPATH,"//input[@id='password']")
  btnLogin=driver.find_element(By.XPATH,"//button[normalize-space()='Login']")

  txtEmail.send_keys(consts.USER_EMAIL)
  txtPassword.send_keys(consts.USER_PASS)
  btnLogin.click()


