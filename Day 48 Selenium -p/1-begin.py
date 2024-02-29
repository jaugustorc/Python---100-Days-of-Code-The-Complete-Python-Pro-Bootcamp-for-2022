from selenium import webdriver
from selenium.webdriver.common.by import By

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

#test 1
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# value=driver.find_element(By.CLASS_NAME, value="a-offscreen")
# print(value.text)

#test 2
driver.get("https://www.python.org")
value=driver.find_element(By.NAME, value="q")
print(value.tag_name)
print(value.get_attribute("placeholder"))
value=driver.find_element(By.ID, value="submit")
print(value.size)
value=driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(value.text)
value=driver.find_element(By.XPATH, value="/html/body/div/footer/div[1]/div/ul/li[1]/ul/li[3]/a")
print(value.text)


#driver.close()
driver.quit()


