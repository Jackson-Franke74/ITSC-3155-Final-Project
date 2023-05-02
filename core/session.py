from typing import List
import requests

currentDifficulty = "Any Difficulty"
currentType = "Any Type"

class PointSystem:
    def __init__(self):
        self.points = {}
    
    def add_points(self, user, points):
        if user in self.points:
            self.points[user] += points
        else:
            self.points[user] = points
    
    def remove_points(self, user, points):
        if user in self.points:
            self.points[user] -= points
            if self.points[user] < 0:
                self.points[user] = 0

    def get_points(self, user):
        return self.points.get(user, 0)
    
class TriviaQuestion:
    def __init__(self, question: str, answers: List[str], correct_answer: str, point_value: int):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.point_value = point_value
    
    @classmethod
    def create_question(cls):
        question = input("Please enter the trivia question: ")
        answers = []
        while True:
            answer = input("Please enter the answers (or 'done' to finish): ")
            if answer == 'done':
                break
            answers.append(answer)
        correct_answer = input("Please enter the correct answer: ")
        point_value = int(input("Please enter the point value: "))
        return cls(question, answers, correct_answer, point_value)

    
    def check_answer(self, player_answer: str) -> bool:
        return player_answer.lower() == self.correct_answer.lower()
    
    
class TriviaGame:
    def __init__(self, questions: List[dict]):
        self.questions = questions
        self.players = {}

    def add_player(self, name: str):
        self.players[name] = 0
    
    def play_question(self, questions: dict, player: str, answer: str) -> bool:
        q = TriviaQuestion(questions["question"], questions["answer"], questions["correct_answer"], questions["point_value"])
        if answer.lower() == q.correct_answer.lower():
            print("Correct!")
            self.players[player] += q.point_value
        else:
            print("Incorrect!")
    
    def play_game(self):
        for question in self.questions:
            print("Question:", question["question"],"\nPoint Value:",question["point_value"])
            for i, answer in enumerate(question["answer"]):
                print(f"{i+1}. {answer}")
            response = input("Your answer (put the number that's corresponding.): ")
            player = input("Your name: ")
            if player not in self.players:
                self.add_player(player)
            if response.isdigit():
                response = int(response)
                if response >= 1 and response <= len(question["answer"]):
                    if self.play_question(question, player, question["answer"][response-1]):
                        pass
                    else:
                        pass
                else:
                    print("invalid answer number")
            else:
                print("invalid input")
    
    def print_leaderboard(self):
        sorted_players = sorted(self.players.items(), key= lambda x:x[1], reverse= True)
        for player, score in sorted_players:
            print(f"{player}: {score} points")
            
# Define current difficulty level, category of questions and type of question
def changeQuestions():
    diff = input("What level of difficulty would you like? (1, 2 or 3)")
    typ = input ("What type of quesiton would you like? (Multiple choice or True/False&token=myToken)")
    if diff == "1" and typ == "Multiple choice": 
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple&token=myToken")
        print("Changed difficulty level to easy!")
        currentDifficulty = "Easy"
        currentType = "Multiple Choice"
    elif diff == "2" and typ == "Multiple choice":
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=multiple&token=myToken")
        print("Changed difficulty level to medium and type to True/False!")
        currentDifficulty = "Medium"
        currentType = "Multiple choice"
    elif diff == "3" and typ == "Multiple choice":
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=hard&type=multiple&token=myToken")
        print("Changed difficulty level to hard and type to True/False!")
        currentDifficulty = "Hard"
        currentType = "Multiple choice"
    elif diff == "1" and typ == "True/False":
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean&token=myToken")
        print("Changed difficulty level to easy and type to True/False!")
        currentDifficulty = "Easy"
        currentType = "True/False"
    elif diff == "2" and typ == "True/False": 
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean&token=myToken")
        print("Changed difficulty level to medium and type to True/False!")
        currentDifficulty = "Medium"
        currentType = "True/False"
    elif diff == "3" and typ == "True/False":
        response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean&token=myToken")
        print("Changed difficulty level to hard and type to True/False!")
        currentDifficulty = "Hard"
        currentType = "True/False"
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
    design = "User: " + user_name + "scored " + user_score + " on " + currentDifficulty +" difficulty and " + currentType + " type!" 
    return design


def main():
    makeOwnq1 = TriviaQuestion.create_question()

    questins = [{"question": makeOwnq1.question,
                 "answer" : makeOwnq1.answers,
                 "correct_answer": makeOwnq1.correct_answer,
                 "point_value": makeOwnq1.point_value}]

    
    game = TriviaGame(questins)
    game.play_game()
    game.print_leaderboard()

if __name__ == "__main__":
    main()