from abc import ABC

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base import BasePage


class Carleton360RegistrationPage(BasePage, ABC):
    # Locators for the text and buttons
    SUBTEXT_1 = (By.XPATH, "//p[contains(text(),'Please fill in the details below to sign up for Carleton360')]")
    SUBTEXT_2 = (By.XPATH, "//p[text()='If you have previously signed up for a Carleton360 account,  ']")
    PANEL_TITLE = (By.XPATH, "//h2[@class='sv-panel-title']/span[text()=' Provide Your Details']")
    LOCATORS_BY_LINK_TEXT = {
        "login here": (By.XPATH, "//a[text()='login here']"),
        "Data Protection Policy": (By.XPATH, "//a[text()='Data Protection Policy']"),
    }
    LINK_TEXT = (By.XPATH, "//a[text()='login here']")
    LOCATORS_BY_LABEL = {
        "First Name": (By.XPATH, "//label[text()='First Name']"),
        "Middle Name(s)": (By.XPATH, "//label[text()='Middle Name(s)']"),
        "Last Name": (By.XPATH, "//label[text()='Last Name']"),
        "Email Address": (By.XPATH, "//label[text()='Email Address']"),
        "Verify Email Address": (By.XPATH, "//label[text()='Verify Email Address']"),
        "Date of Birth": (By.XPATH, "//p[contains(text(),'Date of Birth')]"),
        "Day": (By.XPATH, "//label[@class='splitdatelabel' and @for='SPLITDATE_D.TTQ.MENSYS.7']"),
        "Month": (By.XPATH, "//label[@class='splitdatelabel' and @for='SPLITDATE_M.TTQ.MENSYS.7']"),
        "Year": (By.XPATH, "//label[@class='splitdatelabel' and @for='SPLITDATE_Y.TTQ.MENSYS.7']"),
        "In which level of study are you interested?": (
            By.XPATH, "//label[text()='In which level of study are you interested?']"),
        "Country of Residence": (By.XPATH, "//label[text()='Country of Residence']"),
        "Select your program(s) of interest*": (By.XPATH, "//label[text()='Select your program(s) of interest*']"),
        "Expected Entry Term1": (By.XPATH, "//label[text()='Expected Entry Term' and @for='ANSWER.TTQ.MENSYS.15.']"),
        "In which graduate level(s) of study are you interested?": (
            By.XPATH, "//label[text()='In which graduate level(s) of study are you interested?']"),
        "Country of Citizenship": (By.XPATH, "//label[text()='Country of Citizenship']"),
        "Is your most recent degree from a Canadian institution?": (
            By.XPATH, "//label[text()='Is your most recent degree from a Canadian institution?']"),
        "Current or highest level of education": (By.XPATH, "//label[text()='Current or highest level of education']"),
    }
    LOCATORS_BY_INPUT = {
        "First Name": (By.XPATH, "//input[@type='text' and @data-name-field='first']"),
        "Middle Name(s)": (By.XPATH, "//input[@type='text' and @data-name-field='middle']"),
        "Last Name": (By.XPATH, "//input[@type='text' and @data-name-field='last']"),
        "Email Address": (By.XPATH, "//input[@id='ANSWER.TTQ.MENSYS.5.']"),
        "Verify Email Address": (By.XPATH, "//input[@id='ANSWER.TTQ.MENSYS.6.']"),
        "Day": (By.XPATH, "//select[@id='SPLITDATE_D.TTQ.MENSYS.7']"),
        "Month": (By.XPATH, "//select[@id='SPLITDATE_M.TTQ.MENSYS.7']"),
        "Year": (By.XPATH, "//select[@id='SPLITDATE_Y.TTQ.MENSYS.7']"),
        "In which level of study are you interested?": (
            By.XPATH, "//div[@id='ANSWER_TTQ_MENSYS_8__chosen']"),
        "Country of Residence": (By.XPATH, "//div[@data-ttip='Select the country where you currently live']"),
        "Select your program(s) of interest*": (By.XPATH, "//div[@aria-label='Select your program(s) of interest*']"),
        "Master's Programs": (By.XPATH, "//input[@aria-label=\"Master's Programs search\"]"),
        "PhD Programs": (By.XPATH, "//input[@aria-label='PhD Programs search']"),
        "Collaborative Programs": (By.XPATH, "//input[@aria-label='Collaborative Programs search']"),
        "Graduate Diplomas": (By.XPATH, "//input[@aria-label='Graduate Diplomas search']"),
        "Expected Entry Term": (
            By.XPATH, "//div[@id='ANSWER_TTQ_MENSYS_34__chosen']"),
        "Expected Entry Term1": (
            By.XPATH, "//label[@class='sv-col-sm-12 sv-control-label' and text()='Expected Entry Term']"),
        "In which graduate level(s) of study are you interested?": (
            By.XPATH, "//input[@aria-label='In which graduate level(s) of study are you interested? search']"),
        "Country of Citizenship": (By.XPATH, "//div[@data-ttip='Select the country which issued your passport']"),
        "Is your most recent degree from a Canadian institution?": (
            By.XPATH, "//div[@id='ANSWER_TTQ_MENSYS_22__chosen']"),
        "Current or highest level of education": (By.XPATH, "//span[@id='ANSWER_TTQ_MENSYS_36__chosenspan']"),

    }
    DROPDOWN_LIST_SELECT = (By.XPATH, "//a[@class='chosen-single chosen-single-with-deselect']")
    LOCATORS_BY_DROPDOWN_LIST = {
        "In which level of study are you interested? options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='In which level of study are you interested? options']//li"),
        "Country of Residence options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='Country of Residence options']//li"),
        "Select your program(s) of interest* options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='Select your program(s) of interest* options']//li"),
        "Master's Programs options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label=\"Master's Programs options\"]//li"),
        "PhD Programs options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='PhD Programs options']//li"),
        "Collaborative Programs options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='Collaborative Programs search options']//li"),
        "Graduate Diplomas options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='Graduate Diplomas options']//li"),
        "Expected Entry Term options": (
            By.XPATH, "//ul[@role='listbox' and @aria-label='Expected Entry Term options']//li"
        ),
        "In which graduate level(s) of study are you interested? options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='In which graduate level(s) of study are you interested? options']//li"
        ),
        "Country of Citizenship options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='Country of Citizenship options']//li"),
        "Is your most recent degree from a Canadian institution? options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='Is your most recent degree from a Canadian institution? options']//li"
        ),
        "Current or highest level of education options": (
            By.XPATH,
            "//ul[@role='listbox' and @aria-label='Current or highest level of education options']//li"
        ),

    }

    SUBMIT_BUTTON = (By.XPATH, "//input[@value='SUBMIT']")

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

    def find_element_link_text(self, link_text):
        locator = self.LOCATORS_BY_LINK_TEXT.get(link_text)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{link_text}'")

        element = self.find_element_by_locator(locator)

        if element and element.is_displayed():
            return element
        else:
            return None

    def find_element_label(self, option_text):
        locator = self.LOCATORS_BY_LABEL.get(option_text)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{option_text}'")

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

    # def get_drop_down_list(self):
    #     return self.browser.find_element(*self.DROPDOWN_LIST)

    # def get_drop_down_list(self, option):
    #     dropdown_elements = self.browser.find_elements(*self.DROPDOWN_LIST)
    #     for element in dropdown_elements:
    #         if element.text.split(" (")[0] == option:
    #             return element
    #     return None

    # Web elements available in Carleton360 Registration page can be maintained here
    def get_drop_down_list(self, list_options, option):
        locator = self.LOCATORS_BY_DROPDOWN_LIST.get(list_options)
        if locator is None:
            raise ValueError(f"Locator not found for option text '{list_options}'")
        dropdown_elements = self.browser.find_elements(*locator)
        for element in dropdown_elements:
            if element.text.split(" (")[0] == option:
                return element
        return None

    def select_option_by_text(self, text):
        dropdown = Select(self.browser.find_element(*self.DROPDOWN_LIST))
        dropdown.select_by_visible_text(text)

    def select_option_by_index(self, index):
        dropdown = Select(self.browser.find_element(*self.DROPDOWN_LIST))
        dropdown.select_by_index(index)

    def get_submit_button(self):
        return self.browser.find_element(*self.SUBMIT_BUTTON)
