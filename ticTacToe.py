theBoard = {'topL': ' ', 'top': ' ', 'topR': ' ',
            'midL': ' ', 'mid': ' ', 'midR': ' ',
            'bottomL': ' ', 'bottomMid': ' ', 'bottomR': ' '}

def printBoard(board):
    print(board['topL'] + '|' + board['top'] + '|' + board['topR'])
    print('-+-+-')
    print(board['midL'] + '|' + board['mid'] + '|' + board['midR'])
    print('-+-+-')
    print(board['bottomL'] + '|' + board['bottomMid'] + '|' + board['bottomR'])
printBoard(theBoard)

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn ='O'
    else: 
        turn = 'X'
printBoard(theBoard)
