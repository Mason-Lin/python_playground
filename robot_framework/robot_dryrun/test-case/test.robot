***Settings***
Library    RobotLib/TestUtility.py
Library    Screenshot
Library    RobotLib/robotlib.py
Resource    keywords/keywords.robot

***Test Cases***
My Test
    ${screenshot_path} =    Take Screenshot Without Embedding
    TestUtility.Log Snapshot By Base64    ${screenshot_path}
    ${result} =    This Keyword Exist In Test
    This Keyword Not Exist In Test
    ${result} =    This Keyword Exist In Keywords    hello keyword
    ${result} =    This Keyword Exist In RobotLib    hello robotlib

***Keywords***
This Keyword Exist In Test
    [Return]    OK
