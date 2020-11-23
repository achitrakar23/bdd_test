# Created by Patrick at 11/21/2020
Feature: Retirement age calculator
  # Enter feature description here

  Scenario: The user input birth year earlier or on 1937
    Given The Retirement age calculator is running
    When The user input 1905 for birth year and 5 for birth month
    Then The full retirement age is 65 and 0 months

  Scenario: The user input birth year that is 1938
    Given The Retirement age calculator is running
    When The user input 1938 for birth year and 5 for birth month
    Then The full retirement age is 65 and 2 months

  Scenario: The user input birth year that is 1939
    Given The Retirement age calculator is running
    When The user input 1939 for birth year and 5 for birth month
    Then The full retirement age is 65 and 4 months

  Scenario: The user input birth year that is 1940
    Given The Retirement age calculator is running
    When The user input 1940 for birth year and 5 for birth month
    Then The full retirement age is 65 and 6 months

  Scenario: The user input birth year that is 1941
    Given The Retirement age calculator is running
    When The user input 1941 for birth year and 5 for birth month
    Then The full retirement age is 65 and 8 months

  Scenario: The user input birth year that is 1942
    Given The Retirement age calculator is running
    When The user input 1942 for birth year and 5 for birth month
    Then The full retirement age is 65 and 10 months

  Scenario: The user input birth year that is 1943
    Given The Retirement age calculator is running
    When The user input 1943 for birth year and 5 for birth month
    Then The full retirement age is 66 and 0 months

  Scenario: The user input birth year that is 1954
    Given The Retirement age calculator is running
    When The user input 1954 for birth year and 5 for birth month
    Then The full retirement age is 66 and 0 months

  Scenario: The user input birth year that is 1955
    Given The Retirement age calculator is running
    When The user input 1955 for birth year and 5 for birth month
    Then The full retirement age is 66 and 2 months

  Scenario: The user input birth year that is 1956
    Given The Retirement age calculator is running
    When The user input 1956 for birth year and 5 for birth month
    Then The full retirement age is 66 and 4 months

  Scenario: The user input birth year thatis 1957
    Given The Retirement age calculator is running
    When The user input 1957 for birth year and 5 for birth month
    Then The full retirement age is 66 and 6 months

  Scenario: The user input birth year that is 1958
    Given The Retirement age calculator is running
    When The user input 1958 for birth year and 5 for birth month
    Then The full retirement age is 66 and 8 months

  Scenario: The user input birth year that is 1959
    Given The Retirement age calculator is running
    When The user input 1959 for birth year and 5 for birth month
    Then The full retirement age is 66 and 10 months

  Scenario: The user input birth year that is 1960
    Given The Retirement age calculator is running
    When The user input 1960 for birth year and 5 for birth month
    Then The full retirement age is 67 and 0 months

  Scenario: The user input birth year that is 3000
    Given The Retirement age calculator is running
    When the user input 3000 for birth year
    Then the calculator output ValueError about 3000

  Scenario: The user input birth year that is 1899
    Given The Retirement age calculator is running
    When the user input 1899 for birth year
    Then the calculator output ValueError about 1899


  Scenario Outline: The user input birth year that is between 1944 and 1953
    Given The Retirement age calculator is running
    When The user input "<year>" for birth year and 5 for birth month
    Then the full retirement age is 66 and 0 month

    Examples:
      | year  |
      | 1944  |
      | 1945  |
      | 1946  |
      | 1947  |
      | 1948  |
      | 1949  |
      | 1950  |
      | 1951  |
      | 1952  |
      | 1953  |
