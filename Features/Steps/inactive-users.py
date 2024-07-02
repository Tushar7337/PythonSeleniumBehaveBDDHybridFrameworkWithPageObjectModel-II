from behave import *

from Features.pages.ProviderPage import ProviderPage


@when(u'I click on Search box and Search Student with "{name}"')
def step_impl(context,name):
    context.provider_page = ProviderPage(context.driver)
    context.provider_page.search_student_name(name)
    print(name)

@when(u'Click on Active Status toggle button')
def step_impl(context):
    context.provider_page = ProviderPage(context.driver)
    context.provider_page.click_on_student_inactive_button()


@then(u'Selected Student should get Inactive')
def step_impl(context):
    context.provider_page = ProviderPage(context.driver)
    status = "Inactive"
    assert context.provider_page.verify_student_status(status)