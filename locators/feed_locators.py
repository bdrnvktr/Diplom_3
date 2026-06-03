from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Заголовок
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Счётчики
    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    
    # Раздел "В работе"
    IN_PROGRESS_ORDERS = (By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady')]/li[contains(@class,'text_type_digits-default')]")