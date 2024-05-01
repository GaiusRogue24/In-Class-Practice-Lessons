# Write A Code To Find The Number Of Eggs Miss Farida Put In A Basket
numberOfEggs = 60

while numberOfEggs <= 100:
    if numberOfEggs % 2 == 1 and numberOfEggs % 3 == 2 and numberOfEggs % 5 == 3:
        break
    numberOfEggs += 1

print("The Number Of Eggs Is ", numberOfEggs)
