from selenium.webdriver.common.by import By


class ScooterOrderPageLocators:
    name_field = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_field = [By.CSS_SELECTOR, ".select-search"]
    metro_element = [By.XPATH, "//button[@value='30']"]
    phone_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    order_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    order_form = [By.CLASS_NAME, 'Order_Content__bmtHS']
    date_field = [By.XPATH, "//div[@class='react-datepicker__input-container']"]
    delivery_date = [By.XPATH, "//div[@aria-label='Choose вторник, 31-е октября 2023 г.']"]
    rental_field = [By.CLASS_NAME, "Dropdown-placeholder"]
    dropdown_menu = [By.CLASS_NAME, 'Dropdown-menu']
    rental_period = [By.XPATH, "//div[contains(text(),'четверо суток')]"]
    scooter_color_checkbox = [By.CLASS_NAME, "Order_Checkboxes__3lWSI"]
    comments_field = [By.XPATH, "//div[@class='Order_Form__17u6u']//div[@class='Input_InputContainer__3NykH']//input["
                                "@type='text']"]
    confirm_order_popup = [By.CLASS_NAME, "Order_Modal__YZ-d3"]
    yes_button_on_popup = [By.XPATH, "//button[contains(text(), 'Да')]"]
    success_popup = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
    next_button = [By.CLASS_NAME, "Button_Middle__1CSJM"]
