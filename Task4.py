# REAGAN MCLUCKIE | 30226399 | B01888719

# displays the username and ip
def displayUNIP(info: dict) -> None:
    # prints the username from info
    print(info["username"])
    # prints the ip from info
    print(info["ip"])

# Adds an element to the Dictionary
def addElement(info: dict) -> dict:
    # asks the user for a name of the new field
    userinput = str(input("Please enter the name of the element you would like to add: "))
    # asks the user to input the value of the new field
    valueinput = str(input("Please enter the value of the new element: "))

    info[userinput] = valueinput

    return info

# updates a value in the Dictionary using the key and the new value
def updateRiskLevel(info: dict) -> dict:
    # asks the user for a new risk level
    userinput = str(input("Please enter the new risk level: "))

    # sets the risk level to the new value
    info["risklevel"] = userinput

    return info

# Removes an element from the Dictionary
def removeElement(info: dict) -> dict:
    # asks the user for the name of the field to remove
    userinput = str(input("Please enter the element you would like to remove: "))

    # deletes the field from info
    del info[userinput]

    return info

def printKeysandValues(info: dict) -> None:
    # prints the remaining keys
    print(f"Remaining Keys: {info.keys()}")
    # prints the remaining values
    print(f"Remaining Values: {info.values()}")

# Gets the length of Key Value Pairs and returns it as an int
def totalKeyValuePairs(info: dict) -> int:
    # sets length to the length of info
    length = len(info)

    return length


def main():
    print("======================")
    print("=       TASK 4       =")
    print("======================")

    info = {
        "username" : "Reagan",
        "ip" : "192.168.0.1",
        "eventtype" : "Login Failure",
        "risklevel" : "2"
    }


    """
    These bellow are all the functions being called and passing in the info which is the information
    allowing you to edit the dictionary
    """
    displayUNIP(info)

    info = addElement(info)

    info = updateRiskLevel(info)

    info = removeElement(info)

    printKeysandValues(info)

    length = totalKeyValuePairs(info)
    print(length)


if __name__ == "__main__":
    main()