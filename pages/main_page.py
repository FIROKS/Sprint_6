import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    question_accordion = (By.CLASS_NAME, 'accordion')
    cookie_button = (By.ID, 'rcc-confirm-button')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по элементу с вопросом')
    def click_on_accordion_item(self, selector):
        super().click_on_element(selector)
        
    @allure.step('Ждем загрузки главной страницы')
    def wait_for_load_main_page(self):
        super().wait_for_load(self.question_accordion)
