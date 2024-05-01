# Write a program that accepts the status of a customer and calculates the price of the calculator

# Price Of The Calculator
priceOfCalculator = 100

# Prompt To Accept Status
statusOfACustomer = input("Enter Your Status \n (Student, Lecturer, Shop Staff, Others): ").upper()

# Calculating Discount Based On Customer's Status
if statusOfACustomer == "STUDENT":
    discount = 0.4
    discounted_price = priceOfCalculator - (priceOfCalculator * discount)
    print("Your Discount Price For The Calculator Is: ", discounted_price, " Cedis")
elif statusOfACustomer == "LECTURER":
    discount = 0.15
    discounted_price = priceOfCalculator - (priceOfCalculator * discount)
    print("Your Discount Price For The Calculator Is: ", discounted_price, " Cedis")
elif statusOfACustomer == "SHOP STAFF" or statusOfACustomer == "STAFF" or statusOfACustomer == "SHOP":
    discount = 0.20
    discounted_price = priceOfCalculator - (priceOfCalculator * discount)
    print("Your Discount Price For The Calculator Is: ", discounted_price, " Cedis")
elif statusOfACustomer == "OTHER" or statusOfACustomer == "" or statusOfACustomer == " ":
    discount = 0
    discounted_price = priceOfCalculator - (priceOfCalculator * discount)
    print("Your Discount Price For The Calculator Is: ", discounted_price, " Cedis")
