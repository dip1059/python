from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio

async def run_chrome():
  try:
    print("chrome start...")
    driver  = webdriver.Chrome()
    try:
      driver.get('https://exchange-tradex.nftarttoken.xyz/markets')
      loginbtn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/header/div/div[3]/a[2]')
      await asyncio.sleep(10)
      print("chrome after sleep...")
      loginbtn.click()
      # serachbox = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/ul/div[2]/div/input')
      # serachbox.send_keys("USDT")
      # btcbutton = driver.find_element(By.CSS_SELECTOR, '#react-tabs-1687 > div.MarketPage_section_tradeCodes__9Fgro > button:nth-child(4)')
      # btcbutton.click()
    except Exception as e:
      print(e)

  except Exception as e:
    print(e)
    if driver:
      driver.quit()

async def run_firefox():
  try:
    print("firefox start...")
    driver  = webdriver.Firefox()
    try:
      driver.get('https://exchange-tradex.nftarttoken.xyz/markets')
      loginbtn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/header/div/div[3]/a[2]')
      await asyncio.sleep(10)
      print("firefox after sleep...")
      loginbtn.click()
      # serachbox = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/ul/div[2]/div/input')
      # serachbox.send_keys("USDT")
      # btcbutton = driver.find_element(By.CSS_SELECTOR, '#react-tabs-1687 > div.MarketPage_section_tradeCodes__9Fgro > button:nth-child(4)')
      # btcbutton.click()
    except Exception as e:
      print(e)

    # input_str = input()
    # while input_str != "exit":
    #   input_str = input()

  except Exception as e:
    print(e)
    if driver:
      driver.quit()

async def main():
  try:
    # asyncio.run(run_firefox())
    # asyncio.run(run_chrome())

    await asyncio.gather(run_firefox(), run_chrome())

  except Exception as e:
    print(e)

  input_str = input()
  while input_str != "exit":
    input_str = input()

if __name__ == "__main__":
  asyncio.run(main())