from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.realcanadiansuperstore.ca/")
time.sleep(3)

search_bar_job = driver.find_element("id","autocomplete-listbox-desktop-site-header-")
search_bar_job.send_keys("Orange")
time.sleep(3)

search_bar_job.send_keys(Keys.RETURN)
time.sleep(3)

scroll = driver.find_element("xpath", "/html/body/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div[4]/p")
driver.execute_script('arguments[0].scrollIntoView(true)',scroll)
time.sleep(3)

item = driver.find_element("xpath", "/html/body/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div[5]/div/ul/li[1]/div/div/div[2]/div/button")
item.click()
time.sleep(5)

select_item = driver.find_element("xpath","/html/body/div[3]/div/div[6]/div[2]/div/div/div/div/div/div[2]/div[5]/div/div[2]/button")
select_item.click()
time.sleep(3)

deliver_confirm = driver.find_element(By.CLASS_NAME, "fulfillment-mode-confirm-auto-localization__actions__confirm")
deliver_confirm.click()
time.sleep(20)

checkout1 = driver.find_element(By.CSS_SELECTOR, ".checkout-button.checkout-button--menu-bar")
checkout1.click()
time.sleep(10)

scroll2 = driver.find_element("xpath", "/html/body/div[3]/div/div[2]/main/div/div[2]/div[2]/div/div[1]/div[3]/div/div[3]/p")
driver.execute_script('arguments[0].scrollIntoView(true)',scroll2)
time.sleep(3)

checkout2 = driver.find_element(By.CLASS_NAME, "mkt-proceed-to-checkout__button")
checkout2.click()
time.sleep(6)

driver.close()