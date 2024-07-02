Feature: Add Provider

  Background:
    Given I am on application Dashboard

  @provider @super-provider @smoke
  Scenario: Add Provider with all fields
    When I click on Add Provider button
    And I enter all the fields
    And I click on Submit button
    Then Provider should get added

   @provider @update-provider
   Scenario: Update Provider
     When I click on Action button and then Edit button
     And I made changes in Student
     And I click on Submit button
     Then Provider details should get updated

   @provider @delete-provider
   Scenario: Delete Provider
     When I click on Action button and then Delete button
     And I click on Yes Confirmation button
     Then Provider details should get deleted

   @provider-role
   Scenario Outline: Add different Provider Type
     When I click on Add Provider button
     And I enter all the fields and select provider type as "<provider_type>"
     And I click on Submit button
     Then Provider should get added
   Examples:
     |provider_type                   |
     |Prescribing Provider Student    |
     |Non Prescribing Provider Student|
     |Clinical Staff Student          |
     |Clerical Student                |
     |Billing Student                 |