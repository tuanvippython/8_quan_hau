def is_valid_move(board, row, col, N):
    """
    Kiểm tra nước đi của con hậu có hợp lệ hay không
    """
    # Kiểm tra cột
    for i in range(N):
        if board[row][i] == 1:
            return False

    # Kiểm tra đường chéo chính
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i, j = i - 1, j - 1

    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i, j = i - 1, j + 1

    # Kiểm tra hàng
    for j in range(N):
        if board[j][col] == 1:
            return False

    return True


QUEEN = "\u265B"

def print_solution(board):
    """
    In ra ma trận giải pháp với hình ảnh con hậu
    """
    for row in board:
        for cell in row:
            if cell == 1:
                print(QUEEN, end=' ')
            else:
                print('.', end=' ')
        print()



def solve_n_queens(board, row, N):
    """
    Tìm giải pháp cho bài toán 8 con hậu bằng backtracking
    """
    # Nếu đã đặt được 8 con hậu thì in ra giải pháp
    if row == N:
        print_solution(board)
        return True

    # Duyệt qua các cột để đặt con hậu vào
    for col in range(N):
        if is_valid_move(board, row, col, N):
            # Đặt con hậu vào vị trí (row, col)
            board[row][col] = 1

            # Gọi đệ quy để đặt các con hậu tiếp theo
            if solve_n_queens(board, row + 1, N):
                return True

            # Nếu không tìm được giải pháp, bỏ con hậu khỏi vị trí (row, col)
            board[row][col] = 0

    # Nếu không thể đặt con hậu vào bất kỳ vị trí nào trong cột hiện tại, trả về False
    return False

n = int(input("Nhập kích thước bàn cờ: "))
board = [[0 for _ in range(n)] for _ in range(n)]
solve_n_queens(board, 0, n)
