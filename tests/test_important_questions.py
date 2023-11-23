import pytest
import allure
from pages.home_page import HomePage


expected_answers = [
    "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
    "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать "
    "несколько заказов — один за другим.",
    "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды "
    "начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда "
    "закончится 9 мая в 20:30.",
    "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
    "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
    "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без "
    "передышек и во сне. Зарядка не понадобится.",
    "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
    "Да, обязательно. Всем самокатов! И Москве, и Московской области."
]


class TestImportantQuestions:
    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    @allure.description('проверить: когда нажимаешь на стрелочку, открывается соответствующий текст')
    @pytest.mark.parametrize("index, expected_answer", enumerate(expected_answers))
    def test_important_question_answers(self, driver, index, expected_answer):
        questions_page = HomePage(driver)
        questions_page.go_to_home_page()
        questions_page.consent_cookies()
        questions_page.scroll_to_important_question(index)
        questions_page.click_important_question(index)
        actual_answer = questions_page.get_important_answer_text(index)
        assert actual_answer == expected_answer, f"Expected '{expected_answer}', but got '{actual_answer}'"
