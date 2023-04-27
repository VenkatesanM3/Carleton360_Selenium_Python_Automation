from abc import ABC

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base import BasePage


class CarletonSSOLoginPage(BasePage, ABC):
    # Locators for the text and buttons
    LOGO = (By.XPATH, "//img[@id='companyLogo']")
    LOGIN_MESSAGE = (By.XPATH, "//div[@id='loginMessage']")
    MY_CARLETON_ONE_LINK_TEXT = (By.XPATH, "//strong[text()='MyCarletonOne']")
    LOCATORS_BY_LINK_TEXT = {
        "MyCarletonOne": (By.XPATH, "//strong[text()='MyCarletonOne']"),
        "Password": (By.XPATH, "//strong[text()='Password']"),
    }
    LOCATORS_BY_INPUT = {
        "Username": (By.XPATH, "//input[@id='userNameInput']"),
        "Password": (By.XPATH, "//input[@id='passwordInput']"),
    }
    SIGN_IN_BUTTON = (By.XPATH, "//span[@id='submitButton']"),
    FORGOT_PASSWORD = (By.XPATH, "//p[text()='Forgotten your ']")
    LOCATORS_BY_BUTTON = {
        "Sign In": (By.XPATH, "//span[@id='submitButton']"),
        "Forgot password?": (By.XPATH, "//p[text()='Forgotten your ']"),
    }
    LOCATORS_BY_ERROR_TEXT = {
        "Username Not Provided": (By.XPATH, "//span[@id='errorText']"),
        "Password Not Provided": (
            By.XPATH, "//span[@id='errorText' and text()='Enter your current MyCarletonOne password.']"),
        "Username and/or password Invalid": (By.XPATH, "//div[@id='error']"),
    }

    def __init__(self, browser):
        super().__init__(browser)

    def navigate(self):
        self.browser.get(self.BASE_URL)

    PAGE_TITLE = "Sign In"  # Or the exact title you expect for the Carleton SSO page

    @property
    def page_title(self):
        return self.PAGE_TITLE

    def get_page_title_text(self):
        return self.browser.title

    def get_logo(self):
        return self.browser.find_element(*self.LOGO)

    def get_login_message(self):
        return self.browser.find_element(*self.LOGIN_MESSAGE)

    def get_link_text(self):
        return self.browser.find_element(*self.MY_CARLETON_ONE_LINK_TEXT)

    def find_element_by_locator(self, locator):
        try:
            element = self.browser.find_element(*locator)
            return element
        except NoSuchElementException:
            return None

    # Methods to get the text and buttons

    # Web elements available in CarletonSSO login page can be maintained here
    def find_element_link_text(self, link_text):
        locator = self.LOCATORS_BY_LINK_TEXT.get(link_text)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{link_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def find_element_input(self, option_text):
        locator = self.LOCATORS_BY_INPUT.get(option_text)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{option_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def find_element_button(self, button):
        locator = self.LOCATORS_BY_BUTTON.get(button)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{button}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def get_sign_in_button(self):
        return self.browser.find_element(*self.SIGN_IN_BUTTON)

    def get_forgot_password_text(self):
        return self.browser.find_element(*self.FORGOT_PASSWORD)

    def find_element_error_text(self, error_text):
        locator = self.LOCATORS_BY_ERROR_TEXT.get(error_text)
        if locator is None:
            raise ValueError(f"Locator not found for error text '{error_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None
