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
    for student in student_list:
        studentDetails(student)
