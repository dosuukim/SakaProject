import copy

def print_board(board):
    """9x9 스도쿠 보드를 출력합니다."""
    print("-" * 37) # 가로 길이 조정
    for i in range(9):
        if i % 3 == 0 and i != 0: # 3x3 서브그리드 구분을 위한 가로줄
            print("|-----------+-----------+-----------|")
        row_str = "| "
        for j in range(9):
            row_str += str(board[i][j] if board[i][j] != 0 else '.') + " " # 0은 .으로 표시
            if (j + 1) % 3 == 0: # 3x3 서브그리드 구분을 위한 세로줄
                row_str += "| "
        print(row_str.strip())
    print("-" * 37) # 가로 길이 조정

def find_empty_location(board):
    """보드에서 비어있는 위치 (0 또는 '.')를 찾습니다. 없으면 None, None을 반환합니다."""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0: # 0을 빈 칸으로 간주
                return r, c
    return None, None

def is_valid(board, num, row, col):
    """
    해당 위치에 숫자를 넣는 것이 유효한지 확인합니다.
    1. 행 검사
    2. 열 검사
    3. 3x3 서브그리드 검사
    """
    # 행 검사
    if num in board[row]:
        return False

    # 열 검사
    for r in range(9):
        if board[r][col] == num:
            return False

    # 3x3 서브그리드 검사
    subgrid_row_start = (row // 3) * 3
    subgrid_col_start = (col // 3) * 3

    for r in range(subgrid_row_start, subgrid_row_start + 3):
        for c in range(subgrid_col_start, subgrid_col_start + 3):
            if board[r][c] == num:
                return False

    return True

def solve_sudoku_for_check(board_to_solve):
    """스도쿠 퍼즐을 푸는 함수 (백트래킹 사용) - 정답 확인용"""
    # 원본 수정을 막기 위해 깊은 복사 사용
    board = copy.deepcopy(board_to_solve)

    row, col = find_empty_location(board)
    if row is None: # 빈 칸이 없으면 해결된 것
        return True # 성공적으로 풀리면 True 반환 (실제 풀린 board는 내부에서만 사용)

    for num in range(1, 10): # 1부터 9까지의 숫자 시도
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve_sudoku_for_check(board): # 재귀 호출
                return True
            board[row][col] = 0 # 백트래킹: 실패하면 원래대로 (0으로)
    return False

def get_solution(puzzle_board):
    """주어진 퍼즐의 해답을 반환합니다. 풀 수 없으면 None을 반환합니다."""
    board = copy.deepcopy(puzzle_board)
    
    # 임시 백트래킹 솔버 함수
    # (solve_sudoku_for_check와 유사하나, 실제 풀린 board를 반환하도록 수정)
    temp_empty_cells = []

    def find_next_empty(b):
        for r_idx in range(9):
            for c_idx in range(9):
                if b[r_idx][c_idx] == 0:
                    return r_idx, c_idx
        return None, None

    def solve(b):
        r, c = find_next_empty(b)
        if r is None:
            return True # 다 채웠으면 성공

        for number_to_try in range(1, 10):
            if is_valid(b, number_to_try, r, c):
                b[r][c] = number_to_try
                if solve(b):
                    return True
                b[r][c] = 0 # 백트랙
        return False

    if solve(board):
        return board
    else:
        return None # 풀 수 없는 퍼즐인 경우 (이론상으론 잘 만들어진 스도쿠는 항상 해가 있음)


def generate_puzzle():
    """미리 정의된 9x9 스도쿠 퍼즐과 그 해답을 생성합니다."""
    # 예시 퍼즐 (0은 빈 칸)
    puzzle = [
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
    # 위 퍼즐의 해답
    solution = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    return puzzle, solution


def play_game():
    """9x9 스도쿠 게임을 시작합니다."""
    puzzle_board, solution_board = generate_puzzle()
    current_board = copy.deepcopy(puzzle_board) # 사용자가 풀 게임 보드
    initial_board = copy.deepcopy(puzzle_board) # 초기 상태 보드 (힌트나 수정 불가 칸 표시용)

    print("--- 9x9 스도쿠 게임 시작! ---")
    print("빈 칸(.)에 1부터 9까지의 숫자를 입력하세요.")

    while True:
        print_board(current_board)
        empty_row, empty_col = find_empty_location(current_board)

        if empty_row is None: # 빈 칸이 없으면
            is_correct = all(current_board[r][c] == solution_board[r][c] for r in range(9) for c in range(9))
            if is_correct:
                print("축하합니다! 스도쿠를 완성했습니다!")
            else:
                # 이 경우는 is_valid에서 모든 입력을 체크하므로,
                # 사용자가 모든 칸을 채웠지만 오답인 경우는 발생하기 어렵습니다.
                # 만약 발생한다면, is_valid 로직이나 solution_board에 문제가 있을 수 있습니다.
                print("모든 칸을 채웠지만, 정답과 다릅니다. 확인해보세요.")
            break

        try:
            action = input("행,열,숫자 입력 (예: 3,5,7) / 지우기 (예: 3,5,0) / 종료 (q): ").strip().lower()

            if action == 'q':
                print("게임을 종료합니다.")
                break

            parts = action.split(',')
            if len(parts) != 3:
                print("입력 형식이 잘못되었습니다. '행,열,숫자' 형식으로 입력해주세요.")
                continue

            row, col, num_str = parts
            row = int(row.strip())
            col = int(col.strip())
            num = int(num_str.strip())


            row -= 1 # 0-indexed로 변환
            col -= 1 # 0-indexed로 변환

            if not (0 <= row < 9 and 0 <= col < 9):
                print("잘못된 행 또는 열 번호입니다. 1부터 9 사이로 입력해주세요.")
                continue

            if initial_board[row][col] != 0:
                print("이 칸은 처음부터 숫자가 채워져 있어 변경할 수 없습니다.")
                continue

            if num == 0: # 숫자 지우기
                if current_board[row][col] != 0 :
                    current_board[row][col] = 0
                    print(f"({row+1},{col+1}) 위치의 숫자를 지웠습니다.")
                else:
                    print(f"({row+1},{col+1}) 위치는 이미 비어있습니다.")
                continue

            if not (1 <= num <= 9):
                print("잘못된 숫자입니다. 1부터 9 사이의 숫자를 입력하거나, 지우려면 0을 입력하세요.")
                continue

            # 같은 숫자를 다시 입력하려고 하면 경고 (선택적)
            # if current_board[row][col] == num:
            # print(f"({row+1},{col+1}) 위치에는 이미 숫자 {num}이(가) 있습니다.")
            # continue

            # 다른 숫자를 넣기 전에 해당 칸을 비워야 is_valid가 올바르게 작동
            temp_val = current_board[row][col]
            current_board[row][col] = 0 # 임시로 비워서 유효성 검사
            if is_valid(current_board, num, row, col):
                current_board[row][col] = num
            else:
                current_board[row][col] = temp_val # 유효하지 않으면 원래 값으로 복원
                print(f"({row+1},{col+1})에 숫자 {num}을(를) 넣을 수 없습니다. (행, 열, 또는 3x3 서브그리드 규칙 위반)")

        except ValueError:
            print("잘못된 입력입니다. 숫자 형식으로 '행,열,숫자'를 입력해주세요 (예: 3,5,7).")
        except Exception as e:
            print(f"예상치 못한 오류 발생: {e}")

if __name__ == "__main__":
    play_game()