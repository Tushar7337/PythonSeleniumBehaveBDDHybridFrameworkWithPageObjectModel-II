Feature: Assign Patient Case

  Background:
    Given I am on application Dashboard

  @assign-patient
  Scenario: Assign Patient Case To Student
    When I navigate to Patient tab
    And Click on First Patient from the Patient list
    And I Click on Assign Provider Button
    And Fill all the reuqired details and click on Save Button
    Then Patient Case should get assign to Student

