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
            questions.append({
                "Question": question_text,
            })
            i += 7
        else:
            i += 1
    return questions

quiz = load_quiz()
print(quiz)
# load questions from file
# shuffle the questions
# start the quiz
# print result