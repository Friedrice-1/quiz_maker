# Initialize an empty list to store questions
questions = []
# Create a loop that breaks if user wants to
while True:
# Ask user to input a question
    question = input("Please enter a question: ")
# Ask user to input choices A - D
    choice_a = input("Please enter choice 'A': ")
    choice_b = input("Please enter choice 'B': ")
    choice_c = input("Please enter choice 'C': ")
    choice_d = input("Please enter choice 'D': ")

    continue_input = input("Do you want to continue input [Y/N]?: ").upper()
    if continue_input == "N":
        break
# Write the collected data to a text file