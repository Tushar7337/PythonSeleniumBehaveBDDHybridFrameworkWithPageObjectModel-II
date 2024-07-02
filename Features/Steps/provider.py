import random
import time

from behave import *
from selenium.webdriver.common.by import By

from Features.pages.LoginPage import LoginPage
from Features.pages.ProviderPage import ProviderPage
from utilities import TimeGenerator, RandomDataGenerator


@when(u'I click on Add Provider button')
def step_impl(context):
    time.sleep(5)
    context.provider_page = ProviderPage(context.driver)
    context.provider_page.click_on_add_provider_button()

@when(u'I enter all the fields')
def step_impl(context):
    context.driver.implicitly_wait(2)
    random_number = str(random.randint(1111111111,9999999999))
    context.provider_page = ProviderPage(context.driver)
    first_name = RandomDataGenerator.random_first_name()
    last_name = RandomDataGenerator.random_last_name()
    context.provider_page.enter_first_name(first_name)
    context.provider_page.enter_last_name(last_name)
    unq = TimeGenerator.current_timestamp()
    context.provider_page.enter_email_address(f"{first_name}_Student_{unq}@mailinator.com")
    context.provider_page.enter_phone_number(random_number)
    context.provider_page.click_on_gender_drop_down()
    context.provider_page.click_on_male_gender()
    context.provider_page.click_on_select_role_drop_down()
    context.provider_page.click_supervising_provider_role_option()
    context.provider_page.enter_npi_number(random_number)
    context.provider_page.enter_years_of_experience("3")
    context.provider_page.select_class_from_drop_down()
    address = RandomDataGenerator.random_address()
    context.provider_page.enter_address_line1(address)
    context.provider_page.enter_address_line2("52nd Avenue Street")
    state = RandomDataGenerator.random_state()
    context.provider_page.enter_state_address(state)
    city = RandomDataGenerator.random_city()
    context.provider_page.enter_city_address(city)
    context.provider_page.enter_country("United States of America")
    zip = RandomDataGenerator.random_zip_code()
    context.provider_page.enter_zip_code(zip)
    time.sleep(1)

@when(u'I enter all the fields and select provider type as {provider_type}')
def step_impl(context,provider_type):
    context.provider_page = ProviderPage(context.driver)
    context.driver.implicitly_wait(2)
    random_number = str(random.randint(1111111111, 9999999999))
    context.provider_page = ProviderPage(context.driver)
    first_name = RandomDataGenerator.random_first_name()
    last_name = RandomDataGenerator.random_last_name()
    context.provider_page.enter_first_name(first_name)
    context.provider_page.enter_last_name(last_name)
    unq = TimeGenerator.current_timestamp()
    context.provider_page.enter_email_address(f"{first_name}_Student_{unq}@mailinator.com")
    context.provider_page.enter_phone_number(random_number)
    context.provider_page.click_on_gender_drop_down()
    context.provider_page.click_on_male_gender()
    context.provider_page.click_on_select_role_drop_down()
    select_role = provider_type.replace('"','')
    provider_role_xpath = f"//p[text()='{select_role}']"
    context.driver.find_element(By.XPATH,provider_role_xpath).click()
    print(select_role)
    context.provider_page.select_supervising_provider_from_drop_down()
    context.provider_page.enter_npi_number(random_number)
    context.provider_page.enter_years_of_experience("3")
    context.provider_page.select_class_from_drop_down()
    address = RandomDataGenerator.random_address()
    context.provider_page.enter_address_line1(address)
    context.provider_page.enter_address_line2("52nd Avenue Street")
    state = RandomDataGenerator.random_state()
    context.provider_page.enter_state_address(state)
    city = RandomDataGenerator.random_city()
    context.provider_page.enter_city_address(city)
    context.provider_page.enter_country("United States of America")
    zip = RandomDataGenerator.random_zip_code()
    context.provider_page.enter_zip_code(zip)
    time.sleep(1)


@when(u'I click on Submit button')
def step_impl(context):
    context.provider_page = ProviderPage(context.driver)
    context.provider_page.click_on_save_button()
    time.sleep(3)

@then(u'Provider should get added')
def step_impl(context):
    context.driver.implicitly_wait(3)
    #random_number = context.random_number
    context.provider_page = ProviderPage(context.driver)
    assert context.provider_page.verify_newly_created_provider("Student")

@when(u'I click on Action button and then Edit button')
def step_impl(context):
    context.provider_page = ProviderPage(context.driver)
    context.provider_page.click_on_action_button()
    context.provider_page.click_on_edit_button()
    time.sleep(5)

@when(u'I made changes in Student')
def step_impl(context):
    context.provider_page = ProviderPage(context.driver)
    context.provider_page.enter_first_name("Updated")
    time.sleep(5)

@then(u'Provider details should get updated')
def step_impl(context):
    context.provider_page = ProviderPage(context.driver)
    expt_text = "Updated"
    assert context.provider_page.verify_updated_provider_details(expt_text)

@when(u'I click on Action button and then Delete button')
def step_impl(context):
    context.provider_page =ProviderPage(context.driver)
    time.sleep(5)
    context.provider_page.click_on_action_button()
    context.provider_page.click_on_delete_provider_button()
    time.sleep(5)

@when(u'I click on Yes Confirmation button')
def step_impl(context):
    context.provider_page = ProviderPage(context.driver)
    context.provider_page.click_on_yes_delete_provider_confirmation_button()
    time.sleep(5)

@then(u'Provider details should get deleted')
def step_impl(context):
    pass