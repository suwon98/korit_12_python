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
logo = '''                                                  
  ,---,                                                 ____                          
,--.' |                                               ,'  , `.                        
|  |  :                      ,---,                 ,-+-,.' _ |                 ,---,  
:  :  :                  ,-+-. /  |  ,----._,.  ,-+-. ;   , ||             ,-+-. /  | 
:  |  |,--.  ,--.--.    ,--.'|'   | /   /  ' / ,--.'|'   |  || ,--.--.    ,--.'|'   | 
|  :  '   | /       \  |   |  ,"' ||   :     ||   |  ,', |  |,/       \  |   |  ,"' | 
|  |   /' :.--.  .-. | |   | /  | ||   | .\  .|   | /  | |--'.--.  .-. | |   | /  | | 
'  :  | | | \__\/: . . |   | |  | |.   ; ';  ||   : |  | ,    \__\/: . . |   | |  | | 
|  |  ' | : ," .--.; | |   | |  |/ '   .   . ||   : |  |/     ," .--.; | |   | |  |/  
|  :  :_:,'/  /  ,.  | |   | |--'   `---`-'| ||   | |`-'     /  /  ,.  | |   | |--'   
|  | ,'   ;  :   .'   \|   |/       .'__/\_: ||   ;/        ;  :   .'   \|   |/       
`--''     |  ,     .-./'---'        |   :    :'---'         |  ,     .-./'---'        
           `--`---'                  \   \  /                `--`---'                 
                                      `--`-'                                          
'''
word_list = [
    'apple', 'banana', 'camel', 'dog', 'elephant', 'frog', 'grape', 'horse', 'ice', 'juice',
    'koala', 'lemon', 'melon', 'nurse', 'orange', 'piano', 'queen', 'rabbit', 'snake', 'tiger',
    'umbrella', 'violin', 'whale', 'xylophone', 'yo-yo', 'zebra', 'ant', 'bird', 'cat', 'duck',
    'egg', 'fish', 'goat', 'house', 'ink', 'jam', 'kite', 'leaf', 'moon', 'nest',
    'owl', 'pear', 'quilt', 'rose', 'star', 'tree', 'up', 'vase', 'wind', 'box',
    'airplane', 'anchor', 'arm', 'axe', 'baby', 'ball', 'balloon', 'bat', 'bed', 'bee',
    'bell', 'belt', 'bike', 'boat', 'book', 'boot', 'bottle', 'bowl', 'bread', 'bridge',
    'brush', 'bus', 'butter', 'button', 'cake', 'candle', 'candy', 'car', 'card', 'carrot',
    'castle', 'chair', 'cheese', 'cherry', 'chess', 'chicken', 'cloud', 'coat', 'coin', 'comb',
    'cookie', 'corn', 'cow', 'crab', 'crayon', 'cup', 'desk', 'diamond', 'dice', 'door',
    'dolphin', 'donut', 'door', 'dragon', 'drum', 'eagle', 'ear', 'earth', 'eel', 'elbow',
    'eye', 'face', 'fan', 'feather', 'feet', 'fence', 'fire', 'flag', 'flower', 'flute',
    'fly', 'foot', 'fork', 'fox', 'fruit', 'gate', 'ghost', 'giraffe', 'glass', 'glove',
    'glue', 'gold', 'goose', 'grass', 'guitar', 'gum', 'hair', 'hammer', 'hand', 'hat',
    'heart', 'hippo', 'honey', 'hook', 'horn', 'hose', 'iron', 'island', 'jacket', 'jar',
    'jelly', 'jet', 'jewel', 'key', 'king', 'knee', 'knife', 'ladder', 'ladybug', 'lake',
    'lamp', 'lamp', 'laptop', 'leaf', 'leg', 'letter', 'light', 'lion', 'lips', 'lizard',
    'lock', 'log', 'lunch', 'magnet', 'mail', 'map', 'mask', 'match', 'milk', 'mirror',
    'monkey', 'mountain', 'mouse', 'mouth', 'mushroom', 'music', 'nail', 'neck', 'needle', 'net',
    'night', 'nose', 'note', 'ocean', 'octopus', 'onion', 'ostrich', 'otter', 'oven', 'ox',
    'paint', 'pan', 'pants', 'paper', 'parrot', 'party', 'peach', 'peacock', 'pen', 'pencil',
    'penguin', 'phone', 'pig', 'pillow', 'pilot', 'pine', 'pipe', 'pizza', 'plant', 'plate',
    'pocket', 'pool', 'pot', 'potato', 'pumpkin', 'puppy', 'purse', 'pyramid', 'rain', 'rainbow',
    'rake', 'rat', 'ring', 'river', 'road', 'robot', 'rock', 'rocket', 'rope', 'ruler',
    'sail', 'salt', 'sand', 'sandwich', 'sauce', 'school', 'scissors', 'scorpion', 'seal', 'seed',
    'shark', 'sheep', 'shell', 'ship', 'shirt', 'shoe', 'shrimp', 'sink', 'skate', 'skirt',
    'skull', 'sky', 'slide', 'snail', 'snow', 'soap', 'sock', 'sofa', 'soup', 'spider',
    'spoon', 'sponge', 'spoon', 'squid', 'squirrel', 'stairs', 'stamp', 'stick', 'stone', 'stool',
    'stove', 'straw', 'street', 'sun', 'swan', 'swing', 'table', 'tail', 'tank', 'tea',
    'teeth', 'tent', 'tiger', 'toast', 'toe', 'toilet', 'tomato', 'tongue', 'tool', 'tooth',
    'top', 'torch', 'towel', 'tower', 'town', 'toy', 'train', 'tray', 'truck', 'trumpet',
    'turtle', 'tv', 'ufo', 'unicorn', 'uniform', 'valley', 'van', 'vegetable', 'vest', 'volcano',
    'wagon', 'wall', 'wallet', 'watch', 'water', 'wave', 'web', 'wheel', 'whistle', 'wig',
    'window', 'wing', 'witch', 'wolf', 'woman', 'wood', 'wool', 'worm', 'wrist', 'yacht',
    'yak', 'yard', 'yarn', 'yoke', 'zebra', 'zero', 'zipper', 'zoo', 'actor', 'adult',
    'alarm', 'album', 'alien', 'alley', 'angel', 'animal', 'answer', 'apartment', 'area', 'arena',
    'army', 'art', 'artist', 'ash', 'atlas', 'attic', 'author', 'award', 'badge', 'bagel',
    'bakery', 'bank', 'barber', 'bark', 'barn', 'base', 'basket', 'beak', 'beam', 'bean',
    'beard', 'beast', 'beaver', 'beef', 'beer', 'bench', 'berry', 'bill', 'birth', 'bite',
    'blade', 'blanket', 'blast', 'blaze', 'blimp', 'block', 'blood', 'bloom', 'blouse', 'board'
]
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