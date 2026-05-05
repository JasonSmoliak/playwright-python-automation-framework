import pytest
import allure

pytestmark = pytest.mark.ui


@pytest.mark.smoke
@allure.epic("User Management")
@allure.feature("Authentication")
@allure.story("Successful Login")
@allure.title("Successful login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_login(login_page, credentials):
    with allure.step("Open the login page"):
        login_page.load()

    with allure.step("Enter valid username and password"):
        login_page.login(credentials["username"], credentials["password"])

    with allure.step("Verify user is redirected to secure page"):
        login_page.verify_successful_login()


@pytest.mark.regression
@allure.epic("User Management")
@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.title("Login fails with invalid credentials")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_login(login_page):
    with allure.step("Open the login page"):
        login_page.load()

    with allure.step("Enter invalid credentials"):
        login_page.login("wrong_user", "wrong_password")

    with allure.step("Verify error message is displayed"):
        login_page.verify_failed_login()
