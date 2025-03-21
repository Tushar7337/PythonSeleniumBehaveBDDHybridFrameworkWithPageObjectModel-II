Feature:Login Functionality

@login @smoke
  Scenario Outline: Successful LoginLogin with valid creds
    Given I launch the URL and navigate to Sign in screen
    When Enter username as "<email>" and password as "<password>"
    And I click on the sign in Button
    Then I should be logged in
  Examples:
    |email                        |password        |
    |***************              |Test@123        |
    |***************              |Test@123        |

  @login
  Scenario: Login with Invalid Creds
    Given I launch the URL and navigate to Sign in screen
    When I enter invalid email and valid password
    And I click on the sign in Button
    Then I should get error message

