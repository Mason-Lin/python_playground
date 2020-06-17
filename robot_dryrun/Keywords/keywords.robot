***Settings***

***Keywords***
This Keyword Exist In Keywords
    [Arguments]    ${message}
    Log    ${message}    level=INFO    console=True
    Log    ${message}    level=DEBUG    console=True
    Log    ${message}    level=TRACE    console=True
    This Keyword Not Exist In Keywords
    [Return]    OK
