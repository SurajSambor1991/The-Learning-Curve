#1
# Function to create a tutoring and educational support service
def createEduService():
    print("Creating a Tutoring and Educational Service...")
    #Define educational service
    service = {
        'name': 'Edu Service',
        'description': 'A tutoring and educational support service that helps students of all ages and backgrounds achieve academic success.'
    }

    #Print status message
    print(f"Service created: {service['name']}")

    #Return service object
    return service

#2
# Function to add student to Edu Service
def addStudent(service, name, age, background):
    print(f"Adding student {name} to {service['name']}...")
    #Create student object
    student = {
        'name': name,
        'age': age,
        'background': background
    }

    #Add student to service
    service['students'].append(student)

    #Print status message
    print(f"Student {name} added to {service['name']}")

#3
# Function to add tutor to Edu Service
def addTutor(service, name, age, background):
    print(f"Adding tutor {name} to {service['name']}...")
    #Create tutor object
    tutor = {
        'name': name,
        'age': age,
        'background': background
    }

    #Add tutor to service
    service['tutors'].append(tutor)

    #Print status message
    print(f"Tutor {name} added to {service['name']}")

#4
# Function to remove student from Edu Service
def removeStudent(service, name):
    print(f"Removing student {name} from {service['name']}...")
    #Iterate over students
    for i, student in enumerate(service['students']):
        #Check for student name
        if student['name'] == name:
            #Remove student from service
            service['students'].pop(i)
            #Print status message
            print(f"Student {name} removed from {service['name']}")
            return

#5
# Function to remove tutor from Edu Service
def removeTutor(service, name):
    print(f"Removing tutor {name} from {service['name']}...")
    #Iterate over tutors
    for i, tutor in enumerate(service['tutors']):
        #Check for tutor name
        if tutor['name'] == name:
            #Remove tutor from service
            service['tutors'].pop(i)
            #Print status message
            print(f"Tutor {name} removed from {service['name']}")
            return

#6
# Function to list students in Edu Service
def listStudents(service):
    print(f"Listing students in {service['name']}...")
    #Iterate over students
    for student in service['students']:
        #Print student name
        print(student['name'])

#7
# Function to list tutors in Edu Service
def listTutors(service):
    print(f"Listing tutors in {service['name']}...")
    #Iterate over tutors
    for tutor in service['tutors']:
        #Print tutor name
        print(tutor['name'])

#8
# Function to match student with tutor
def matchStudentTutor(service, studentName, tutorName):
    print(f"Matching student {studentName} with tutor {tutorName}...")
    #Iterate over students
    for student in service['students']:
        #Check for student name
        if student['name'] == studentName:
            #Iterate over tutors
            for tutor in service['tutors']:
                #Check for tutor name
                if tutor['name'] == tutorName:
                    #Print status message
                    print(f"Matched student {studentName} with tutor {tutorName}")
                    #Return student and tutor objects
                    return student, tutor

#9
# Function to print student info
def printStudentInfo(student):
    #Print student info
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Background: {student['background']}")

#10
# Function to print tutor info
def printTutorInfo(tutor):
    #Print tutor info
    print(f"Name: {tutor['name']}")
    print(f"Age: {tutor['age']}")
    print(f"Background: {tutor['background']}")

#11
# Function to start tutoring session
def startSession(student, tutor):
    print(f"Starting tutoring session for {student['name']} with {tutor['name']}...")

#12
# Function to end tutoring session
def endSession(student, tutor):
    print(f"Ending tutoring session for {student['name']} with {tutor['name']}...")

#13
# Main function
def main():
    #Create Edu Service
    eduService = createEduService()
    #Initialize students and tutors list
    eduService['students'] = []
    eduService['tutors'] = []
    #Add students and tutors
    addStudent(eduService, 'John', 15, 'high school')
    addTutor(eduService, 'Jane', 31, 'college professor')
    #List students and tutors
    listStudents(eduService)
    listTutors(eduService)
    #Match student and tutor
    student, tutor = matchStudentTutor(eduService, 'John', 'Jane')
    #Print student and tutor info
    printStudentInfo(student) 
    printTutorInfo(tutor)
    #Start and end tutoring session
    startSession(student, tutor)
    endSession(student, tutor)
    #Remove student and tutor
    removeStudent(eduService, 'John')
    removeTutor(eduService, 'Jane')

