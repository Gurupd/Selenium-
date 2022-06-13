from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path=r"C:\Users\pguru\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

firstname=driver.find_element_by_name("fName")
firstname.send_keys("Guru")

lastname=driver.find_element_by_name("lName")
lastname.send_keys("D")

email=driver.find_element_by_name("email")
email.send_keys("guru.link121@gmail.com")

submit=driver.find_element_by_css_selector("form button")
submit.click()