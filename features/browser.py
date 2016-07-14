from selenium import webdriver


class Browser(object):
    driver = webdriver.Remote(
    desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
    command_executor='http://192.168.1.123:4444/wd/hub')
    #driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.implicitly_wait(5)
    #driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()
