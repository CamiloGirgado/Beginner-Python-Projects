board = {
            # White pieces
            '1h': 'wcastle', '1g': 'wrook', '1f': 'wbishop', '1e': 'wqueen', '1d': 'wking', '1c': 'wbishop', '1b': 'wrook', '1a': 'wcastle',
            '2h': 'wpawn', '2g': 'wpawn', '2f': 'wpawn', '2e': 'wpawn', '2d': 'wpawn', '2c': 'wpawn', '2b': 'wpawn', '2a': 'wpawn',
            # Black pieces

            '8h': 'bcastle', '8g': 'brook', '8f': 'bbishop', '8e': 'bqueen', '8d': 'bking', '8c': 'bbishop', '8b': 'bbrook', '8a': 'bcastle',
            '7h': 'bpawn', '7g': 'bpawn', '7f': 'bpawn', '7e': 'bpawn', '7d': 'bpawn', '7c': 'bpawn', '7b': 'bpawn', '7a': 'bpawn',
            }

def isValidChessBoard(board):
    # Validate counts and locations of pieces

    #Define pieces and colors
    pieces = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']
    colors = ['b', 'w']

    # Set pieces
    all_pieces = set(color + piece for piece in pieces for color in colors)

    # Define valid counts
    valid_counts = {'king':     (1, 1),
                    'queen':    (0, 2),
                    'rook':     (0, 2),
                    'bishop':   (0, 2),
                    'knight':   (0, 2),
                    'pawn':     (0, 8)}
    
    # Get count of pieces
    piece_cnt = {}
    for piece in all_pieces:
        piece_cnt.setdefault(piece, 0)

    for v_outer in board.values():
        piece_cnt[v_outer] += 1
    
    # Check if there are a valid number of pieces on the board
    for piece in pieces:
        cnt = piece_cnt.get(piece, 0)
        lo, hi = valid_counts[piece[1:]]
        if not lo <= cnt <= hi: # The count needs to be between the low and high values (aka not zero)
            if lo != hi:
                print(f'There should be between {lo} and {hi} {piece} but there are {cnt}')
            else:
                print(f'There should be {lo} {piece} but there are {cnt}')
            return False
        
    # Check if locations are valid)
    for location in board.keys():
        row = int(location[1:])
        column = ord(location[0]) - ord('a') + 1
        if not ((1 <= row <= 8) and ('a' <= column <= 'h')):
            print(f'Invalid to have {board[location]} at position {location}')
            return False

    # Check if all peices have valid names
    for loc, piece in board.items():
        if piece:
            if not piece in all_pieces:
                print(f'{piece} is not a valid chess piece at position {loc}')
                return False
    
    return True

print(isValidChessBoard(board))