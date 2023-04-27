import time
from pytest_bdd import given, when, then, scenarios, parsers

from conftest import highlight_element, scroll_to_top, wait_for_url_change, parse_vertical_table
from pages.carleton360_Login import Carleton360LoginPage
from pages.carleton360_Registration import Carleton360RegistrationPage
from pages.carletonSSO_Login import CarletonSSOLoginPage
from pages.forgotPassword import ForgotPasswordPage
from pages.login import LoginPage

# Load the scenarios from the Carleton 360 Login feature file
scenarios('../features/Carleton_360_Login.feature')


# Step to check if the given page title is displayed
@then(parsers.parse('I should see the login page title with icon "{page_title}"'))
def check_login_page_title(browser, page_title):
    assert page_title == LoginPage(browser).get_page_title_text()


# Step to check if the opening text paragraph is displayed
@then(parsers.parse('I should see the correct opening text "{paragraph}"'))
def check_opening_text(browser, paragraph):
    login_page = LoginPage(browser)
    opening_paragraph_element = login_page.get_opening_paragraph_text()
    highlight_element(browser, opening_paragraph_element)
    assert paragraph.replace('\n', ' ') == opening_paragraph_element.text


# Step to check if the given option text and subtext are displayed
@then(parsers.re(r'I should see the option "(?P<option_text>.+)" with text "(?P<text>.+)"'))
def check_option_with_text(browser, option_text, text):
    login_page = LoginPage(browser)
    option_element = login_page.find_element_text(option_text)
    option_element_subtext = login_page.find_element_subtext(option_text)
    highlight_element(browser, option_element)
    highlight_element(browser, option_element_subtext)
    assert option_text.upper() == option_element.text
    assert text.lower() == option_element_subtext.text.lower()


# Step to check if the button for the given option is displayed with the given text
@then(parsers.re(r'I should see the button for the option "(?P<option_text>.+)" with "(?P<button_text>.+)"'))
def check_button_for_option(browser, option_text, button_text):
    login_page = LoginPage(browser)
    option_element_link_text = login_page.find_element_link_text(option_text)
    highlight_element(browser, option_element_link_text)
    assert button_text.lower() == option_element_link_text.text.lower()


# Step to click the button for the given option and check if it's enabled
@then(parsers.parse('I should be able to click the button for the option "{option_text}" with "{link_text}"'))
def step_click_option(browser, option_text, link_text):
    login_page = LoginPage(browser)
    option_element_link_text = login_page.find_element_link_text(option_text)
    highlight_element(browser, option_element_link_text)
    assert option_element_link_text.is_enabled(), f"Element with text '{link_text}' is clickable"
    option_element_link_text.click()


# Step to navigate to the specified page and check if the page title and icon text are displayed
@then(parsers.parse(
    'should navigate to the "{page_title}" page see the Carleton360 login page title with icon "{icon_text}"'))
def step_navigate_to_page_with_title_and_icon(browser, page_title, icon_text):
    time.sleep(5)
    carleton360_login_page = Carleton360LoginPage(browser)
    assert icon_text == carleton360_login_page.get_page_title_text(), f"Not navigated to '{page_title}' page"


# Step to check if the given button text is displayed on the specified page
@then(parsers.re('I should see the "(?P<element_text>.*)" button on the "(?P<page_name>.*)" page'))
def step_see_button_re(browser, element_text, page_name):
    if page_name == "CARLETON 360 LOGIN":
        carleton360_login_page = Carleton360LoginPage(browser)
        scroll_to_top(browser)
        option_element_button_text = carleton360_login_page.find_element_button(element_text)
        highlight_element(browser, option_element_button_text)
        # assert element_text.lower() == option_element_button_text.text.lower()
        assert option_element_button_text.is_displayed(), f"Element with text '{element_text}' is not displayed"
    elif page_name == "Forgot password":
        forgot_pwd_page = ForgotPasswordPage(browser)
        option_element_button_text = forgot_pwd_page.get_go_button()
        highlight_element(browser, option_element_button_text)
        assert element_text.lower() == option_element_button_text.text.lower()
        assert option_element_button_text.is_displayed(), f"Element with text is not displayed"
    elif page_name == "Carleton SSO Federated Portal":
        carleton_sso_page = CarletonSSOLoginPage(browser)
        option_element_button_text = carleton_sso_page.find_element_button(element_text)
        highlight_element(browser, option_element_button_text)
        # assert element_text.lower() == option_element_button_text.text.lower()
        assert option_element_button_text.is_displayed(), f"Element with text '{element_text}' is not displayed"
    elif page_name == "Carleton 360 Registration":
        carleton360_registration_page = Carleton360RegistrationPage(browser)
        option_element_button_text = carleton360_registration_page.get_submit_button()
        highlight_element(browser, option_element_button_text)
        # assert element_text.lower() == option_element_button_text.text.lower()
        assert option_element_button_text.is_displayed(), f"Element with text '{element_text}' is not displayed"
    else:
        raise ValueError(f"Unsupported page name '{page_name}'. Please provide a valid page name.")


