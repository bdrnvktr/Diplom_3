
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from urls import URLs
from data import TestData

@pytest.fixture
def chrome_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_chrome(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.open_page(URLs.LOGIN)
    login_page.login(TestData.USER_EMAIL, TestData.USER_PASSWORD)
    return chrome_driver


@pytest.fixture
def login_firefox(firefox_driver):
    login_page = LoginPage(firefox_driver)
    login_page.open_page(URLs.LOGIN)
    login_page.login(TestData.USER_EMAIL, TestData.USER_PASSWORD)
    return firefox_driver