from abc import ABC

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage


class LoginPage(BasePage, ABC):
    # Locators for the text and buttons
    OPENING_TEXT = (By.XPATH, "//p[@class='login-funnel--description']")
    LOCATORS_BY_OPTION_TEXT = {
        "No Account?": (By.XPATH, "//strong[text()='No Account?']"),
        "Have a Carleton360 account?": (
            By.XPATH, "//h4[@class='sv-list-group-item-heading']/span[text()='Have a Carleton360 account?']"),
        "Already have a MyCarletonOne (MC1) account?": (
            By.XPATH,
            "//h4[@class='sv-list-group-item-heading']/span[text()='Already have a MyCarletonOne (MC1) account?']"),
    }
    LOCATORS_BY_OPTION_SUBTEXT = {
        "No Account?": (By.XPATH, "//strong[text()='No Account?']"),
        "Have a Carleton360 account?": (
            By.XPATH, "//*[@id='login-toggle']/p"),
        "Already have a MyCarletonOne (MC1) account?": (
            By.XPATH,
            "//*[@id='login-funnel']/div/a[2]/p"),
        # "//p[text()='You have previously submitted an application, or are a student, staff or faculty member.']"),
    }
    LOCATORS_BY_OPTION_LINK_TEXT = {
        "No Account?": (By.XPATH, "//strong[text()='Register for Carleton360']"),
        "Have a Carleton360 account?": (By.XPATH, "//span[contains(text(), 'Log in here with your email')]"),
        "Already have a MyCarletonOne (MC1) account?": (
            By.XPATH, "//span[contains(text(), 'Log in here with your MC1 credentials')]"),
    }

    CARLETON360_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Log in here with your email')]")
    MC1_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Log in here with your MC1 credentials')]")

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

    # Methods to get the text and buttons

    def get_opening_paragraph_text(self):
        return self.browser.find_element(*self.OPENING_TEXT)

    # def find_element_by_text(self, option_text):
    #     if option_text == "NO ACCOUNT?":
    #         xpath = f"//strong[contains(text(),'{option_text}')]"
    #     else:
    #         # xpath = f"//span[contains(text(), '{option_text}')]"
    #         xpath = "//h4[@class='sv-list-group-item-heading']/span[text()='Have a Carleton360 account?']"
    #         element = self.browser.find_element_by_xpath(xpath)
    #         return element.is_displayed()

    def find_element_by_locator(self, locator):
        try:
            element = self.browser.find_element(*locator)
            return element
        except NoSuchElementException:
            return None

    def find_element_text(self, option_text):
        locator = self.LOCATORS_BY_OPTION_TEXT.get(option_text)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{option_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def find_element_subtext(self, option_text):
        locator = self.LOCATORS_BY_OPTION_SUBTEXT.get(option_text)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{option_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def find_element_link_text(self, option_text):
        locator = self.LOCATORS_BY_OPTION_LINK_TEXT.get(option_text)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{option_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def get_carleton360_login_button(self):
        return self.browser.find_element(*self.CARLETON360_LOGIN_BUTTON)

    def get_mc1_login_button(self):
        return self.browser.find_element(*self.MC1_LOGIN_BUTTON)
