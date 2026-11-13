# REAGAN MCLUCKIE | 30226399 | B01888719

def validate_ip(ip: str) -> bool:
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

        # this converts part from a string into a new int variable called number
        number = int(part)

        # ensures the number is not bellow or above 255 or else the ip would be invalid
        if number < 0 or number > 255:
            isIpValid = False

    return isIpValid 

def main() -> None:
    try:
        # asks the user to enter an ip to valiate
        userinput = str(input("Please enter an IP: "))

        # isValid can be true or false depending if validate_ip determins it to be an invalid id or valid ip
        isValid = validate_ip(userinput)
    # if there is an error with the input that can cause a crash it will print "Invalid IP address" instead of crashing the program
    except ValueError:
        print("Invalid IP address")

    # if isValid == True it will print "Valid IP address"
    if isValid:
        print("Valid IP address")
    else:
        # it will print "Invalid IP address"
        print("Invalid IP address")

if __name__ == "__main__":
    main()