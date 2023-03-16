import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.yandex_disk_page import YandexPage
from src.config import Urls
from src.locators import YandexDiskLocators


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="",
                     help="Choose browser: chrome, firefox or opera")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        options.set_capability('enableVNC', True)
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_experimental_option(
            'prefs', {"download.default_directory": os.getcwd() + "/documents/"})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxOptions()
        options.headless = False
        browser = webdriver.Firefox(service=FirefoxService(), options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or opera")

    browser.maximize_window()

    yield browser

    print("\nquit browser..")
    browser.quit()


@pytest.fixture()
def teardown_docs(browser):
    yield
    page = YandexPage(browser, Urls.YANDEX_URL)
    page.open()
    page.teardown(YandexDiskLocators.NEW_FOLDER)
    browser.quit()
