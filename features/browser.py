from selenium import webdriver

class Browser(object):

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.implicitly_wait(5)
    #driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()
