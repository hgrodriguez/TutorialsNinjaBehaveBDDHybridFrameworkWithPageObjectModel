"""Implements the account page model"""
from selenium.webdriver.common.by import By


class AccountPage:
    """Implements the account page model"""

    def __init__(self, driver):
        self.driver = driver

    edit_account_info_option = "Edit your account information"

    def display_status_of_edit_your_account_information_option(self):
        """finds the element"""
        return self.driver.find_element(
            By.LINK_TEXT, self.edit_account_info_option
        ).is_displayed()
