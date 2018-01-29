from ..BasePage import BasePage
from ..Recruiter.Common.TopMenu import TopMenu


class HomePage(BasePage):

     def __init__(self, driver, browser):
         super(HomePage, self).__init__(driver, browser)
         self.topMenu = TopMenu(self.driver, self.browser)