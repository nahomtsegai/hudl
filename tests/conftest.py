import pytest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from data.TestUrls import TestUrls


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    match browser.lower():
        case "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        case "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        case other:
            options = Options()
            options.add_argument("--incognito")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-popup-blocking")
            if bool(headless):
                options.add_argument("--window-size=1920x1080")
                options.add_argument("--headless")
            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.get(TestUrls.login_page)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class")
def user_data(request):
    email = request.config.getoption("email")
    password = request.config.getoption("password")
    request.cls.email = email
    request.cls.password = password


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome, firefox, edge, safari"
    )
    parser.addoption(
        "--headless", action="store", default=False
    )
    parser.addoption(
        "--email", action="store"
    )
    parser.addoption(
        "--password", action="store"
    )
