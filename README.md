# UI Testing with Selenium Python & Pytest BDD - Page Object Model for Carleton 360

## Overview

This project provides an example for testing the Carleton 360 UI with Selenium WebDriver, written in Python, using the
Page Object Model design pattern and driven via BDD feature files through Pytest BDD. It can be used to kickstart
testing of other UIs with minimal changes to the project.

This test suite focuses on the following pages:

Carleton 360 Login
Carleton SSO Federated Portal
Carleton 360 New Registration

## Why Use Selenium?

Selenium is a widely recognized open-source framework for testing web applications, often considered the go-to choice
for UI testing. Its compatibility with a variety of browsers (including Chrome, Firefox, Safari, and IE/Edge) and
support for major programming languages (such as Java, Python, JavaScript, C#, and Ruby) make it highly versatile and
suitable for nearly any UI testing project. Moreover, Selenium is highly portable, functioning seamlessly across
Windows, macOS, and Linux/Unix operating systems. As a freeware solution, it provides an accessible option for users.
Furthermore, the extensive and active Selenium community offers valuable support, contributing to the framework's
ongoing development and improvement.

## Web Application Under Test

The website being tested by this framework is Carleton University's web
portal “https://360.carleton.ca/urd/sits.urd/run/siw_lgn “, which encompasses the Carleton 360 New Registration,
Carleton 360 Login, and Carleton SSO Federated Portal pages. These pages are part of a comprehensive web platform that
presents various aspects of UI testing, showcasing the challenges one may encounter when implementing such tests. As a
result, the Carleton University web portal is an excellent choice for practicing automated testing in a realistic
setting.

For this demonstration, we will be focusing on testing a subset of the available functionality, including:

* Carleton 360 New Registration page
* Carleton 360 Login page
* Carleton SSO Federated Portal page
  By concentrating on these pages, we can effectively demonstrate the main interaction and verification methods in
  Selenium, while maintaining a project size that is compact enough to serve as a template.

## Test Framework

The test framework follows the structure and principles outlined in the original README. The main difference is that the
features, pages, and step_defs folders contain files specific to the Carleton 360 application. For example, the features
folder now includes Carleton_360_Login.feature.

### Tech stack

As this is a Python project, build and dependency management is handled by Pipenv, so there is a `Pipfile` (and
associated `.lock` file) defining the versions of the dependencies:

* Python v3.11.1
* Selenium v4.8.3
* Pytest v7.3.1
* Pytest BDD v6.1.1
* Webdriver-Manager v3.8.6

The code is written in Python and built using v3.11.1. This is the most up-to-date Pythons versions available - v3.11.1
being the latest at the time of writing (released 24th October 2019) as it is the version I am most used to and what was
installed when I began this project.

The Selenium version is from November 2018 but is the latest Selenium v3 release and also the latest production
release (all the v4 releases are currently alpha or beta).

I have chosen to use the latest Pytest release (v6.2.4, released May 2021) even though it is more recent than the Python
version I am using.

Similarly, I am using the latest Pytest BDD version (v4.1.0, released July 2021). Other BDD frameworks are available for
Python (e.g. `behave`) but Pytest BDD is the one I am familiar with so seemed like the natural choice at this stage.

Sttable is a small plugin that adds simple support for data tables within BDD scenarios and feature files. This
functionality is native to Cucumber (Java) but seemingly not in Pytest BDD so this additional plugin is required. I have
used the latest version at the time of writing.

Webdriver-manager is a third-party plugin that makes it easier to manage the drivers for multiple browsers, making
cross-browser testing simpler. It is similar to the extension I commonly use for Selenium Java projects. In this project
I am using the latest version (from May 2021).

### Project Structure

Project Structure
The project structure remains the same as in the original README, with the following adjustments to accommodate Carleton
360:

* `features` - This folder contains the Gherkin .feature file for the Carleton 360 pages: Carleton_360_Login.feature.
* `pages` - The Page Object Model implementation of the individual Carleton 360 pages: login page, forgotPassword page,
  carleton360_Registration Page, carleton360_Login Page, and carletonSSO_Login Page. Each class is named after the
  corresponding page. For example, the `carleton360_Login Page` class in the `Carleton360_Login.py` file. There is also
  a `BasePage` which the other page classes implement/extend through inheritance.
* `step_defs` - A collection of files containing the implementation of the steps from the BDD feature files for the
  Carleton 360 pages: test_carleton360_registration_steps.py, test_carleton360_login_steps.py, and
  test_carleton_sso_login_steps.py.

* `config.json` - a JSON object used to define certain configuration options such as the browser, whether to run
  headless and the implicit wait timeout.
* `conftest.py` - This file contains methods to set up the browser (having read in the required parameters from
  the `config.json` file) and make that available to the page methods. It also sets up a few methods required to fully
  utilise data tables in feature files. Finally, steps that are common across multiple feature files (with the exception
  of the page title steps noted above) are contained within this file.

UI_Testing_Carleton_360
│
├─── features
│    └─── Carleton_360_Login.feature
│
├─── pages
│    ├─── BasePage.py
│    ├─── Carleton360_Login.py
│    ├─── Carleton360_Registration.py
│    ├─── CarletonSSO_Login.py
│    └─── ForgotPassword.py
│
├─── step_defs
│    ├─── test_carleton360_login_steps.py
│    ├─── screenshots
│    └─── report
│
├─── config.json
├─── conftest.py
├─── Pipfile
├─── Pipfile.lock
└─── README.md
This folder structure organizes the various components of your project, including the feature files, page object models, step definitions, and configuration files. It also includes a screenshots folder for storing any captured screenshots of failed test cases.


### Page Object Model Classes

As noted above, the `pages` folder contains the relevant Page Object Model classes for each tested page. Each page
class, including the abstract `BasePage` class, follows the same pattern:

* selector/locator tuples declared as pairs, the first element being the locator method (`By.ID`, `By.XPATH` etc) and
  the second element being the locator itself (i.e. the ID, xpath etc).
* interaction methods e.g. to click on an element, get an element’s text etc. These methods use the above locator
  tuples, passing them to `find_element` or `find_elements` calls

This way we encapsulate the web elements themselves, only allowing the interactions that have been implemented via our
methods, ensuring the tests (in effect, the user) can only interact with the web page in known ways.

The `BasePage` class defines constants for the URL for each page, ensuring they are available to methods within each
individual page class. Also declared in the base class are a some common locators for elements used on multiple pages to
avoid the need to declare the locator in each page class (following the DRY principle). Interaction methods for the page
header and footer are declared in the `BasePage` class too, again to reduce code duplication. In order to get round the
fact that the title element on the tested pages doesn't use a consistent HTML tag or class, an
abstract `get_page_title_text` method is declared in the `BasePage` class ensuring that each individual page class
implements a method to get the text of the page title, using a `PAGE_TITLE` locator specific to whatever to that page’s
HTML uses for the title.

Note there are no assertions in the page classes as assertions are a test action rather than a page action. Page
interaction methods will return the result of that interaction, such as the attribute or text value, to the calling
method in the test steps classes, so that it can be asserted as correct there. In other words, we maintain independence
between the tests and the pages.

### Supported Browsers

The `conftest.py` module uses the Webdriver-Manager dependency to manage the various browser drivers. The `browser`
Pytest fixture returns the relevant WebDriver instance for the chosen browser, with support for:

* Chrome - the default option
* Firefox

The browser to be used can be passed in via a Pytest command line parameter with a key of `browser`, defaulting to
Chrome if no such property is specified. Alternatively, the `browser` parameter can be configured via the `config.json`
file.

The `headless` property is used to determine whether the browser should run in headless mode. Headless browsers are
generally faster and consume fewer resources as they don’t actually render the webpages so are preferred when running
automated UI tests. However, when debugging UI tests it is often easier to set this flag to false i.e. run “headed” so
that issues with the tests can be more easily identified. `headless` is true by default but can be changed in
the `config.json` file; it has not been enabled as a command line paramter at this stage.

The Webdriver-Manager plugin also has support for Edge, Opera and Internet Explorer but I have not enabled these options
in this project at this stage.

### Running tests

Running tests
To run the tests, follow the same steps as in the original README. To run the tests for an individual Carleton 360 page,
pass the associated steps file as a parameter to the command. For example, to run just the Carleton 360 login tests:
"pipenv run pytest .\step_defs\test_Carleton360_Login_steps.py" or "=pytest -k Validating_the_Carleton_360_login_home_page --html=report.html"
or just click the run button if using PyCharm.

NB Each test opens up in a separate browser instance (which is closed at the end of the test) so is not the fastest way
to run a test suite, but it is the right way as we should ensure that tests are wholly independent of one another, do
not share state and can run in any order. There are no `BeforeAll` and `AfterAll` hooks (that I am aware of), so we
can’t open a single browser at the start of the test suite, navigate to the relevant page in the setup for each
individual test scenario and close the browser at the end of the test suite. Having a separate browser per test also
allows for test parallelization which wouldn't otherwise be possible.

#### Test Reports

For every test execution, a comprehensive report is created and saved within the step_defs directory. This report
presents an organized list of the executed step classes, each of which is linked to its corresponding feature file, and
provides an overall summary of the test results. In case a test scenario fails, the report displays the discrepancy
between the actual and expected outcomes, along with a screenshot to facilitate efficient debugging and analysis.