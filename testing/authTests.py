from authentication.authTools import *


def test_register():
    name = "user1"
    email = "user@email.com"
    password = "password"
    register.name = name
    register.email = email
    register.password = password
    register()
    with open("users.txt", "a") as f:
        test_var = f.read()
    test_array = test_var.split()
    if name == test_array[0]:
        print("Test Registration Name: Pass")
    else:
        print("Test Registration Name: Fail")

    if email == test_array[1]:
        print("Test Registration Email: Pass")
    else:
        print("Test Registration Email: Fail")
    if password == test_array[2]:
        print("Test Registration Password: Pass")
    else:
        print("Test Registration Password: Fail")
    

def test_login():
    email = "user@email.com"
    password = "password"
    register.email = email
    register.password = password
    register()
    login.email = email
    login.password = password
    login()
