def valid_sudoku(board):
    # board is a 9x9 2D array
    d = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                num = board[i][j]
                row = "row" + str(i) + num
                col = "col" + str(j) + num
                box = "box" + str(i // 3) + str(j // 3) + num
                if row in d or col in d or box in d:
                    return False
                d[row] = d[col] = d[box] = 1
    return True


def main():
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(valid_sudoku(board))

if __name__ == "__main__":
    main()
