Feature: User adds todo item
  As a User
  I want to add items to my todo list
  So that I can be reminded of them later

    Scenario: Add todo item
      Given there are no todo items
      When I add "Buy PyCon tickets"
      Then I should see "1. Buy PyCon tickets"

    Scenario: Add second todo item
      Given there is one todo item
      When I add "Book hotel room"
      Then I should see "2. Book hotel room"
