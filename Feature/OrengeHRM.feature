Feature: OrangeHRM Logo
  Scenario:Logo present on OrangeHRM Home Page
    Given launch chrome browser
    When Open OrangeHRM HomePage
    Then verify that the logo present on home page
    And close browser