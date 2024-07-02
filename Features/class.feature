Feature: Add Class

  Background:
    Given I am on application Dashboard

  @class @add-class @smoke
  Scenario: Add class with all required fields
    When I click on Add Class button
    And I enter all the fields required for class
    And I click on Submit Class button
    Then Class should get created

  @class @update-class
  Scenario: Update Class
     When I click on Class Action button and then Edit button
     And I made changes in Class
     And I click on Submit Class button
     Then Class details should get updated

  @class @delete-class
  Scenario: Delete Class
     When I click on Class Action button and then Delete button
     And I click on Yes button
     Then Class should get deleted