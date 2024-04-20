# 3 EN RAYA
# Implementacion de minmax
# -1 Circulo Gana - 0 Empate - 1 X Gana


def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
            

def is_winner():
    winner = 0
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    else:
        return 0


# def max_value(state):


def draw():
    # initialize an empty board
    board = ""

    # there are 5 rows in a standard tic-tac-toe board
    for i in range(5):
        # switch between printing vertical and horizontal bars
        if i%2 == 0:
            board += "|    " * 4
        else:
            board += " --- " * 3
        # don't forget to start a new line after each row using "\n"
        board += "\n"

    print(board)

draw()

def min_value(state):
    if board(state) || is_winner(state):
        return is_winner(state)
    
    for action in actions(state):
        
        
        