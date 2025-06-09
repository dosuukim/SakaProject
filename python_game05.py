def print_board(board):
    """스도쿠 보드를 출력합니다."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def is_valid_move(board, row, col, num):
    """입력한 숫자가 해당 위치에 유효한지 확인합니다."""
    # 행 검사
    if num in board[row]:
        return False
    # 열 검사
    if num in [board[i][col] for i in range(9)]:
        return False
    # 3x3 박스 검사
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def is_board_filled(board):
    """스도쿠 보드가 모두 채워졌는지 확인합니다."""
    for row in board:
        if 0 in row:
            return False
    return True

def solve_sudoku(board):
    """스도쿠를 푸는 함수 (백트래킹 알고리즘 사용) - 이 예제에서는 사용자가 직접 풀도록 합니다."""
    # 이 함수는 자동 풀이용이며, 이 예제에서는 정답 확인용으로만 활용 가능합니다.
    # 실제 게임 플레이에서는 사용자가 직접 숫자를 입력합니다.
    # (구현 생략)
    pass

def main():
    """메인 스도쿠 게임 함수입니다."""
    # 예제 스도쿠 보드 (0은 빈 칸)
    # 좀 더 쉬운 퍼즐로 변경
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

    # 수정 불가능한 초기 숫자 표시 (선택 사항)
    initial_board = [row[:] for row in board] # 초기 상태 복사

    print("🎉 9x9 스도쿠 게임에 오신 것을 환영합니다! 🎉")
    print("숫자를 입력하려면 '행 열 숫자' 형식으로 입력하세요 (예: 1 2 3).")
    print("게임을 종료하려면 'q'를 입력하세요.")

    while True:
        print_board(board)
        if is_board_filled(board):
            # 모든 칸이 채워졌는지 확인하고, 실제 정답인지 확인하는 로직 추가 가능
            # 여기서는 간단히 모든 칸이 채워지면 종료하도록 함
            print("\n🎉 스도쿠를 완성했습니다! (정답 여부는 확인하지 않았습니다.) 🎉")
            break

        user_input = input("\n입력 (행 열 숫자 또는 'q'): ").strip().lower()

        if user_input == 'q':
            print("\n👋 게임을 종료합니다. 다음에 또 만나요!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("❌ 잘못된 입력입니다. '행 열 숫자' 형식으로 입력해주세요. 예: 1 2 3")
                continue

            row, col, num = int(parts[0]) - 1, int(parts[1]) - 1, int(parts[2])

            if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                print("❌ 잘못된 입력입니다. 행, 열은 1-9, 숫자는 1-9 사이여야 합니다.")
                continue

            if initial_board[row][col] != 0: # 초기 숫자인지 확인
                print("🚫 이 칸은 게임 시작 시 주어진 숫자이므로 변경할 수 없습니다.")
                continue

            if is_valid_move(board, row, col, num):
                board[row][col] = num
                print(f"✅ ({row + 1}, {col + 1})에 {num}을(를) 입력했습니다.")
            else:
                print("❌ 유효하지 않은 입력입니다. 다른 숫자를 시도해보세요.")

        except ValueError:
            print("❌ 잘못된 입력입니다. 숫자를 정확히 입력해주세요.")
        except Exception as e:
            print(f"알 수 없는 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()