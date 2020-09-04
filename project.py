from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

#driver.get("https://www.google.com")
#gmail = driver.find_element_by_link_text("Gmail")

search = driver.find_element_by_id("gsc-i-id1")
search.send_keys("facebook")
search.send_keys(Keys.RETURN)

#search_results = driver.find_element_by_class_name("gsc-wrapper")
#print(search_results.text)

#gmail.click()

try:
    search_result = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gsc-wrapper"))
   )
    print(search_result.text)
except:
   driver.quit()