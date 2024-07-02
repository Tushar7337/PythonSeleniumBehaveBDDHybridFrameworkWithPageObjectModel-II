import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProviderPage:
    def __init__(self,driver):
        self.driver = driver

    add_provider_button_xpath = "//button[@class='MuiButtonBase-root css-190o0xf']"
    first_name_textfield_xpath = "//input[@name='firstName']"
    last_name_textfield_xpath = "//input[@name='lastName']"
    email_address_textfield_xpath = "//input[@name='email']"
    phone_number_textfield_xpath = "//input[@value='+1']"
    gender_drop_down_xpath = "//span[text()='Select Gender']"
    male_gender_drop_down_xpath = "//li[@data-value='MALE']"
    select_role_drop_down_xpath = "//span[text()='Select Role']"
    selecting_role_as_supervising_provider_xpath = "//li[@data-value='SUPERVISING_PROVIDER']"
    #select_supervising_provider_for_student_drop_down_xpath = ""
    #select_supervising_provider_for_student_xpath = ""
    npi_number_textfield_xpath = "//input[@name='npi']"
    experience_textfield_xpath = "//input[@name='experience']"
    address_line1_textfield_xpath = "//input[@name='address.line1']"
    address_line2_textfield_xpath = "//input[@name='address.line2']"
    state_address_textfield_xpath = "//input[@name='address.state']"
    city_address_textfield_xpath = "//input[@name='address.city']"
    country_address_textfield_xpath = "//input[@name='address.country']"
    zipcode_address_textfield_xpath = "//input[@name='address.zipcode']"
    save_button_xpath = "//button[text()='Save']"
    provider_header_xpath = "//h2[text()='Providers']"
    first_row_action_button_xpath = "(//button[@id='long-button'])[1]"
    first_row_edit_button_xpath = "//li[text()='Edit']"
    very_first_row_name_xpath = "(//div[@class='MuiBox-root css-sza1dm'])[1]"
    delete_provider_button_xpath = "//li[text()='Delete']"
    delete_provider_confirmation_button_xpath = "//button[text()='Yes']"
    first_row_provider_name_xpath = "(//div[@class='MuiBox-root css-sza1dm'])[1]"
    provider_npi_number_xpath = "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-8 css-1wnizpp'])[6]"
    created_provider_email_xpath = "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-8 css-1wnizpp'])[2]"

    supervising_provider_drop_down_xpath = "//span[text()='Select Supervising provider']"
    select_supervising_provider_xpath = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[1]"
    speciality_drop_down_xpath = "//span[text()='Select Speciality']"
    location_drop_down_xpath = "//span[text()='Select Location']"
    first_location_from_drop_down_xpath = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[1]"


    # Search Related Xpath's
    student_search_box_xpath = "//input[@id='document-name-label']"
    active_inactive_student_toggle_button_xpath = "//input[@type='checkbox']"
    student_status_label_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 jss81 css-1d2q46q']"



    def click_on_add_provider_button(self):
        self.driver.find_element(By.XPATH,self.add_provider_button_xpath).click()
    def enter_first_name(self,first_name):
        self.driver.find_element(By.XPATH,self.first_name_textfield_xpath).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.driver.find_element(By.XPATH,self.last_name_textfield_xpath).send_keys(last_name)

    def enter_email_address(self,email_address):
        self.driver.find_element(By.XPATH,self.email_address_textfield_xpath).send_keys(email_address)

    def enter_phone_number(self,phone_number):
        self.driver.find_element(By.XPATH,self.phone_number_textfield_xpath).send_keys(phone_number)

    def click_on_gender_drop_down(self):
        self.driver.find_element(By.XPATH,self.gender_drop_down_xpath).click()

    def click_on_male_gender(self):
        self.driver.find_element(By.XPATH,self.male_gender_drop_down_xpath).click()

    def click_on_select_role_drop_down(self):
        self.driver.find_element(By.XPATH,self.select_role_drop_down_xpath).click()

    def click_supervising_provider_role_option(self):
        self.driver.find_element(By.XPATH,self.selecting_role_as_supervising_provider_xpath).click()

    def select_supervising_provider_for_student(self):
        self.driver.find_element(By.XPATH,self.select_supervising_provider_for_student_drop_down_xpath).click()
        self.driver.find_element(By.XPATH,self.select_supervising_provider_for_student_xpath).click()

    def enter_npi_number(self,unique_npi_number):
        self.driver.find_element(By.XPATH,self.npi_number_textfield_xpath).send_keys(unique_npi_number)

    def enter_years_of_experience(self,years_of_experience):
        self.driver.find_element(By.XPATH,self.experience_textfield_xpath).send_keys(years_of_experience)

    def select_class_from_drop_down(self):
        self.driver.find_element(By.XPATH,self.location_drop_down_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.first_location_from_drop_down_xpath).click()


    def enter_address_line1(self,address_line1):
        self.driver.find_element(By.XPATH,self.address_line1_textfield_xpath).send_keys(address_line1)

    def enter_address_line2(self,address_line2):
        self.driver.find_element(By.XPATH,self.address_line2_textfield_xpath).send_keys(address_line2)

    def enter_state_address(self,state_address):
        self.driver.find_element(By.XPATH,self.state_address_textfield_xpath).send_keys(state_address)

    def enter_city_address(self,city_address):
        self.driver.find_element(By.XPATH,self.city_address_textfield_xpath).send_keys(city_address)

    def enter_country(self,country):
        self.driver.find_element(By.XPATH,self.country_address_textfield_xpath).send_keys(country)

    def enter_zip_code(self,zipcode):
        self.driver.find_element(By.XPATH,self.zipcode_address_textfield_xpath).send_keys(zipcode)

    def click_on_save_button(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()

    def verify_newly_created_provider(self,npi):
        self.driver.find_element(By.XPATH,self.first_row_provider_name_xpath).click()
        time.sleep(3)
        return (self.driver.find_element(By.XPATH,self.created_provider_email_xpath)
                .text.__contains__(npi))

    def click_on_action_button(self):
        self.driver.find_element(By.XPATH,self.first_row_action_button_xpath).click()

    def click_on_edit_button(self):
        self.driver.find_element(By.XPATH,self.first_row_edit_button_xpath).click()

    def verify_updated_provider_details(self,expt_txt):
        self.driver.find_element(By.XPATH,self.first_row_provider_name_xpath).click()
        time.sleep(3)
        return (self.driver.find_element(By.XPATH,self.very_first_row_name_xpath).text
                .__contains__(expt_txt))

    def click_on_delete_provider_button(self):
        self.driver.find_element(By.XPATH,self.delete_provider_button_xpath).click()

    def click_on_yes_delete_provider_confirmation_button(self):
        self.driver.find_element(By.XPATH,self.delete_provider_confirmation_button_xpath).click()

    def select_supervising_provider_from_drop_down(self):
        self.driver.find_element(By.XPATH,self.supervising_provider_drop_down_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.select_supervising_provider_xpath).click()


    def search_student_name(self,student_name):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.student_search_box_xpath).click()
        self.driver.find_element(By.XPATH,self.student_search_box_xpath).send_keys(student_name)
        time.sleep(3)

    def click_on_student_inactive_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.active_inactive_student_toggle_button_xpath).click()
        time.sleep(2)

    def verify_student_status(self,expt_txt):
        return (self.driver.find_element(By.XPATH,self.student_status_label_xpath)
                .text.__contains__(expt_txt))

