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

    def wait_for_load(self, selector):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(selector))

    def click_on_element(self, selector):
        self.driver.find_element(*selector).click()
        
    def fill_input(self, selector, value):
        self.driver.find_element(*selector).send_keys(value)

    def get_element_text(self, selector):
        return self.driver.find_element(*selector).text
    
    def get_current_url(self):
        return self.driver.current_url
    
    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def wait_for_load_dzen(self):
        self.wait_for_load((By.XPATH, '//div[contains(@class, "dzen")]'))
    
    @allure.step('Переходим на страницу - {endpoint}')
    def go_to_page(self, endpoint):
        self.driver.get(endpoint)
    
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
