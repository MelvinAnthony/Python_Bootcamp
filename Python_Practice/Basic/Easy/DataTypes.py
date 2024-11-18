#Problem 1
''' Need to create a nested list to store student name and grade and print second lowest student name in alphabetically
    Input Format:
        1. first input ask the user how many student
        2. ask student name and grade of the student in nested list
'''
if __name__ == '__main__':
    store_student = []
    for i in range(int(input("Enter the range: "))):
        name = input("Enter the name: ")
        score = float(input("Enter the Grade: "))
        store_student.append([name,score])
    
        