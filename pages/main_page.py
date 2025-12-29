import allure

from selenium.webdriver.common.by import By


class MainPage:
    question_accordion = (By.CLASS_NAME, 'accordion')
    cookie_button = (By.ID, 'rcc-confirm-button')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по кнопке согласия с cookie')
    def click_on_cookie_button(self):
        try:
            self.driver.find_element(*self.cookie_button).click()
        except Exception:
            pass

    @allure.step('Кликаем по элементу с вопросом')
    def click_on_accordion_item(self, item):
        self.driver.find_element(*item).click()
