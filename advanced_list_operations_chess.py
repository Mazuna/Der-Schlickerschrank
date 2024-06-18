board = []
EMPTY = "EMPTY"
ROOK = "ROOK"
KNIGHT = "KNIGHT"
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
    
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = KNIGHT
board[7][6] = KNIGHT