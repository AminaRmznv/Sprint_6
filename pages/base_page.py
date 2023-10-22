from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.click()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator),
                                                    message=f'Not find {locator}')

    def send_keys(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator), message=f'Not find {locator}')
        element.send_keys(text)

    def get_element_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def wait_for_element_present(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def wait_for_url_to_contain(self, text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.url_contains(text))