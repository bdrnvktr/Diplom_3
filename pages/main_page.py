import allure
from pages.base_page import BasePage
from locators.main_locators import MainPageLocators
from urls import URLs



class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.open_page(URLs.BASE_URL)
    
    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step('Клик по кнопке "Лента заказов"')
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step('Проверка отображения конструктора')
    def is_constructor_displayed(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)
    
    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_BUN)
    
    @allure.step('Проверка отображения деталей ингредиента')
    def is_ingredient_details_displayed(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)
    
    @allure.step('Проверка отсутствия деталей ингредиента')
    def is_ingredient_details_not_displayed(self):
        return self.is_element_invisible(MainPageLocators.INGREDIENT_DETAILS_TITLE)
    
    @allure.step('Закрытие окна с деталями ингредиента')
    def close_ingredient_popup(self):
        self.click_element_safe(MainPageLocators.INGREDIENT_MODAL_CLOSE, MainPageLocators.LOADING_IMG)
        self.wait_element_invisible(MainPageLocators.INGREDIENT_DETAILS_TITLE)
        self.wait_element_invisible(MainPageLocators.INGREDIENT_MODAL_OVERLAY)
    
    @allure.step('Получение значения счётчика ингредиента')
    def get_ingredient_counter(self):
        return int(self.get_text(MainPageLocators.BUN_COUNTER))
    
    @allure.step('Перетаскивание ингредиента в корзину')
    def drag_ingredient_to_basket(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT_BUN, MainPageLocators.BASKET_AREA)
    
    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_create_order(self):
        self.click_element_safe(MainPageLocators.CREATE_ORDER_BUTTON, MainPageLocators.LOADING_IMG)
    
    @allure.step('Получение номера заказа с подстановкой лидирующего "0"')
    def get_order_number(self):
        self.wait_element_visible(MainPageLocators.ORDER_MODAL)
        order_number = self.get_text(MainPageLocators.ORDER_NUMBER)
        return f'0{order_number}'
    
    @allure.step('Закрытие модального окна заказа')
    def close_order_modal(self):
        self.click_element_safe(MainPageLocators.CLOSE_ORDER_MODAL, MainPageLocators.LOADING_IMG)
        self.wait_element_invisible(MainPageLocators.CLOSE_ORDER_MODAL)

