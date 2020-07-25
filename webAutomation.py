from selenium import webdriver # Control the Chrome driver. Chrome driver isn't the same as Chrome Browser
from selenium.webdriver.common.keys import Keys #Simulate keyboard and mouse actions on the driver
import time

class webAutomation:
    def __init__(self):
        self.PATH = r"C:\Program Files (x86)\chromedriver.exe" #r is just to avoid pylint warning

    def search(self, product_code):
        #Option to open Chrome without opening the display
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        driver = webdriver.Chrome(self.PATH, options=op) #open a webdriver using the path to it

        #waits for the event onload of the page fire. 
        #however, if the page has a lot of AJAX this may not work properly
        driver.get("https://www2.correios.com.br/sistemas/rastreamento/resultado.cfm") #open the site in a new browser
        
        try:
            assert "home" in driver.title
            assert "No results found." not in driver.page_source
            
            searchInput = driver.find_element_by_xpath("//*[@id='objetos']") #find the search Input by xpath
            searchInput.send_keys(product_code) #"Type" this message on the searchInput
            searchInput.send_keys(Keys.RETURN) #"Press" enter on the input

            #search for the latest info about the package
            process = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[4]/table[1]")
            print(process.text)
            

        except AssertionError as identifier:
            print("Essa página não está disponível no momento. Tente mais tarde.")
            print(f"Error: {identifier}")

        driver.close() #close the browser tab
