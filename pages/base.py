from abc import ABC, abstractmethod


class BasePage(ABC):
    # The base URL of the Carleton 360 application, used to construct page URLs.
    BASE_URL = "https://360.carleton.ca/urd/sits.urd/"

    # A dictionary that maps page names to their respective URLs, used for navigation purposes.
    PAGE_URLS = {
        "Carleton 360 login": BASE_URL + "/run/siw_lgn",
        "Forgot password": BASE_URL + "run/siw_pqs.forgot?",
    }

    # Abstract property to be implemented by each subclass to return the title of the specific page.
    @property
    @abstractmethod
    def PAGE_TITLE(self):
        pass

    # Abstract method to be implemented by each subclass to retrieve the page title text from the web page.
    @abstractmethod
    def get_page_title_text(self):
        pass

    # Constructor for the BasePage class, initializing the browser instance variable with the provided browser object.
    def __init__(self, browser):
        self.browser = browser

    # Method that navigates the browser to the specified page using the PAGE_URLS dictionary.
    def visit(self, page_name):
        self.browser.get(self.PAGE_URLS[page_name])
