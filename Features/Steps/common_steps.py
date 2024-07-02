from behave import *
from Features.pages.LoginPage import LoginPage

@given(u'I am on application Dashboard')
def step_impl(context):
    context.driver.implicitly_wait(5)
    context.login_page = LoginPage(context.driver)
    context.login_page.click_sign_in_button()
    context.driver.implicitly_wait(5)
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("gwen@mailinator.com")
    context.login_page.enter_password("Tushar@123")
    context.login_page = LoginPage(context.driver)
    context.login_page.click_second_login_button()

@given(u'I logged in as a Student and I am on Student Dashboard')
def step_impl(context):
    context.driver.implicitly_wait(5)
    context.login_page = LoginPage(context.driver)
    context.login_page.click_sign_in_button()
    context.driver.implicitly_wait(5)
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("sarcasm@atpeak.com")
    context.login_page.enter_password("Test@123")
    context.login_page = LoginPage(context.driver)
    context.login_page.click_second_login_button()