c = 1
n = int(input("Enter Number: "))

while True:
    n = n/10
    if n < 10:
        print(c)
    else:
        c += 1
