# Function 1: Greeting
def greet_student(name):
    return f"Hello, {name}"

# Function 2: Score Analysis
def analyze_scores(scores):
    num_subjects = len(scores)
    average_score = sum(scores) / num_subjects if num_subjects > 0 else 0
    return num_subjects, average_score

# Function 3: Pass/Fail Evaluation
def evaluate_performance(average_score):
    if average_score >= 50:
        return "Pass"
    else:
        return "Fail"

# Main Function
def main():
    # Input from user
    student_name = input("Enter student name: ")
    scores_input = input("Enter scores separated by spaces: ")
    student_scores = [float(score) for score in scores_input.split()]

    # Call functions
    greeting = greet_student(student_name)
    num_subjects, average_score = analyze_scores(student_scores)
    result = evaluate_performance(average_score)

    # Print final output
    print(greeting)
    print(f"Subjects: {num_subjects}")
    print(f"Average Score: {average_score:.1f}")
    print(f"Result: {result}")

# Run the program
main()
