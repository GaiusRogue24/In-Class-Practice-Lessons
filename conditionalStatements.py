userInput = float(input("Please Enter A Number: "))
userInput2 = float(input("Please Enter A Number: "))

print("")

print("Using The MAX Function")
max_value = max(userInput, userInput2)
print("The Maximum Value: ", max_value)

print("")

print("Using THE IF Statement")
if userInput > userInput2:
    print(userInput, " is greater than ", userInput2)
elif userInput == userInput2:
    print(userInput, " is equal to ", userInput2)
else:
    print(userInput, " is less than ", userInput2)
