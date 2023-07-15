"""Home page of the application"""

from features.pages.base_page import BasePage
from features.pages.login_page import LoginPage
from features.pages.register_page import RegisterPage
from features.pages.search_page import SearchPage


class HomePage(BasePage):
    """Home page of the application"""

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"

    def click_on_my_account(self):
        """Simulates a click on the account"""
        self.click_on_element("my_account_option_xpath",
                              self.my_account_option_xpath)

    def select_login_option(self):
        """Selects the login option"""
        self.click_on_element("login_option_link_text",
                              self.login_option_link_text)
        return LoginPage(self.driver)

    def select_register_option(self):
        """Simulates a click on the register option"""
        self.click_on_element(
            "register_option_link_text", self.register_option_link_text
        )
        return RegisterPage(self.driver)

    def check_home_page_title(self, expected_title_text):
        """Checks, if the title is as expected"""
        return self.verify_page_title(expected_title_text)

    def enter_product_into_search_box_field(self, product_text):
        """Enters text into the search box"""
        self.type_into_element(
            "search_box_field_name", self.search_box_field_name, product_text
        )

    def click_on_search_button(self):
        """Clicks on search button"""
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)
