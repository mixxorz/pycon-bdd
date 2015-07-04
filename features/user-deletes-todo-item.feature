Feature: User delets todo item
  As a User
  I want to delete items from my todo list
  So that I won't see them anymore

    Scenario: Delete todo item
      Given the following todo items
        | todo_items             |
        | Buy PyCon tickets      |
        | Book hotel room        |
        | Check travel itinerary |
      When I delete "Buy PyCon tickets"
      Then I should not see "Buy PyCon tickets"
