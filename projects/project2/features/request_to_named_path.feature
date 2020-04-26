Feature: A User request is made to a path underneath the root URL path (`/`)

  Scenario Outline: User makes request
    Given Path is "<path>"
    When User requests said path
    Then They should get a 200 response
    Then They should receive the following message from a JSON payload: <message>

  Examples: Different Requests
   | path             | message                          |
   | /                | Hello World!                     |
   | /scott           | Hello Scott!                     |
   | /Scott           | Hello Scott!                     |
   | /super_secret    | You found the secret, good job!  |
