while True:
    print("enter your age: ")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age")

while True:
    print('Select a new password (Letters and Numbers only)')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')