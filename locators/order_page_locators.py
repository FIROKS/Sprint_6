from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_input = (By.XPATH, '//input[@placeholder="* Имя"]')
    surname_input = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address_input = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro_select = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    phone_input = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    accept_button = (By.XPATH, '//button[text()="Далее"]')
    date_input = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    rental_input = (By.CLASS_NAME, 'Dropdown-control')
    comment_input = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    order_accept_button = (By.XPATH, '//button[text()="Да"]')
    order_number_popup = (By.XPATH, '//div[contains(text(), "Номер заказа:")]')