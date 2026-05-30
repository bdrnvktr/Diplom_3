import pytest
import allure
from locators.locators import FLUORESCENT_BUN, BEEF_METEORITE
from pages.main_page import MainPage
from pages.feed_page import FeedPage
import time


@allure.feature("Лента заказов")
class TestFeed:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.feed_page = FeedPage(driver)  # При создании FeedPage произойдёт автоматический логин

    @allure.story("Проверка счётчиков заказов")
    @allure.title("Счётчик «Выполнено за всё время» увеличивается после оформления заказа")
    def test_total_orders_counter_increases_after_order(self):
        """Проверяет, что счётчик «Выполнено за всё время» увеличивается после оформления заказа"""
        # Получаем начальное значение счётчика
        self.main_page.go_to_feed()
        initial_total = self.feed_page.get_total_orders_count()

        # Создаём заказ: переходим в конструктор, добавляем ингредиенты, оформляем заказ
        self.main_page.go_to_constructor()
        self.main_page.add_bun_to_basket()  # Добавляем булочку
        self.main_page.switch_to_fillings_tab()
        self.main_page.add_beef_meteorite_to_basket()  # Добавляем начинку

        # Используем метод create_order для оформления заказа — он сам кликнет по кнопке и дождётся модального окна
        order_number = self.main_page.create_order()

        # Закрываем модальное окно
        self.main_page.close_order_modal()

        # Переходим в ленту заказов
        self.main_page.go_to_feed()

        # Получаем новое значение счётчика и проверяем, что оно увеличилось
        final_total = self.feed_page.get_total_orders_count()
        assert final_total > initial_total, (
            f"Счётчик 'Выполнено за всё время' не увеличился: было {initial_total}, стало {final_total}"
        )

    @allure.story("Проверка счётчиков заказов")
    @allure.title("Счётчик «Выполнено за сегодня» увеличивается после оформления заказа")
    def test_today_orders_counter_increases_after_order(self):
        """Проверяет, что счётчик «Выполнено за сегодня» увеличивается после оформления заказа"""
        # Получаем начальное значение счётчика
        self.main_page.go_to_feed()
        initial_today = self.feed_page.get_today_orders_count()

        # Создаём заказ
        self.main_page.go_to_constructor()
        self.main_page.add_bun_to_basket()  # Добавляем булочку
        self.main_page.switch_to_fillings_tab()
        self.main_page.add_beef_meteorite_to_basket()  # Добавляем начинку

        # Оформляем заказ через create_order
        order_number = self.main_page.create_order()

        # Закрываем модальное окно
        self.main_page.close_order_modal()

        # Переходим в ленту заказов
        self.main_page.go_to_feed()

        # Получаем новое значение счётчика и проверяем, что оно увеличилось
        final_today = self.feed_page.get_today_orders_count()
        assert final_today > initial_today, (
            f"Счётчик 'Выполнено за сегодня' не увеличился: было {initial_today}, стало {final_today}"
        )

    @allure.story("Отображение заказов в ленте")
    @allure.title("Заказ появляется в разделе «В работе» после оформления")
    def test_order_appears_in_current_orders_after_creation(self):
        """Проверяет, что после оформления заказа его номер появляется в разделе «В работе»"""
        # Создаём заказ
        self.main_page.go_to_constructor()
        self.main_page.add_bun_to_basket()  # Добавляем булочку
        self.main_page.switch_to_fillings_tab()
        self.main_page.add_beef_meteorite_to_basket()  # Добавляем начинку

        # Оформляем заказ и получаем номер
        order_number = self.main_page.create_order().strip()

        # Закрываем модальное окно
        self.main_page.close_order_modal()

        # Переходим в ленту заказов
        self.main_page.go_to_feed()
        time.sleep(15)
        # Получаем список текущих заказов
        current_orders = self.feed_page.get_current_orders()

        # Проверяем, что список не пуст (заказ появился)
        assert len(current_orders) > 0, "В разделе 'В работе' нет заказов после оформления"

        # Проверяем, что в списке текущих заказов есть номер созданного заказа
        clean_order_number = order_number.lstrip('0') if order_number.startswith('0') else order_number
        order_found = any(clean_order_number in order for order in current_orders)
        assert order_found, f"Номер заказа {order_number} не найден в списке текущих заказов: {current_orders}"
