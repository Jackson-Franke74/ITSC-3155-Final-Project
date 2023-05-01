from hashlib import sha512
import os
import requests

currentDifficulty = "Any Difficulty"
currentType = "Any Type"

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

# Define current difficulty level, category of questions and type of question
def changeQuestions():
    diff = input("What level of difficulty would you like? (1, 2 or 3)")
    typ = input ("What type of quesiton would you like? (Multiple choice or True/False&token=myToken)")
    if diff == "1" and typ == "Multiple choice": 
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple&token=myToken")
        print("Changed difficulty level to easy!")
    elif diff == "2" and typ == "Multiple choice":
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=multiple&token=myToken")
        print("Changed difficulty level to medium and type to True/False!")
    elif diff == "3" and typ == "Multiple choice":
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=hard&type=multiple&token=myToken")
        print("Changed difficulty level to hard and type to True/False!")
    elif diff == "1" and typ == "True/False":
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean&token=myToken")
        print("Changed difficulty level to easy and type to True/False!")
    elif diff == "2" and typ == "True/False": 
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean&token=myToken")
        print("Changed difficulty level to medium and type to True/False!")
    elif diff == "3" and typ == "True/False":
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean&token=myToken")
        print("Changed difficulty level to hard and type to True/False!")
    else: 
        print("Invalid choice")
    if response.status_code == 200: 
        print("Request successful!")
    else:
        print("Request failed with status code ", response.status_code)
    data = response.json()
    questions =  data["results"]
    for question in questions:
        print("Question: ", questions["question"])
        print("Correct answer: ", questions["correct_answer"])
        print("Incorrect answers: ", questions["incorrect_answers"])
        print()

def socialShare():
    response = requests.get("https://opentdb.com/api_token.php?command=request")
    if response.status_code == 200: 
        print("Request successful!")
    else:
        print("Request failed with status code ", response.status_code)
    data = response.json()
    user_name = input("Please enter your name: ")
    user_score = data["results"] #the score of correct answers from the user in the current round
    design = "User: " + user_name + "scored " + user_score + " on " + currentDifficulty +" difficulty and " + currentType + "type!" 
    return design

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change difficulty or question type")
        print("5. Share your score")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            changeQuestions()
        elif choice == "5":
            socialShare()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
