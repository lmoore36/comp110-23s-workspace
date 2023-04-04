"""Choose Your Own Adventure - EX06!"""

__author__ = "730556876"

import random

player: str = ""
points: int = 0
GREEN_CHECK: str = "\U00002705"
RED_X: str = "\U0000274C"


def greet() -> None:
    """Greets player."""
    global player
    player = input("What is your name?\n")
    print(f"Hello {player}! Are you ready to take quizzes about UNC?")
  

def main() -> None:
    """Runs the main outline of the game."""
    global points

    greet()
  
    while True:
        print("")
        print(f"{player}, you have {points} adventure points.")
        print("Make a choice:")
        print("1. Take North Campus Quiz")
        print("2. Take South Campus Quiz")
        print("3. Graduate")

        choice = int(input("Type 1, 2, or 3.\n"))

        if choice == 1:
            north_campus()
        if choice == 2:
            points = south_campus(points)
        if choice == 3:
            print("Thanks for playing! Congrats on graduating from UNC!")
            print(f"You received {points} adventure points and no student debt!")
            return


north_campus_quiz_data: list[dict] = [
    {"Question": "What is the oldest north campus dorm?", 
     "Answers": ["Old East", "Spencer", "Winston"]},
    {"Question": "What is the busiest Franklin Street resturant?", 
     "Answers": ["Spicy 9", "Que Chula", "Cosmic Cantina"]},
    {"Question": "What is the coolest floor of Davis Library?", 
     "Answers": ["Floor 8", "Floor 10", "The Reading Room"]},
    {"Question": "Which dorm still has lead in the water?", 
     "Answers": ["Stacy", "McIver", "Teague"]},
    {"Question": "What is the best place to get coffee?", 
     "Answers": ["Carolina Coffee Shop", "Starbucks", "Epilogue"]}
]

south_campus_quiz_data: list[dict] = [
    {"Question": "What is the best south campus dorm?", 
     "Answers": ["Ehaus", "Hojo", "Morrison"]},
    {"Question": "Which sport has the biggest field?", 
     "Answers": ["Baseball", "Field Hockey", "Tennis"]},
    {"Question": "How often does the Chase soft serve work?", 
     "Answers": ["Occasionally", "Always", "Never"]},  
    {"Question": "Which building is the tallest?", 
     "Answers": ["Hojo", "Ehaus", "Koury"]},
    {"Question": "Which bus stops in front of Ehaus?", 
     "Answers": ["The RU", "The NU", "The U"]},
]


def north_campus() -> None:
    """Runs north campus quiz."""
    global points
    print("Starting north campus quiz.")
    points += do_quiz(north_campus_quiz_data)


def south_campus(points: int) -> int:
    """Runs south campus quiz."""
    print("Starting south campus quiz.")
    return points + do_quiz(south_campus_quiz_data)


def do_quiz(quiz_data: list[dict]) -> int:
    """Administers the quiz in quiz data and returns the number of points earned."""
    quiz_points: int = 0
    shuffled_quiz = quiz_data.copy()
    random.shuffle(shuffled_quiz)
  
    for q in shuffled_quiz:
        print(f"The questions is: {q['Question']}")
        answers = q['Answers']
 
        correct_answer = answers[0]
        shuffled_answers = answers.copy()
        random.shuffle(shuffled_answers)

        print("The options are:")
 
        for i in range(len(shuffled_answers)):
            print(f"{i+1}. {shuffled_answers[i]}")

        player_answer = int(input("Choose your answer.\n"))

        if shuffled_answers[player_answer - 1] == correct_answer:
            quiz_points += 1
            print(f"{GREEN_CHECK} Correct! You're a true Tar Heel! {GREEN_CHECK}")
        else:
            print(f"{RED_X} Incorrect! Are you sure you don't go to Duke? {RED_X}")
    
    return quiz_points


if __name__ == "__main__":
    main()
