'''1.Find Highest Scoring Student From Nested Dictionary
Input
students = {
    "Ravi": {"marks": 85},
    "Anu": {"marks": 92},
    "Kiran": {"marks": 78},
    "Meena": {"marks": 95}
}
Output
Highest Scoring Student: Meena
Marks: 95'''

students = {
    "Ravi": {"marks": 85},
    "Anu": {"marks": 98},
    "Kiran": {"marks": 78},
    "Meena": {"marks": 95}
}


high=float('-inf')
st_name = ''
for student,marks in students.items():
    st_marks = marks['marks']
    if st_marks>high:
        high = st_marks
        st_name = student
print(st_name,high)

'''
2. Store Employee Details Using Nested Dictionaries
Input
employees = {
    1: {"name": "Rahul", "department": "HR", "salary": 40000},
    2: {"name": "Sneha", "department": "IT", "salary": 55000},
    3: {"name": "Arjun", "department": "Finance", "salary": 50000}
}
Output
Employee ID: 1
Name: Rahul
Department: HR
Salary: 40000
'''
employees = {
    1: {"name": "Rahul", "department": "HR", "salary": 40000},
    2: {"name": "Sneha", "department": "IT", "salary": 55000},
    3: {"name": "Arjun", "department": "Finance", "salary": 50000}
}
for employee,emp_details in employees.items():
    print('Employee Id: ',employee,end='\n')
    print('Name: ',emp_details['name'],end='\n')
    print('Department: ',emp_details['department'],end='\n')
    print('Salary: ',emp_details['salary'],end='\n')
    print('',end='\n')
