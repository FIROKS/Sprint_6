import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем загрузки страницы заказа')
    def wait_for_load_form(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.name_input))
        
    @allure.step('Вводим имя - {name}')
    def input_name(self, name):
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(name)

    @allure.step('Вводим фамилию - {surname}')
    def input_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.surname_input).send_keys(surname)

    @allure.step('Вводим адрес - {address}')
    def input_address(self, address):
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(address)

    @allure.step('Кликаем по селекту станции метро')
    def click_on_metro_input(self):
        self.driver.find_element(*OrderPageLocators.metro_select).click()

    @allure.step('Вводим название станции метро - {metro_option}')
    def click_on_metro_option(self, metro_option):
        self.driver.find_element(By.XPATH, f'//li[@data-value="{metro_option}"]/button[@value="{metro_option}"]').click()

    @allure.step('Вводим телефон - {phone}')
    def input_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.phone_input).send_keys(phone)

    @allure.step('Кликаем по кнопке "Далее"')
    def click_access_button(self):
        self.driver.find_element(*OrderPageLocators.accept_button).click()

    @allure.step('Кликаем по полю выбора даты')
    def click_date_input(self):
        self.driver.find_element(*OrderPageLocators.date_input).click()

    @allure.step('Выбираем {day} день в календаре')
    def click_date_picker(self, day):
        self.driver.find_element(By.XPATH, f'//div[text()="{day}"]').click()     

    @allure.step('Кликаем по селекту выбора срока аренды')
    def click_rental_period_select(self):
        self.driver.find_element(*OrderPageLocators.rental_input).click()

    @allure.step('Кликаем по варианту срока аренды - {period}')
    def click_rental_period_option(self, period):
        self.driver.find_element(By.XPATH, f'//div[text()="{period}"]').click()

    @allure.step('Кликаем по варианту цвета - {color}')
    def click_color_input(self, color):
        self.driver.find_element(By.XPATH, f'//input[@id="{color}"]').click()

    @allure.step('Заполняем поле комментария - "{comment}"')
    def fill_comment_input(self, comment):
        self.driver.find_element(*OrderPageLocators.comment_input).send_keys(comment)

    @allure.step('Кликнуть по кнопке оформления заказа')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    @allure.step('Ждем отрисовки попапа с подтверждением')
    def wait_for_order_accept_popup_load(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_all_elements_located(OrderPageLocators.order_accept_button))

    @allure.step('Кликнуть по кнопке подтверждения')
    def click_order_accept_button(self):
        self.driver.find_element(*OrderPageLocators.order_accept_button).click()

    @allure.step('Ждем отрисовки попапа с номером заказа')
    def wait_for_order_number_load(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_all_elements_located(OrderPageLocators.order_number_popup))
        return True
