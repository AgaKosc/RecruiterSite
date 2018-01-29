from ..BaseTesCase import BaseTestCase


class NewQuestionTests(BaseTestCase):

    def test_createNewQuestion(self):
        self.page.loginWithProperData(self.envSettings.User).\
            topMenu.openNewQuestionPage()