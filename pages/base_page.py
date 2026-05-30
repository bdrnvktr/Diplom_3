from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Находит элемент по локатору"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Кликает по элементу"""
        element = self.find_element(locator)
        element.click()

    def get_text(self, locator):
        """Получает текст элемента"""
        element = self.find_element(locator)
        return element.text

    def wait_for_invisibility(self, locator, timeout=10):
        """Ожидает, пока элемент станет невидимым"""
        self.wait.until(EC.invisibility_of_element_located(locator))

    def is_element_visible(self, locator):
        """Проверяет, виден ли элемент"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False

    def scroll_to_element(self, locator):
        """Прокручивает к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def execute_js(self, script, *args):
        """Выполняет JavaScript в контексте страницы"""
        return self.driver.execute_script(script, *args)
