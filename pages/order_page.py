import allure

from selenium.webdriver.common.by import By

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем загрузки страницы заказа')
    def wait_for_load_order_page(self):
        super().wait_for_load(OrderPageLocators.name_input)
        
    @allure.step('Вводим имя - {name}')
    def input_name(self, name):
        super().fill_input(OrderPageLocators.name_input, name)

    @allure.step('Вводим фамилию - {surname}')
    def input_surname(self, surname):
        super().fill_input(OrderPageLocators.surname_input, surname)

    @allure.step('Вводим адрес - {address}')
    def input_address(self, address):
        super().fill_input(OrderPageLocators.address_input, address)

    @allure.step('Кликаем по селекту станции метро')
    def click_on_metro_input(self):
        super().click_on_element(OrderPageLocators.metro_select)

    @allure.step('Вводим название станции метро - {metro_option}')
    def click_on_metro_option(self, metro_option):
        super().click_on_element((By.XPATH, f'//li[@data-value="{metro_option}"]/button[@value="{metro_option}"]'))

    @allure.step('Вводим телефон - {phone}')
    def input_phone(self, phone):
        super().fill_input(OrderPageLocators.phone_input, phone)

    @allure.step('Кликаем по кнопке "Далее"')
    def click_access_button(self):
        super().click_on_element(OrderPageLocators.accept_button)

    @allure.step('Кликаем по полю выбора даты')
    def click_date_input(self):
        super().click_on_element(OrderPageLocators.date_input)

    @allure.step('Выбираем {day} день в календаре')
    def click_date_picker(self, day):
        super().click_on_element((By.XPATH, f'//div[text()="{day}"]'))   

    @allure.step('Кликаем по селекту выбора срока аренды')
    def click_rental_period_select(self):
        super().click_on_element(OrderPageLocators.rental_input)

    @allure.step('Кликаем по варианту срока аренды - {period}')
    def click_rental_period_option(self, period):
        super().click_on_element((By.XPATH, f'//div[text()="{period}"]'))

    @allure.step('Кликаем по варианту цвета - {color}')
    def click_color_input(self, color):
        super().click_on_element((By.XPATH, f'//input[@id="{color}"]'))

    @allure.step('Заполняем поле комментария - "{comment}"')
    def fill_comment_input(self, comment):
        super().fill_input(OrderPageLocators.comment_input, comment)

    @allure.step('Кликнуть по кнопке оформления заказа')
    def click_order_button(self):
        super().click_on_element(OrderPageLocators.order_button)

    @allure.step('Ждем отрисовки попапа с подтверждением')
    def wait_for_order_accept_popup_load(self):
        super().wait_for_load(OrderPageLocators.order_accept_button)

    @allure.step('Кликнуть по кнопке подтверждения')
    def click_order_accept_button(self):
        super().click_on_element(OrderPageLocators.order_accept_button)

    @allure.step('Ждем отрисовки попапа с номером заказа')
    def wait_for_order_number_load(self):
        super().wait_for_load(OrderPageLocators.order_number_popup)
        return True
