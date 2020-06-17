***Settings***
Library    RobotLib${/}robotlib.py
Resource    keywords${/}keywords.robot

***Test Cases***
My Test
    ${result} =    This Keyword Exist In Test
    This Keyword Not Exist In Test
    ${result} =    This Keyword Exist In Keywords    hello keyword
    ${result} =    This Keyword Exist In RobotLib    hello robotlib

***Keywords***
This Keyword Exist In Test
    [Return]    OK
