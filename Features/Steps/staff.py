import random
import time

from behave import *

from Features.pages.LoginPage import LoginPage
from Features.pages.StaffPage import StaffPage
from utilities import RandomDataGenerator, TimeGenerator




@when(u'I click on staff tab')
def step_impl(context):
    context.staff_page = StaffPage(context.driver)
    time.sleep(5)
    context.staff_page.click_on_staff_tab()

@when(u'I click on Add Staff button and fill all required details')
def step_impl(context):
    context.staff_page = StaffPage(context.driver)
    context.staff_page.click_on_add_staff_button()
    context.staff_page = StaffPage(context.driver)
    first_name = RandomDataGenerator.random_first_name()
    last_name = RandomDataGenerator.random_last_name()
    context.staff_page.enter_first_name(first_name)
    context.staff_page.enter_last_name(last_name)
    unq = TimeGenerator.current_timestamp()
    context.staff_page.enter_email_address(f"{first_name}_Staff_{unq}@mailinator.com")
    num = str(random.randint(1111111111,9999999999))
    context.staff_page.enter_phone_number(num)
    context.staff_page.click_on_gender_drop_down()
    context.staff_page.click_on_male()
    context.staff_page.click_on_role_drop_down()
    context.staff_page.select_frontdesk_as_role()
    time.sleep(1)


@when(u'I click on Save button')
def step_impl(context):
    context.staff_page = StaffPage(context.driver)
    context.staff_page.click_on_save_button()
    time.sleep(3)

@then(u'Staff should get created')
def step_impl(context):
    context.staff_page = StaffPage(context.driver)
    time.sleep(3)
    expected_txt = "Staff updated successfully!"
    assert context.staff_page.verify_staff_created_text(expected_txt)
    #time.sleep(10)

    context.staff_page.view_staff_on_to_of_list()

@when(u'I click on Action button and edit button')
def step_impl(context):
    context.staff_page = StaffPage(context.driver)
    context.staff_page.click_on_first_row_action_button()
    context.staff_page.click_on_edit_button()
    time.sleep(3)

@when(u'I made changes in staff')
def step_impl(context):
    context.staff_page = StaffPage(context.driver)
    context.staff_page.enter_first_name("Updated")
    time.sleep(3)


@then(u'Staff details should get updated')
def step_impl(context):
    expt_text = "Updated"
    context.staff_page = StaffPage(context.driver)
    assert context.staff_page.verifying_updated_changes(expt_text)

@when(u'I click on Action button and Delete button')
def step_impl(context):
    context.staff_page = StaffPage(context.driver)
    context.staff_page.click_on_first_row_action_button()
    context.staff_page.click_on_delete_option()

@when(u'I click on Yes button')
def step_impl(context):
    context.staff_page = StaffPage(context.driver)
    context.staff_page.click_on_yes_option_for_delete()
    time.sleep(5)

@then(u'Staff details should get deleted')
def step_impl(context):
    pass
