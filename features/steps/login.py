"""Implements the login page feature"""
# pylint: disable=wildcard-import,unused-wildcard-import

from behave import *  # noqa: F403
from features.pages.home_page import HomePage
from utilities.email_with_timestamps_generator import get_new_email_with_timestamp


@given("I navigated to Login page")  # noqa: F405
def step_navigate_to_login_page(context):
    """X"""
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.select_login_option()


@when(
    'I enter valid email address as "{email}" and valid password as "{password}" into the fields'
)
def step_valid_email_password(context, email, password):
    """X"""
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when("I click on Login button")  # noqa: F405
def step_login(context):
    """X"""
    context.account_page = context.login_page.click_on_login_button()


@then("I should get logged in")  # noqa: F405
def step_logged_in(context):
    """X"""
    assert context.account_page.display_status_of_edit_your_account_information_option()


@when(
    'I enter invalid email and valid password say "{password}" into the fields'
)  # noqa: F405
def step_invalid_email_valid_password(context, password):
    """X"""
    invalid_email = get_new_email_with_timestamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@then("I should get a proper warning message")  # noqa: F405
def step_proper_warning_message(context):
    """X"""
    assert context.login_page.display_status_of_warning_message(
        "Warning: No match for E-Mail Address and/or Password."
    )


@when(
    'I enter valid email say "{email}" and invalid password say "{password}" into the fields'
)  # noqa: F405
def step_email_invalid_password(context, email, password):
    """X"""
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(
    'I enter invalid email and invalid password say "{password}" into the fields'
)  # noqa: F405
def step_invalid_email_invalid_password(context, password):
    """X"""
    invalid_email = get_new_email_with_timestamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@when("I dont enter anything into email and password fields")  # noqa: F405
def step_empty_email_password(context):
    """X"""
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
