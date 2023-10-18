from selenium.webdriver.common.by import By


class HomePageLocators:

    order_button_in_header = [By.XPATH, "//button[1][@class = 'Button_Button__ra12g']"]
    order_button_in_content = [By.CLASS_NAME, 'Home_FinishButton__1_cWm']
    home_page_url = "https://qa-scooter.praktikum-services.ru/"
    scooter_image = [By.XPATH, "//img[@alt='Scooter blueprint']"]
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    cookie_consent = [By.ID, "rcc-confirm-button"]
