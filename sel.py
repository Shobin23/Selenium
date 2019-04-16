from selenium import webdriver
import os
import time

class Run():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driverloca = "C:\\Users\\params4\\Downloads\\chromedriver_win32\\chromedriver.exe"

        os.environ["webdriver.chrome.driver"] = driverloca
        driver = webdriver.Chrome(driverloca)
        driver.get(baseUrl)

        # element_ID = driver.find_element_by_id("name")
        #
        # if element_ID is not None:
        #     print("We found the element element_ID")
        #
        # nelement_ID = driver.find_element_by_name("show-hide")
        #
        # if nelement_ID is not None:
        #     print("We found the element nelement_ID")

        # elemenxpath=driver.find_element_by_xpath("//input[@id='name']")
        # if elemenxpath is not None:
        #
        #     print("We found the element elemenxpath")
        #
        # elemencss = driver.find_element_by_css_selector("#displayed-text")
        # if elemencss is not None:
        #
        #     print("We found the element elemencss")
        #
        # elemenlink = driver.find_element_by_link_text("Login")
        # if elemenlink is not None:
        #
        #     print("We found the element elemenlink")
        #
        # elemenopartilink = driver.find_element_by_partial_link_text("Prac")
        # if elemenopartilink is not None:
        #     print("We found the element elemenopartilink")

        elemenclass = driver.find_element_by_class_name("displayed-class")
        elemenclass.send_keys("Hello")

        if elemenclass is not None:
            print("We found the element elemenopartilink")

        return driver



chromeTest = Run()
chromeTest.test()



