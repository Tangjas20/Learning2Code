import sys

password = input("Please input your password: ")
correct_pass = "Test123"
attempts = 1

while password != correct_pass:
    if attempts <= 3:
        password = input("Invalid password, please try again")
        attempts += 1
print("Your account is locked")
