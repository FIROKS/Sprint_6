import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from data import Endpoints, QUESTIONS_DATA
from pages.main_page import MainPage


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка текста для вопроса "{question}" на соответствие')
    @allure.description('')
    @allure.testcase('-', 'Выпадающий список в разделе «Вопросы о важном»')
    @pytest.mark.parametrize(
        'heading_count, panel_count, expected_answer, question',
        QUESTIONS_DATA
    )
    def test_check_cost_question(self, heading_count, panel_count, expected_answer, question):
        heading_id = f'accordion__heading-{heading_count}'
        accordion_panel = (By.XPATH, f'//*[@id="accordion__panel-{panel_count}"]/p')
        mainPage = MainPage(self.driver)

        mainPage.go_to_page(Endpoints.MAIN_PAGE)
        mainPage.wait_for_load_main_page()
        mainPage.click_on_cookie_button()
        mainPage.click_on_accordion_item((By.ID, heading_id))
        answer = mainPage.get_element_text(accordion_panel)
        
        assert answer == expected_answer

        
    @allure.title('Открытие страницы Дзена при клике на логотип Яндекса')
    @allure.testcase('-', 'Если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_go_to_main_page(self):
        mainPage = MainPage(self.driver)
        
        mainPage.go_to_page(Endpoints.MAIN_PAGE)
        mainPage.wait_for_load_main_page()
        mainPage.click_on_yandex_logo()
        mainPage.switch_to_window(1)
        mainPage.wait_for_load_dzen()

        assert mainPage.get_current_url() == Endpoints.DZEN_PAGE, 'Страница Дзена не открылась через редирект'


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
