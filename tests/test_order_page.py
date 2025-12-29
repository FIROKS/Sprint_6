import allure
import pytest

from selenium import webdriver

from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import Endpoints


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
        orderPage = OrderPage(self.driver)
        mainPage = MainPage(self.driver)

        mainPage.go_to_page(Endpoints.MAIN_PAGE)
        mainPage.wait_for_load_main_page()
        orderPage.click_on_cookie_button()
        match enter_point:
            case 'nav':
                orderPage.click_on_order_in_nav()
            case 'section':
                orderPage.click_on_order_in_section()

        orderPage.wait_for_load_order_page()
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
        orderPage = OrderPage(self.driver)
        mainPage = MainPage(self.driver)
        orderPage.go_to_page(Endpoints.ORDER_PAGE)
        
        orderPage.wait_for_load_order_page()
        orderPage.click_on_scooter_logo()
        mainPage.wait_for_load_main_page()

        assert mainPage.get_current_url() == Endpoints.MAIN_PAGE

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
