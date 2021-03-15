# Student list
student_list = []


# Create a method for creating new students
def create_students():
    # Ask the user for the student's name
    student_name = input("Please enter student's name ?: ")
    # Create the dictionary
    student = {"name": student_name, "marks" : []}
    # Return that dictionary
    return(student)

# Method for appending marks to the student dictionary, created previously
def addMarks(student, mark):
    student["marks"].append(mark)


def calculateAverageMark(student):
    marks_count = len(student["marks"])
    # What happens if the student has no marks
    if marks_count == 0:
        return(0)
    
    # we put the rest of the elements here to make the code more optimal   
    marks_total = sum(student["marks"]) # since we do not calculate it when marks_count = 0
    marks_avg = marks_total / marks_count
    return(marks_avg)


def studentDetails(student):
    # print important infos about the student
    print("{}, average mark: {}.".format(student['name'],calculateAverageMark(student))) # find a way to use f-strings -> is better


def printStudents(student_list): # we are shadowing the same name, but there is no problem
    for i, student in enumerate(student_list):
        print(f"ID is equal to: {i}")
        print(student_list)


def menu():

    selection = input("Enter 'p' to print the student list, "
                "'s' to add a new student,'a' to add a mark to the student, "
                " or 'q' to quit: ")
    while selection != "q": 
        if selection == "p":
            printStudents(student_list)
        elif selection == "s":
            student_list.append(create_students())
        elif selection == 'a':
            student_id = int(input("Enter a student ID to add mark to: "))
            student = student_list[student_id]
            newMark = int(input("Enter the new mark to the student: "))
            addMarks(student, newMark)
        else:
            print("nothing to show here")
        selection = input("Enter 'p' to print the student list, "
                    "'s' to add a new student,'a' to add a mark to the student, "
                    " or 'q' to quit: ")



menu()