#14
if __name__ == '__main__':
    main()

#15
# Function to create a tutoring and educational support service
def createEduService():
    print("Creating a Tutoring and Educational Service...")
    #Define educational service
    service = {
        'name': 'Edu Service',
        'description': 'A tutoring and educational support service that helps students of all ages and backgrounds achieve academic success.'
    }

    #Print status message
    print(f"Service created: {service['name']}")

    #Return service object
    return service

#16
# Function to add student to Edu Service
def addStudent(service, name, age, background):
    print(f"Adding student {name} to {service['name']}...")
    #Create student object
    student = {
        'name': name,
        'age': age,
        'background': background
    }

    #Add student to service
    service['students'].append(student)

    #Print status message
    print(f"Student {name} added to {service['name']}")

#17
# Function to add tutor to Edu Service
def addTutor(service, name, age, background):
    print(f"Adding tutor {name} to {service['name']}...")
    #Create tutor object
    tutor = {
        'name': name,
        'age': age,
        'background': background
    }

    #Add tutor to service
    service['tutors'].append(tutor)

    #Print status message
    print(f"Tutor {name} added to {service['name']}")

#18
# Function to remove student from Edu Service
def removeStudent(service, name):
    print(f"Removing student {name} from {service['name']}...")
    #Iterate over students
    for i, student in enumerate(service['students']):
        #Check for student name
        if student['name'] == name:
            #Remove student from service
            service['students'].pop(i)
            #Print status message
            print(f"Student {name} removed from {service['name']}")
            return

#19
# Function to remove tutor from Edu Service
def removeTutor(service, name):
    print(f"Removing tutor {name} from {service['name']}...")
    #Iterate over tutors
    for i, tutor in enumerate(service['tutors']):
        #Check for tutor name
        if tutor['name'] == name:
            #Remove tutor from service
            service['tutors'].pop(i)
            #Print status message
            print(f"Tutor {name} removed from {service['name']}")
            return

#20
# Function to list students in Edu Service
def listStudents(service):
    print(f"Listing students in {service['name']}...")
    #Iterate over students
    for student in service['students']:
        #Print student name
        print(student['name'])

#21
# Function to list tutors in Edu Service
def listTutors(service):
    print(f"Listing tutors in {service['name']}...")
    #Iterate over tutors
    for tutor in service['tutors']:
        #Print tutor name
        print(tutor['name'])

#22
# Function to match student with tutor
def matchStudentTutor(service, studentName, tutorName):
    print(f"Matching student {studentName} with tutor {tutorName}...")
    #Iterate over students
    for student in service['students']:
        #Check for student name
        if student['name'] == studentName:
            #Iterate over tutors
            for tutor in service['tutors']:
                #Check for tutor name
                if tutor['name'] == tutorName:
                    #Print status message
                    print(f"Matched student {studentName} with tutor {tutorName}")
                    #Return student and tutor objects
                    return student, tutor

#23
# Function to print student info
def printStudentInfo(student):
    #Print student info
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Background: {student['background']}")

#24
# Function to print tutor info
def printTutorInfo(tutor):
    #Print tutor info
    print(f"Name: {tutor['name']}")
    print(f"Age: {tutor['age']}")
    print(f"Background: {tutor['background']}")

#25
# Function to start tutoring session
def startSession(student, tutor):
    print(f"Starting tutoring session for {student['name']} with {tutor['name']}...")

#26
# Function to end tutoring session
def endSession(student, tutor):
    print(f"Ending tutoring session for {student['name']} with {tutor['name']}...")

#27
# Main function
def main():
    #Create Edu Service
    eduService = createEduService()
    #Initialize students and tutors list
    eduService['students'] = []
    eduService['tutors'] = []
    #Add students and tutors
    addStudent(eduService, 'John', 15, 'high school')
    addTutor(eduService, 'Jane', 31, 'college professor')
    #List students and tutors
    listStudents(eduService)
    listTutors(eduService)
    #Match student and tutor
    student, tutor = matchStudentTutor(eduService, 'John', 'Jane')
    #Print student and tutor info
    printStudentInfo(student) 
    printTutorInfo(tutor)
    #Start and end tutoring session
    startSession(student, tutor)
    endSession(student, tutor)
    #Remove student and tutor
    removeStudent(eduService, 'John')
    removeTutor(eduService, 'Jane')

#28
if __name__ == '__main__':
    main()