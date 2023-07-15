"""Behave hooks
https://behave.readthedocs.io/en/stable/index.html
"""
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities import config_reader


def before_scenario(context, driver):  # pylint: disable=unused-argument
    """ "before all scenarios, get ready"""
    chrome_options = Options()
    #    chrome_options.add_argument(
    #        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"\
    #        + " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"\
    #        + " Safari/537.36")
    #    chrome_options.add_argument("--headless")
    # chrome_options.headless = True  # also works

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    context.driver.get(config_reader.read_configuration("basic info", "url"))


def after_scenario(context, driver):  # pylint: disable=unused-argument
    """After all scenarios"""
    context.driver.quit()


def after_step(context, step):
    """After every step"""
    if step.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="failed_screenshot",
            attachment_type=AttachmentType.PNG,
        )
