# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium import *
from browser import Browser
import time
import json
import os.path

target = None

# def load_config(file):
#     global target
#     if target is None:
#         config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
#         with open(config_file) as f:
#             target = json.load(f)
#     return target

with open('target.json','r', encoding='utf-8') as fh:
    data = json.load(fh)

name = data['name']
email = data['email']
phone = data['phone']
testname = data['testname']
testemail = data['testemail']
testphone = data['testphone']


class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "term")
    SUBMIT_BUTTON = (By.ID, "submit")


class Profile(Browser):
    # Home Page

    with open('target.json','r', encoding='utf-8') as fh:
        data = json.load(fh)

    def testingemail(self, testemail):
        testemail = data['testemail']


    email = data['email']
    phone = data['phone']
    testname = data['testname']
    testemail = data['testemail']
    testphone = data['testphone']
    name = data['name']


    def navigate(self, address):
        wd = self.driver
        wd.get(address)

    def button_edit_profile(self):
        wd = self.driver
        wd.find_element_by_css("a.bttn")

    def button_edit_profile_click(self):
        wd = self.driver
        wd.find_element_by_css_selector("a.bttn").click()

    def profile_name(self):
        wd = self.driver
        wd.find_element_by_id("name").click()
        wd.find_element_by_id("name").clear()
        wd.find_element_by_id("name").send_keys(name)

    def profile_email(self):
        wd = self.driver
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        time.sleep(3)
        wd.find_element_by_id("email").send_keys(testemail)

    def profile_mob_phone1(self):
        wd = self.driver
        wd.find_element_by_id("phone1").click()
        wd.find_element_by_id("phone1").clear()
        wd.find_element_by_id("phone1").send_keys(testphone)

    def profile_subscribed(self):
        wd = self.driver
        wd.find_element_by_name("subscribed").click()
        wd.find_element_by_name("enable_sms").click()
        wd.find_element_by_name("enable_email").click()

    def button_save_profile(self):
        wd = self.driver
        wd.find_element_by_css_selector("a.button_static.green.edit-profile-form__submit").click()



