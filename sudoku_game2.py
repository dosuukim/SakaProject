import random
import copy

# 스도쿠 유효성 검사
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    sr, sc = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[sr + i][sc + j] == num:
                return False
    return True

# 스도쿠 풀기 (백트래킹 알고리즘)
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# 완성된 스도쿠 보드 생성
def generate_board():
    board = [[0] * 9 for _ in range(9)]
    solve(board)
    return board

# 숫자 일부 제거하여 퍼즐 생성
def remove_numbers(board, num_to_remove=40):
    puzzle = copy.deepcopy(board)
    removed = 0
    while removed < num_to_remove:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            removed += 1
    return puzzle

# 보드 출력
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

# 메인 게임 로직
def play_game():
    solution = generate_board()
    puzzle = remove_numbers(solution, 40)

    print("🎮 스도쿠 퍼즐 시작!")
    print_board(puzzle)

    while True:
        user_input = input("입력 (행,열,값) 또는 '종료': ")
        if user_input.lower() in ['종료', 'exit', 'quit']:
            print("게임을 종료합니다.")
            break
        try:
            row, col, val = map(int, user_input.split(','))
            if 0 <= row <= 8 and 0 <= col <= 8 and 1 <= val <= 9:
                if puzzle[row][col] == 0:
                    if is_valid(puzzle, row, col, val):
                        puzzle[row][col] = val
                        print_board(puzzle)
                        if puzzle == solution:
                            print("🎉 축하합니다! 스도쿠를 완성했습니다.")
                            break
                    else:
                        print("❌ 유효하지 않은 숫자입니다.")
                else:
                    print("⚠️ 이미 값이 있는 칸입니다.")
            else:
                print("❗ 범위는 행:0-8, 열:0-8, 값:1-9 입니다.")
        except Exception:
            print("⚠️ 형식이 잘못되었습니다. 예: 1,3,5")

# 실행
if __name__ == "__main__":
    play_game()
