from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the (fake) newsletter registration page
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
end_time = time.time() + 60*60  # 5 minutes

while True:
    cookie.click()

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > end_time:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break