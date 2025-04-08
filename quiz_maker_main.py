# Initialize an empty list to store questions
questions = []
# Create a loop that breaks if user wants to
while True:
# Ask user to input a question
    question = input("Please enter a question: ").capitalize()
# Ask user to input choices A - D
    choice_a = input("Please enter choice 'A': ").upper()
    choice_b = input("Please enter choice 'B': ").upper()
    choice_c = input("Please enter choice 'C': ").upper()
    choice_d = input("Please enter choice 'D': ").upper()

    correct_answer = input("Please enter the correct answer [A/B/C/D]: ").upper()

    continue_input = input("Do you want to continue input [Y/N]?: ").upper()
    if continue_input == "N":
        break
# Write the collected data to a text file