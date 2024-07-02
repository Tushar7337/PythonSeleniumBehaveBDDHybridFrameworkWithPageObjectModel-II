from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

from Features.pages.LoginPage import LoginPage


@given(u'I launch the URL and navigate to Sign in screen')
def step_impl(context):
    context.driver.implicitly_wait(5)
    context.login_page = LoginPage(context.driver)
    context.login_page.click_sign_in_button()

@when(u'Enter username as "{email}" and password as "{password}"')
def step_impl(context,email,password):
    context.driver.implicitly_wait(5)
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)

@when(u'I enter invalid email and valid password')
def step_impl(context):
    context.driver.implicitly_wait(5)
    context.login_page = LoginPage(context.driver)
    time = datetime.now().time().strftime("%y_%m_%d_%H_%M_%S")
    unq_email = f"raw{time}@gmail.com"
    context.login_page.enter_email_address(unq_email)
    context.login_page.enter_password("Pass@1234")


@then(u'I should get error message')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    error_msg = "Invalid username or password"
    assert context.login_page.verify_failed_login_attempt_error_message(error_msg)

@when(u'I click on the sign in Button')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_second_login_button()

@then(u'I should be logged in')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    Dashboard_text = 'Provider'
    assert context.login_page.verify_dashboard_tab(Dashboard_text)