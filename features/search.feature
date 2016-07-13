# -*- coding: utf-8 -*-

Feature: Search

#  Scenario: Delivery Club Login
#    Given I navigate to the Delivery Club Home page
#    Given I Login in Home Page
#    When I go to Profile
#    When I delete first address
#    When I delete any address in list
#    Then I check the address removed
#    And I logout


   Scenario: Edit Profile
     Given I navigate to the Delivery Club Home page and Login
     When I go to Profile and click Edit
      And I edit "Имя", email and mailing flags and save change
#     Then I see that the changes are preserved
     And I logout
