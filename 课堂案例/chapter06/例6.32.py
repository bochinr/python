employee_1 = {'name': 'david', 'dept': 'ops', 'post': 'NOC', 'salary': 12000, 'id': 113}
employee_2 = {'name': 'brain', 'dept': 'auto', 'post': 'DBA', 'salary': 13000, 'id': 115}
employee_3 = {'name': 'chris', 'dept': 'search', 'post': 'PJM', 'salary': 20000, 'id': 150}
employees = [employee_1, employee_2, employee_3]
for employee in employees:
    employee['salary'] = employee['salary'] + 1000
print(employee['salary'])
