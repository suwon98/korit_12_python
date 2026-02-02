# play_hangman이라는 함수를 call1() 유형으로 정의하고 호출
import random
import hangman_arts
import hangman_word_list

def play_hangman():
    import random
    from hangman_arts import logo, stages
    from hangman_word_list import word_list
    chosen_word = random.choice(word_list)
    display = []

    for _ in range(len(chosen_word)):
        display.append('_')

    lives = 6
    end_of_game = False
    print(logo)
    while not end_of_game:
        print(stages[lives])
        print(' '.join(display))
        print(f'기회가 {lives}번 남았습니다.')
        guess = input('알파벳을 입력하세요 >>> ').lower()
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            if lives == 0:
                print(f'모든 기회를 잃었습니다')
                end_of_game = True
                print(f'정답은 {chosen_word}입니다.')
        if '_' not in display:
            print(f'정답입니다!!! ')
            end_of_game = True