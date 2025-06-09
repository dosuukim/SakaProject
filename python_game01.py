import random

def rock_paper_scissors_game():
    """가위바위보 게임입니다."""
    options = ["가위", "바위", "보"]  # 리스트 정의

    while True:
        computer_choice = random.choice(options) # 컴퓨터가 랜덤하게 내는 가위/바위/보
        user_choice = input("가위(1), 바위(2), 보(3) 중에서 하나를 선택하세요 (끝내려면 '종료(0)' 입력): ") # 사용자가 내는 가위/바위/보

        if user_choice == "1":
           v_user_choice = "가위"
        elif user_choice == "2":
           v_user_choice = "바위"
        elif user_choice == "3":
           v_user_choice = "보"
        elif user_choice == "0":
           v_user_choice = "종료"
        else:
           v_user_choice = user_choice

        if v_user_choice == "종료":
            print("😇 게임을 종료합니다.")
            break

        if v_user_choice not in options:
            print("😢 유효한 입력을 해주세요.")
            continue

        print(f"컴퓨터는 {computer_choice}를 냈습니다.")

        if v_user_choice == computer_choice:
            print("😤 무승부입니다!")
        elif (
            (v_user_choice == "가위" and computer_choice == "보")
            or (v_user_choice == "바위" and computer_choice == "가위")
            or (v_user_choice == "보" and computer_choice == "바위")
        ):
            print("😊 사용자 승리!")
        else:
            print("😭 컴퓨터 승리!")

if __name__ == "__main__":
    rock_paper_scissors_game()
