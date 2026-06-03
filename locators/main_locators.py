from selenium.webdriver.common.by import By


class MainPageLocators:
    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')
    
    # Заголовки
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    
    # Ингредиенты
    INGREDIENT_BUN = (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")
    BUN_COUNTER = (By.XPATH, "//p[contains(@class, 'num')]")
    
    # Корзина
    BASKET_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    
    # Кнопка оформления заказа
    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    
    # Модальное окно подтверждения заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//p[contains(text(), 'Ваш заказ начали готовить')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2[contains(@class, 'Modal_modal__title')]")
    CLOSE_ORDER_MODAL = (By.XPATH, './/p[text()="идентификатор заказа"]/../../button[contains(@class,"close")]')
    
    # Окно с деталями ингредиента
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    INGREDIENT_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")

    LOADING_IMG = (By.XPATH, './/img[contains(@class,"Modal_modal__loading")]')