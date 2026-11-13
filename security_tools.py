# REAGAN MCLUCKIE | 30226399 | B01888719

# importing modules to use functions from them
import string
import random

def validatePassword(password: str, minlen: int=10) -> bool:
    isLenValid = False
    hasCharacter = False
    hasDigit = False
    hasSymbol = False

    # defining symbols to check if the password has any of them
    symbols = string.punctuation

    # checks if the password length if long enough for the minimum length required
    if len(password) < minlen:
        isLenValid = False
    else:
        isLenValid = True

    # Loops through the paassword to see if it has any digits or symbols in it
    for i in range(len(password)):
        # makes sure the password has a letter
        if password[i].isalpha():
            hasCharacter = True

        # Makes sure there is at least 1 number in the str by looping through every character
        if password[i].isdigit():
            hasDigit = True

        # Makes sure there is at least 1 symbol in the str by looping through every character
        if password[i] in symbols:
            hasSymbol = True

    # ensures all the requirements are met before returning the passwordValid as True or False
    if isLenValid and hasCharacter and hasDigit and hasSymbol:
        passwordValid = True
    else:
        passwordValid = False

    return passwordValid

def validateIpAddress(ip: str) -> bool:
    # divdies the ip address into parts
    parts = ip.split(".")
    # removes any whitespace from the parts of the ip address
    parts = [part.strip() for part in parts]
    isIpValid = True

    # checks if the ip address has 4 parts and if it doesnt its invalid
    if len(parts) != 4:
        isIpValid = False

    # loops through the parts of the ip address to make sure they are valid numbers between 0 and 255
    for part in parts:
        if not part.isdigit():
            isIpValid = False
            # Continues the program out of the loop because if a string like one is entered it will cause the program to crash trying to convert it to an int
            continue

        # Changes part from a str to an int to ensure its value is within the correct range
        number = int(part)

        if number < 0 or number > 255:
            isIpValid = False

    return isIpValid

def generateSecurePassword() -> str:
    # makes a pool of characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # randomly sets the length of the password to be between 10 and 16 characters long
    length = random.randint(10, 16)

    while True:
        password = ""
        hasUpper = False
        hasLower = False
        hasDigit = False
        hasSymbol = False

        # loops the the length the password is supposed to be chosing randomly from the character pool
        for x in range(length):
            character = random.choice(characters)
            # adds each character onto the password str making it one character longer every loop
            password += character

            if character.isupper():
                hasUpper = True

            if character.islower():
                hasLower = True

            if character.isdigit():
                hasDigit = True

            # uses string.punctucation from the string import to ensure it has a range of symbols to use
            if character in string.punctuation:
                hasSymbol = True

        # ensures the password has uppercase, lowercase, digits and a symbol to ensure that it is a secure password
        if hasUpper and hasLower and hasDigit and hasSymbol:
            return password