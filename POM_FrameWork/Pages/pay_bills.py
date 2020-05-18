from POM_FrameWork.Pages.Base_Page import BasePage
from selenium.webdriver.common.by import By

# Class inherit BasePage.
class PayBills(BasePage):
    add_new_payee_link = By.XPATH, "//a[text()='Add New Payee']"
    payee_name = By.ID, "np_new_payee_name"
    payee_address = By.ID, "np_new_payee_address"
    payee_account = By.ID, "np_new_payee_address"
    payee_details = By.ID, "np_new_payee_details"
    add_button = By.ID, "add_new_payee"

# Actions:
    def click_add_new_payee(self):
        self._click(self.add_new_payee_link)

    def do_addnewpayee(self, name, addr, acc, details):
        self._wait_for_element(self.payee_name, "visibility").send_keys(name)
        self._enter_text(self.payee_address, addr)
        self._enter_text(self.payee_account, acc)
        self._enter_text(self.payee_details, details)
        self._click(self.add_button)







