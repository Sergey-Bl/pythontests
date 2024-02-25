Feature: Product Reviews
    In order to enhance product information for shoppers
    As a user
    I want to leave reviews on products

    Scenario: Opening the review module
        Given I find and select a product
        When I click on the review link
        And I click on the add review button
        Then I should see fields for name, description, phone, and a send button
        And none of these fields should be empty
