# import random
import random
# function to read the quiz file
def load_quiz(filename="quiz_data.txt"):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

quiz = load_quiz()
print(quiz)
# convert the file into a dictionary
# load questions from file
# shuffle the questions
# start the quiz
# print result