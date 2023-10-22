import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import allure


@pytest.fixture
@allure.title("Prepare for the test")
def driver():
    service = GeckoDriverManager().install()
    browser = webdriver.Firefox(service=Service(service))

    yield browser
    browser.quit()