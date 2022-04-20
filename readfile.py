# r- read, 2 - write, r+ - read/write, a - append
#insert file into directory and call out with open command

employee_file = open("Names.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

