Feature: Introduction

  Scenario: Roboy Welcomes Groups
    When Roboy is started
    Then Roboy says
      """
      Welcome to the Guessing Game with Roboy
      Group 1, please tell me the name of your group.
      """

  Scenario: Ask for first Group
    Given Roboy asks for first Group Name
    When I say
      """
      Number One
      """
    Then Roboy says
      """
      Group 1 will now be called Number One
      Group 2, please tell me the name of your group.
      """
