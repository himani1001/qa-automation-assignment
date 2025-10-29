from utils.config import BASE_URL

class LoginPage:
    def __init__(self, page_handle):
        self.page_handle = page_handle
        self.username_input = '//input[@name="username"]'
        self.password_input = '//input[@name="password"]'
        self.submit_btn = '//button[@id="submit"]'
        self.error = '//*[@id="error"]'
        self.success = '//h1[@class="post-title"]'
        self.logout_btn = '//a[text()="Log out"]'

    def navigate(self):
        self.page_handle.goto(BASE_URL)

    def login(self, username, password):
        self.page_handle.wait_for_selector(self.username_input).type(username)
        self.page_handle.wait_for_selector(self.password_input).type(password)
        self.page_handle.wait_for_selector(self.submit_btn).click()
            
    def get_error(self):
        return self.page_handle.wait_for_selector(self.error).text_content()

    def get_success(self):
        return self.page_handle.wait_for_selector(self.success).text_content()

    def logout(self):
        self.page_handle.wait_for_selector(self.logout_btn).click()