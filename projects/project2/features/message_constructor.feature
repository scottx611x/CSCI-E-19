Feature: A MessageConstructor exists to construct JSON payloads from plain strings

  Scenario Outline: MessageConstructor is given different messages to construct
    Given message is "<message>"
    When MessageConstructor is initialized with said message
    Then the resulting message attribute should be: <message_dict>

  Examples: Different Messages
   | message  | message_dict       |
   | hey      | {"message": "hey"}  |
   | you      | {"message": "you"}  |
   | dude     | {"message": "dude"} |

