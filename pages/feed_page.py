import allure
from pages.base_page import BasePage
from locators.feed_locators import OrderFeedLocators
from urls import URLs


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Открытие ленты заказов')
    def open_order_feed(self):
        self.open_page(URLs.ORDER_FEED)
    
    @allure.step('Проверка отображения ленты заказов')
    def is_order_feed_displayed(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_FEED_TITLE)
    
    @allure.step('Получение счётчика "Выполнено за всё время"')
    def get_total_orders_count(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_ORDERS))
    
    @allure.step('Получение счётчика "Выполнено за сегодня"')
    def get_today_orders_count(self):
        return int(self.get_text(OrderFeedLocators.TODAY_ORDERS))
    
    @allure.step('Проверка наличия заказа в разделе "В работе"')
    def is_order_in_progress(self, order_number):
        self.wait_element_visible(OrderFeedLocators.IN_PROGRESS_ORDERS)
        elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDERS)
        for element in elements:
            if element.text == order_number:
                return True
        return False