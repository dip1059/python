from selenium import webdriver
from selenium.webdriver.common.by import By
try:
  driver  = webdriver.Chrome()
  driver.get('https://exchange-tradex.nftarttoken.xyz/markets')
  serachbox = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/ul/div[2]/div/input')
  serachbox.send_keys("USDT")
  btcbutton = driver.find_element(By.CSS_SELECTOR, '#react-tabs-1687 > div.MarketPage_section_tradeCodes__9Fgro > button:nth-child(4)')
  btcbutton.click()
except Exception as e:
  print(e)

input = input()
while(input != "done"):
  input = input()


