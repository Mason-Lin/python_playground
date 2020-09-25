*** Settings ***
Library    DateTime

*** Variables ***
${MESSAGE}    Good Morning!

*** Keywords ***


*** Test Cases ***
Simple Test Case
    Log    Hello World ${MESSAGE}
    ${today}    DateTime.Get Current Date
    Log    ${today}
