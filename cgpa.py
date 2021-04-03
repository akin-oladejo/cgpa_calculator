from datetime import datetime
import os

def cgpa(inp):

    # assign a grade score to each grade
    grade_values = {'A':5,
                    'B':4,
                    'C':3,
                    'D':2,
                    'E':1,
                    'F':0}
    gp = []
    units = []
    for name, unit, grade in inp:
        gp.append(unit * grade_values[grade])
        units.append(unit)
    # return gp
    # return units
    return round(sum(gp)/sum(units), 3)

name = input('Enter first name: ').lower()
matric = input('Enter your matric number: ').replace('/','-')

#create directory for scores
if not os.path.exists(os.path.join(os.getcwd(), 'results')):
    os.mkdir(os.path.join(os.getcwd(), 'results'))

#create file name from name, matric and current time
file_name = f"results/{name}{matric}_{datetime.now().year}{datetime.now().month:02}{datetime.now().day:02}_{datetime.now().hour}{datetime.now().minute}{datetime.now().microsecond}.txt"


#the actual nucleus of the code
with open(file_name, mode='w+', encoding='utf-8') as file:

    #initially populate the log file with name and matric number
    file.write(f"Student(first name): {name.title()}\nMatric Number: {matric.replace('-','/')}")
    
    #run this step as many times as the number of semesters
    print('\n(P.S: To avoid errors in calculation, enter only the most recent score and grade of retaken courses)\n')
    semesters = int(input('Enter number of semesters you have taken: '))
    file.write(f'\nNumber of semesters taken: {semesters}')

    outer_loop_count = 1 #track the number of semesters inputted

    total_array = [] #contain all the grades, for cgpa purposes

    while semesters != 0:
        semester_name = input(f'\t-------------------\n\tEnter academic session of semester {outer_loop_count} (eg 2020/2021.1): ')
        file.write(f'\n\n--------------------\nSession: {semester_name}')

        #run this step as many times as the number of courses
        course_count = int(input('\tHow many courses did you take this semester? '))
        file.write(f"\nNumber of courses taken: {course_count}")

        inner_loop_count = 1 #track the number of courses inputted

        course_array = [] #array to contain the semester results
        while course_count != 0:
            course_name = input(f'\t\t-------------------\n\t\tCourse {inner_loop_count} code: ')
            credit = int(input('\t\tCourse credit value: '))
            grade = input('\t\tEnter obtained grade: ').capitalize()
            
            course_array.append((course_name, credit, grade)) #update the semester results with the course scores

            total_array.append((course_name, credit, grade)) # update the umbrella array with this semester's results

            inner_loop_count += 1 #increment the number of courses inputted
            course_count -= 1 #decrement the number of courses to go

        file.write('\n\nResults:')
        file.write(f"\n{'Course code':<28}{'Credit':<28}{'Grade':<28}")
        for element in course_array:
            file.write(f"\n{element[0]:<28}{element[1]:<28}{element[2]:<28}")
        print(f'\tSemester GPA: {cgpa(course_array)}')
        file.write(f'\n\nSemester GPA: {cgpa(course_array)}\n')

        outer_loop_count += 1 #increment the number of semesters inputted  
        semesters -= 1 #decrement the number of semesters to go 

    print(f'\n\n-------------------\nCumulative GPA: {cgpa(total_array)}\n-------------------')
    file.write(f'\n\n\n--------------------\nCumulative GPA: {cgpa(total_array)}\n--------------------')
    file.write(f'\n\nCOURSE LIST:{total_array}') #use lstrip when rerunning from a results file to get the cgpa back
    print(f"\n\nResults saved as '{file_name[8:]}' in 'results' folder.")