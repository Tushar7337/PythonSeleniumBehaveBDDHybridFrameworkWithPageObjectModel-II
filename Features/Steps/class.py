import time

from behave import *

from Features.pages.ClassPage import ClassPage
from Features.pages.LoginPage import LoginPage
from utilities import RandomDataGenerator, TimeGenerator


@when(u'I click on Add Class button')
def step_impl(context):
    time.sleep(3)
    context.class_page = ClassPage(context.driver)
    context.class_page.click_on_staff_tab()
    context.class_page.click_on_add_class_button()

@when(u'I enter all the fields required for class')
def step_impl(context):
    time.sleep(2)
    context.class_page = ClassPage(context.driver)
    remove_space = RandomDataGenerator.random_city()
    university_name = remove_space.replace(" ","")
    phone_number = RandomDataGenerator.random_phone_number()
    city = RandomDataGenerator.random_city()
    state = RandomDataGenerator.random_state()
  # address = RandomDataGenerator.random_address()
    current_time = TimeGenerator.current_timestamp()
    zip = RandomDataGenerator.random_zip_code()
    context.class_page.enter_class_name(f"{university_name} College Psychiatrist Class")
    context.class_page.enter_email_address(f"{university_name}_{current_time}@mailinator.com")
    context.class_page.enter_phone_number(phone_number)
    context.class_page.enter_fax_number(phone_number)
    context.class_page.enter_address_line1("Blvd Avenue")
    context.class_page.enter_address_line2("Happy Street")
    context.class_page.enter_state(state)
    context.class_page.enter_city(city)
    context.class_page.enter_country("USA")
    context.class_page.enter_zip_code(zip)

@when(u'I click on Submit Class button')
def step_impl(context):
    time.sleep(2)
    context.class_page = ClassPage(context.driver)
    context.class_page.click_on_save_class_button()
    time.sleep(5)


@then(u'Class should get created')
def step_impl(context):
    time.sleep(2)
    name = RandomDataGenerator.random_city()
    replace_space = name.replace(" ","")
    expt_txt = f"{replace_space} College Psychiatrist Class"
    context.class_page = ClassPage(context.driver)
    context.class_page.verify_class_added_successfully(expt_txt)
    time.sleep(3)

@when(u'I click on Class Action button and then Edit button')
def step_impl(context):
    context.class_page = ClassPage(context.driver)
    context.class_page.click_on_action_button()
    print("Passed")
    context.class_page.click_on_edit_button()

@when(u'I made changes in Class')
def step_impl(context):
    time.sleep(2)
    context.class_page = ClassPage(context.driver)
    context.class_page.enter_class_name("Updated")

@then(u'Class details should get updated')
def step_impl(context):
    pass

@when(u'I click on Class Action button and then Delete button')
def step_impl(context):
    time.sleep(2)
    context.class_page = ClassPage(context.driver)
    context.class_page.click_on_action_button()
    context.class_page.click_on_delete_class_button()
    context.class_page.click_on_yes_option_of_delete_button()
    time.sleep(2)

@then(u'Class should get deleted')
def step_impl(context):
    pass