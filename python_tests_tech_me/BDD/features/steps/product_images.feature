Feature: Viewing Product Images
    In order to get a better idea of the product before purchasing
    As a user
    I want to view product images

    Scenario: Opening the product image gallery
        Given I find and select a product
        When I click on the product image
        Then I should see the image panel and a close button
        And the image panel should not be empty
