from POM_FrameWork.Pages.Base_Page import BasePage
from selenium.webdriver.common.by import By

# Class inherit BasePage.
class AccountSummaryPage(BasePage):
    pay_bills = By.XPATH, "//a[text()='Pay Bills']"
    title_link = By.XPATH, "//a[text()='Zero Bank']"

# Actions:
    def click_pay_bills(self):
        self._click(self.pay_bills)

    def click_title_link(self):
        self._click(self.title_link)



