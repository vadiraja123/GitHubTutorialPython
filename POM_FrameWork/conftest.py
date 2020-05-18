# Create Fixture for Zero Web App
import pytest
from ctreport_selenium.ctlistener import Session
from selenium import webdriver

@pytest.fixture(scope="session",autouse=True)

def driver(request):
    driver_ = webdriver.Chrome(executable_path=r'F:\Personal\WebDriver\chromedriver.exe')
    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com/")

    session_details = {
        "owner": "Vadiraja A V",
        "application": "MyApp1",
        "application version": "V1.0",
        "os": "Windows10",
        "browser": "Chrome"
    }

    report_options = {
        "title": "Test Report",
        "Logo":r"C:\Users\Vadiraja\Desktop\download",
        "show_reference": True,
    }

    Session.start(test_name="Smoke Test - MyApp1",
                  path-str(Path(__file__).parent)+r"\reports",
                  driver=driver_,
                  session_details=session_details,
                  report_options=report_options)

    def quit():
        pass
    request.addfinalizer(quit)

    return driver_


def pytest_sessioninish(session):
    Session.end()

