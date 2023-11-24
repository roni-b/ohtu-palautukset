*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    username    salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials   kalle    kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials    as    salasana123
    Output Should Contain  Invalid username

Register With Enough Long But Invald Username And Valid Password
    Input Credentials    kissa@    salasana123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials    kissa    lyhyt1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    validi    password
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
