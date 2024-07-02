Feature: Staff CRUD Operation

  Background:
    Given I am on application Dashboard

  @staff @add-staff @smoke
  Scenario: Add staff with all fields
    When I click on staff tab
    And I click on Add Staff button and fill all required details
    And I click on Save button
    Then Staff should get created

  @staff @update-staff @update
  Scenario: Update Staff
    When I click on staff tab
    And I click on Action button and edit button
    And I made changes in staff
    And I click on Save button
    Then Staff details should get updated

  @staff @delete-staff
  Scenario: Delete Staff
    When I click on staff tab
    And I click on Action button and Delete button
    And I click on Yes button
    Then Staff details should get deleted

