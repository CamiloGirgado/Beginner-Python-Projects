birthdays = {'Alice': 'April 1', 'Bob': 'July 10', 'Anne': 'September 31'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        birthday = input()
        birthdays[name] = birthday
        print('Birthday database updated')