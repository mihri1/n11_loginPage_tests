import ssl
import certifi
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPageSecurityTest:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def verify_https(self, url):
        assert url.startswith('https://'), 'Login page is not served over HTTPS'

    def verify_ssl_certificate(self, hostname):
        context = ssl.create_default_context(cafile=certifi.where())
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                certificate = ssock.getpeercert()
                if certificate:
                    subject = dict(x[0] for x in certificate['subject'])
                    issuer = dict(x[0] for x in certificate['issuer'])
                    expiration_date = certificate['notAfter']

                    print("Certificate Details:")
                    print("Subject:", subject)
                    print("Issuer:", issuer)
                    print("Expiration Date:", expiration_date)
                else:
                    print("No SSL certificate found.")

    def login(self, username, password):
        self.driver.get("https://www.n11.com/giris-yap")
        username_element = self.driver.find_element(By.ID, 'email')
        password_element = self.driver.find_element(By.ID, 'password')
        submit_button = self.driver.find_element(By.ID, 'loginButton')

        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_button.click()

    def verify_login_success(self):
        my_account = self.driver.find_element(By.XPATH, "//a[@title='Hesabım']")
        assert my_account.is_displayed(), "Login failed"
        print("Successfully logged in!")

    def verify_session_timeout(self, timeout_duration):
        time.sleep(timeout_duration)

        try:
            login_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'loginButton')))
            assert login_button.text == 'Giriş Yap'
        except:
            print('Session timeout functionality not working')

    def close_browser(self):
        self.driver.quit()


login_test = LoginPageSecurityTest("/Users/okumusm/PycharmProjects/n11_casestudy/drivers/chromedriver.exe")

# test case 1 - Verify HTTPS
login_test.verify_https("https://www.n11.com/giris-yap")

# test case 2 - Verify SSL certificate
login_test.verify_ssl_certificate("www.n11.com")

# test case 3 - Verify login success
login_test.login("m.okumuss95@gmail.com", "199506M")
login_test.verify_login_success()

# test case 4 - Verify session timeout
timeout_duration = 600
login_test.verify_session_timeout(timeout_duration)

# Close the browser
login_test.close_browser()
