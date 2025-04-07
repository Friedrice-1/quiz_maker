# Initialize an empty list to store questions
questions = []
# Create a loop that breaks if user wants to
while True:
# Ask user to input a question
# Ask user to input choices A - D
    continue_input = input("Do you want to continue input [Y/N]?: ").upper()
    if continue_input == "N":
        break
# Write the collected data to a text file