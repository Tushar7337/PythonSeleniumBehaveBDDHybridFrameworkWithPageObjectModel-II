import os
import random
import time

from behave import *

from Features.pages.PatientPage import PatientPage
from utilities import RandomDataGenerator, TimeGenerator


@when(u'I click on Patient tab')
def step_impl(context):
    context.patient_page = PatientPage(context.driver)
    context.patient_page.click_on_patient_tab()

@when(u'I click on Add Patient button and fill only required fields')
def step_impl(context):
    context.patient_page = PatientPage(context.driver)
    context.patient_page.click_on_add_patient()
    time.sleep(3)

    # Patient Personal Details
    first_name = RandomDataGenerator.random_first_name()
    last_name = RandomDataGenerator.random_last_name()
    current = TimeGenerator.current_timestamp()
    email = f"{first_name}_{current}@behave.com"
    dob = "03/08/1998"
    number = str(random.randint(1000000000,9999999999))
    ssn = str(random.randint(0000000000,9999999999))
    context.patient_page.enter_patient_personal_details(first_name,last_name,email,number,dob,ssn)

    # Patient Reason for Visit
    context.patient_page.enter_patient_reason_for_visit("NA")

    # Patient Allergy Details
    allergy_name = "Anaphylaxis"
    #allergy_type = "IgE-mediated (type 1) hypersensitivity"
    allergy_date = "02/02/2024"
    severity = "7"
    reaction = "Shock"
    context.patient_page.enter_patient_allergy_details(allergy_name,allergy_date,severity,reaction)

    # Patient Problem Details
    diagnosed_date = "03/03/2020"
    context.patient_page.enter_patient_problem("Flu",diagnosed_date)

    # Patient Medication Details
    medication_start_date = "05/25/2024"
    medication_end_date = "06/25/2024"
    context.patient_page.enter_patient_medication_details("Zanamivir",medication_start_date,medication_end_date,"2 mg","oral","Glaxo")

    # Patient Vitals Details
    oxy_saturation = str(random.randint(90,99))
    context.patient_page.enter_patient_vitals(oxy_saturation,"5'7","65","73","1.3","73",120,"7.3","01/01/2024")

    # Patient Social History
    context.patient_page.enter_patient_social_history("Captain","Close-knit family, supportive friends","$45,000 per year","Lots of it","Rented apartment in downtown","Bachelor's degree in Computer Science","No criminal record","marijuanas","Feels safe in current environment","No current concerns, regular check-ups","Works 9am-5pm, Monday to Friday","Practices meditation, attends church occasionally","Enjoys hiking, reading, and swimming")

    # Patient Care Note And Pharmacy Details
    context.patient_page.enter_patient_care_note("NA")
    context.patient_page.enter_patient_preferred_pharmacy_details("CVS Pharmacy","Eastern Coast")

    #time.sleep(3)
    #relative_path = os.path.abspath("C:\\Users\\lnv0176\\PycharmProjects\\FireFly-EHR-Behave-BDD\\utilities\\SOAP.pdf")
    #context.patient_page.upload_patient_report(relative_path)

@when(u'I click on Save Patient Button')
def step_impl(context):
    context.patient_page = PatientPage(context.driver)
    context.patient_page.click_on_save_patient_button()
    time.sleep(3)


@then(u'Patient case should get created')
def step_impl(context):
    pass