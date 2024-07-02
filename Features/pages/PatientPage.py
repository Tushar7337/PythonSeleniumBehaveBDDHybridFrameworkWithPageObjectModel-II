import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class PatientPage:
    def __init__(self,driver):
        self.driver = driver

    patient_tab_xpath = "//h5[text()='Patients']"
    add_patient_button_xpath = "//button[text()='Add Patients']"
    patient_first_name_text_field_xpath = "//input[@name='patient.firstName']"
    patient_last_name_text_field_xpath = "//input[@name='patient.lastName']"
    patient_email_address_text_field_xpath = "//input[@name='patient.email']"
    patient_phone_number_textfield_xpath = "//input[@value='+1']"
    patient_gender_drop_down = "//span[text()='Select Gender']"
    patient_gender_select_option = "//li[@data-value='MALE']"
    patient_dob_xpath = "(//input[@placeholder='MM/DD/YYYY'])[1]"
    patient_ssn_xpath = "//input[@name='patient.ssn']"
    patient_age_xpath = "//input[@name='patient.age']"
    patient_reason_for_visit_xpath = "//textarea[@name='intakeForm.reasonOfVisit']"


    patient_allergy_name_xpath = "//input[@name='intakeForm.patientAllergies.0.name']"
    patient_allergy_type_drop_down_xpath = "//span[text()='Select Allergy Type']"
    patient_allergy_select_allergy_type_xpath = "//li[@data-value='DRUG']"
    patient_allergy_date_xpath = "(//input[@placeholder='MM/DD/YYYY'])[2]"
    patient_allergy_severity_xpath = "//input[@name='intakeForm.patientAllergies.0.severity']"
    patient_allergy_reaction_xpath = "//input[@name='intakeForm.patientAllergies.0.reaction']"
    patient_problem_name_xpath = "//input[@name='intakeForm.patientProblems.0.problemName']"
    patient_diagnosed_date_xpath = "(//input[@placeholder='MM/DD/YYYY'])[3]"
    patient_medication_name_xpath = "//input[@name='intakeForm.patientMedications.0.medicine']"
    patient_medication_start_date_xpath = "(//input[@placeholder='MM/DD/YYYY'])[4]"
    patient_medication_end_date_xpath = "(//input[@placeholder='MM/DD/YYYY'])[5]"
    patient_medication_dose_xpath = "//input[@name='intakeForm.patientMedications.0.dose']"
    patient_medication_direction_xpath = "//input[@name='intakeForm.patientMedications.0.direction']"
    patient_medication_past_xpath = "//input[@placeholder='Enter Past Medication']"

    patient_vitals_oxygen_saturation_xpath = "//input[@name='intakeForm.vitals.0.oxygenSaturation']"
    patient_vitals_height_xpath = "//input[@name='intakeForm.vitals.0.height']"
    patient_vitals_weight_xpath = "//input[@name='intakeForm.vitals.0.weight']"
    patient_vitals_heart_rate_xpath = "//input[@name='intakeForm.vitals.0.heartRate']"
    patient_vitals_pain_scale_xpath = "//input[@name='intakeForm.vitals.0.pain']"
    patient_vitals_systolic_blood_pressure_xpath = "//input[@name='intakeForm.vitals.0.systolic']"
    patient_vitals_diastolic_blood_pressure_xpath = "//input[@name='intakeForm.vitals.0.diastolic']"
    patient_vitals_ph_xpath = "//input[@name='intakeForm.vitals.0.ph']"
    patient_vitals_date_xpath = "(//input[@placeholder='MM/DD/YYYY'])[6]"

    patient_past_medical_history_xpath = "//textarea[@name='intakeForm.patientHistory.patientPastMedicalHistory.note']"
    patient_past_surgical_history_xpath = "//textarea[@name='intakeForm.patientHistory.patientPastSurgicalHistory.note']"
    patient_family_history_xpath = "//textarea[@name='intakeForm.patientHistory.patientFamilyHistory.note']"
    patient_psychiatric_history_xpath = "//textarea[@name='intakeForm.patientHistory.patientPsychiatricHistory.note']"
    patient_development_history_xpath = "//textarea[@name='intakeForm.patientHistory.patientDevelopmentalHistory.note']"
    patient_social_history_identity_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.identity']"
    patient_social_history_family_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.relationalSupport']"
    patient_social_history_income_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.income']"
    patient_social_history_trauma_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.trauma']"
    patient_social_history_housing_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.housing']"
    patient_social_history_education_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.education']"
    patient_social_history_legal_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.legal']"
    patient_social_history_substance_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.substances']"
    patient_social_history_personal_safety_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.personalSafety']"
    patient_social_history_sexual_health_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.sexualHealth']"
    patient_social_history_schedule_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.schedule']"
    patient_social_history_spirituality_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.spirituality']"
    patient_social_history_interest_xpath = "//input[@name='intakeForm.patientHistory.socialHistory.interests']"

    patient_care_note_text_box_xpath = "//textarea[@name='intakeForm.careNotes']"
    patient_preferred_pharmacy_name_xpath = "//input[@name='intakeForm.preferredPharmacy.preferredPharmacyName']"
    patient_preferred_pharmacy_address_xpath = "//textarea[@name='intakeForm.preferredPharmacy.preferredPharmacyAddress']"
    patient_report_upload_box_xpath = "//div[@class='MuiDropzoneArea-textContainer']//*[name()='svg']"

    patient_case_save_button_xpath = "//button[text()='Save']"

