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
    
    question_data = {
        "question": question,
        "choices": {
            "A": choice_a,
            "B": choice_b,
            "C": choice_c,
            "D": choice_d
        },
        "correct": correct_answer
    }
    questions.append(question_data)

    continue_input = input("Do you want to continue input [Y/N]?: ").upper()
    if continue_input == "N":
        break

# Write the collected data to a text file
with open("quiz_data.txt", "w") as file:
    for q in questions:
        file.write(f"Question: {q['question']}\n")
        for key, val in q["choices"].items():
            file.write(f"  {key}: {val}\n")
        file.write(f"Correct Answer: {q['correct']}\n")
        file.write("-" * 40 + "\n")

print("All questions saved to 'quiz_data.txt' in the same directory")