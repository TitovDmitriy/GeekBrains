from task_2_chess_module import generate_board as gbrd
from task_2_chess_module import check_queens as chq

if __name__ == '__main__':
    successful_boards = []

    while len(successful_boards) < 4:
        board = gbrd()
        if chq(board):
            successful_boards.append(board)

    for board in successful_boards:
        print(board)
