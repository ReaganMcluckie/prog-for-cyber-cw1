# REAGAN MCLUCKIE | 30226399 | B01888719

# importing modules to use their functions
import random
import socket
from datetime import datetime

# uses the random module to generate a random number between 1000 and 9999
def generateEventID() -> int:
    return random.randint(1000, 9999)

# uses datetime to make a timestamp
def generateTimestamp() -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp

# uses socket to get the local ip
def getIPAddress() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()

    return ip_address

# has defined login credentials and the function takes 2 parameters and if the credentials are correct it returns True
def login(username: str, password: str) -> bool:
    valid_username = "admin"
    valid_password = "admin123"

    if username == valid_username and password == valid_password:
        return True
    else:
        return False

def main():
    # asks the user to input a username and password
    userinput = str(input("Please enter your username: "))
    passinput = str(input("Please enter your password: "))

    # validates the login using the login function passing in the userinput and passinput
    loginValid = login(userinput, passinput)

    print("SECURITY EVENT LOG")
    print("------------------")

    # if the loginValid is true it prints all the info plus "Event: Successful login"
    if loginValid:
        print(f"Event ID: {generateEventID()}")
        print(f"Username: {userinput}")
        print(f"IP Address: {getIPAddress()}")
        print(f"Event: Successful login")
        print(f"Timestamp: {generateTimestamp()}")
    else:
        # if the loginValid is false it prints all the info plus "Event: Failed login"
        print(f"Event ID: {generateEventID()}")
        print(f"Username: {userinput}")
        print(f"IP Address: {getIPAddress()}")
        print(f"Event: Failed login")
        print(f"Timestamp: {generateTimestamp()}")

if __name__ == "__main__":
    main()