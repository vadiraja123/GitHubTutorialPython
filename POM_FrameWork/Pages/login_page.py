from POM_FrameWork.Pages.Base_Page import BasePage
from selenium.webdriver.common.by import By

# Class inherit BasePage.
class LoginPage(BasePage):

# Locators:
    uname_inputtext = By.ID, "user_login"
    pword_inputtext = By.ID, "user_password"
    signin_button = By.NAME, "submit"

# Actions:
    def do_login(self, uname, pword):
        self._enter_text(self.uname_inputtext, uname)
        self._enter_text(self.pword_inputtext, pword)
        self._click(self.signin_button)



