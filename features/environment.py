from selenium import webdriver
from features.browser import Browser
from features.pages.home_page import HomePage
from features.pages.search_results_page import SearchResultsPage
from features.pages.profile import Profile

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.profile = Profile()
    context.search_results_page = SearchResultsPage()

def after_all(context):
    context.browser.close()
