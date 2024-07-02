from behave import *

from Features.pages.PatientPage import PatientPage


@when(u'I navigate to Patient tab')
def step_impl(context):
    context.patient_page = PatientPage(context.driver)
    context.patient_page.click_on_patient_tab()

@when(u'Click on First Patient from the Patient list')
def step_impl(context):
    context.patient_page = PatientPage(context.driver)
    context.patient_page.click_on_first_patient_from_list()


@when(u'I Click on Assign Provider Button')
def step_impl(context):
    context.patient_page = PatientPage(context.driver)
    context.patient_page.click_on_assign_provider_button()

@when(u'Fill all the reuqired details and click on Save Button')
def step_impl(context):
    context.patient_page = PatientPage(context.driver)
    appointment_date = "07/03/2024"
    appointment_start_time = "09:00PM"
    appointment_end_time = "10:00PM"
    context.patient_page.enter_details_on_assign_patient_case_form(appointment_date,appointment_start_time,appointment_end_time)

@then(u'Patient Case should get assign to Student')
def step_impl(context):
    pass