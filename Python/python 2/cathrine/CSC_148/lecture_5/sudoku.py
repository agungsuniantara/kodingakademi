def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
    # Periksa baris
    if num in board[row]:
        return False

    # Periksa kolom
    if num in [board[i][col] for i in range(9)]:
        return False

    # Periksa kotak 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Sudoku telah selesai
    else:
        row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Kembalikan ke nilai awal jika solusi tidak berhasil
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

if __name__ == "__main__":
    # Papan Sudoku yang belum diisi, dengan 0 sebagai sel kosong
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Papan Sudoku sebelum diisi:")
    print_board(board)

    if solve_sudoku(board):
        print("\nPapan Sudoku setelah diisi:")
        print_board(board)
    else:
        print("Tidak ada solusi untuk papan Sudoku ini.")
