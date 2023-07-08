import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context,driver):

    browser_name = ConfigReader.read_configuration("basic info","browser")

    context.driver = webdriver.Chrome()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info","url"))


def after_scenario(context,driver):
    context.driver.quit()


def after_step(context,step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="failed_screenshot"
                      ,attachment_type=AttachmentType.PNG)
