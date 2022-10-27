# # Task3. Создйте программу для игры в "Крестики-нолики".

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def disign_board():
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')

def check(board):
    p1 = 'X'
    p2 = '0'
    if board[0] == board[1] == board[2] == p1 or board[0] == board[1] == board[2] == p2:
        return True
    elif board[3] == board[4] == board[5] == p1 or board[3] == board[4] == board[5] == p2:
        return True
    elif board[6] == board[7] == board[8] == p1 or board[6] == board[7] == board[8] == p2:
        return True
    elif board[0] == board[3] == board[6] == p1 or board[0] == board[3] == board[6] == p2:
        return True
    elif board[1] == board[4] == board[7] == p1 or board[1] == board[4] == board[7] == p2:
        return True
    elif board[2] == board[5] == board[8] == p1 or board[2] == board[5] == board[8] == p2:
        return True
    elif board[0] == board[4] == board[8] == p1 or board[0] == board[4] == board[8] == p2:
        return True
    elif board[2] == board[4] == board[6] == p1 or board[2] == board[4] == board[6] == p2:
        return True
    else:
        return False

def inp(board):
    x = int(input("Выберите позицию: "))
    if board[x-1] != '-':
        print("Эта позиция уже была выбрана, выберите другую")
        return inp(board)
    else:
        return x

player1 = 'Игрок1'
player2 = 'Игрок2'
disign_board()
for i in range(9):
    if i % 2 == 0:
        x = inp(board)
        board[x-1] = 'X'
        disign_board()
        if check(board):
            print('Игрок1 победил!')
            break
    else:
        x = inp(board)
        board[x-1] = '0'
        disign_board()
        if check(board):
            print('Игрок2 победил!')
            break
print('Game over!')

