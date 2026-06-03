import allure
from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators
from urls import URLs
from locators.main_locators import MainPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Авторизация пользователя: {email}')
    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element_safe(LoginPageLocators.LOGIN_BUTTON, MainPageLocators.LOADING_IMG)
        self.wait_url_to_be(URLs.BASE_URL)