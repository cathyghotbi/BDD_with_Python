Feature: Addition
  Scenario: test adding 1 and 2
    # Given inputjkjk 1 undefined
    Given input
    When add
    Then result


  Scenario Outline: Test addition of two positive numbers
    Given two numbers, <first_number> and <second_number>
    When two numbers
    Then <result>
    Examples:
    | first_number | second_number | result|
    | 2            | 2             | 4     |
    | 3            | 5             | 8     |
