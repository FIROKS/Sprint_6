import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    scooter_logo = (By.XPATH, '//a[@href="/"]')
    yandex_logo = (By.XPATH, '//a[@href="//yandex.ru"]')
    order_button_in_nav = (By.XPATH, '//div[starts-with(@class, "Header_Nav")]/button[text()="Заказать"]')
    order_button_in_section = (By.XPATH, '//div[starts-with(@class, "Home_RoadMap")]/div/button[text()="Заказать"]')
    cookie_button = (By.ID, 'rcc-confirm-button')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по кнопке согласия с cookie')
    def click_on_cookie_button(self):
        try:
            self.driver.find_element(*self.cookie_button).click()
        except Exception:
            pass

    @allure.step('Ждем загрузки страницы')
    def wait_for_load_page(self, selector):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(selector))
        
    @allure.step('Кликаем по кнопке "Заказать" в шапке')
    def click_on_order_in_nav(self):
        self.driver.find_element(*self.order_button_in_nav).click()

    @allure.step('Кликаем по кнопке "Заказать" в секции "Как это работает"')
    def click_on_order_in_section(self):
        self.driver.find_element(*self.order_button_in_section).click()
        
    @allure.step('Кликаем по лого "Самоката"')
    def click_on_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()
        
    @allure.step('Кликаем по лого Яндекса')
    def click_on_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()
        