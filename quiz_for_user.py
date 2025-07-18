# import random
import random
# function to read the quiz file
def load_quiz(filename="quiz_data.txt"):
    questions = []
    with open(filename, "r") as file:
        lines = file.readlines()

# convert the file into a dictionary
    index = 0
    while index < len(lines):
        if lines[index].startswith("Question"):
            question_text = lines[index].strip().split("Question: ")[1]
            choices = {}
            for j in range(1,5):
                line = lines[index+j].strip()
                key, val = line.split(": ")
                choices[key] = val
            correct_line = lines[index + 5].strip()
            correct_answer = correct_line.split(": ")[1]
            questions.append({
                "Question": question_text,
                "Choices": choices,
                "Correct": correct_answer
            })
            index += 7
        else:
            index += 1
    return questions

# load questions from file
quiz = load_quiz()
# shuffle the questions
random.shuffle(quiz)

# start the quiz
score = 0
for q in quiz:
    print("\n" + q["Question"])
    for key, val in q["Choices"].items():
        print(f"  {key}: {val}")
    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid choice. Please enter A, B, C, or D.")
    if user_answer == q["Correct"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer was {q['Correct']}.")
# print result
print(f"\nYou got {score} out of {len(quiz)} correct.")