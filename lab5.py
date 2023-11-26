import random

students = ["Fatma", "Taha", "Aras"]
questions = ["What is the difference between while and for loops?",
              "How can you print custom error messages for runtime errors?"]

def show_students():
    print("Student List:")
    for x in students:
        print(f"{students.index(x) + 1} . {x}")

def show_questions():
    print("Questions:")
    for x in questions:
        print(f"{questions.index(x) + 1} . {x}")

def menu():
    print("--STUDENT QUESTION GENERATOR--")

    show_students()

    show_questions()

    print("Choose an action")
    print("A -> Add student")
    print("M -> Move the student up in the list")
    print("R -> Remove student by name")
    print("RL -> Remove the last student")
    print("----------------------------------")
    print("a -> Add question")
    print("r -> Remove question by item number")
    print("rl -> Remove the last question")
    print("G -> Randomly assign a question to a student")
    print("Q -> Quit the application")


def add_student(name):
    students.append(name)
    print(f"New student is added.")
    show_students()

def remove_student(name):
    if name in students:
        students.remove(name)
        print(f"{name} removed from list.")
        show_students()
    else:
        print(f"Student {name} is not şn list.")

def remove_last_student():
    if students:
        removed_student = students.pop()
        print(f"The last student '{removed_student}' is deleted.")
        show_students()
    else:
        print("No students to remove.")

def add_question(question):
    questions.append(question)
    print("New question added.")
    show_questions()

def remove_last_question():
    if questions:
        removed_question = questions.pop()
        print(f"The last question '{removed_question}' removed.")
        show_questions()
    else:
        print("No questions..")

def random_question():
    if students and questions:
        random_student = random.choice(students)
        random_question = random.choice(questions)
        print(f"{random_question} is asked for {random_student}")
    else:
        print("Not enough students or questions to perform random assignment.")

def remove_question_by_number(question_number):
    if 1 <= question_number <= len(questions):
        removed_question = questions.pop(question_number - 1)
        print(f"The question '{removed_question}' removed.")
        show_questions()
    else:
        print("Invalid question number. Please try again.")

def move_student_up(number):
    if 1 <= number <= len(students):
        index = number - 1
        student = students.pop(index)
        students.insert(index - 1, student)
        print(f"{student} moved up in the list.")
        show_students()
    else:
        print("Invalid student number. Please try again.")



def program():
    while True:
        menu()
        action = input("Please choose an action: ")

        if action == "A":
            name = input("Enter the student name to be added: ")
            add_student(name)
        elif action == "M":
            show_students()
            number = int(input("Enter student number to up in the list: "))
            move_student_up(number)
        elif action == "R":
            name = input("Enter student to remove: ")
            remove_student(name)
        elif action == "RL":
            remove_last_student()
        elif action == "a":
            question = input("Enter a question to add list: ")
            add_question(question)
        elif action == "r":
            show_questions()
            question_number = int(input("Enter the question number to remove: "))
            remove_question_by_number(question_number)
        elif action == "rl":
            remove_last_question()
        elif action == "G":
            random_question()
        elif action == "Q":
            print("Goodbye.")
            break
        else:
            print("Invalid action. Please try again.")

program()