# Step to check if the panel title with the given text is displayed
@then(parsers.parse('I should see the "{panel_title}" panel title'))
def step_see_panel_title(browser, panel_title):
    carleton360_login_page = Carleton360LoginPage(browser)
    option_element_panel_title = carleton360_login_page.get_panel_title()
    highlight_element(browser, option_element_panel_title)
    assert panel_title.lower() == option_element_panel_title.text.lower()
    assert option_element_panel_title.is_displayed(), f"Element with text '{panel_title}' is not displayed"


# This step definition checks if the specified input box is visible and enabled on the specified page
@then(parsers.re('I should see the "(?P<input_label>.*)" input box on the "(?P<page_name>.*)" page'))
def step_see_input_box_re(browser, input_label, page_name):
    if page_name == "CARLETON 360 LOGIN":
        carleton360_login_page = Carleton360LoginPage(browser)
        option_element_input = carleton360_login_page.find_element_input(input_label)
        highlight_element(browser, option_element_input)
        assert option_element_input.is_displayed() and option_element_input.is_enabled(), f"Element with text '{input_label}' is not displayed"
    elif page_name == "Forgot password":
        forgot_pwd_page = ForgotPasswordPage(browser)
        option_element_input = forgot_pwd_page.find_element_input(input_label)
        highlight_element(browser, option_element_input)
        assert option_element_input.is_displayed() and option_element_input.is_enabled(), f"Element with text '{input_label}' is not displayed"
    elif page_name == "Carleton SSO Federated Portal":
        carleton_sso_page = CarletonSSOLoginPage(browser)
        option_element_input = carleton_sso_page.find_element_input(input_label)
        highlight_element(browser, option_element_input)
        assert option_element_input.is_displayed() and option_element_input.is_enabled(), f"Element with text '{input_label}' is not displayed"
    else:
        raise ValueError(f"Unsupported page name '{page_name}'. Please provide a valid page name.")


# This step definition allows clicking a button with the specified text on the specified page
@then(parsers.re('I should be able to click "(?P<button_text>.*)" button on the "(?P<page_name>.*)" page'))
def step_click_button(browser, button_text, page_name):
    if page_name == "CARLETON 360 LOGIN":
        carleton360_login_page = Carleton360LoginPage(browser)
        option_element_button_text = carleton360_login_page.find_element_button(button_text)
        highlight_element(browser, option_element_button_text)
        assert option_element_button_text.is_enabled(), f"Element with text '{button_text}' is expected to be clickable but is not"
        option_element_button_text.click()
    elif page_name == "Carleton SSO Federated Portal":
        carleton_sso_page = CarletonSSOLoginPage(browser)
        option_element_button_text = carleton_sso_page.find_element_button(button_text)
        highlight_element(browser, option_element_button_text)
        assert option_element_button_text.is_enabled(), f"Element with text '{button_text}' is expected to be clickable but is not"
        option_element_button_text.click()
    else:
        raise ValueError(f"Unsupported page name '{page_name}'. Please provide a valid page name.")


# This step definition checks if the user is redirected to the correct URL after performing an action
@then(parsers.parse('should redirected to the correct link page "{expected_url}"'))
def step_redirected_to_correct_link(browser, expected_url):
    wait_for_url_change(browser, expected_url)
    assert browser.current_url == expected_url


# This step definition validates the text of various elements on a page
@then(parsers.parse('should validate the text "{title}" "{subtitle}" "{note_label}" "{link_text}"'))
def step_validate_text(browser, title, subtitle, note_label, link_text):
    forgot_pwd_page = ForgotPasswordPage(browser)
    option_element_title = forgot_pwd_page.get_title()
    option_element_subtitle1 = forgot_pwd_page.get_sub_title1()
    option_element_subtitle2 = forgot_pwd_page.get_sub_title2()
    option_element_link_text = forgot_pwd_page.get_link_text()
    highlight_element(browser, option_element_title)
    highlight_element(browser, option_element_subtitle1)
    highlight_element(browser, option_element_subtitle2)
    highlight_element(browser, option_element_link_text)
    assert option_element_title.text == title
    assert option_element_subtitle1.text == subtitle
    assert option_element_subtitle2.text == note_label
    assert option_element_link_text.text == link_text


