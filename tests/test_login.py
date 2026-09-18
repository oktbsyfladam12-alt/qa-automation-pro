from pages.login_page import LoginPage


def test_login_sukses(page):
    # 1. Buka halaman
    login_page = LoginPage(page)
    login_page.buka_website()

    # 2. Login
    login_page.login('standard_user', 'secret_sauce')

    # 3. Cek apakah berhasil (kalo ada tulisan Products berarti sukses)
    assert page.locator('.title').inner_text() == 'Products'