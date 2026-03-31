from pages.login_page import LoginPage


def test_successful_login(page, app_url, credentials):
    login_page = LoginPage(page, app_url)

    login_page.load()
    login_page.login(credentials["username"], credentials["password"])
    login_page.verify_successful_login()


def test_invalid_login(page, app_url):
    login_page = LoginPage(page, app_url)

    login_page.load()
    login_page.login("wrong_user", "wrong_password")
    login_page.verify_failed_login()
