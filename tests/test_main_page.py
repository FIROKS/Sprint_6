import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from data import MainPageQuestions
from pages.main_page import MainPage
from pages.base_page import BasePage


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title('Проверка текста для вопроса "{question}" на соответствие')
    @allure.description('')
    @allure.testcase('-', 'Выпадающий список в разделе «Вопросы о важном»')
    @pytest.mark.parametrize(
        'heading_count, panel_count, expected_answer, question',
        [
            (0, 0, MainPageQuestions.ANSWERS['COST'], MainPageQuestions.QUESTIONS['COST']),
            (1, 1, MainPageQuestions.ANSWERS['SEVERAL_SCOOTERS'], MainPageQuestions.QUESTIONS['SEVERAL_SCOOTERS']),
            (2, 2, MainPageQuestions.ANSWERS['RENTAL_TIME'], MainPageQuestions.QUESTIONS['RENTAL_TIME']),
            (3, 3, MainPageQuestions.ANSWERS['ORDER_FOR_TODAY'], MainPageQuestions.QUESTIONS['ORDER_FOR_TODAY']),
            (4, 4, MainPageQuestions.ANSWERS['EXTEND_OR_RETURN'], MainPageQuestions.QUESTIONS['EXTEND_OR_RETURN']),
            (5, 5, MainPageQuestions.ANSWERS['CHARGING_DELIVERY'], MainPageQuestions.QUESTIONS['CHARGING_DELIVERY']),
            (6, 6, MainPageQuestions.ANSWERS['CANCEL_ORDER'], MainPageQuestions.QUESTIONS['CANCEL_ORDER']),
            (7, 7, MainPageQuestions.ANSWERS['OUTSIDE_MRR'], MainPageQuestions.QUESTIONS['OUTSIDE_MRR']),
        ]
    )
    def test_check_cost_question(self, heading_count, panel_count, expected_answer, question):
        heading_id = f'accordion__heading-{heading_count}'
        accordion_panel = (By.XPATH, f'//*[@id="accordion__panel-{panel_count}"]/p')

        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        mainPage = MainPage(self.driver)
        basePage = BasePage(self.driver)

        basePage.wait_for_load_page(mainPage.question_accordion)
        mainPage.click_on_cookie_button()
        mainPage.click_on_accordion_item((By.ID, heading_id))

        answer = self.driver.find_element(*accordion_panel).text
        
        assert answer == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
