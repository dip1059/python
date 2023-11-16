from selenium import webdriver
from selenium.webdriver.common.by import By
from login import do_login
import time
import constants as consts
from datetime import datetime, timedelta

def click_redeem(driver: webdriver.Chrome or webdriver.Firefox): 
  btnConfirm=driver.find_element(By.XPATH, '/html/body/div[4]/div/div[6]/button[1]')
  btnConfirm.click()

def reedem_giftcard(driver: webdriver.Chrome or webdriver.Firefox, target_timestamp: float = -1):
  url = consts.BASE_URL+'gift-cards/my-cards'
  do_login(driver, url)
  time.sleep(consts.COMMON_SLEEP_SEC)

  driver.execute_script("window.scrollBy(0, 5000)")
  time.sleep(consts.COMMON_SLEEP_SEC)
  myGiftTemplate=driver.find_element(By.XPATH,"//div[@class='GiftCards_section_item__Dbanm']")
  myGiftTemplate.click()
  time.sleep(consts.COMMON_SLEEP_SEC)

  btnReedem=driver.find_element(By.XPATH,"//button[normalize-space()='Redeem']")
  btnReedem.click()
  time.sleep(consts.COMMON_SLEEP_SEC)

  while True:
    if datetime.now().timestamp() >= target_timestamp:
      click_redeem(driver)
      print("clicked at: ", datetime.now())
      print("clicked at: ", datetime.now().timestamp())
      break


  


