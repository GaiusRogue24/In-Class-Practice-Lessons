max_attempts = 3
username = "uenr"
password = "!password@123"
attempts = 0

print('Welcome To The \n UENR MIS \n Portal')
print('***************')

while attempts <= max_attempts:
    entered_username = input("Enter Your Username:")
    if entered_username == username:
        entered_password = input("Enter Your Password:")
        if entered_password == password:
            print("Login successful. Access granted to the UENR MIS.")
        else:
            print("Incorrect password. Please try again.")
            attempts += 1
    else:
        print("Incorrect username. Please try again.")
        attempts += 1
print("You've exceeded the maximum number of attempts. Account locked.")