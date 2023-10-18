from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.important_page_questions_locators import ImportantQuestionsLocators


class ImportantQuestions:


    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru/"

    def go_to_important_questions_page(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ImportantQuestionsLocators.scooter_image))


    def scroll_to_important_question(self, index):
        element = self.driver.find_element(*ImportantQuestionsLocators.important_question[index])
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ImportantQuestionsLocators.important_question[index]))

    def click_important_question(self, index):
        self.scroll_to_important_question(index)
        self.driver.find_element(*ImportantQuestionsLocators.important_question[index]).click()

    def get_important_answer_text(self, index):
        return self.driver.find_element(*ImportantQuestionsLocators.important_answer[index]).text
