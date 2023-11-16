from selenium import webdriver
from selenium.webdriver.common.by import By
# import asyncio
from datetime import datetime, timedelta

def click_login_btn(driver: webdriver.Firefox):
  loginbtn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/header/div/div[3]/a[2]')
  loginbtn.click()

def run_firefox():
  try:
    print("firefox start...")
    driver  = webdriver.Firefox()
    try:
      driver.get('https://exchange-tradex.nftarttoken.xyz')

      target_datetime = datetime(2023, 11, 16, 16, 49, 0)
      while True:
        if datetime.now() >= target_datetime:
          click_login_btn()
          print("clicked at: ", datetime.now())
          print("clicked at: ", datetime.now().timestamp())
          break
        timedelta(seconds=1)
      
      # loginbtn.click()
      # print("clicked at: ", datetime.now())

      # serachbox = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/ul/div[2]/div/input')
      # serachbox.send_keys("USDT")
      # btcbutton = driver.find_element(By.CSS_SELECTOR, '#react-tabs-1687 > div.MarketPage_section_tradeCodes__9Fgro > button:nth-child(4)')
      # btcbutton.click()
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
  run_firefox()

if __name__ == "__main__":
  main()
  # asyncio.run(main())