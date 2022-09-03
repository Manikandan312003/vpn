from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
chrome_options=webdriver.ChromeOptions()
from selenium.webdriver.common.by import By

chrome_options.add_extension("vpn.crx")

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://www.1tamilmv.cyou/")

print_string = driver.find_element(By.XPATH, "/html/body").text
print(print_string)
input("Enter 1")

driver.close()
