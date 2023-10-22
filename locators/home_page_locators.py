from selenium.webdriver.common.by import By


class HomePageLocators:

    order_button_in_header = [By.XPATH, "//button[1][@class = 'Button_Button__ra12g']"]
    order_button_in_content = [By.CLASS_NAME, 'Home_FinishButton__1_cWm']
    scooter_image = [By.XPATH, "//img[@alt='Scooter blueprint']"]
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    cookie_consent = [By.ID, "rcc-confirm-button"]
    important_question = [
        (By.ID, 'accordion__heading-0'),
        (By.ID, 'accordion__heading-1'),
        (By.ID, 'accordion__heading-2'),
        (By.ID, 'accordion__heading-3'),
        (By.ID, 'accordion__heading-4'),
        (By.ID, 'accordion__heading-5'),
        (By.ID, 'accordion__heading-6'),
        (By.ID, 'accordion__heading-7')
    ]
    important_answer = [
        (By.ID, 'accordion__panel-0'),
        (By.ID, 'accordion__panel-1'),
        (By.ID, 'accordion__panel-2'),
        (By.ID, 'accordion__panel-3'),
        (By.ID, 'accordion__panel-4'),
        (By.ID, 'accordion__panel-5'),
        (By.ID, 'accordion__panel-6'),
        (By.ID, 'accordion__panel-7')
    ]
