import random

from ..BaseTesCase import BaseTestCase


class SanityChecksTests(BaseTestCase):

    def test_successfullLogin(self):
        self.page = self.page.loginWithProperData(self.envSettings.User)
        self.assertTrue(self.page.topMenu.isLoggedUserAsExpected(self.envSettings.User))

    def test_loginWithWrongCredentials(self):
        user = self.envSettings.User
        user.password += random.choice("abcdefghi12345")
        self.page.loginWithWrongData(user).\
            checkWrongLoginErrorMessage()