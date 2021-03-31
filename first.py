from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("https://google.co.in")
time.sleep(1)

input_element = driver.find_element_by_name("q")
input_element.send_keys("test automation")

script_text = "var searchButton = document.getElementsByName(\"btnK\")[1]; searchButton.click();"
try:
    driver.execute_script(script_text)  # if it work, an alert with 'yes' should display
except:
    pass
time.sleep(2)

results_div = driver.find_element_by_id('rso')
results = results_div.find_elements_by_class_name("g")

for result in results:
    text_link = result.find_element_by_tag_name('h3')
    if "automation" in text_link.text.lower():
        link = result.find_element_by_tag_name('a')
        link.click()
        break
