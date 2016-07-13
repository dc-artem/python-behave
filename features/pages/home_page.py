from selenium.webdriver.common.by import By
from browser import Browser
import time

class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "term")
    SUBMIT_BUTTON = (By.ID, "submit")


class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        wd = self.driver
        wd.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        wd = self.driver
        wd.find_element(*locator).click()

    def navigate(self, address):
        wd = self.driver
        wd.get(address)

    def get_page_title(self):
        wd = self.driver
        return wd.title

    def search(self, search_term):
        wd = self.driver
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)

    def login_main_page(self, username="atom2k@gmail.com1", password="111111"):
        wd = self.driver
        wd.find_element_by_link_text("Вход / Регистрация").click()
        wd.find_element_by_name("c_l").click()
        wd.find_element_by_name("c_l").clear()
        wd.find_element_by_name("c_l").send_keys(username)
        wd.find_element_by_name("c_p").click()
        wd.find_element_by_name("c_p").clear()
        wd.find_element_by_name("c_p").send_keys(password)
        wd.find_element_by_css_selector("a.sbm").click()

    def logout(self):
        wd = self.driver
        wd.find_element_by_css_selector("span.user-profile__span").click()
        wd.find_element_by_xpath("//ul[@class='user-profile__list']//span[.='Выход']").click()

    def assert_balls(self):
        wd = self.driver
        return (len(wd.find_elements_by_id("user-points") !=0))

    def enter_profile_in_main_page(self):
        wd = self.driver
        if wd.current_url.endswith("/profile/") and len(wd.find_elements_by_css_selector("a.bttn")) > 0:
            return
        wd.find_element_by_css_selector("span.user-profile__span").click()
        wd.find_element_by_css_selector("span.user-profile__title").click()

    def del_address_in_profile(self):
        wd = self.driver
        wd.find_element_by_css_selector("a.delete_uaddress").click()
        time.sleep(2)
        alert = wd.switch_to_alert()
        alert.accept()
        time.sleep(2)