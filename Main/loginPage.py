import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class LoginPageTest:
    def __init__(self, driver_path):
        options = webdriver.ChromeOptions()

        # Set ChromeDriver path for Mac
        if sys.platform == "darwin":
            driver_path += "/chromedriver_mac"

        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()

    def login(self, username, password):

        self.driver.get("https://www.n11.com/")
        go_to_login_page = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btnSignIn')))
        go_to_login_page.click()
        username_element = self.wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        password_element = self.driver.find_element(By.ID, 'password')
        submit_button = self.driver.find_element(By.ID, 'loginButton')

        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_button.click()
        try:
            error_message = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[text()='E-posta adresiniz veya şifreniz hatalı']")))
        except:
            print('Successful login!')

    def forgot_password(self):
        forgotPassword_button = self.driver.find_element(By.XPATH, "//span[text()='Şifremi Unuttum']")
        forgotPassword_button.click()
        pop_title = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h3[text()='Şifre Yenileme']")))
        assert pop_title.text == "Şifre Yenileme"

    def log_out(self):
        my_account_dropdown = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'myAccountHolder')]")))

        # Perform an action on the My Account dropdown
        action = ActionChains(self.driver)
        action.move_to_element(my_account_dropdown).perform()

        logout_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "logoutBtn")))
        logout_button.click()
        print("Successful Logout!")

        signin_button = self.driver.find_element(By.CLASS_NAME, "btnSignIn")  # to get login page after log out
        signin_button.click()

    def remember_me(self):
        remember_me_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'rememberMe')))
        assert remember_me_checkbox.is_enabled(), "Remember Me checkbox is not clickable."
        print("Remember Me checkbox is clickable.")

    def other_login_buttons(self):
        self.driver.get("https://www.n11.com/giris-yap")
        buttons_classes = ['apple-login-btn', 'facebookBtn', 'quickLogin', 'google-login-btn']

        for button_class in buttons_classes:
            button = self.driver.find_element(By.CLASS_NAME, button_class)
            assert button.is_displayed(), f"Other login button '{button_class}' is not present."
        print("All other login buttons are present.")

    def close_browser(self):
        self.driver.quit()


driver_path = "/Users/okumusm/PycharmProjects/n11_casestudy/drivers/chromedriver"
login_test = LoginPageTest(driver_path)

# test case 1 - Login with an invalid username and a valid password
login_test.login("mihri@gmail.com", "199506M")

# test case 2 - Login with an valid username and an invalid password
login_test.login("m.okumuss95@gmail.com", "199506")

# test case 3 - Login with an valid username and an valid password
login_test.login("m.okumuss95@gmail.com", "199506M")

# test case 4 - Scroll menu and log out
login_test.log_out()

# test case 5 - verify 'Şifremi Unuttum' button on login page
login_test.forgot_password()

# test case 6 - verify 'Beni Unutma' button on login page
login_test.remember_me()

# test case 7 - verify other login buttons
login_test.other_login_buttons()

login_test.close_browser()