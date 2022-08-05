from random import randint
import timeit
start = timeit.default_timer()
def get_field():
    for i in range(3):
        for j in range(3):
            if field[i][j] == 'X': print("\033[1;32m X", end='\t')
            elif field[i][j] == 'O': print("\033[1;31m O", end='\t')
            else: print("\033[1;37m _", end='\t')
        print()

def get_cols():
    return [[row[i] for row in field] for i in range(3)]

def get_rows():
    return [field[i] for i in range(3)]

def get_diameters():
    return [[field[i][i] for i in range(3)], [field[i][2-i] for i in range(3)]]

def get_winner(p):
    if [p, p, p] in get_cols() + get_rows() + get_diameters():
        get_field()
        print("Player", p, "Won!")
        print_time()
        exit()

def print_time():
    stop = timeit.default_timer()
    print('Time: ', stop - start)

def change_player(p):
    if p == 'X': return 'O'
    else: return 'X'


while True:
    mode = int(input("Enter 1 for single player, 2 for multiplayer: "))
    if mode in [1, 2]: break

field = [['_'] * 3 for i in range(3)]
player = 'X'
while any('_' in sublist for sublist in field):
    get_field()
    print("Player", player)
    if mode == 1 and player == 'O':
        while True:
            row = randint(0, 2)
            col = randint(0, 2)
            if field[row][col] == '_': break
    else:
        row = int(input("Row: "))
        col = int(input("Column: "))
    if 0 <= row <= 2 and 0 <= col <= 2 and field[row][col] == '_':
        field[row][col] = player
        get_winner(player)
        player = change_player(player)
    else:
        print("Wrong! Try Again!")
print("No Winner!")
print_time()

