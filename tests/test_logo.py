from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from pages.home_page import HomePage


class TestLogo:

    @allure.description('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_open_dzen_page(self, driver):
        home_page = HomePage(driver)

        home_page.go_to_home_page()

        home_page.consent_cookies()

        current_window = driver.current_window_handle

        home_page.click_yandex_logo()

        for window_handle in driver.window_handles:
            if window_handle != current_window:
                driver.switch_to.window(window_handle)
                break

        WebDriverWait(driver, 10).until(EC.url_contains("https://dzen.ru/"))

        assert "https://dzen.ru/" in driver.current_url

        driver.close()

        driver.switch_to.window(current_window)

    @allure.description(
        'Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        home_page.consent_cookies()
        home_page.click_scooter_logo()
        assert 'https://qa-scooter.praktikum-services.ru/' in driver.current_url
