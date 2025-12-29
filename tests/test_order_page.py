import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.order_page import OrderPage
from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Успешное оформление заказа')
    @allure.description('Оформление заказа с корректными данными')
    @allure.testcase('-', 'Заказ самоката')
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, day, period, color, comment, enter_point",
        [
            ('Иван', 'Иванов', 'ул. Пушкина, 67', '1', '88888888888', '10', 'сутки', 'black', 'Комментарий', 'nav'),
            ('Федор', 'Васильев', 'ул. Новогодняя, 26', '2', '88005553535', '31', 'двое суток', 'grey', '', 'section'),
        ]
    )
    def test_order_success(self, name, surname, address, metro, phone, day, period, color, comment, enter_point):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        orderPage = OrderPage(self.driver)
        basePage = BasePage(self.driver)

        basePage.wait_for_load_page(MainPage.question_accordion)
        basePage.click_on_cookie_button()
        match enter_point:
            case 'nav':
                basePage.click_on_order_in_nav()
            case 'section':
                basePage.click_on_order_in_section()

        orderPage.wait_for_load_form()
        orderPage.input_name(name)
        orderPage.input_surname(surname)
        orderPage.input_address(address)
        orderPage.click_on_metro_input()
        orderPage.click_on_metro_option(metro)
        orderPage.input_phone(phone)
        orderPage.click_access_button()
        orderPage.click_date_input()
        orderPage.click_date_picker(day)
        orderPage.click_rental_period_select()
        orderPage.click_rental_period_option(period)
        orderPage.click_color_input(color)
        orderPage.fill_comment_input(comment)
        orderPage.click_order_button()
        orderPage.wait_for_order_accept_popup_load()
        orderPage.click_order_accept_button()
        orderPage.wait_for_order_number_load()
        
        assert True, 'Не удалось оформить заказ'

    @allure.title('Переход на главную при клике на логотип "Самоката"')
    @allure.testcase('-', 'Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_go_to_main_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        basePage = BasePage(self.driver)
        
        basePage.wait_for_load_page(OrderPageLocators.name_input)
        basePage.click_on_scooter_logo()
        basePage.wait_for_load_page(MainPage.question_accordion)

        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Открытие страницы Дзена при клике на логотип Яндекса')
    @allure.testcase('-', 'Если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_go_to_main_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru')
        basePage = BasePage(self.driver)
        
        basePage.wait_for_load_page(MainPage.question_accordion)
        basePage.click_on_yandex_logo()
        self.driver.switch_to.window(self.driver.window_handles[1])
        basePage.wait_for_load_page((By.XPATH, '//div[contains(@class, "dzen")]'))

        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true', 'Страница Дзена не открылась через редирект'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