# This step definition allows clicking a link with the specified text on the specified page
@then(parsers.re('I should be able to click "(?P<link_text>.*)" link text on the "(?P<page_name>.*)" page'))
def step_click_link(browser, link_text, page_name):
    if page_name == "CARLETON 360 LOGIN":
        forgot_pwd_page = ForgotPasswordPage(browser)
        option_element_link_text = forgot_pwd_page.get_link_text()
        assert option_element_link_text.is_displayed() and option_element_link_text.is_enabled(), f"Element with text '{link_text}' is not displayed"
        option_element_link_text.click()

    elif page_name == "Carleton SSO Federated Portal":
        carleton_sso_page = CarletonSSOLoginPage(browser)
        option_element_link_text = carleton_sso_page.find_element_link_text(link_text)
        assert option_element_link_text.is_displayed() and option_element_link_text.is_enabled(), f"Element with text '{link_text}' is not displayed"
        option_element_link_text.click()

    elif page_name == "Forgot password":
        forgot_pwd_page = ForgotPasswordPage(browser)
        option_element_link_text = forgot_pwd_page.get_link_text()
        assert option_element_link_text.is_displayed() and option_element_link_text.is_enabled(), f"Element with text '{link_text}' is not displayed"
        option_element_link_text.click()

    elif page_name == "Carleton 360 Registration":
        carleton360_registration_page = Carleton360RegistrationPage(browser)
        option_element_link_text = carleton360_registration_page.find_element_link_text(link_text)
        assert option_element_link_text.is_displayed() and option_element_link_text.is_enabled(), f"Element with text '{link_text}' is not displayed"
        option_element_link_text.click()


@then(parsers.parse('should validate the redirected page "{expected_url}"'))
def step_validate_redirected_page(browser, expected_url):
    # Switch to the new tab
    browser.switch_to.window(browser.window_handles[-1])
    assert browser.current_url == expected_url


# This step definition checks if the specified input box is empty on the specified page
@then(parsers.parse('I should see an empty "{input_box}" input box on the "{page_name}" page'))
def step_see_empty_input_box(browser, input_box, page_name):
    if page_name == "CARLETON 360 LOGIN":
        carleton360_login_page = Carleton360LoginPage(browser)
        option_element_input = carleton360_login_page.find_element_input(input_box)
        highlight_element(browser, option_element_input)
        # Clear the input text box
        option_element_input.clear()

        # Check if the input text box is empty
        input_value = option_element_input.get_attribute("value")
        assert input_value == "", f"The input text box '{input_box}' is not empty."

    elif page_name == "Carleton SSO Federated Portal":
        carleton_sso_page = CarletonSSOLoginPage(browser)
        option_element_input = carleton_sso_page.find_element_input(input_box)
        highlight_element(browser, option_element_input)
        # Clear the input text box
        option_element_input.clear()

        # Check if the input text box is empty
        input_value = option_element_input.get_attribute("value")
        assert input_value == "", f"The input text box '{input_box}' is not empty."
    else:
        raise ValueError(f"Unsupported page name '{page_name}'. Please provide a valid page name.")


# This step definition checks if the specified error message is displayed on the page
@then(parsers.parse('I should see a "{error_type}" error message "{error_message}"'))
def step_see_error_message(browser, error_type, error_message):
    carleton360_login_page = Carleton360LoginPage(browser)
    option_element_error_text = carleton360_login_page.find_element_error_head(error_type)
    highlight_element(browser, option_element_error_text)
    assert error_type == option_element_error_text.text
    option_element_error_text_body = carleton360_login_page.find_element_error_body(error_type)
    highlight_element(browser, option_element_error_text_body)
    assert error_message == option_element_error_text_body.text


# This step definition allows entering text into the specified input box on the specified page
@then(parsers.parse('I should be able to enter "{text}" in "{input_box}" input box on the "{page_name}" page'))
def step_enter_text_in_input_box(browser, text, input_box, page_name):
    if page_name == "CARLETON 360 LOGIN":
        carleton360_login_page = Carleton360LoginPage(browser)
        option_element_input = carleton360_login_page.find_element_input(input_box)
        highlight_element(browser, option_element_input)
        # Clear the input text box
        option_element_input.clear()

        # Enter text into the input text box
        option_element_input.send_keys(text)

        input_value = option_element_input.get_attribute("value")
        assert input_value == text, f"The input text box '{input_box}' is empty."

    elif page_name == "Carleton SSO Federated Portal":
        carleton_sso_page = CarletonSSOLoginPage(browser)
        option_element_input = carleton_sso_page.find_element_input(input_box)
        highlight_element(browser, option_element_input)
        # Clear the input text box
        option_element_input.clear()

        # Enter text into the input text box
        option_element_input.send_keys(text)

        input_value = option_element_input.get_attribute("value")
        assert input_value == text, f"The input text box '{input_box}' is empty."

    else:
        raise ValueError(f"Unsupported page name '{page_name}'. Please provide a valid page name.")


