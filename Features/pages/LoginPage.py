from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    sign_in_button_xpath = "//p[text()='Sign In']"
    email_address_textfield_xpath = "//input[@name='username']"
    password_textfield_xpath = "//input[@name='password']"
    second_login_button_xpath = "//input[@id='kc-login']"
    dashboard_tab_xpath = "//h5[text()='Provider']"
    failed_login_error_message_xpath = "//span[@id='input-error']"

    def click_sign_in_button(self):
        self.driver.find_element(By.XPATH,self.sign_in_button_xpath).click()

    def enter_email_address(self,unq_email):
        self.driver.find_element(By.XPATH,self.email_address_textfield_xpath).send_keys(unq_email)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.password_textfield_xpath).send_keys(password)

    def click_second_login_button(self):
        self.driver.find_element(By.XPATH,self.second_login_button_xpath).click()

    def verify_dashboard_tab(self,Dashboard_text):
        return (self.driver.find_element(By.XPATH,self.dashboard_tab_xpath).text
                .__eq__(Dashboard_text))

    def verify_failed_login_attempt_error_message(self,error_msg):
        return (self.driver.find_element(By.XPATH,self.failed_login_error_message_xpath).text
                .__contains__(error_msg))