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

event_time=driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name=driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events={}
for n in range(len(event_name)):
     # Extrai o ano do atributo datetime
    year = event_time[n].get_attribute("datetime").split("-")[0]
    # Extrai a data do texto do elemento
    date = event_time[n].text
    events[n] = {
        "time": f"{year}-{date}",
        "name": event_name[n].text,
    }

print(events)

#driver.close()
driver.quit()


