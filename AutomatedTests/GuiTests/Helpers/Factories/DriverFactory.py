import selenium.webdriver as webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DriverFactory:

    @staticmethod
    def getWebdriver(browserName):
        browserName = browserName.lower()
        if browserName == 'firefox':
            return webdriver.Firefox()
        elif browserName == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            return webdriver.Chrome(chrome_options=options)
        elif browserName == 'ie':
            ieCapabilities = DesiredCapabilities.INTERNETEXPLORER
            ieCapabilities['ie.ensureCleanSession'] = True
            return webdriver.Ie(capabilities=ieCapabilities)
        raise Exception("No such '{0}' browser exists".format(browserName))