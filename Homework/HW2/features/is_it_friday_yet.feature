Feature: Is it Friday yet?
  Everybody wants to know when it's Friday

  Scenario Outline: Day is or isn't Friday
    Given today is "<day>"
    When I ask whether it is "Friday"
    Then I should be told "<message>"

  Examples: All Weekdays
   | day       | message |
   | Sunday    | Nope    |
   | sun       | Nope    |
   | Monday    | Nope    |
   | mon       | Nope    |
   | Tuesday   | Nope    |
   | tue       | Nope    |
   | Wednesday | Nope    |
   | wed       | Nope    |
   | Thursday  | Nope    |
   | thu       | Nope    |
   | Friday    | TGIF    |
   | fri       | TGIF    |
   | Saturday  | Nope    |
   | sat       | Nope    |
