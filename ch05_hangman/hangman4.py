import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
# print(f'test world : {chosen_word}')

display = []
for _ in range(len(chosen_word)):
    display.append('_')
# todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화하세요.

# todo - 2 : while문의 조건을 수정하여 6 번의 기회가 소진되면 반복문이 종료 될 수 있도록 조건을 작성하시오.
lives = 6
end_of_game = False
while not end_of_game:
    print(f'기회가 {lives}번 남았습니다.')
    guess = input('알파벳을 입력하세요 >>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(' '.join(display))
    #     else :
    #         lives -= 1
    #         print(stages[lives])
    #         print(f'기회가 {lives}번 남았습니다')
    # if lives == 0:
    #     end_of_game = True
    # 라고 작성하면 문자 하나 당 일치 여부를 확인하기 때문에 예상했던 것과 다르게 맞추더라도 나머지 문자에 대해서 lives -= 1이 누적적으로 적용됩니다. 그런데 각 element에 대한 반복 때문에 누적적으로 값이 빠진다면, 반복문 바깥에 따로 작성해주면 되겠네요
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f'기회가 {lives}번 남았습니다.')
# lives == 0 일 때 게임 종료를 표시해주셔야 합니다.
# 정답을 맞췄을 때 정답입니다!! 를 출력해주셔야 합니다
# 맞추거나 틀렸을 경우에 안내를 출력해야 함. _ p p _ _ 와 같은 식으로
    elif lives == 0:
        end_of_game = True
    elif '_' not in display:
        display = ' '.join(display)
        print(f'정답입니다!!! \n{display}')
        end_of_game = True
