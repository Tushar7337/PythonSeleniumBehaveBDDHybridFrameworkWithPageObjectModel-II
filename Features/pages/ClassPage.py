from selenium.webdriver.common.by import By


class ClassPage:
    def __init__(self,driver):
        self.driver = driver

    class_tab_xpath = "//h5[text()='Classes']"
    add_class_button_xpath = "//button[@class='MuiButtonBase-root css-190o0xf']"
    class_name_text_field_xpath = "//input[@placeholder='Class Name']"
    email_address_text_field_xpath = "//input[@name='email']"
    phone_number_text_field_xpath = "//input[@type='tel']"
    fax_number_text_field_xpath = "//input[@name='fax']"
    address_line1_text_field_xpath = "//input[@name='physicalAddress.line1']"
    address_line2_text_field_xpath = "//input[@name='physicalAddress.line2']"
    address_state_text_field_xpath = "//input[@name='physicalAddress.state']"
    address_city_text_field_xpath = "//input[@name='physicalAddress.city']"
    address_country_text_field_xpath = "//input[@name='physicalAddress.country']"
    address_zip_code_text_field_xpath = "//input[@name='physicalAddress.zipcode']"
    save_class_button_xpath = "//button[@class='MuiButtonBase-root css-a4el3e']"
    college_name_first_row_xpath = "(//div[@class='MuiBox-root css-sza1dm'])[1]"
    first_row_class_action_btn_xpath = "(//button[@id='long-button'])[1]"
    first_row_class_edit_btn_xpath = "//li[text()='Edit']"
    first_row_class_delete_button_xpath = "//li[text()='Delete']"
    yes_option_for_delete_btn_xpath = "//button[text()='Yes']"

    def click_on_staff_tab(self):
        self.driver.find_element(By.XPATH,self.class_tab_xpath).click()

    def click_on_add_class_button(self):
        self.driver.find_element(By.XPATH,self.add_class_button_xpath).click()

    def enter_class_name(self,class_name):
        self.driver.find_element(By.XPATH,self.class_name_text_field_xpath).send_keys(class_name)

    def enter_email_address(self,email_address):
        self.driver.find_element(By.XPATH,self.email_address_text_field_xpath).send_keys(email_address)

    def enter_phone_number(self,phone_number):
        self.driver.find_element(By.XPATH,self.phone_number_text_field_xpath).send_keys(phone_number)

    def enter_fax_number(self,fax_num):
        self.driver.find_element(By.XPATH,self.fax_number_text_field_xpath).send_keys(fax_num)

    def enter_address_line1(self,address_line1):
        self.driver.find_element(By.XPATH,self.address_line1_text_field_xpath).send_keys(address_line1)

    def enter_address_line2(self,address_line2):
        self.driver.find_element(By.XPATH,self.address_line2_text_field_xpath).send_keys(address_line2)

    def enter_state(self,state):
        self.driver.find_element(By.XPATH,self.address_state_text_field_xpath).send_keys(state)

    def enter_city(self,city):
        self.driver.find_element(By.XPATH,self.address_city_text_field_xpath).send_keys(city)

    def enter_country(self,country):
        self.driver.find_element(By.XPATH,self.address_country_text_field_xpath).send_keys(country)

    def enter_zip_code(self,zip):
        self.driver.find_element(By.XPATH,self.address_zip_code_text_field_xpath).send_keys(zip)

    def click_on_save_class_button(self):
        self.driver.find_element(By.XPATH,self.save_class_button_xpath).click()

    def verify_class_added_successfully(self,expt_txt):
        return (self.driver.find_element(By.XPATH,self.college_name_first_row_xpath).text
         .__eq__(expt_txt))

    def click_on_action_button(self):
        self.driver.find_element(By.XPATH,self.first_row_class_action_btn_xpath).click()

    def click_on_edit_button(self):
        self.driver.find_element(By.XPATH,self.first_row_class_edit_btn_xpath).click()

    def click_on_delete_class_button(self):
        self.driver.find_element(By.XPATH,self.first_row_class_delete_button_xpath).click()

    def click_on_yes_option_of_delete_button(self):
        self.driver.find_element(By.XPATH,self.yes_option_for_delete_btn_xpath).click()

