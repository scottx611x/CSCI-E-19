Feature: A User request is made to the root URL path (`/`)

  Scenario: User makes request
    Given Path is "/"
    When User requests said path
    Then They should get a 200 response
    Then They should receive the following message from a JSON payload: Hello World!