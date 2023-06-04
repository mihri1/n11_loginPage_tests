import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service


class LoginPageUiTest:
    def __init__(self, driver_path):
        options = webdriver.ChromeOptions()

        # Set ChromeDriver path for Mac
        if sys.platform == "darwin":
            driver_path += "/chromedriver_mac"

        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def test_labels_texts_buttons(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

        # Verify presence of label texts
        label_texts = ['email', 'password', 'rememberMe']
        for label_text in label_texts:
            label = self.driver.find_element(By.XPATH, f"//label[@for='{label_text}']")
            assert label.is_displayed(), f"Label '{label_text}' is not present."
        print("All labels are displayed!")

        # Verify presence of text boxes
        text_box_ids = ['email', 'password']
        for text_box_id in text_box_ids:
            text_box = self.driver.find_element(By.ID, text_box_id)
            assert text_box.is_displayed(), f"Text box '{text_box_id}' is not present."
        print("All text boxes are displayed!")

        # Verify presence of buttons
        button_classes = ['green_flat', 'black_flat', 'forgotPassword', 'google-login-btn', 'quickLogin ',
                          'apple-login-btn', 'showPass']
        for button_class in button_classes:
            button = self.driver.find_element(By.CLASS_NAME, button_class)
            assert button.is_displayed(), f"Button '{button_class}' is not present."
        print("Buttons are displayed!")

    def close_browser(self):
        self.driver.quit()


driver_path = "/Users/okumusm/PycharmProjects/n11_casestudy/drivers/chromedriver.exe"
login_test = LoginPageUiTest(driver_path)
login_test.test_labels_texts_buttons("https://www.n11.com/giris-yap")
login_test.close_browser()