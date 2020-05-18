import pytest

from POM_FrameWork.Pages.accountsummarypage import AccountSummaryPage
from POM_FrameWork.Pages.home_page import HomePage
from POM_FrameWork.Pages.login_page import LoginPage
from POM_FrameWork.Pages.onlinebankingpage import OnlineBankingPage

class Test_Validating_Links:
    test = None

    @pytest.fixture(scope="class", autouse=True)
    def page(self, driver):
        home = HomePage(driver)
        home.click_onlinebanking_link()

    @pytest.mark.parametrize("feature_name", ["Account Summary", "Account Activity", "Transfer Funds"])
    def test_validating_without_signin(self, driver, feature_name):
        self.test = Test("Validating feature link without signin", +feature_name)
        self.test.log("Navigate online banking page")
        onlineBanking = OnlineBankingPage(driver)
        onlineBanking.click_feature_link(feature_name)
        self.test.verify_are_equal(driver.title, "Zero - Log in", True, "Verify the title of the page",
                                   Sevrity.critical)
        self.test.log("Navigate to the signin page")

       # assert driver.title == "Zero - Log in"
        driver.back()

    @pytest.fixture(scope="class")
    def signin(self, driver):
        home = HomePage(driver)
        home.click_Signin_button()
        login = LoginPage(driver)
        login.do_login("username","password")
        account=AccountSummaryPage(driver)
        account.click_title_link()
        home.click_onlinebanking_link()

    @pytest.mark.parametrize("feature_name", ["Account Summary", "Account Activity", "Transfer Funds"])
    def test_validating_with_signin(self, driver, signin, feature_name):
        self.test = Test("Validating feature link with signin", +feature_name)
        self.test.log("Navigate online banking page")
        onlineBanking = OnlineBankingPage(driver)
        onlineBanking.click_feature_link(feature_name)
        self.test.verify_are_equal(feature_name in driver.title, True, "Verify the following of the title", Sevrity.critical)
        self.test.log("Navigate to the feature page")
        # assert feature_name in driver.title
        driver.back()

    def tear_down_method(self, method):
        Test_Validating_Links.test=self.test


