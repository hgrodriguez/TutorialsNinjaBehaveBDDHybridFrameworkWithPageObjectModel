"""Search page"""
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchPage(BasePage):
    """Search page"""

    valid_product_link_text = "HP LP3065"
    message_xpath = "//input[@id='button-search']/following-sibling::p"
    error_message_xpath = "/html/body/div[2]/div/div/p[2]"

    def display_status_of_product(self):
        """Status of the product"""
        return self.display_status(
            "valid_product_link_text", self.valid_product_link_text
        )

    def display_status_of_message(self, expected_message_text):
        """ "Status message"""
        return self.retrieved_element_text_equals(
            "message_xpath", self.message_xpath, expected_message_text
        )

    def status_of_error_message(self, expected_message_text):
        """Check, if the message has the expected text."""
        return self.retrieved_element_text_equals("error_message_xpath",
                                                  self.error_message_xpath,
                                                  expected_message_text)
