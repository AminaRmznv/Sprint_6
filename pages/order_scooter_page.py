from locators.order_scooter_page_locators import ScooterOrderPageLocators
from pages.base_page import BasePage
import allure


class ScooterOrderPage(BasePage):

    @allure.step("Нажать на кнопку 'Заказать'")
    def click_order_button(self):
        self.click_element(ScooterOrderPageLocators.order_button)

    @allure.step("Ожидать появление формы заказа")
    def wait_for_order_form(self):
        self.wait_for_element_present(ScooterOrderPageLocators.order_form)

    @allure.step("Установить имя: {1}")
    def set_name(self, name):
        self.send_keys(ScooterOrderPageLocators.name_field, name)

    @allure.step("Установить фамилию: {1}")
    def set_surname(self, surname):
        self.send_keys(ScooterOrderPageLocators.surname_field, surname)

    @allure.step("Установить адрес: {1}")
    def set_address(self, address):
        self.send_keys(ScooterOrderPageLocators.address_field, address)

    @allure.step("Выбрать станцию метро")
    def select_metro_station(self):
        self.click_element(ScooterOrderPageLocators.metro_field)
        self.click_element(ScooterOrderPageLocators.metro_element)

    @allure.step("Установить номер телефона: {1}")
    def set_phone(self, phone):
        self.send_keys(ScooterOrderPageLocators.phone_field, phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_element(ScooterOrderPageLocators.next_button)

    @allure.step("Выбрать время доставки")
    def select_delivery_time(self):
        self.click_element(ScooterOrderPageLocators.date_field)
        self.click_element(ScooterOrderPageLocators.delivery_date)

    @allure.step("Выбрать период аренды")
    def select_rental_period(self):
        self.click_element(ScooterOrderPageLocators.rental_field)
        self.click_element(ScooterOrderPageLocators.rental_period)

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self):
        self.click_element(ScooterOrderPageLocators.scooter_color_checkbox)

    @allure.step("Установить комментарии: {1}")
    def set_comments(self, comments):
        self.scroll_to_element(ScooterOrderPageLocators.comments_field)
        self.send_keys(ScooterOrderPageLocators.comments_field, comments)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_order_button()
        self.wait_for_element_present(ScooterOrderPageLocators.confirm_order_popup)
        self.click_element(ScooterOrderPageLocators.yes_button_on_popup)

    @allure.step("Получить текст успешного сообщения из всплывающего окна")
    def get_success_text_from_popup(self):
        return self.get_element_text(ScooterOrderPageLocators.success_popup)
