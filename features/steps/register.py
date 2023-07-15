"""Implements the register page"""
# pylint: disable=wildcard-import,unused-wildcard-import

from behave import *  # noqa: F403
from features.pages.home_page import HomePage
from utilities.email_with_timestamps_generator import get_new_email_with_timestamp


@given("I navigate to Register Page")  # noqa: F405
def step_navigate(context):
    """X"""
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.select_register_option()


@when("I enter below details into mandatory fields")  # noqa: F405
def step_enter_mandatory_fields(context):
    """X"""
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        new_email = get_new_email_with_timestamp()
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])


@when("I select Privacy Policy option")  # noqa: F405
def step_privacy_option(context):
    """X"""
    context.register_page.select_privacy_policy()


@when("I click on Continue button")  # noqa: F405
def step_continue(context):
    """X"""
    context.account_success_page = context.register_page.click_on_continue_button()


@then("Account should get created")  # noqa: F405
def step_create_account(context):
    """X"""
    assert context.account_success_page.display_status_of_account_created_heading(
        "Your Account Has Been Created!"
    )


@when("I enter below details into all fields")  # noqa: F405
def step_fill_all_fields(context):
    """X"""
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        new_email = get_new_email_with_timestamp()
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
        context.register_page.select_yes_newsletter_option()


@when("I enter details into all fields except email field")  # noqa: F405
def step_all_details_except_mail(context):
    """X"""
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
        context.register_page.select_yes_newsletter_option()


@when("I enter existing accounts email into email field")  # noqa: F405
def step_existing_email(context):
    """X"""
    context.register_page.enter_email("amotooriApril202328190133@gmail.com")


@then(
    "Proper warning message informing about duplicate account should be displayed"
)  # noqa: F405
def step_proper_warning(context):
    """X"""
    assert context.register_page.display_status_of_duplicate_email_warning(
        "Warning: E-Mail Address is already registered!"
    )


@when("I dont enter anything into the fields")  # noqa: F405
def step_empty_fields(context):
    """X"""
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_password_confirm("")


@then(
    "Proper warning messages for every mandatory fields should be displayed"
)  # noqa: F405
def step_proper_warning_2(context):
    """X"""
    assert context.register_page.display_status_of_all_warning_messages(
        "Warning: You must agree to the Privacy Policy!",
        "First Name must be between 1 and 32 characters!",
        "Last Name must be between 1 and 32 characters!",
        "E-Mail Address does not appear to be valid!",
        "Telephone must be between 3 and 32 characters!",
        "Password must be between 4 and 20 characters!",
    )
