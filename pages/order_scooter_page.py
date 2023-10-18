from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_scooter_page_locators import ScooterOrderPageLocators

class ScooterOrderPage:


    def __init__(self, driver):
        self.driver = driver

    def click_order_button(self):
        self.driver.find_element(*ScooterOrderPageLocators.order_button).click()

    def wait_for_order_form(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(ScooterOrderPageLocators.order_form))

    def set_name(self, name):
        self.driver.find_element(*ScooterOrderPageLocators.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*ScooterOrderPageLocators.surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*ScooterOrderPageLocators.address_field).send_keys(address)

    def select_metro_station(self):
        self.driver.find_element(*ScooterOrderPageLocators.metro_field).click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(ScooterOrderPageLocators.metro_element))
        element.click()


    def set_phone(self, phone):
        self.driver.find_element(*ScooterOrderPageLocators.phone_field).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*ScooterOrderPageLocators.next_button).click()

    def select_delivery_time(self):
        self.driver.find_element(*ScooterOrderPageLocators.date_field).click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(ScooterOrderPageLocators.delivery_date))

        self.driver.find_element(*ScooterOrderPageLocators.delivery_date).click()

    def select_rental_period(self):
        self.driver.find_element(*ScooterOrderPageLocators.rental_field).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ScooterOrderPageLocators.dropdown_menu))
        self.driver.find_element(*ScooterOrderPageLocators.rental_period).click()

    def select_scooter_color(self):
        scooter_color_checkbox = self.driver.find_element(*ScooterOrderPageLocators.scooter_color_checkbox)
        scooter_color_checkbox.click()

    def set_comments(self, comments):
        element = self.driver.find_element(*ScooterOrderPageLocators.comments_field)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.send_keys(comments)


    def confirm_order(self):
        self.click_order_button()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(ScooterOrderPageLocators.confirm_order_popup))
        self.driver.find_element(*ScooterOrderPageLocators.yes_button_on_popup).click()
        wait.until(EC.visibility_of_element_located(ScooterOrderPageLocators.success_popup))
