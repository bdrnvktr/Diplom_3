import allure
import pytest
from pages.main_page import MainPage
from pages.feed_page import OrderFeedPage


@allure.feature('Лента заказов')
class TestOrderFeed:
    
    @allure.title('Увеличение счётчика "Выполнено за всё время" при создании заказа')
    @pytest.mark.parametrize('login_fixture', ['login_chrome', 'login_firefox'])
    def test_create_order_order_feed_total_counter_increased(self, request, login_fixture):
        driver = request.getfixturevalue(login_fixture)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        order_feed_page.open_order_feed()
        total_before = order_feed_page.get_total_orders_count()
        
        main_page.open_main_page()
        main_page.drag_ingredient_to_basket()
        main_page.click_create_order()
        main_page.close_order_modal()
        
        order_feed_page.open_order_feed()
        order_feed_page.is_order_feed_displayed()
        total_after = order_feed_page.get_total_orders_count()
        
        assert total_after > total_before
    
    @allure.title('Увеличение счётчика "Выполнено за сегодня" при создании заказа')
    @pytest.mark.parametrize('login_fixture', ['login_chrome', 'login_firefox'])
    def test_create_order_order_feed_today_counter_increased(self, request, login_fixture):
        driver = request.getfixturevalue(login_fixture)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        order_feed_page.open_order_feed()
        today_before = order_feed_page.get_today_orders_count()
        
        main_page.open_main_page()
        main_page.drag_ingredient_to_basket()
        main_page.click_create_order()
        main_page.close_order_modal()
        
        order_feed_page.open_order_feed()
        order_feed_page.is_order_feed_displayed()
        today_after = order_feed_page.get_today_orders_count()
        
        assert today_after > today_before
    
    
    @allure.title('Появление номера заказа в разделе "В работе"')
    @pytest.mark.parametrize('login_fixture', ['login_chrome', 'login_firefox'])
    def test_create_order_order_feed_order_appears_in_progress(self, request, login_fixture):
        driver = request.getfixturevalue(login_fixture)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        
        main_page.open_main_page()
        main_page.drag_ingredient_to_basket()
        main_page.click_create_order()
        
        order_number = main_page.get_order_number()
        main_page.close_order_modal()
        
        order_feed_page.open_order_feed()
        
        
        assert order_feed_page.is_order_in_progress(order_number)