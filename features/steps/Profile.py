# -*- coding: utf-8 -*-

from nose.tools import assert_equal, assert_true


@step('I navigate to the Delivery Club Home page and Login')
def step_impl(context):
    context.home_page.navigate("https://delivery-club.ru")
    assert_equal(context.home_page.get_page_title(), "«Delivery Club» — круглосуточная доставка из любимых ресторанов города")
    context.home_page.login_main_page()



@step('I go to Profile and click Edit')
def go_to_edit_profile(context):
    context.home_page.enter_profile_in_main_page()
    context.profile.button_edit_profile_click()



@step('I edit "Имя", email and mailing flags and save change')
def edit_profile(context):
    context.profile.profile_email()
    context.profile.profile_mob_phone1()
    context.profile.profile_name()
    # context.profile.profile_subscribed()
    context.profile.button_save_profile()

@step('Then I see that the changes are preserved')
def assert_profile_change(content):
    pass
