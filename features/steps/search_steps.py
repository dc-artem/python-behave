# -*- coding: utf-8 -*-

from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I navigate to the Delivery Club Home page')
def step_impl(context):
    context.home_page.navigate("https://delivery-club.ru")
    assert_equal(context.home_page.get_page_title(), "u«Delivery Club» — круглосуточная доставка из любимых ресторанов города")


@step('I Login in Home Page')
def login_home_page(context):
    context.home_page.login_main_page()
    #assert_true((len(context.home_page.assert_balls) != 0))

@step('I go to Profile')
def go_to_profile(context):
    context.home_page.enter_profile_in_main_page()

@step('I delete first address')
def dell_first_adress(context):
    context.home_page.del_address_in_profile()

@step('I delete any address in list')


# @step('I search for "{search_term}"')
# def step_impl(context, search_term):
#     context.home_page.search(search_term)

@step('I check the address removed')
def step_impl(context):
    pass

@step('I logout')
def logout(context):
    context.home_page.logout()
