from prettytable import PrettyTable

table = PrettyTable()

print('\n')
print("First lets start with student's personal details.")
print('\n')

name = input("Enter the name of the student : ")
class_ = input("Enter the class/sec of the student : ")
roll_no = input("Enter the roll no. of the student : ")

print('\n')
print("Now, lets get to the academic details.")
print('\n')

print('1. Maths')
print('\n')
term1_1 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
term2_1 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
term_1 = max(term1_1,term2_1)
pt_1 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
assignment_1 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
practical_1 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
grade_1 = input("Enter the grade to be given ( best of 2 ) : ")
totalmarks_1 = term_1 + pt_1 + assignment_1 + practical_1
print('\n')

print('2. Physics')
print('\n')
term1_2 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
term2_2 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
term_2 = max(term1_2,term2_2)
pt_2 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
assignment_2 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
practical_2 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
grade_2 = input("Enter the grade to be given ( best of 2 ) : ")
totalmarks_2 = term_2 + pt_2 + assignment_2 + practical_2
print('\n')

print('3. Chemistry')
print('\n')
term1_3 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
term2_3 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
term_3 = max(term1_3,term2_3)
pt_3 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
assignment_3 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
practical_3 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
grade_3 = input("Enter the grade to be given ( best of 2 ) : ")
totalmarks_3 = term_3 + pt_3 + assignment_3 + practical_3
print('\n')

print('4. Computer / Bio')
print('\n')
term1_4 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
term2_4 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
term_4 = max(term1_4,term2_4)
pt_4 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
assignment_4 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
practical_4 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
grade_4 = input("Enter the grade to be given ( best of 2 ) : ")
totalmarks_4 = term_4 + pt_4 + assignment_4 + practical_4
print('\n')

print('5. English')
print('\n')
term1_5 = float(input("Enter the marks obtained in term 1 ( out of 80 ) : "))
term2_5 = float(input("Enter the marks obtained in term 2 ( out of 80 ) : "))
term_5 = max(term1_5,term2_5)
pt_5 = float(input("Enter the marks to be given in periodic tests ( out of 10 ) : "))
assignment_5 = float(input("Enter the marks to be given in assignments ( out of 5 ) : "))
practical_5 = float(input("Enter the marks to be given in practicals ( out of 5 ) : "))
grade_5 = input("Enter the grade to be given ( best of 2 ) : ")
totalmarks_5 = term_5 + pt_5 + assignment_5 + practical_5
print('\n')

average = ( totalmarks_1 + totalmarks_2 + totalmarks_3 + totalmarks_4 + totalmarks_5 ) / 5




print('                                      Atomic Energy Central School No. 3                              ')
print('                                                 REPORT CARD                                          ')
print('\n')

print( "Name of the student : ", name )
print( "Class/Sec : ", class_ )
print( "Roll no. : ", roll_no )
print('\n')

table.field_names = ["SUBJECT", "TERM 1", "TERM 2", "PERIODIC TESTS", "ASSIGNMENT", "PRACTICALS", "TOTAL MARKS", "GRADE(Best of 2)"]

table.add_row(["Maths", term1_1, term2_1, pt_1, assignment_1, practical_1, totalmarks_1, grade_1])
table.add_row(["Physics", term1_2, term2_2, pt_2, assignment_2, practical_2, totalmarks_2, grade_2])
table.add_row(["Chemistry", term1_3, term2_3, pt_3, assignment_3, practical_3, totalmarks_3, grade_3])
table.add_row(["Computer / Bio", term1_4, term2_4, pt_4, assignment_4, practical_4, totalmarks_4, grade_4])
table.add_row(["English", term1_5, term2_5, pt_5, assignment_5, practical_5, totalmarks_5, grade_5])
table.add_row(["C.G.P.A. ", " ", " ", " = ", " ", " ", average, " "])
table_line = table.get_string().split('\n')
horizontal_line = table_line[0]
result_lines = 1
print("\n".join(table_line[:-(result_lines + 1)]))
print(horizontal_line)
print("\n".join(table_line[-(result_lines + 1):]))