# Assign Patient Case WorkFlow
    first_patient_case_from_list_xpath = "(//div[@class='MuiBox-root css-sza1dm'])[1]"
    assign_patient_case_button_xpath = "//h4[text()='Assign Provider']"
    select_provider_drp_down_xpath = "//h5[text()='Select']"
    selecting_provider_from_top_of_list_xpath = "(//h6[@class='MuiTypography-root MuiTypography-h6 MuiTypography-noWrap css-1nuqfj'])[1]"
    select_location_drop_down_xpath = "//span[text()='Select Location']"
    selecting_location_from_top_of_list_xpath = "(//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-g4lzgy'])[1]"
    appointment_date_xpath = "//input[@placeholder='MM/DD/YYYY']"
    appointment_start_time_xpath = "(//input[@placeholder='hh:mm aa'])[1]"
    appointment_end_time_xpath = "(//input[@placeholder='hh:mm aa'])[2]"
    save_button_from_patient_assign_xpath = "//button[text()='Save']"

    def click_on_patient_tab(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.patient_tab_xpath).click()

    def click_on_add_patient(self):
        self.driver.find_element(By.XPATH,self.add_patient_button_xpath).click()

    def enter_patient_personal_details(self,first_name,last_name,email,number,dob,ssn):
        self.driver.find_element(By.XPATH,self.patient_first_name_text_field_xpath).send_keys(first_name)
        self.driver.find_element(By.XPATH,self.patient_last_name_text_field_xpath).send_keys(last_name)
        self.driver.find_element(By.XPATH,self.patient_email_address_text_field_xpath).send_keys(email)
        self.driver.find_element(By.XPATH,self.patient_phone_number_textfield_xpath).send_keys(number)
        self.driver.find_element(By.XPATH,self.patient_gender_drop_down).click()
        self.driver.find_element(By.XPATH,self.patient_gender_select_option).click()
        self.driver.find_element(By.XPATH,self.patient_dob_xpath).click()
        self.driver.find_element(By.XPATH,self.patient_dob_xpath).send_keys(dob)
        self.driver.find_element(By.XPATH,self.patient_ssn_xpath).send_keys(ssn)


    def enter_patient_reason_for_visit(self,rov):
        self.driver.find_element(By.XPATH,self.patient_reason_for_visit_xpath).send_keys(rov)

    def enter_patient_allergy_details(self,allergy_name,allergy_date,severity,reaction):
        self.driver.find_element(By.XPATH,self.patient_allergy_name_xpath).send_keys(allergy_name)
        self.driver.find_element(By.XPATH,self.patient_allergy_type_drop_down_xpath).click()
        self.driver.find_element(By.XPATH,self.patient_allergy_select_allergy_type_xpath).click()
        self.driver.find_element(By.XPATH,self.patient_allergy_date_xpath).click()
        self.driver.find_element(By.XPATH,self.patient_allergy_date_xpath).send_keys(allergy_date)
        self.driver.find_element(By.XPATH,self.patient_allergy_severity_xpath).send_keys(severity)
        self.driver.find_element(By.XPATH,self.patient_allergy_reaction_xpath).send_keys(reaction)

    def enter_patient_problem(self,problem_name,diagnosed_date):
        self.driver.find_element(By.XPATH,self.patient_problem_name_xpath).send_keys(problem_name)
        self.driver.find_element(By.XPATH,self.patient_diagnosed_date_xpath).click()
        self.driver.find_element(By.XPATH,self.patient_diagnosed_date_xpath).send_keys(diagnosed_date)

    def enter_patient_medication_details(self,medi_name,medi_start_date,medi_end_date,medi_dose,medi_direction,past_medication):
        self.driver.find_element(By.XPATH,self.patient_medication_name_xpath).send_keys(medi_name)
        self.driver.find_element(By.XPATH,self.patient_medication_start_date_xpath).click()
        self.driver.find_element(By.XPATH,self.patient_medication_start_date_xpath).send_keys(medi_start_date)
        self.driver.find_element(By.XPATH,self.patient_medication_end_date_xpath).click()
        self.driver.find_element(By.XPATH,self.patient_medication_end_date_xpath).send_keys(medi_end_date)
        self.driver.find_element(By.XPATH,self.patient_medication_dose_xpath).send_keys(medi_dose)
        self.driver.find_element(By.XPATH,self.patient_medication_direction_xpath).send_keys(medi_direction)
        self.driver.find_element(By.XPATH,self.patient_medication_past_xpath).send_keys(past_medication)

    def enter_patient_vitals(self,oxy_saturation,height,weight,heart_rate,pain,systolic,diastolic,ph,vitals_date):
        self.driver.find_element(By.XPATH,self.patient_vitals_oxygen_saturation_xpath).send_keys(oxy_saturation)
        self.driver.find_element(By.XPATH,self.patient_vitals_height_xpath).send_keys(height)
        self.driver.find_element(By.XPATH,self.patient_vitals_weight_xpath).send_keys(weight)
        self.driver.find_element(By.XPATH,self.patient_vitals_heart_rate_xpath).send_keys(heart_rate)
        self.driver.find_element(By.XPATH,self.patient_vitals_pain_scale_xpath).send_keys(pain)
        self.driver.find_element(By.XPATH,self.patient_vitals_systolic_blood_pressure_xpath).send_keys(systolic)
        self.driver.find_element(By.XPATH,self.patient_vitals_diastolic_blood_pressure_xpath).send_keys(diastolic)
        self.driver.find_element(By.XPATH,self.patient_vitals_ph_xpath).send_keys(ph)
        self.driver.find_element(By.XPATH,self.patient_vitals_date_xpath).click()
        self.driver.find_element(By.XPATH,self.patient_vitals_date_xpath).send_keys(vitals_date)

    def enter_patient_social_history(self,identity,family_support,income,trauma,housing,education,legal,substance,personal_safety,sexual_health,schedule,spirituality,interest):
        self.driver.find_element(By.XPATH,self.patient_social_history_identity_xpath).send_keys(identity)
        self.driver.find_element(By.XPATH,self.patient_social_history_family_xpath).send_keys(family_support)
        self.driver.find_element(By.XPATH,self.patient_social_history_income_xpath).send_keys(income)
        self.driver.find_element(By.XPATH,self.patient_social_history_trauma_xpath).send_keys(trauma)
        self.driver.find_element(By.XPATH,self.patient_social_history_housing_xpath).send_keys(housing)
        self.driver.find_element(By.XPATH,self.patient_social_history_education_xpath).send_keys(education)
        self.driver.find_element(By.XPATH,self.patient_social_history_legal_xpath).send_keys(legal)
        self.driver.find_element(By.XPATH,self.patient_social_history_substance_xpath).send_keys(substance)
        self.driver.find_element(By.XPATH,self.patient_social_history_personal_safety_xpath).send_keys(personal_safety)
        self.driver.find_element(By.XPATH,self.patient_social_history_sexual_health_xpath).send_keys(sexual_health)
        self.driver.find_element(By.XPATH,self.patient_social_history_schedule_xpath).send_keys(schedule)
        self.driver.find_element(By.XPATH,self.patient_social_history_spirituality_xpath).send_keys(spirituality)
        self.driver.find_element(By.XPATH,self.patient_social_history_interest_xpath).send_keys(interest)

    def enter_patient_care_note(self,care_note):
        self.driver.find_element(By.XPATH,self.patient_care_note_text_box_xpath).send_keys(care_note)

    def enter_patient_preferred_pharmacy_details(self,pharma_name,pharma_address):
        self.driver.find_element(By.XPATH,self.patient_preferred_pharmacy_name_xpath).send_keys(pharma_name)
        self.driver.find_element(By.XPATH,self.patient_preferred_pharmacy_address_xpath).send_keys(pharma_address)

    def upload_patient_report(self,relative_path):
        #relative_path = "../../" + "utilities/SOAP.pdf"
        #self.driver.find_element(By.XPATH,self.patient_report_upload_box_xpath).click()

        self.driver.find_element(By.XPATH,self.patient_report_upload_box_xpath).send_keys(relative_path)

        #self.driver.execute_script("arguments[0].style.display = 'block';", upload_file)
        print('Pass')

    def click_on_save_patient_button(self):
        self.driver.find_element(By.XPATH,self.patient_case_save_button_xpath).click()

    def click_on_first_patient_from_list(self):
        self.driver.find_element(By.XPATH,self.first_patient_case_from_list_xpath).click()

    def click_on_assign_provider_button(self):
        self.driver.find_element(By.XPATH,self.assign_patient_case_button_xpath).click()

    def enter_details_on_assign_patient_case_form(self,enter_date,start_time,end_time):
        self.driver.find_element(By.XPATH,self.select_provider_drp_down_xpath).click()
        self.driver.find_element(By.XPATH,self.selecting_provider_from_top_of_list_xpath).click()

        # Press Escape Button from Keyboard
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE).perform()

        self.driver.find_element(By.XPATH,self.select_location_drop_down_xpath).click()
        self.driver.find_element(By.XPATH,self.selecting_location_from_top_of_list_xpath).click()

        self.driver.find_element(By.XPATH,self.appointment_date_xpath).click()
        self.driver.find_element(By.XPATH, self.appointment_date_xpath).send_keys(enter_date)

        self.driver.find_element(By.XPATH, self.appointment_start_time_xpath).click()
        self.driver.find_element(By.XPATH,self.appointment_start_time_xpath).send_keys(start_time)

        self.driver.find_element(By.XPATH, self.appointment_end_time_xpath).click()
        self.driver.find_element(By.XPATH,self.appointment_end_time_xpath).send_keys(end_time)
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.save_button_from_patient_assign_xpath).click()
        time.sleep(3)
