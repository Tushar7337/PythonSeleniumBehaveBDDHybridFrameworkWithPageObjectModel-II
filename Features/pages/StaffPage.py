import time

from selenium.webdriver.common.by import By


class StaffPage:
    def __init__(self,driver):
        self.driver = driver

    staff_tab_xpath = "//h5[text()='Staff']"
    add_staff_button_xpath = "//button[text()='Add Staff']"
    first_name_text_field_xpath = "//input[@name='firstName']"
    last_name_textfield_xpath = "//input[@name='lastName']"
    email_address_textfield_xpath = "//input[@name='email']"
    phone_number_textfield_xpath = "//input[@value='+1']"
    gender_drop_down_xpath = "//span[text()='Select Gender']"
    male_gender_drop_down_xpath = "//li[@data-value='MALE']"
    select_role_drop_down_xpath = "//span[text()='Select Role']"
    selecting_role_as_frontdesk_xpath = "//li[@data-value='FRONTDESK']"
    staff_header_xpath = "//h2[text()='Staff']"
    save_button_xpath = "//button[text()='Save']"

    first_row_action_button_xpath = "(//button[@id='long-button'])[1]"
    edit_staff_button_xpath = "//li[text()='Edit']"
    very_first_row_name_xpath = "(//div[@class='MuiBox-root css-sza1dm'])[1]"
    delete_staff_button_xpath = "//li[text()='Delete']"
    delete_confirmation_button_xpath = "//button[text()='Yes']"

    staff_created_text_message_xpath = "//div[text()='Staff updated successfully!']"



    def click_on_staff_tab(self,):
        self.driver.find_element(By.XPATH,self.staff_tab_xpath).click()

    def click_on_add_staff_button(self):
        self.driver.find_element(By.XPATH,self.add_staff_button_xpath).click()

    def enter_first_name(self,first_name):
        self.driver.find_element(By.XPATH,self.first_name_text_field_xpath).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.driver.find_element(By.XPATH,self.last_name_textfield_xpath).send_keys(last_name)

    def enter_email_address(self,email_address):
        self.driver.find_element(By.XPATH,self.email_address_textfield_xpath).send_keys(email_address)

    def enter_phone_number(self,phone_number):
        self.driver.find_element(By.XPATH,self.phone_number_textfield_xpath).send_keys(phone_number)

    def click_on_gender_drop_down(self):
        self.driver.find_element(By.XPATH,self.gender_drop_down_xpath).click()

    def click_on_male(self):
        self.driver.find_element(By.XPATH,self.male_gender_drop_down_xpath).click()

    def click_on_role_drop_down(self):
        self.driver.find_element(By.XPATH,self.select_role_drop_down_xpath).click()

    def select_frontdesk_as_role(self):
        self.driver.find_element(By.XPATH,self.selecting_role_as_frontdesk_xpath).click()

    def click_on_save_button(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()

    def verify_staff_created_text(self,expected_txt):
        self.driver.find_element(By.XPATH,self.staff_created_text_message_xpath).click()
        return (self.driver.find_element(By.XPATH,self.staff_created_text_message_xpath).text
                .__eq__(expected_txt))


    def view_staff_on_to_of_list(self):
        self.driver.find_element(By.XPATH,self.very_first_row_name_xpath).click()


    def click_on_first_row_action_button(self):
        self.driver.find_element(By.XPATH,self.first_row_action_button_xpath).click()

    def click_on_edit_button(self):
        self.driver.find_element(By.XPATH,self.edit_staff_button_xpath).click()

    def verifying_updated_changes(self,expt_txt):
        return (self.driver.find_element(By.XPATH,self.very_first_row_name_xpath).text
                .__contains__(expt_txt))

    def click_on_delete_option(self):
        self.driver.find_element(By.XPATH,self.delete_staff_button_xpath).click()

    def click_on_yes_option_for_delete(self):
        self.driver.find_element(By.XPATH,self.delete_confirmation_button_xpath).click()


