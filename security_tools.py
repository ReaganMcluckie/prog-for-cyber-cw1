# REAGAN MCLUCKIE | 30226399 | B01888719

import string
import random

def validatePassword(password: str, minlen: int="10") -> bool:
    isLenValid = False
    hasDigit = False
    hasSymbol = False

    symbols = "!", "@", "#", "$", "%"

    if len(password) < minlen:
        isLenValid = False
    else:
        isLenValid = True

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


    if isLenValid and hasDigit and hasSymbol:
        passwordValid = True
    else:
        passwordValid = False

    return passwordValid

def validateIpAddress(ip: str) -> bool:
    parts = ip.split(".")
    parts = [part.strip() for part in parts]
    isIpValid = True

    if len(parts) != 4:
        isIpValid = False

    for part in parts:
        if not part.isdigit():
            isIpValid = False

        number = int(part)

        if number < 0 or number > 255:
            isIpValid = False

    return isIpValid

def generateSecurePassword() -> str:
    characters = string.ascii_letters + string.digits + string.punctuation

    length = random.randint(10, 16)

    password = ''.join(random.choice(characters) for x in range(length))

    return password