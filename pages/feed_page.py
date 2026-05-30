from locators.locators import (
    TOTAL_COUNTER,
    TODAY_COUNTER,
    CURRENT_ORDER_ITEMS,
    LOGIN_ACCOUNT_BUTTON,
    LOGIN_EMAIL_FIELD,
    LOGIN_PASSWORD_FIELD,
    LOGIN_BUTTON,
    ORDER_FEED_HEADER
)
from .base_page import BasePage
from .main_page import MainPage


class FeedPage(BasePage):
    def _login(self):
        """Выполняет вход в аккаунт с тестовыми данными"""
        self.click_element(LOGIN_ACCOUNT_BUTTON)

        # Вводим email
        email_field = self.find_element(LOGIN_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys("budarin42@mail.ru")

        # Вводим пароль
        password_field = self.find_element(LOGIN_PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys("123456")

        # Нажимаем кнопку входа
        self.click_element(LOGIN_BUTTON)

    def __init__(self, driver):
        super().__init__(driver)
        # Сначала убираем возможные модальные окна
        main_page = MainPage(driver)
        main_page.ensure_modal_closed()
        # Теперь безопасно выполняем логин
        self._login()

    def get_total_orders_count(self):
        """Получение количества заказов за всё время"""
        return int(self.get_text(TOTAL_COUNTER))

    def get_today_orders_count(self):
        """Получение количества заказов за сегодня"""
        return int(self.get_text(TODAY_COUNTER))

    def get_current_orders(self):
        """Получение списка текущих заказов"""
        orders = self.driver.find_elements(*CURRENT_ORDER_ITEMS)
        return [order.text for order in orders]

    def verify_feed_header_is_displayed(self):
        """Проверяет, что заголовок ленты заказов отображается"""
        return self.is_element_visible(ORDER_FEED_HEADER)
