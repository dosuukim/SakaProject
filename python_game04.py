def quiz_game():
    """간단한 텍스트 기반 퀴즈 게임입니다."""
    questions = [
        {
            "question": "1. 파이썬의 창시자는 누구입니까?",
            "options": ["a) 귀도 반 로섬", "b) 제임스 고슬링", "c) 도널드 크누스"],
            "answer": "a",
        },
        {
            "question": "2. 파이썬의 자료형이 아닌 것은 무엇입니까?",
            "options": ["a) int", "b) float", "c) string", "d) boolean", "e) char"],
            "answer": "e",
        },
        {
            "question": "3. 다음 중 파이썬의 특징이 아닌 것은 무엇입니까?",
            "options": ["a) 인터프리터 언어", "b) 객체 지향 프로그래밍", "c) 정적 타입 언어"],
            "answer": "c",
        },
        {
            "question": "4. 다음 중 파이썬에서 파일에 문자열을 쓰는 명령어는 무었입니까?",
            "options": ["a) f.write", "b) f.readlines", "c) f.read"],
            "answer": "a",
        },
        {
            "question": "5. 다음 중 파이썬에서 print 명령어의 기능은 무었입니까?",
            "options": ["a) 객체의 속성 목록 조회", "b) 값을 출력", "c) 파이썬 나가기"],
            "answer": "b",
        },
    ]

    score = 0

    print("간단한 퀴즈 게임입니다.")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("정답을 선택하세요 (a, b, c 등): ").lower()

        if user_answer == q["answer"]:
            print("🥳 정답입니다!")
            score += 1
        else:
            print("😭 틀렸습니다!")

    print(f"퀴즈가 끝났습니다. 당신의 점수는 {score}/{len(questions)}입니다.")

if __name__ == "__main__":
    quiz_game()