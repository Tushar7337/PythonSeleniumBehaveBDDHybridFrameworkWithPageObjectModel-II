Feature: Check In Appointment as Student

  Background:
    Given I logged in as a Student and I am on Student Dashboard

  Scenario: Check In appointment
    When I click on Patient Name
    And Navigate to Appointment section and Click on Check In Button
    And Enter all required details of Clinical Note
    And Click on Sign Off button
    Then Clinical Note for respective patient should get created