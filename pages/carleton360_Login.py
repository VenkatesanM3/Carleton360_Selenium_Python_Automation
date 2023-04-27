from abc import ABC

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base import BasePage


# Web elements available in Carleton360 login page can be maintained here
class Carleton360LoginPage(BasePage, ABC):
    # Locators for the text and buttons
    PANEL_TITLE = (By.XPATH, "//h2[@class='sv-panel-title']")
    LOCATORS_BY_INPUT = {
        "Username": (By.XPATH, "//input[@type='text' or @id='MUA_CODE.DUMMY.MENSYS']"),
        "Password": (By.XPATH, "//input[@type='password' or @id='PASSWORD.DUMMY.MENSYS']"),
    }
    LOCATORS_BY_BUTTON = {
        "← Back": (By.XPATH, "//div[@class='back-button']"),
        "Log in": (By.XPATH, "//input[@type='submit' or @value='Log in']"),
        # "Forgot password?": (By.LINK_TEXT, "Forgot password?"),
        "Forgot password?": (By.XPATH, "//a[text() = 'Forgot password?']"),
    }
    LOCATORS_BY_ERROR_TEXT_HEAD = {
        "Username Not Provided": (By.XPATH, "//strong[text()='Username Not Provided']"),
        "Password Not Provided": (By.XPATH, "//strong[text()='Password Not Provided']"),
        "Username and/or password Invalid": (By.XPATH, "//strong[text() = 'Username and/or password Invalid']"),
    }
    LOCATORS_BY_ERROR_TEXT_BODY = {
        "Username Not Provided": (
            By.XPATH, "//div[contains(text(),'In order to login, you must provide a username.')]"),
        "Password Not Provided": (
            By.XPATH, "//div[contains(text(),'In order to login, you must provide a password.')]"),
        "Username and/or password Invalid": (
            By.XPATH, "//div[contains(text(),'The user name or password you supplied are invalid')]"),
    }

    def __init__(self, browser):
        super().__init__(browser)

    def navigate(self):
        self.browser.get(self.BASE_URL)

    PAGE_TITLE = "Carleton 360"  # Or the exact title you expect for the login page

    @property
    def page_title(self):
        return self.PAGE_TITLE

    def get_page_title_text(self):
        return self.browser.title

    def find_element_by_locator(self, locator):
        try:
            element = self.browser.find_element(*locator)
            return element
        except NoSuchElementException:
            return None

    # Methods to get the text and buttons

    def find_element_button(self, button):
        locator = self.LOCATORS_BY_BUTTON.get(button)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{button}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

        # if element and element.is_displayed() and element.is_enabled():
        #     print("Element is visible and clickable")
        #     # element.click()
        # else:
        #     print("Element is either not visible or not clickable")
        #     return None

    def get_panel_title(self):
        return self.browser.find_element(*self.PANEL_TITLE)

    def find_element_input(self, option_text):
        locator = self.LOCATORS_BY_INPUT.get(option_text)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{option_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def find_element_error_head(self, error_text):
        locator = self.LOCATORS_BY_ERROR_TEXT_HEAD.get(error_text)
        if locator is None:
            raise ValueError(f"Locator not found for error text '{error_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def find_element_error_body(self, error_text):
        locator = self.LOCATORS_BY_ERROR_TEXT_BODY.get(error_text)
        if locator is None:
            raise ValueError(f"Locator not found for error text '{error_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None
