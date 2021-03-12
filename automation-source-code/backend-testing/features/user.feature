Feature: User
    
    
    
    Scenario: TC_001 - Verify that it is possible to search an user by name
        Given I search user by name "Naik"
        Then  I verify response has the status code "200"
