from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Setup:
    def driver_setup(self):
        ## driver setup
        def __init__(self, driver):
            self.driver = driver

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://18.209.122.163/admin/dashboard")

        ## find title name
        print(driver.title)

        ## login into the system
        email = driver.find_element_by_name("email")
        password = driver.find_element_by_name("password")
        email.send_keys("superadmin@gmail.com")
        password.send_keys("superadmin")
        login = driver.find_element_by_class_name("btn-primary")
        login.click()


        ##click on catalogue
        catalogue = driver.find_element_by_xpath("/html/body/div/div/nav/ul/li[3]/a")
        catalogue.click()





