# The program below accepts 10 numbers from the user and performs a series
# of computation on it.
# This includes; SUMMATION, AVERAGE, DIFFERENCE and DIVISION

#
"""
userGeneratedList = []
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
userInput = float(input("Please Enter A Number: "))
userGeneratedList.append(userInput)
print(userGeneratedList)
"""


print("THIS PROGRAM WILL ASK THE USER TO PROVIDE TEN NUMBERS")
print("")


# Simplifying the Code into a function
def populate_list(num_entries):
    userGeneratedList = []
    for i in range(num_entries):
        userInput = float(input("Please Enter A Number: "))
        userGeneratedList.append(userInput)
    return userGeneratedList


num_entries = 10
userGeneratedList = populate_list(num_entries)

# This line of code provides a description and blank lines to improve code readability
print("")
print("")
print("A. SUMMATION OF THE TEN NUMBERS")

# Summation Of List Goes Here
sumOfList = 0
for x in userGeneratedList:
    sumOfList += x
print("The Sum Of The Values In The List Is: ", sumOfList)

# This line of code provides a description and blank lines to improve code readability
print("")
print("")
print("B. MEAN OF THE TEN NUMBERS")

# The Average Of The List Goes Here
listItemCounter = len(userGeneratedList)
averageOfList = sumOfList / listItemCounter
print("The Mean Of The List Is: ", averageOfList)

# This line of code provides a description and blank lines to improve code readability
print("")
print("")
print("C. DIFFERENCE OF THE TEN NUMBERS")

# The Difference Of The List Goes Here
# The List splicing function is used here to create a new list from the user generated list
firstFive = userGeneratedList[:5]
lastFive = userGeneratedList[5:]

# The Sum() function is employed on the lists to sum up all the elements of the two lists and
# assign them their own variables
sumOfFirst5 = sum(firstFive)
sumOfLast5 = sum(lastFive)

# This calculates the difference between the sum of the two lists.
differenceOfList = sumOfFirst5 - sumOfLast5
print("The Difference Between The Two Halves Is: ", differenceOfList)

# This line of code provides a description and blank lines to improve code readability
print("")
print("")
print("D. DIVISION OF THE TEN NUMBERS")

# The Division Of The List Goes Here
# Using a for loop to iterate through the elements of the list and multiply them together
productOfFirst5 = 1
for x in userGeneratedList[:5]:
    productOfFirst5 *= x

productOfLast5 = 1
for x in userGeneratedList[5:]:
    productOfLast5 *= x

# This line computes the division of the two products of the lists:1
divisionOfTheList = productOfFirst5 / productOfLast5
divisionOfTheList = round(divisionOfTheList, 4)  # This round the number of the decimal points to 4
print("The Result Of The Divisions Is: ", divisionOfTheList)
