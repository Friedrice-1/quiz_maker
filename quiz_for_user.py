# import random
import random
# function to read the quiz file
def load_quiz(filename="quiz_data.txt"):
    questions = []
    with open(filename, "r") as file:
        lines = file.readlines()

# convert the file into a dictionary
    i = 0
    while i < len(lines):
        if lines[i].startswith("Question"):
            question_text = lines[i].strip().split("Question: ")[1]
            choices = {}
            for j in range(1,5):
                line = lines[i+j].strip()
                key, val = line.split(": ")
                choices[key] = val
            correct_line = lines[i + 5].strip()
            correct_answer = correct_line.split(": ")[1]
            questions.append({
                "Question": question_text,
                "Choices": choices,
                "Correct": correct_answer
            })
            i += 7
        else:
            i += 1
    return questions

# load questions from file
quiz = load_quiz()
# shuffle the questions
random.shuffle(quiz)

# start the quiz
# print result