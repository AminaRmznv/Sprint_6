from pages.home_page import HomePage
from pages.order_scooter_page import ScooterOrderPage
from locators.order_scooter_page_locators import ScooterOrderPageLocators
import allure


class TestScooterOrderPage:

    @allure.description('Заказ самоката. Проверить флоу позитивного сценария нажав на кнопку «Заказать» вверху страницы')
    def test_positive_scooter_order_with_button_in_header(self, driver):
        home_page = HomePage(driver)


        home_page.go_to_home_page()

        home_page.consent_cookies()

        home_page.click_order_button_in_header()

        order_page = ScooterOrderPage(driver)

        order_page.wait_for_order_form()

        order_page.set_name("Миша")

        order_page.set_surname("Полянкин")

        order_page.set_address("Улица Солнечная, дом 5")

        order_page.select_metro_station()

        order_page.set_phone("12345678901")

        order_page.click_next_button()

        order_page.wait_for_order_form()

        order_page.select_delivery_time()

        order_page.select_rental_period()

        order_page.select_scooter_color()

        order_page.set_comments("Очень жду")

        order_page.confirm_order()

        assert "Заказ оформлен" in driver.find_element(*ScooterOrderPageLocators.success_popup).text

    @allure.description(
        'Заказ самоката. Проверить флоу позитивного сценария нажав на кнопку «Заказать» внизу страницы')
    def test_positive_scooter_order_with_button_in_content(self, driver):
        home_page = HomePage(driver)

        home_page.go_to_home_page()

        home_page.consent_cookies()

        home_page.click_order_button_in_content()

        order_page = ScooterOrderPage(driver)

        order_page.wait_for_order_form()

        order_page.set_name("Миша")

        order_page.set_surname("Полянкин")

        order_page.set_address("Улица Солнечная, дом 5")

        order_page.select_metro_station()

        order_page.set_phone("12345678901")

        order_page.click_next_button()

        order_page.wait_for_order_form()

        order_page.select_delivery_time()

        order_page.select_rental_period()

        order_page.select_scooter_color()

        order_page.set_comments("Очень жду")

        order_page.confirm_order()

        assert "Заказ оформлен" in driver.find_element(*ScooterOrderPageLocators.success_popup).text
