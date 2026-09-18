class LoginPage:
    def __init__(self, page):
        self.page = page
        # ini alamat element nya
        self.input_username = page.locator('#user-name')
        self.input_password = page.locator('#password')
        self.tombol_login = page.locator('#login-button')

    def buka_website(self):
        self.page.goto('https://www.saucedemo.com/')

    def login(self, username, password):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.tombol_login.click()