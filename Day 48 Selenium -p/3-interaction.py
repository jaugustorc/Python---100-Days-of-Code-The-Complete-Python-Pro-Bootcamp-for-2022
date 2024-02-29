from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#navigate
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#Hone in on anchor tag using CSS selectors
article_cont=driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#article_cont.click()

# Find elemnt by Link Text
all_portals=driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()

# Find the "search" <input> by NAME
search=driver.find_element(By.NAME, value="search")
search.send_keys("Python",Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)
#search.send_keys(Keys.ENTER)

#bt=driver.find_element(By.CLASS_NAME, value="cdx-button cdx-search-input__end-button")
#bt.Click()


#driver.close()
#driver.quit()
