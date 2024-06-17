import requests
import json
import random
import html


def start_quiz(questions):
    score = 0 

    for idx, question in enumerate(questions):
        decoded_question = html.unescape(question['question'])
        print(f"\nQuestion {idx + 1}: {decoded_question}")

        options = question['incorrect_answers']
        options.append(question['correct_answer'])
        random.shuffle(options)  # Shuffle so correct answer is a different option each time

        for i, option in enumerate(options):
            decoded_option = html.unescape(option)
            print(f"{i + 1}. {decoded_option}")

        while True:
            try:
                answer = int(input("Enter the number of your answer: "))
                if 1 <= answer <= len(options):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if options[int(answer) - 1] == question['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {question['correct_answer']}")

    print(f"\nFinal score is {score}/{len(questions)}")


def fetch_questions():
    url = "https://opentdb.com/api.php?amount=10&category=9&type=multiple"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None


def main():
    print("Welcome to my Quiz!")

    while True:
        playing = input("Are you ready to begin? (yes/no): ").strip().lower()
        if playing != "yes":
            print("Goodbye!")
            break

        questions = fetch_questions()
        if questions:
            start_quiz(questions)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
