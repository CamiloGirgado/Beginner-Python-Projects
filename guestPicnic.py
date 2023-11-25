allGuests = {'Alice': {'apples':5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 5, 'apples': 3}, 
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of items being brought: ')
print(' - Apples            ' + str(totalBrought(allGuests, 'apples')))
print(' - Pretzels          ' + str(totalBrought(allGuests, 'pretzels')))
print(' - Ham Sanwiches     ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Cakes             ' + str(totalBrought(allGuests, 'cakes')))
print(' - Apple Pies        ' + str(totalBrought(allGuests, 'apple Pies')))
