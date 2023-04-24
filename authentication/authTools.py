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

# Define current difficulty level
def changeDifficulty():
    questions = [] #this is the array where we would draw the questions and answers from
    diff = input("What level of difficulty would you like? (1, 2 or 3) ")
    if diff == "1": 
        def foreach (question, questions):
            if (question.Diffuculty() == "Easy"): #Dificulty is already a setting in the question database online
                questions.add(question);
    elif diff == "2": 
        def foreach (question, questions):
            if (question.Diffuculty() == "Medium"):
                questions.add(question);
    elif diff == "3": 
        def foreach (question, questions):
            if (question.Diffuculty() == "Hard"):
                questions.add(question);
    else: 
        print("Invalid difficulty")
    return questions

def TFMode():
    questions = [] #this array represents the question database
    def foreach (question, questions):
        if (question.Type() == "True / False"): #Type is an option for each question in the question database.
            #The other option is multiple choice
            questions.add(question)
    return questions

def SocialShare():
    user_name = input("Please enter your name: ")
    user_score = number_correct() #the score of correct answers from the user in the current round
    design = "User: " + user_name + "scored " + user_score + " on " + user_difficulty + "!" 
    return 

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4: Change diffuculty")
        print("5: Change to True/False")
        print("6: Share your score")
        print("7. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            changeDifficulty()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
