import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    @allure.step('Открытие страницы: {url}')
    def open_page(self, url):
        self.driver.get(url)
    
    @allure.step('Поиск элемента: {locator}')
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # Добавим метод для явного ожидания наличия элемента в DOM
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Клик по элементу: {locator}')
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    @allure.step('Получение текста элемента: {locator}')
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step('Проверка видимости элемента: {locator}')
    def is_element_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return True
    
    @allure.step('Проверка отсутствия элемента: {locator}')
    def is_element_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
        return True
    
    @allure.step('Ожидание невидимости элемента: {locator}')
    def wait_element_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
    
    @allure.step('Ожидание видимости элемента: {locator}')
    def wait_element_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Перетаскивание элемента с помощью JS DragEvent')
    def drag_and_drop(self, source_locator, target_locator):
        """
        Перетаскивает элемент из source_locator в target_locator с использованием JavaScript DragEvent.
        :param source_locator: Локатор элемента, который нужно перетащить.
        :param target_locator: Локатор элемента, куда нужно перетащить.
        """
        self.find_element_with_wait(source_locator)
        self.find_element_with_wait(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Ввод текста в поле: {locator}')
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)


    @allure.step('Поиск кликабельного элемента: {locator}')
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step('Безопасный клик по элементу с ожиданием загрузки: {locator}')
    def click_element_safe(self, locator, loading_locator):
        self.wait_element_invisible(loading_locator)  
        self.find_clickable_element(locator).click()
        self.wait_element_invisible(loading_locator)  

    @allure.step('Поиск всех элементов по локатору: {locator}')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Ожидание перехода на URL: {url}')
    def wait_url_to_be(self, url):
        self.wait.until(EC.url_to_be(url))