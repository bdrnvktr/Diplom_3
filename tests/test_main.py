import allure
import pytest
from pages.main_page import MainPage
from pages.feed_page import OrderFeedPage


@allure.feature('Основной функционал')
class TestMainFunctionality:
    
    @allure.title('Переход по клику на "Конструктор"')
    @pytest.mark.parametrize('driver_fixture', ['chrome_driver', 'firefox_driver'])
    def test_click_constructor_button_main_page_constructor_displayed(self, request, driver_fixture):
        driver = request.getfixturevalue(driver_fixture)
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        main_page.click_order_feed_button()
        main_page.click_constructor_button()
        
        assert main_page.is_constructor_displayed()
    
    @allure.title('Переход по клику на "Лента заказов"')
    @pytest.mark.parametrize('driver_fixture', ['chrome_driver', 'firefox_driver'])
    def test_click_order_feed_button_main_page_order_feed_displayed(self, request, driver_fixture):
        driver = request.getfixturevalue(driver_fixture)
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        main_page.click_order_feed_button()
        
        order_feed_page = OrderFeedPage(driver)
        assert order_feed_page.is_order_feed_displayed()
    
    @allure.title('Открытие всплывающего окна с деталями ингредиента')
    @pytest.mark.parametrize('driver_fixture', ['chrome_driver', 'firefox_driver'])
    def test_click_ingredient_main_page_details_popup_opened(self, request, driver_fixture):
        driver = request.getfixturevalue(driver_fixture)
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        main_page.click_ingredient()
        
        assert main_page.is_ingredient_details_displayed()
    
    @allure.title('Закрытие всплывающего окна кликом по крестику')
    @pytest.mark.parametrize('driver_fixture', ['chrome_driver', 'firefox_driver'])
    def test_click_close_button_ingredient_popup_popup_closed(self, request, driver_fixture):
        driver = request.getfixturevalue(driver_fixture)
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        main_page.click_ingredient()
        main_page.close_ingredient_popup()
        
        assert main_page.is_ingredient_details_not_displayed()
    
    @allure.title('Увеличение счётчика при добавлении ингредиента')
    @pytest.mark.parametrize('login_fixture', ['login_chrome', 'login_firefox'])
    def test_drag_ingredient_to_basket_main_page_counter_increased(self, request, login_fixture):
        driver = request.getfixturevalue(login_fixture)
        main_page = MainPage(driver)
        main_page.open_main_page()
        
        initial_counter = main_page.get_ingredient_counter()
        main_page.drag_ingredient_to_basket()
        new_counter = main_page.get_ingredient_counter()
        
        assert new_counter > initial_counter
