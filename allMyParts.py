partNames = []
# Creating list of input recieved items
while True:
    print('Enter the name of part: ' + str(len(partNames) +1 ) + 
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    partNames = partNames + [name] #list concatination
print('Your part names are:')
for name in partNames:
    print(' ' + name)

#Assigning an inde number to the items previously input
for index, item in enumerate(partNames):
    print('Index' + str(index) + ' in suplies is: ' + item)

#Part search
print('Enter a part that you are looking for')
name = input()
if name not in partNames:
    print('That part is not in your parts list')
else:
    print(name + ' is in the parts list')