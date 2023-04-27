import csv
import os
import time
import pytest
import json

from io import StringIO
from typing import List
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pytest_bdd import given, parsers
from pages.base import BasePage


# Add options for the command-line parser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


# Fixture to read the configuration file and return the configuration settings
@pytest.fixture(scope='session')
def config(request):
    BROWSERS = ['Chrome', 'Firefox']

    # Read config file
    config_path = os.path.join(os.path.dirname(__file__),
                               'config.json')  # Replace 'config.json' with the correct path if needed
    with open(config_path) as config_file:
        config = json.load(config_file)

    browser = request.config.option.browser
    if browser is not None:
        config['browser'] = browser

    # Assert values are acceptable
    assert config['browser'] in BROWSERS
    assert isinstance(config['headless'], bool)
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


# Fixture to initialize the WebDriver instance based on the configuration
@pytest.fixture(scope='session')
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        if config['headless']:
            opts.add_argument('headless')
        b = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        if config['headless']:
            opts.headless = True
        b = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make call wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])
    b.maximize_window()

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the teardown
    b.quit()


# Function to scroll the browser to the top of the page
def scroll_to_top(browser):
    browser.execute_script("document.documentElement.scrollTop = 0;")


# Function to wait for the URL to change in the browser
def wait_for_url_change(browser, expected_url_part, timeout=10):
    WebDriverWait(browser, timeout).until(EC.url_contains(expected_url_part))


# Function to set the title of the HTML report generated by pytest
def pytest_html_report_title(report):
    report.title = "CARLETON 360 LOGIN AUTOMATION"


# Fixture to create and return an instance of the DataTable class
@pytest.fixture
def datatable():
    return DataTable()


# Hook to capture a screenshot when a test fails or is skipped
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail) or call.excinfo:
            driver = item._request.getfixturevalue("browser")
            file_name = report.nodeid.replace("::", "_").replace("/", "_").replace(".py", "") + ".png"

            screenshot_path = _capture_screenshot(driver, file_name)

            if screenshot_path:
                rel_screenshot_path = os.path.relpath(screenshot_path)
                html = ('<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % rel_screenshot_path)
                extra.append(pytest_html.extras.html(html))

        report.extra = extra


# Helper function to capture a screenshot using the provided WebDriver instance and save it to a file
def _capture_screenshot(driver, file_name):
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshots_dir, file_name)
    driver.save_screenshot(screenshot_path)
    return screenshot_path


# Function to highlight an element on the page using the provided WebDriver instance
def highlight_element(driver, element):
    original_style = element.get_attribute("style")
    driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", element)
    time.sleep(1)  # Adjust the sleep duration as needed
    driver.execute_script(f"arguments[0].setAttribute('style', '{original_style}');", element)


# Function to parse a vertical table from a string and return a list of values
def parse_vertical_table(raw_table: str) -> List[str]:
    values = []
    table_io = StringIO(raw_table.strip())
    reader = csv.reader(table_io, delimiter='|')
    header = True
    for row in reader:
        if header:
            header = False
            continue
        value = row[1].strip()
        values.append(value)
    return values


# Class to store data in a tabular format
class DataTable(object):
    def __init__(self):
        pass

    def __str__(self):
        dt_str = ''
        for field, value in self.__dict__.items():
            dt_str = f'{dt_str}\n{field} = {value}'
        return dt_str

    def __repr__(self) -> str:
        return self.__str__()


# BDD step definition for navigating to a specified page using the provided browser instance
@given(parsers.parse('I have navigated to the "{page_name}" page'), target_fixture='navigate_to')
def navigate_to(browser, page_name):
    url = BasePage.PAGE_URLS.get(page_name)
    browser.get(url)
