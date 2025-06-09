def adventure_game():
    """간단한 텍스트 기반의 길찾기 어드벤처 게임입니다."""
    print("어두운 숲 속에 있습니다.")
    print("당신은 길을 잃었고, 출구를 찾아야 합니다.")

    v_find_cnt = 0 # 찾은 횟수 COUNT : 1이면 한번에 찾은 경우.

    while True:
        # choice = input("어떻게 하시겠습니까? (왼쪽/오른쪽/직진): ")
        choice = input(" ▶ 어떻게 하시겠습니까? (왼쪽(L), 오른쪽(R), 직진(S) 중에서 선택(끝내려면 '종료(E)' 입력): ")
        v_find_cnt += 1

        if choice == "L":
           v_choice = "왼쪽"
        elif choice == "R":
           v_choice = "오른쪽"
        elif choice == "S":
           v_choice = "직진"
        elif choice == "E":
           v_choice = "종료"
        else:
           v_choice = choice

        if v_choice == "종료":
            print("😇 게임을 종료합니다.")
            break

        if v_choice == "왼쪽":
            print("😄 작은 개울을 만났습니다. 건너가시겠습니까? (예(Y), 아니오(N)): ")

            stream_choice = input()

            if stream_choice == "Y":
               v_stream_choice = "예"
            elif stream_choice == "N":
               v_stream_choice = "아니오"
            else:
               v_stream_choice = stream_choice

            if v_stream_choice == "예":
                print("😋 개울을 건너다가 넘어졌습니다. 옷이 젖었지만, 계속 나아갑니다.")
            else:
                print("😋 다른 길을 찾아봅니다.")
        elif v_choice == "오른쪽":
            print("😄 동굴을 발견했습니다. 들어가시겠습니까? (예(Y), 아니오(N)): ")
            cave_choice = input()

            if cave_choice == "Y":
               v_cave_choice = "예"
            elif cave_choice == "N":
               v_cave_choice = "아니오"
            else:
               v_cave_choice = cave_choice

            if v_cave_choice == "예":
                print("😋 동굴 속에서 보물을 발견했습니다! 하지만 출구는 없습니다.")
            else:
                print("😋 다른 길을 찾아봅니다.")
        elif v_choice == "직진":
            if v_find_cnt == 1:
               print("🤩 숲의 출구를 찾았습니다! 마을이 보입니다.")
            else:
               print("🤩 드디어 숲의 출구를 찾았습니다! 마을이 보입니다.")

            print(f"🥳 축하합니다! {v_find_cnt}번만에 탈출 성공했습니다!")   
            break
        else:
            print("😢 유효한 선택을 해주세요.")

if __name__ == "__main__":
    adventure_game()