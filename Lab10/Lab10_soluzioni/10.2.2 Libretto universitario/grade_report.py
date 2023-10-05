# Esercizio 10.2.2
# Libretto universitario

#  Generate a grade report for a student.

# Read the student id from the user.
sid = input("Enter the student id: ")

# Process each class found in classes.txt.
courses = open("classes.txt", "r", encoding='utf-8')
print("Student ID: ", sid)

for course in courses:
    # Remove the trailing newline from the class number.
    course = course.rstrip()

    # Open the list for the class and search for the student.
    in_f = open(course + ".txt", "r", encoding='utf-8')
    for line in in_f:
        parts = line.split()
        # If the student is in the class then print the mark.
        if sid == parts[0]:
            print(course + ' ' + line, end="")

    # Close the class file.
    in_f.close()

# Close the list of classes.
courses.close()
