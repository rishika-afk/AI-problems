def printInformation(location):
    print("Location " + location + " is Dirty.")
    print("Cost for CLEANING " + location + ": 1")
    print("Location " + location + " has been Cleaned.")


def vacuumCleaner(goalState, currentState, location):
    # printing necessary data
    print("Goal State Required:", goalState)
    print("\nVacuum is placed in Location " + location)

    # cleaning locations
    totalCost = 0

    while (currentState != goalState):
        if (location == "A"):
            # cleaning
            if (currentState["A"] == 1):
                currentState["A"] = 0
                totalCost += 1
                printInformation("A")
            # moving
            if (currentState["B"] == 1 or currentState["C"]==1):
                print("Moving right to the location B.\nCost for moving RIGHT: 1")
                location = "B"
                totalCost += 1
            elif (currentState["D"] == 1):
                print("Moving down to the location D.\nCost for moving DOWN: 1")
                location = "D"
                totalCost += 1

        elif (location == "B"):
            # cleaning
            if (currentState["B"] == 1):
                currentState["B"] = 0
                totalCost += 1
                printInformation("B")
            # moving
            if (currentState["A"] == 1 ):
                print("Moving left to the location A.\nCost for moving LEFT: 1")
                location = "A"
                totalCost += 1
            elif (currentState["C"] == 1 or currentState["D"]==1):
                print("Moving down to the location C.\nCost for moving DOWN: 1")
                location = "C"
                totalCost += 1

        elif (location == "C"):
            # cleaning
            if (currentState["C"] == 1):
                currentState["C"] = 0
                totalCost += 1
                printInformation("C")
            # moving
            if (currentState["B"] == 1):
                print("Moving up to the location B.\nCost for moving UP: 1")
                location = "B"
                totalCost += 1
            elif (currentState["D"] == 1 or currentState["A"] == 1):
                print("Moving left to the location D.\nCost for moving LEFT: 1")
                location = "D"
                totalCost += 1
        
        elif (location == "D"):
            # cleaning
            if (currentState["D"] == 1):
                currentState["D"] = 0
                totalCost += 1
                printInformation("D")
            # moving
            if (currentState["A"] == 1 or currentState["B"] == 1):
                print("Moving up to the location A.\nCost for moving UP: 1")
                location = "A"
                totalCost += 1
            elif (currentState["C"] == 1):
                print("Moving right to the location C.\nCost for moving RIGHT: 1")
                location = "C"
                totalCost += 1
            
    print("GOAL STATE:", currentState)
    return totalCost


# declaring dictionaries
goalState = {"A": 0, "B": 0, "C": 0, "D" : 0 }
currentState = {"A": -1, "B": -1, "C": -1, "D" : -1 }

# taking input from user
location = input("Enter Location of Vacuum (A/B/C/D): ");
currentState["A"] = int(input("Enter status of A (0/1): "))
currentState["B"] = int(input("Enter status of B (0/1): "))
currentState["C"] = int(input("Enter status of C (0/1): "))
currentState["D"] = int(input("Enter status of D (0/1): "))

# calling function
totalCost = vacuumCleaner(goalState, currentState, location)
print("Performance Measurement:", totalCost)
