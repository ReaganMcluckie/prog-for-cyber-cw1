# REAGAN MCLUCKIE | 30226399 | B01888719

import security_tools as st

def isIpValid(ip: str) -> bool:
    # returns a bool either true or false depending if the ip address is valid or not.
    return st.validateIpAddress(ip)

def isPasswordValid(password: str) -> bool:
    # returns a bool either true or false depending if the password is valid or not.
    return st.validatePassword(password)

def main() -> None:
    try:
        # asks the user to input an ip address and checks if its valid.
        ipinput = str(input("Please enter an IP: "))
        if isIpValid(ipinput):
            validIP = True
        else:
            validIP = False

    # if the input isnt a valid input it will print the error message.
    except ValueError:
        print("Invalid input.")

    try:
        # asks the user to input a password and checks if its valid.
        passwordinput = str(input("Please enter a password: "))
        if isPasswordValid(passwordinput):
            validPassword = True
        else:
            validPassword = False

    # if the input isnt a valid input it will print the error message.
    except ValueError:
        print("Invalid input.")

    if validIP:
        print("The IP address is valid.")
    else:
        print("The IP address is invalid.")

    if validPassword:
        print("The password is strong.")
    else:
        print("The password is weak.")
        # if the password is weak it will generate a stronger password using the function from security_tools.py
        suggestedPassword = st.generateSecurePassword()
        # prints the stronger password suggestion to the user.
        print(f"Here is a stronger password suggestion: {suggestedPassword}")

if __name__ == "__main__":
    main()