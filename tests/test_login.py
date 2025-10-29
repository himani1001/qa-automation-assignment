import pytest
from playwright.sync_api import sync_playwright
from pages.loginPage import LoginPage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD

@pytest.fixture(scope = "module")
def handle_browser():
    with sync_playwright() as p:
        browser =  p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope = 'function')
def page_handle(handle_browser):
    page = handle_browser.new_page()
    yield page
    page.close()

def test_valid(page_handle):
    login_page = LoginPage(page_handle)
    login_page.navigate()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    page_handle.wait_for_timeout(2000)

    success = login_page.get_success()
    assert "Logged In Successfully" in success

@pytest.mark.parametrize('username, password, expected_result', [('incorrectUser', 'Password123', 'Your username is invalid!'), ('student', 'incorrectPassword', 'Your password is invalid!')],)
def test_invalid(page_handle, username, password, expected_result):
    login_page = LoginPage(page_handle)
    login_page.navigate()
    login_page.login(username, password)

    page_handle.wait_for_timeout(4000)

    error = login_page.get_error()
    assert expected_result == error

def test_blank(page_handle):
    login_page = LoginPage(page_handle)
    login_page.navigate()

    page_handle.wait_for_timeout(2000)
    page_handle.wait_for_selector(login_page.submit_btn).click()

    page_handle.wait_for_timeout(2000)

    error = login_page.get_error()
    assert "Your username is invalid!" == error

def test_logout(page_handle):
    login_page = LoginPage(page_handle)
    login_page.navigate()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    page_handle.wait_for_timeout(2000)
    login_page.logout()

    page_handle.wait_for_timeout(2000)
    assert page_handle.url == BASE_URL