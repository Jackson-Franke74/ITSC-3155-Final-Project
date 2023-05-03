from hashlib import sha512
import os

# Register new user 
def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    with open("users.txt", "a") as f:
        f.write(f"{email},{password},{name}\n")
    print("Registration successful!")

# log in a user
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    with open("users.txt", "r") as f:
        for line in f:
            user_email, user_password, user_name = line.strip().split(",")
            if user_email == email and user_password == password:
                print(f"Welcome, {user_name}!")
                return
    print("Invalid email or password.")

# Log out a user
def logout():
    print("Logged out.")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
