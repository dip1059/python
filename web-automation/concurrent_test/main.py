from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from gift_card import reedem_giftcard
from login import do_login
import constants as consts

def start():
  print("start at: ", datetime.now())
  try:
    driver = webdriver.Firefox()
    
    try:
      target_timetamp = datetime(2023, 11, 17, 00, 19, 0).timestamp()
      reedem_giftcard(driver, target_timetamp)
    except Exception as e:
      print(e)
    
    input_str = input()
    while input_str != "exit":
      input_str = input()
    
    driver.quit()

  except Exception as e:
    print(e)
    if driver:
      driver.quit()

def main():
  start()

if __name__ == "__main__":
  main()
  # asyncio.run(main())