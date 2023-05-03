from typing import List
import requests
    
def create_points_system() -> dict:
    return{}

def add_points(points: dict, user: str, points_to_add: int):
    if user in points:
        points[user] += points_to_add
    else:
        points[user] = points_to_add

def remove_points(points: dict, user: str, points_to_remove: int):
    if user in points:
        points[user] -= points_to_remove
        if points[user] < 0:
            points[user] = 0

def get_points(points: dict, user: str) -> int:
    return points.get(user, 0)


def create_question() -> dict:
    question = input("Please enter your trivia question: ")
    answers = []
    while True:
        answer = input("Please enter the answers (or 'done' to finish): ")
        if answer == 'done':
            break
        answers.append(answer)
    while True:
        correct_answer = input("Please enter the correct answer: ")
        if correct_answer not in answers:
            print("Please only enter the answers that you have previously made.")
        else:
            print("Your selected correct answer is:", correct_answer)
            break
    while True:
        point_value = input("Please enter the point value: ")
        if point_value.isnumeric():
            print("Your selected point value is:", point_value)
            break
        else:
            print("Please only input numbers.")
    return{
        'question' : question,
        'answers' : answers,
        'correct_answer' : correct_answer,
        'point_value' : point_value
    }
 

def add_player(players: dict[str, int], name: str) -> None:
    players[name] = 0

def play_question(question: dict[str, any], players: dict[str, int], player: str, answer: str) -> None:
    if answer.lower() == question['correct_answer'].lower():
        print("Correct!")
    else:
        print("Incorrect!")

def play_game(questions: List[dict[str, any]]) -> dict[str, int]:
    players = {}
    for question in questions:
        print("Question: ", question["question"], "\nPoint Value: ", question["point_value"])
        for i, answer in enumerate(question["answers"]):
            print(f"{i+1}.{answer}")
        response = input("Your answer (put the number that's corresponding.): ")
        player = input("Your name: ")
        if player not in players:
            add_player(players, player)
        if response.isdigit():
            response = int(response)
            if response >= 1 and response <= len(question["answers"]):
                play_question(question, players, player, question["correct_answer"][response-1])
            else:
                print("invalid answer number")
        else:
            print("invalid input")
    return players

def play_game_free_response(game):
    for question in game.questions:
        print("Question:", question["question"], "\nPoint Value:", question["point_value"])
        response = input("Please input your answer: ")
        player = input("Your name: ")
        if player not in game.players:
            add_player(game, player)
        if response is not (type(str)):
            if play_question(game, question, player, response):
                pass
            else:
                pass
        else:
            print("invalid answer!")

def print_leaderboard(players: dict[str, int]) -> None:
    sorted_players = sorted(players.items(), key= lambda x:x[1], reverse= True)
    for player, score in sorted_players:
        print(f"{player}: {score} points")
        
def socialShare():
    response = requests.get("https://opentdb.com/api_token.php?command=request")
    if response.status_code == 200: 
        print("Request successful!")
    else:
        print("Request failed with status code ", response.status_code)
    data = response.json()
    user_name = input("Please enter your name: ")
    user_score = data["results"] #the score of correct answers from the user in the current round
    design = "User: " + user_name + "scored " + user_score + " on " + data["difficulty"] +" difficulty and " + data["type"] + " type!" 
    return design
