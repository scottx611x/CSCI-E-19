Feature: Is it Friday yet?
  Everybody wants to know when it's Friday

  Scenario Outline: Day is or isn't Friday
    Given today is "<day>"
    When I ask whether it is "Friday"
    Then I should be told "<message>"

  Examples: All Weekdays
   | day       | message |
   | Sunday    | Nope    |
   | sunday    | Nope    |
   | sun       | Nope    |
   | Monday    | Nope    |
   | monday    | Nope    |
   | mon       | Nope    |
   | Tuesday   | Nope    |
   | tuesday   | Nope    |
   | tue       | Nope    |
   | Wednesday | Nope    |
   | wednesday | Nope    |
   | wed       | Nope    |
   | Thursday  | Nope    |
   | thursday  | Nope    |
   | thu       | Nope    |
   | Friday    | Yep     |
   | friday    | Yep     |
   | fri       | Yep     |
   | Saturday  | Nope    |
   | saturday  | Nope    |
   | sat       | Nope    |
