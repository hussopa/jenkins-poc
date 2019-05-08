*** Settings ***
Documentation    Read the file and test string length
Library          reader.py

*** Test Cases ***
My Test
    [Documentation]    Should be 20
    Test String  20

*** Keywords ***
Test String
    [Arguments]          ${value}
    check file           ${value}