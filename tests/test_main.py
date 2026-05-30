import pytest
import allure
from locators.locators import (
    BURGER_BUILDER_HEADER,
    ORDER_FEED_HEADER,
    INGREDIENT_DETAILS_HEADER,
    BEEF_METEORITE_IN_BASKET
)
from pages.main_page import MainPage


@allure.feature("Основные разделы приложения")
class TestMain:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_page = MainPage(driver)

    @allure.story("Навигация")
    @allure.title("Переход в раздел «Конструктор»")
    def test_go_to_constructor(self):
        """Проверка перехода в раздел «Конструктор»"""
        self.main_page.go_to_feed()
        self.main_page.go_to_constructor()
        assert self.main_page.is_element_visible(BURGER_BUILDER_HEADER), "Не удалось перейти в раздел «Конструктор»"

    @allure.story("Навигация")
    @allure.title("Переход в раздел «Лента заказов»")
    def test_go_to_order_feed(self):
        """Проверка перехода в раздел «Лента заказов»"""
        self.main_page.go_to_feed()
        assert self.main_page.is_element_visible(ORDER_FEED_HEADER), "Не удалось перейти в раздел «Лента заказов»"

    @allure.story("Работа с ингредиентами")
    @allure.title("Открытие модального окна с деталями ингредиента")
    def test_open_ingredient_details(self):
        """Проверка открытия модального окна с деталями ингредиента"""
        self.main_page.go_to_constructor()
        self.main_page.switch_to_fillings_tab()
        self.main_page.open_ingredient_details()
        assert self.main_page.is_element_visible(INGREDIENT_DETAILS_HEADER), "Модальное окно с деталями ингредиента не открылось"

    @allure.story("Работа с модальными окнами")
    @allure.title("Закрытие модального окна кликом по крестику")
    def test_close_modal(self):
        """Проверка закрытия модального окна кликом по крестику"""
        self.main_page.go_to_constructor()
        self.main_page.switch_to_fillings_tab()
        self.main_page.open_ingredient_details()
        self.main_page.close_modal()
        assert not self.main_page.is_element_visible(INGREDIENT_DETAILS_HEADER), "Модальное окно не закрылось"

    @allure.story("Добавление ингредиентов")
    @allure.title("Счётчик ингредиента увеличивается при добавлении в корзину")
    def test_add_ingredient_increases_counter(self):
        """Проверка, что при добавлении ингредиента счётчик увеличивается с 0 до 1"""
        self.main_page.go_to_constructor()
        self.main_page.switch_to_fillings_tab()

        # Получаем начальное значение счётчика
        initial_count = self.main_page.get_beef_meteorite_counter()
        print(f"Начальное значение счётчика: {initial_count}")

        # Убедимся, что изначально счётчик равен 0
        assert initial_count == 0, f"Ожидалось начальное значение 0, но получено {initial_count}"

        # Перетаскиваем ингредиент в корзину
        self.main_page.add_beef_meteorite_to_basket()

        # Проверяем, что счётчик увеличился
        final_count = self.main_page.get_beef_meteorite_counter()
        print(f"Конечное значение счётчика: {final_count}")
        assert final_count == 1, f"Ожидалось значение 1, но получено {final_count}"
