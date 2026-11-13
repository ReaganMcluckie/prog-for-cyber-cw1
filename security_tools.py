# REAGAN MCLUCKIE | 30226399 | B01888719

# importing modules to use functions from them
import string
import random

def validatePassword(password: str, minlen: int="10") -> bool:
    isLenValid = False
    hasDigit = False
    hasSymbol = False

    # defining symbols to check if the password has any of them
    symbols = "!", "@", "#", "$", "%"

    # checks if the password length if long enough for the minimum length required
    if len(password) < minlen:
        isLenValid = False
    else:
        isLenValid = True

    # Loops through the paassword to see if it has any digits or symbols in it
    for i in range(len(password)):
        if password[i].isdigit():
            hasDigit = True
        else:
            hasDigit = False

        for symbol in symbols:
            if symbol in password:
                hasSymbol = True
            else:
                hasSymbol = False

    # if the password meets all requirements it is valid else its invalid
    if isLenValid and hasDigit and hasSymbol:
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

        number = int(part)

        if number < 0 or number > 255:
            isIpValid = False

    return isIpValid

def generateSecurePassword() -> str:
    # makes a pool of characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # randomly sets the length of the password to be between 10 and 16 characters long
    length = random.randint(10, 16)

    # loops the the length the password is supposed to be chosing randomly from the character pool
    for x in range(length):
        password = ''.join(random.choice(characters))

    return password