import logging

from selenium.webdriver.common.by import By

from ...BasePage import BasePage


class TopMenu(BasePage):

    LoggedUser = (By.ID, 'userMenu')
    QuestionMenu = (By.ID, 'questionMenu')
    QuestionListLink = (By.LINK_TEXT, 'Questions List')
    NewQuestionLink = (By.LINK_TEXT, 'Add Question')

    def isLoggedUserAsExpected(self, user):
        logging.info("Checking if logged user is as expected: {0}".format(user.login))
        self.waitUntilElementIsVisible(self.LoggedUser)
        currentLoggedUser = self.driver.find_element(*self.LoggedUser).text.strip()
        return currentLoggedUser == user.login

    def openNewQuestionPage(self):
        logging.info("Opening New Question page")
        self.waitUntilElementIsVisible(self.QuestionMenu)
        self.driver.find_element(*self.QuestionMenu).click()
        self.waitUntilElementIsClickable(self.NewQuestionLink)
        self.driver.find_element(*self.NewQuestionLink).click()
        from ..Questions.NewQuestionPage import NewQuestionPage
        return NewQuestionPage(self.driver, self.browser)
