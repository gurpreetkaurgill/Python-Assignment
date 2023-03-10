emp_data = {}
count = 0
choice1 = int(input('Press 1 to Add employee\nPress 2 to exit '))
while choice1 < 1 or choice1 > 2:
    print('Enter correct input')
    choice1 = int(input('Press 1 to Add employee\nPress 2 to exit '))

if choice1 == 1:
    choice2 = 'y'
    while choice2.lower() == 'yes' or choice2.lower() == 'y':
        count += 1
        emp_no = int(input('Enter employee number: '))
        emp_name = input('Enter employee name: ')
        emp_salary = int(input('Enter employee salary: '))
        emp_address = input('Enter employee address: ')
        emp_married = input('Enter y if married and n or another letter if unmarried: ')
        if emp_married.lower() == 'y':
            emp_married = True
        else:
            emp_married = False
        
        emp_data[count] = [f'Employee number: {emp_no} ', f'Employee name: {emp_name} ', f'Employee salary: {emp_salary} ', f'Employee Address: {emp_address} ', f'Employee married: {emp_married}']
        choice2 = input('\nEnter yes or y to add another user\nEnter no or n to exit ')

    for i in emp_data:
        print(emp_data[i])


f = open ('emp_data.txt', 'w')
for i in emp_data:
    for j in range(0, len(emp_data[i])):
        f.write(emp_data[i][j])
    f.write('\n')