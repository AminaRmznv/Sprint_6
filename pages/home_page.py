from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure


class HomePage(BasePage):

    home_page_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step(f"Перейти на главную страницу сайта")
    def go_to_home_page(self):
        self.go_to_site(HomePage.home_page_url)
        self.wait_for_element_present(HomePageLocators.scooter_image)

    @allure.step("Дать согласие на использование файлов cookie")
    def consent_cookies(self):
        self.click_element(HomePageLocators.cookie_consent)

    @allure.step("Нажать на кнопку 'Заказать' в заголовке")
    def click_order_button_in_header(self):
        self.click_element(HomePageLocators.order_button_in_header)

    @allure.step("Нажать на кнопку 'Заказать' в контенте")
    def click_order_button_in_content(self):
        self.wait_for_element_present(HomePageLocators.order_button_in_content)
        self.scroll_to_element(HomePageLocators.order_button_in_content)
        self.click_element(HomePageLocators.order_button_in_content)

    @allure.step("Нажать на логотип 'Самоката'")
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.scooter_logo)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(HomePageLocators.yandex_logo)

    @allure.step("Прокрутить к важному вопросу: {index}")
    def scroll_to_important_question(self, index):
        self.scroll_to_element(HomePageLocators.important_question[index])

    @allure.step("Нажать на важный вопрос: {index}")
    def click_important_question(self, index):
        self.click_element(HomePageLocators.important_question[index])

    @allure.step("Получить текст важного ответа: {index}")
    def get_important_answer_text(self, index):
        return self.get_element_text(HomePageLocators.important_answer[index])

    @allure.step("перейти на новую вкладку https://dzen.ru/")
    def get_redirected_url(self):
        self.switch_to_new_window()
        self.wait_for_url_to_contain("https://dzen.ru/")
        return self.get_current_url()
