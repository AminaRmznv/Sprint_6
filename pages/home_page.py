from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators

class HomePage:



    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get(HomePageLocators.home_page_url)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(HomePageLocators.scooter_image))

    def consent_cookies(self):
        self.driver.find_element(*HomePageLocators.cookie_consent).click()

    def click_order_button_in_header(self):
        self.driver.find_element(*HomePageLocators.order_button_in_header).click()

    def click_order_button_in_content(self):
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(HomePageLocators.order_button_in_content))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_scooter_logo(self):
        self.driver.find_element(*HomePageLocators.scooter_logo).click()

    def click_yandex_logo(self):
        self.driver.find_element(*HomePageLocators.yandex_logo).click()
