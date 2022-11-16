Feature: Instagram Login

  Scenario: Test the instagram login
    Given I launch the Browser
    When I Open the instagam Page
    And  I Enter the username "ms.vaishnavi_1207" and password "vaishnavi@ajinkya29"
    And  I click login Button
    Then user must successfully login to the dash board page

  Scenario Outline: Test the instagram login with multiple parameters
    Given I launch the Browser
    When I Open the instagam Page
    And  I Enter the username "<username>" and password "<password>"
    And  I click login Button
    Then user must successfully login to the dash board page

    Examples:
    | username | password |
    | ms.vaishnavi_1207 | vaishnavi@ajinkya29 |
    | vaishnavi@ajinkya29 | ms.vaishnavi_1207 |
    | ms.vaishnavi_12  | vaishnavi@ajinkya29 |
    | ms.vaishnavi_1207 | vaishnavi@ajinkya |




