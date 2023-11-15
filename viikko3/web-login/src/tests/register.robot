*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Reset App

*** Test Cases ***

Register With Valid Username And Password
    Set Username    username
    Set Password    salasana1
    Set Password Confirmation    salasana1
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    ab
    Set Password    salasana1
    Set Password Confirmation    salasana1
    Submit Credentials
    Page Should Contain  Invalid username

Register With Valid Username And Invalid Password
    Set Username    username
    Set Password    salasana
    Set Password Confirmation    salasana
    Submit Credentials
    Page Should Contain  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username    username
    Set Password    salasana1
    Set Password Confirmation    salasan1
    Submit Credentials
    Page Should Contain  Passwords are different

Login After Successful Registration
    Create User And Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Do Failed Register Attempt
    Set Username    user
    Set Password    incorrect
    Submit Credentials Login

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button    Register

Submit Credentials Login
    Click Button    Login

Register Should Succeed
    Title Should Be    Welcome to Ohtu Application!

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

Do Failed Register Attempt
    Create User    user    incorrect
    Go To Login Page

Login Should Succeed
    Main Page Should Be Open

Go To Register Page And Reset App
    Go To Register Page
    Reset Application