# This step definition navigates to the specified page and checks if the page title matches the expected title
@then(parsers.parse('should navigate to the "{page_name}" page see the "{page_title}" page title'))
def step_navigate_to_page(browser, page_name, page_title):
    time.sleep(5)
    carleton_sso_page = CarletonSSOLoginPage(browser)
    assert page_title == carleton_sso_page.get_page_title_text(), f"Not navigated to '{page_name}' page"


# This step definition validates login messages on a page
@then(parsers.re('I should validate the login message "(?P<message1>.*)" "(?P<message2>.*)"'))
def step_validate_login_message(browser, message1, message2):
    carleton_sso_page = CarletonSSOLoginPage(browser)
    option_element_message1 = carleton_sso_page.get_login_message()
    option_element_message2 = carleton_sso_page.get_link_text()
    highlight_element(browser, option_element_message1)
    highlight_element(browser, option_element_message2)
    # assert option_element_message1.text in message1, f"Expected part of message '{message1}' not found in login message"
    assert option_element_message2.text == message2


# This step definition checks if the specified error message is displayed for a given error type
@then(parsers.parse('I should see a "{error_type}" error message for "{error_message}"'))
def step_see_error_message(browser, error_type, error_message):
    carleton_sso_page = CarletonSSOLoginPage(browser)
    option_element_error_text = carleton_sso_page.find_element_error_text(error_message)
    highlight_element(browser, option_element_error_text)
    assert error_type == option_element_error_text.text


# This step definition checks if input labels are visible on the Carleton 360 Registration page
@then(parsers.parse('I should see the input labels on the Carleton 360 Registration page\n{labels}'))
def validate_input_labels(browser, labels):
    label_list = parse_vertical_table(labels)
    carleton360_registration_page = Carleton360RegistrationPage(browser)

    for label in label_list:
        option_element_input = carleton360_registration_page.find_element_label(label)
        # Scroll to the element
        browser.execute_script("arguments[0].scrollIntoView();", option_element_input)
        highlight_element(browser, option_element_input)
        assert label == option_element_input.text


# This step definition validates various messages on a page
@then(parsers.re('I should validate the message "(?P<message1>.*)" "(?P<message2>.*)" "(?P<message3>.*)"'))
def step_validate_login_message(browser, message1, message2, message3):
    carleton360_registration_page = Carleton360RegistrationPage(browser)
    option_element_message1 = carleton360_registration_page.get_sub_title1()
    option_element_message2 = carleton360_registration_page.get_sub_title2()
    option_element_message3 = carleton360_registration_page.get_link_text()
    highlight_element(browser, option_element_message1)
    highlight_element(browser, option_element_message2)
    highlight_element(browser, option_element_message3)
    # assert option_element_message1.text in message1, f"Expected part of message '{message1}' not found in login message"
    assert option_element_message1.text == message1
    # assert option_element_message2.text == message2
    assert option_element_message3.text == message3


@then(parsers.parse('I should be able to click "{option_text}" input "{link_text}"'))
def step_click_option(browser, option_text, link_text):
    login_page = LoginPage(browser)
    option_element_link_text = login_page.find_element_link_text(option_text)
    highlight_element(browser, option_element_link_text)
    assert option_element_link_text.is_enabled(), f"Element with text '{link_text}' is clickable"
    option_element_link_text.click()


@then(parsers.parse('I should be able to click "{input_text}" input on the "{page_name}" page'))
def click_input(browser, input_text, page_name):
    carleton360_registration_page = Carleton360RegistrationPage(browser)
    input_element = carleton360_registration_page.find_element_input(input_text)
    # scroll_to_top(browser)
    # browser.execute_script("window.scrollTo(0, arguments[0].offsetTop);", input_element)
    # highlight_element(browser, input_element)
    assert input_element.is_enabled(), f"Element with text '{input_text}' is clickable"
    input_element.click()


@then(parsers.parse('the dropdown contains the following "{list_options}"\n{options}'))
def verify_dropdown_options(browser, datatable, list_options, options):
    option_list = parse_vertical_table(options)
    carleton360_registration_page = Carleton360RegistrationPage(browser)

    for option in option_list:
        option_element_input = carleton360_registration_page.get_drop_down_list(list_options, option)
        # # Scroll to the element
        # browser.execute_script("arguments[0].scrollIntoView();", option_element_input)
        # browser.execute_script("window.scrollTo(0, arguments[0].offsetTop);", option_element_input)

        if option_element_input is not None:
            highlight_element(browser, option_element_input)


@then(parsers.parse('I select "{option}" from the dropdown list for the "{list_options}"'))
def select_option_from_dropdown(browser, option, list_options):
    time.sleep(1)
    Carleton360RegistrationPage(browser).get_drop_down_list(list_options, option).click()
