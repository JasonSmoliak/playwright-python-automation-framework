from pages.login_page import LoginPage


def test_successful_login(page):
    login_page = LoginPage(page)

    login_page.load()
    login_page.login("practice", "SuperSecretPassword!")
    login_page.verify_successful_login()


def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.load()
    login_page.login("wrong_user", "wrong_password")
    login_page.verify_failed_login()

