import pytest

from POM_FrameWork.Pages.accountsummarypage import AccountSummaryPage
from POM_FrameWork.Pages.home_page import HomePage
from POM_FrameWork.Pages.login_page import LoginPage
from POM_FrameWork.Pages.logoutpage import LogoutPage
from POM_FrameWork.Pages.pay_bills import PayBills
from POM_FrameWork.Test_Data.read_excel_data import get_data
from ctreport_selenium.ctlistener import Test, Priority, Severity


class Test_AddNewPayee:
    test=None

    @pytest.fixture(scope="class", autouse=True)
    def page(self, driver):
        home = HomePage(driver)
        home.click_Signin_button()
        login = LoginPage(driver)
        login.do_login("username", "password")
        account = AccountSummaryPage(driver)
        account.click_pay_bills()
        yield
        logout = LogoutPage(driver)
        logout.do_logout()

    @pytest.fixture(autouse=True)
    def pay_bills(self, driver):
        self.paybills = PayBills(driver) # We made it as global variable to use anywhere.
        self.paybills.click_add_new_payee()


    @pytest.mark.parametrize("name, addr, acc, details", get_data())
    def test_addnewpayee(self, name, addr, acc, details):
        self.test = Test("Add New Payee", +name, Descripton="adding a new payee to zero bank", priority=Priority.HIGH)
        self.test.log("Navigated Successfully for Add new payee page")
        self.paybills.do_addnewpayee(name, addr, acc, details)
        self.test.log("Successfully added new payee")

    def tear_down_method(self, method):
        Test_AddNewPayee.test=self.test


