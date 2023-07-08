from random import randint as rndit


def check_queens(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][0] == arr[j][0] or arr[i][1] == arr[j][1] or abs(arr[i][0] - arr[j][0]) == abs(
                    arr[i][1] - arr[j][1]):
                return False

    return True


def generate_board():
    board = []
    for i in range(8):
        row = rndit(1, 8)
        board.append((i + 1, row))
    return board
