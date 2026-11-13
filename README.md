# Student Information
- Reagan Mcluckie
- New College Lanarkshire Motherwell
- B01888719

# Overview
This repository holds my programs for the course work 1.

Each one of my tasks are stored on separate branches being

- **Task 1:** `security-tool`
- **Task 2:** `security-event-logger`
- **Task 3:** `ip-address-validator`
- **Task 4:** `security-incident-manager`
- **Task 5:** `cyber-security-utilities`

## Changing Branch
You can change between each branch using the branch dropdown on GitHub being at the left the complete opposite of the green "Code" button and there you can see each task.

# Short Description Of Each Task

## Task 1

This task makes a little command line interface menu to allow you to choose what section of the task you want to run being either the Security Event Counter, Brute-Force Simulation, Login Authentication or the Exit option.

### Security Event Counter
This asks the user to enter a password 10 times. The correct password is stored in a variable inside of the function. It will count the number of times the password was entered correctly and incorrectly. It also displays the percentage of incorrect passwords entered and if the percentage is more than 50% it will make an alert

### Brute-Force Simulation
This asks the user to enter a password with a defined password in a variable. There is a maximum amount of attempts the user can try and when they reach the maximum the user is stopped being asked to enter a password and it lets them know that they have entered the maximum amount of attempts

### Login Authentication
prompts the user to enter a username and password and compares it to the username and password stored in the function. It gives you a maximum number of login attempts and if you fail to login within the maximum attempts it stops asking you for login details and displays a message that the account has been frozen for 24 hours

### Exit
Allows the user to exit the program printing "Thank you for using the security tool"

## Task 2

This program generates a log looking something like this if the login is successful

```
SECURITY EVENT LOG
-------------------
Event ID: 1105
Username: admin
IP Address: 192.168.0.143
Event: Successful Login
Timestamp: 2026-11-13 19:39:15
```

or it looks like this if its unsuccessful

```
SECURITY EVENT LOG
-------------------
Event ID: 1105
Username: admin
IP Address: 192.168.0.143
Event: Failed Login
Timestamp: 2026-11-13 19:39:15
```

## Task 3

This program validates if an IP address is valid or not using the validate_ip() function.

- Accepts an IP address that the user has entered
- Remove any spaces
- Checks if the IP address provided contains periods or dots
- Checks that the IP address has 3 periods or dots
- Checks if there is 4 numbers in the IP address
- Checks all numbers are between 0 and 255
- Returns True or False

## Task 4

The functionalities of this program are below

- Display Username and IP address
- Add a new field using an input to give it a name and value
- Update Risk Level
- Remove a field using its name you enter from an input
- Displays all remaining keys and values
- Displays the total amount of key value pairs

## Task 5

The program does the following

- validates a password ensuring it has at least 1 letter, digit and symbol
- ensures that an IP address is valid making sure there is 3 dots/periods, 4 octets and the range is between 0 and 255
- Generates a strong password using the random and string imports

In this task the code is seperated into the 2 files being main.py and security_tools.py. At the top of main you can see i import security_tools.py as st and throught the code you will see "st." which allows me to use the functions from that import.