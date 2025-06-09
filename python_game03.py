import random

def hangman_game():
    """행맨 게임입니다."""
    words = ["python", "programming", "computer", "keyboard", "hangman", "goodgames"]
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|/  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|/  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|/  |
          / /  |
               |
        --------
        """,
    ]

    print("행맨 게임을 시작합니다!")
    print(hangman_stages[0])
    print(f"맞춰야 할 단어는 {len(secret_word)}글자입니다.")

    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        if "_" not in display_word:
            print(f"🥳 축하합니다! {secret_word}단어를 맞추셨습니다!")
            break

        guess = input("🙂 글자를 추측하세요: ").lower()

        if len(guess) != 1:
            print("🙂 한 글자만 입력해주세요.")
            continue

        if guess in guessed_letters:
            print("🙂 이미 추측한 글자입니다.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            attempts -= 1
            print(hangman_stages[6 - attempts])
            print(f"😭 틀렸습니다! 남은 기회: {attempts}")

            if attempts == 0:
                print(f"   Game Over! 정답은 {secret_word}입니다.")
                break

if __name__ == "__main__":
    hangman_game()
