import hashlib
import os

# Register new user 
def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha512(password.encode()).hexdigest() # hash the password before storing it
    with open("users.txt", "a") as f:
        f.write(f"{email},{hashed_password},{name}\n")
    print("Registration successful!")

# log in a user
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha512(password.encode()).hexdigest() # hash the password before comparing it
    with open("users.txt", "r") as f:
        for line in f:
            user_email, user_password, user_name = line.strip().split(",")
            if user_email == email and user_password == hashed_password:
                print(f"Welcome, {user_name}!")
                return
    print("Invalid email or password.")

# Log out a user
def logout():
    print("Logged out.")

# Define current difficulty level
def changeDifficulty():
    questions = [] #this is the array where we would draw the questions and answers from
    diff = input("What level of difficulty would you like? (1, 2 or 3) ")
    if diff == "1": 
        def foreach(question, questions):
            if question.Difficulty() == "Easy": # spelling mistake corrected, and the Diffuculty() function replaced with Difficulty()
                questions.append(question)
    elif diff == "2": 
        def foreach(question, questions):
            if question.Difficulty() == "Medium":
                questions.append(question)
    elif diff == "3": 
        def foreach(question, questions):
            if question.Difficulty() == "Hard":
                questions.append(question)
    else: 
        print("Invalid difficulty")
    return questions

def TFMode():
    questions = [] #this array represents the question database
    def foreach(question, questions):
        if question.Type() == "True / False":
            #Type is an option for each question in the question database.
            #The other option is multiple choice
            questions.append(question)
    return questions

def SocialShare():
    user_name = input("Please enter your name: ")
    user_score = number_correct() #the score of correct answers from the user in the current round
    user_difficulty = changeDifficulty() # added a call to the changeDifficulty() function to get the current difficulty level
    design = f"User: {user_name} scored {user_score} on difficulty level {user_difficulty}!" # replaced string concatenation with f-string
    return design

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
