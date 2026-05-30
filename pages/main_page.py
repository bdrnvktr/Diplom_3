from locators.locators import (
    CONSTRUCTOR_LINK,
    ORDER_FEED_LINK,
    FILLINGS_TAB,
    BEEF_METEORITE,
    INGREDIENT_DETAILS_HEADER,
    MODAL_CLOSE_BUTTON,
    BEEF_METEORITE_COUNTER,
    BASKET_DROP_ZONE,
    BURGER_BUILDER_HEADER,
    BUN_COUNTER,
    FLUORESCENT_BUN,
    ORDER_MODAL_NUMBER,
    ORDER_MODAL_CLOSE_BUTTON,
    MODAL_OVERLAY,
    ORDER_BUTTON
)
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    def ensure_modal_closed(self):
        """Гарантированно убирает модальное окно и его оверлей"""
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable(ORDER_MODAL_CLOSE_BUTTON),
                timeout=5
            )
            close_btn.click()
            self.wait_for_invisibility(ORDER_MODAL_NUMBER)
        except:
            try:
                overlay = self.driver.find_element(*MODAL_OVERLAY)
                if overlay.is_displayed():
                    overlay.click()
                    self.wait_for_invisibility(ORDER_MODAL_NUMBER)
            except:
                pass
        # Финальный шаг: принудительно удаляем оверлей и модальное окно из DOM через JS
        self.execute_js("""
            const overlay = document.querySelector('.Modal_modal_overlay__x2ZCr');
            if (overlay) overlay.remove();
            const modal = document.querySelector('h2[class*="Modal_modal__title"]').closest('.Modal_modal__2c1pE');
            if (modal) modal.remove();
        """)

    def go_to_constructor(self):
        """Переход в раздел «Конструктор»"""
        self.ensure_modal_closed()
        self.click_element(CONSTRUCTOR_LINK)
        self.find_element(BURGER_BUILDER_HEADER)

    def go_to_feed(self):
        """Переход в раздел «Лента заказов»"""
        self.ensure_modal_closed()
        self.click_element(ORDER_FEED_LINK)

    def switch_to_fillings_tab(self):
        """Переключается на вкладку «Начинки»"""
        self.click_element(FILLINGS_TAB)

    def open_ingredient_details(self):
        """Клик на ингредиент для открытия модального окна с деталями"""
        self.click_element(BEEF_METEORITE)
        self.find_element(INGREDIENT_DETAILS_HEADER)

    def close_modal(self):
        """Закрытие модального окна кликом по крестику"""
        self.click_element(MODAL_CLOSE_BUTTON)
        self.wait_for_invisibility(INGREDIENT_DETAILS_HEADER)

    def get_bun_counter(self):
        """Получает текущее значение счётчика для булочки"""
        try:
            counter_element = self.wait.until(
                EC.visibility_of_element_located(BUN_COUNTER)
            )
            return int(counter_element.text)
        except Exception:
            return 0

    def add_bun_to_basket(self):
        """Добавляет булочку в корзину путём перетаскивания"""
        bun_element = self.find_element(FLUORESCENT_BUN)
        drop_zone = self.find_element(BASKET_DROP_ZONE)
        ActionChains(self.driver).drag_and_drop(bun_element, drop_zone).perform()
        # Ждём появления счётчика булочек (не просто >0, а именно элемент)
        counter_element = self.wait.until(EC.presence_of_element_located(BUN_COUNTER))
        # Теперь ждём, когда значение счётчика станет > 0
        self.wait.until(lambda _: int(counter_element.text) > 0)

    def get_beef_meteorite_counter(self):
        """Получает текущее значение счётчика для метеорита"""
        try:
            counter_element = self.wait.until(
                EC.visibility_of_element_located(BEEF_METEORITE_COUNTER)
            )
            return int(counter_element.text)
        except Exception:
            return 0

    def add_beef_meteorite_to_basket(self):
        """Добавляет говяжий метеорит в корзину путём перетаскивания"""
        meteorite_element = self.find_element(BEEF_METEORITE)
        drop_zone = self.find_element(BASKET_DROP_ZONE)
        ActionChains(self.driver).drag_and_drop(meteorite_element, drop_zone).perform()
        self.wait.until(lambda driver: self.get_beef_meteorite_counter() > 0)

    def create_order(self, ingredients=None):
        """Создаёт заказ, добавляя ингредиенты и нажимая кнопку «Оформить заказ»"""
        if ingredients:
            for ingredient in ingredients:
                self.click_element(ingredient)
        self.click_element(ORDER_BUTTON)
        wait = WebDriverWait(self.driver, 20)
        order_number_element = wait.until(
            EC.presence_of_element_located(ORDER_MODAL_NUMBER)
        )
        return order_number_element.text

    def get_order_number_from_modal(self):
        """Получает номер заказа из модального окна"""
        modal_element = self.wait.until(
            EC.visibility_of_element_located(ORDER_MODAL_NUMBER)
        )
        return modal_element.text.strip()

    def close_order_modal(self):
        """Закрывает модальное окно с заказом"""
        self.click_element(ORDER_MODAL_CLOSE_BUTTON)
        self.wait_for_invisibility(ORDER_MODAL_NUMBER)
