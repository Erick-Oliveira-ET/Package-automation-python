from selenium import webdriver # Control the Chrome driver. Chrome driver isn't the same as Chrome Browser
from selenium.webdriver.common.keys import Keys #Simulate keyboard and mouse actions on the driver
PATH = r"C:\Program Files (x86)\chromedriver.exe" #r is just to avoid pylint warning

driver = webdriver.Chrome(PATH) #open a webdriver using the path to it

#waits for the event onload of the page fire. 
#however, if the page has a lot of AJAX this may not work properly
driver.get("http://www.correios.com.br/") #open the site in a new browser
searchInput = driver.find_element_by_xpath("//*[@id='objetos']") #find the search Input by xpath
searchInput.send_keys("pyconLB752676935SE") #"Type" this message on the searchInput
searchInput.send_keys(Keys.RETURN) #"Press" enter on the input

driver.close() #close the browser tab
