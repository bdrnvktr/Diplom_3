from selenium.webdriver.common.by import By

# Кнопка «Лента заказов» в шапке: ссылка с классом AppHeader_header__link__3D_hX и текстом «Лента Заказов» внутри p
ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")

# Кнопка «Конструктор» в шапке: ссылка с двумя классами и текстом «Конструктор» внутри p
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']/parent::a")

# Заголовок «Соберите бургер» на странице конструктора — подтверждение, что мы в конструкторе
BURGER_BUILDER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")

# Заголовок «Лента заказов» — подтверждение, что мы в ленте
ORDER_FEED_HEADER = (By.XPATH, "//h1[contains(@class, 'text') and contains(@class, 'text_type_main-large') and text()='Лента заказов']")

# Кнопка "Начинки в конструкторе"
FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'noselect')]/span[text()='Начинки']")

# Говяжий метеорит в начинках
BEEF_METEORITE = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Говяжий метеорит (отбивная)']")

# Говяжий метеорит в корзине  - подтверждение
BEEF_METEORITE_IN_BASKET = (By.XPATH, '//img[@alt="Говяжий метеорит (отбивная)"]/ancestor::li[@class="BasketItem_basketItem__listItem__3yMU_"]')

# Заголовок "Детали ингредиента" - подтверждение что открылась информация об ингредиенте
INGREDIENT_DETAILS_HEADER = (By.XPATH, "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10' and text()='Детали ингредиента']")

# Кнопка закрытия модального окна с информацией об ингредиенте
MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS') and contains(@class, 'Modal_modal__close__TnseK')]")

# Счётчик "Говяжьего метеорита"
BEEF_METEORITE_COUNTER = (
    By.XPATH,
    "//p[text()='Говяжий метеорит (отбивная)']/preceding-sibling::div//p[@class='counter_counter__num__3nue1']"
)

# Булочка «Флюоресцентная булка R2-D3»
FLUORESCENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")

# Локатор счётчика для булочки
BUN_COUNTER = (By.XPATH,"//p[text()='Флюоресцентная булка R2-D3']/preceding-sibling::div//p[@class='counter_counter__num__3nue1']")

# Зона корзины — куда перетаскиваем ингредиенты
BASKET_DROP_ZONE = (By.CSS_SELECTOR, 'ul.BurgerConstructor_basket__list__l9dp_')

# Локаторы для страницы ленты заказов
# Счётчик «Выполнено за всё время»
TOTAL_COUNTER = (By.XPATH, "//div[contains(@class, 'mb-15')]//p[contains(@class, 'text_type_digits-large')][preceding-sibling::p[text()='Выполнено за все время:']]")

# Счётчик «Выполнено за сегодня»
TODAY_COUNTER = (By.XPATH, "//div//p[contains(@class, 'text_type_digits-large')][preceding-sibling::p[text()='Выполнено за сегодня:']]")

# Контейнер текущих заказов в ленте
CURRENT_ORDERS_CONTAINER = (By.CLASS_NAME, "OrderFeed_orderListReady__1YFem")
# Элементы с номерами заказов внутри контейнера
CURRENT_ORDER_ITEMS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[contains(@class, 'text_type_digits-default')]")

# Номер заказа в модальном окне после оформления
ORDER_MODAL_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and string-length(text())=6 and number(text())>0]")
# Кнопка закрытия модального окна с номером заказа (SVG крестик)
ORDER_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")

# КНОПКИ ВХОДА И ЛИЧНЫЙ КАБИНЕТ
LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
PERSONAL_CABINET_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка «Личный кабинет»

# ФОРМА ВХОДА
LOGIN_EMAIL_FIELD = (By.NAME, 'name')  # Поле email в форме входа
LOGIN_PASSWORD_FIELD = (By.NAME, 'Пароль')  # Поле пароля в форме входа (исправлено: было 'Пароль')
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка входа в форме

# ОБЩИЕ ЭЛЕМЕНТЫ
ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # КНОПКА ОФОРМИТЬ ЗАКАЗ

# Модальное окно — overlay (для ожидания исчезновения)
MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
