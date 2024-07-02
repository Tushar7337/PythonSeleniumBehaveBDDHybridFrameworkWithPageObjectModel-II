Feature: Patient Case

  Background:
    Given I am on application Dashboard

    @patient @add-patient
    Scenario: Add Patient with Required Fields
      When I click on Patient tab
      And I click on Add Patient button and fill only required fields
      And I click on Save Patient Button
      Then Patient case should get created