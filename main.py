from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
chrome_options=webdriver.ChromeOptions()
CHROMEDRIVER_PATH="/app/.chromedriver/bin/chromedriver"
chrome_bin=os.environ.get('GOOGLE_CHROME_SHIM',None)
chrome_options.binary_location=chrome_bin
from selenium.webdriver.common.by import By


chrome_options.add_extension("vpn.crx")

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://www.1tamilmv.cyou/")

print_string = driver.find_element(By.XPATH, "/html/body").text
print(print_string)
input("Enter 1")

driver.close()
