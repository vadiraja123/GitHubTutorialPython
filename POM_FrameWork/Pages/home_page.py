
from selenium.webdriver.common.by import By

# Class inherit BasePage.
from POM_FrameWork.Pages.Base_Page import BasePage


class HomePage(BasePage):
# Locators:
    Signin_button = By.ID, "signin_button"
    feedback_link = By.XPATH, "//strong[text()='Feedback']"
    onlinebanking_link = By.XPATH, "//strong[text()='Online Banking']"

# Actions:
    def click_Signin_button(self):
        self._click(self.Signin_button)

    def click_onlinebanking_link(self):
        self._click(self.onlinebanking_link)



