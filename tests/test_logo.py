import allure
from pages.home_page import HomePage


class TestLogo:

    @allure.title("Логотип Яндекс ведет на Dzen Page")
    @allure.description('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная '
                        'страница Дзена.')
    def test_open_dzen_page(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        home_page.consent_cookies()
        home_page.click_yandex_logo()
        redirected_url = home_page.get_redirected_url()
        assert "https://dzen.ru/" in redirected_url, "Redirection to Yandex failed!"

    @allure.title("Логотип Scooter редиректит на https://qa-scooter.praktikum-services.ru/ ")
    @allure.description('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        home_page.consent_cookies()
        home_page.click_scooter_logo()
        assert 'https://qa-scooter.praktikum-services.ru/' in home_page.get_current_url()
