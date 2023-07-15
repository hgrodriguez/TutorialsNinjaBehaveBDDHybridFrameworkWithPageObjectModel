"""Base page for all webpages"""
from selenium.webdriver.common.by import By


class BasePage:
    """Base page for all webpages"""

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator_type, locator_value):
        """Clicks on element"""
        element = self.get_element(locator_type, locator_value)
        element.click()

    def verify_page_title(self, expected_title):
        """Verifies the title of the page"""
        return self.driver.title == expected_title

    def type_into_element(self, locator_type, locator_value, text_to_entered):
        """Enters the text into the element"""
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_entered)

    def get_element(self, locator_type, locator_value):
        """Locates an element based on the locator type"""
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def retrieved_element_text_contains(
        self, locator_type, locator_value, expected_text
    ):
        """Checks, if the element contains the expected text"""
        element = self.get_element(locator_type, locator_value)
        return expected_text in element.text

    def retrieved_element_text_equals(self, locator_type, locator_value, expected_text):
        """Checks, if the element has the texpected text"""
        element = self.get_element(locator_type, locator_value)
        return element.text == expected_text

    def return_and_status(
        self,
        privacy_status,
        first_name_status,
        last_name_status,
        email_status,
        telephone_status,
        password_status,
    ):
        """Checks the status across all elements"""
        if (
            privacy_status
            and first_name_status
            and last_name_status
            and email_status
            and telephone_status
            and password_status
        ):
            return True
        else:
            return False

    def display_status(self, locator_type, locator_value):
        """Checks, if the element is displayed"""
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()
