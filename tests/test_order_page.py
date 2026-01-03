import allure
import pytest

from selenium import webdriver

from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import Endpoints, ORDERDATA


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Успешное оформление заказа')
    @allure.description('Оформление заказа с корректными данными')
    @allure.testcase('-', 'Заказ самоката')
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, day, period, color, comment",
        ORDERDATA
    )
    def test_order_success(self, name, surname, address, metro, phone, day, period, color, comment):
        orderPage = OrderPage(self.driver)
        mainPage = MainPage(self.driver)

        mainPage.go_to_page(Endpoints.MAIN_PAGE)
        mainPage.wait_for_load_main_page()
        orderPage.click_on_cookie_button()
        orderPage.click_on_order_in_nav()
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
        success_popup_button_text = orderPage.wait_for_order_success_popup()
        
        assert success_popup_button_text == 'Посмотреть статус', 'Не удалось оформить заказ'

    def test_go_to_order_page_using_section_button(self):
        orderPage = OrderPage(self.driver)
        mainPage = MainPage(self.driver)
    
        mainPage.go_to_page(Endpoints.MAIN_PAGE)
        mainPage.wait_for_load_main_page()
        orderPage.click_on_cookie_button()
        orderPage.click_on_order_in_section()
        orderPage.wait_for_load_order_page()

        assert orderPage.get_current_url() == Endpoints.ORDER_PAGE

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
