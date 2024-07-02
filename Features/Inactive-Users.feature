Feature: Active/Inactive Users

  Background:
    Given I am on application Dashboard

  Scenario Outline: Active/Inactive Student
    When I click on Search box and Search Student with "<name>"
    And Click on Active Status toggle button
    Then Selected Student should get Inactive

  Examples:
    |name        |
    |Derek       |
    |Behave      |

