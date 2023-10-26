'''
Implement a Function called sort_students that takes a list of student object as input and sorts the
List based on their CGPA(Cumulative Grade Point Average) in descending order . Each student object 
has the following attributes: name (string),roll_number(string), and cgpa(float).Test the function 
With different input list of statement .
'''

class Student:

def__init__(self,name,roll_number,cgpa):
self.name = name
self.roll_number = roll_number
self.cgpa = cgpa


def sort_students(student_list):
# Sort the list of students in descending order at CGPA
sorted_students = sorted(student_list,
key=lambda student: student .cgpa,
reverse=True)
return sorted_students


# Example usage
students = [
  Student("Hari", "A123", 7.8),
  Student("janani","A124",8.9),
  Student("Viji","A125",9.1),
  Student("Amit","A126",8.7),
  ]

sorted_students = sort_students(students)