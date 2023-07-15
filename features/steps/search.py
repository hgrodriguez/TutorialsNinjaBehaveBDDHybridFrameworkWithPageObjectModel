"""Implements the search steps"""
# pylint: disable=wildcard-import,unused-wildcard-import

from behave import *  # noqa: F403
from features.pages.home_page import HomePage


@given("I got navigated to Home page")  # noqa: F405
def step_home_page(context):
    """X"""
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_home_page_title("Your Store")


@when('I enter valid product say "{product}" into the Search box field')  # noqa: F405
def step_valid_product(context, product):
    """X"""
    context.home_page.enter_product_into_search_box_field(product)


@when("I click on Search button")  # noqa: F405
def step_click(context):
    """X"""
    context.search_page = context.home_page.click_on_search_button()


@then("Proper message should be displayed in Search results")  # noqa: F405
def step_proper_message(context):
    """X"""
    assert context.search_page.display_status_of_message(
        "There is no product that matches the search criteria.ABC"
    )


@then("Valid product should get displayed in Search results")  # noqa: F405
def step_valid_product_displayed(context):
    """X"""
    assert context.search_page.display_status_of_product()


@when('I enter invalid product say "{product}" into the Search box field')  # noqa: F405
def step_invalid_product(context, product):
    """X"""
    context.home_page.enter_product_into_search_box_field(product)


@when("I dont enter anything into Search box field")  # noqa: F405
def step_empty_search(context):
    """X"""
    context.home_page.enter_product_into_search_box_field("")
