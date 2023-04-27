from abc import ABC

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base import BasePage


# Web elements available in Forgot Password page can be maintained here
class ForgotPasswordPage(BasePage, ABC):
    # Locators for the text and buttons
    FORGOT_PASSWD = (By.XPATH, "//div[@class='sv-page-header sv-hidden-xs']/h1[text() = 'Forgot Password?']")
    SUBTEXT_1 = (
        By.XPATH,
        "//p[contains(text(), 'Please enter your account details in order to reset your Carleton360 Password.')]")
    SUBTEXT_2 = (By.XPATH, "//strong[text()='Important!']")
    LINK_TEXT = (By.XPATH, "// a[text() = 'MC1 Accounts and Passwords']")
    PANEL_TITLE = (By.XPATH, "//h2[@class='sv-panel-title']")
    LOCATORS_BY_INPUT = {
        "Username": (By.XPATH, "//input[@type='text' and @id='USER_NAME.DUMMY_BUTT.MENSYS']"),
        "Surname": (By.XPATH, "//input[@type='text' and @id='SURNAME.DUMMY_BUTT.MENSYS']"),
        "Date of birth": (By.XPATH, "//input[@type='text' and @id='DOBIRTH.DUMMY_BUTT.MENSYS']"),
    }
    GO_BUTTON = (By.XPATH, "//input[@type='submit' or @value='Go']")

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

    def get_title(self):
        return self.browser.find_element(*self.FORGOT_PASSWD)

    def get_sub_title1(self):
        return self.browser.find_element(*self.SUBTEXT_1)

    def get_sub_title2(self):
        return self.browser.find_element(*self.SUBTEXT_2)

    def get_link_text(self):
        return self.browser.find_element(*self.LINK_TEXT)

    def find_element_input(self, option_text):
        locator = self.LOCATORS_BY_INPUT.get(option_text)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{option_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def get_go_button(self):
        return self.browser.find_element(*self.GO_BUTTON)
