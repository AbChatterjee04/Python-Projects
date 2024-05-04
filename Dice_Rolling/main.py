import random


def roll_dice():
    DICE_ART = {

    1: (

        "┌─────────┐",

        "│         │",

        "│    ●    │",

        "│         │",

        "└─────────┘",

    ),

    2: (

        "┌─────────┐",

        "│  ●      │",

        "│         │",

        "│      ●  │",

        "└─────────┘",

    ),

    3: (

        "┌─────────┐",

        "│  ●      │",

        "│    ●    │",

        "│      ●  │",

        "└─────────┘",

    ),

    4: (

        "┌─────────┐",

        "│  ●   ●  │",

        "│         │",

        "│  ●   ●  │",

        "└─────────┘",

    ),

    5: (

        "┌─────────┐",

        "│  ●   ●  │",

        "│    ●    │",

        "│  ●   ●  │",

        "└─────────┘",

    ),

    6: (

        "┌─────────┐",

        "│  ●   ●  │",

        "│  ●   ●  │",

        "│  ●   ●  │",

        "└─────────┘",

    ),

}

    # DIE_HEIGHT = len(DICE_ART[1])

    # DIE_WIDTH = len(DICE_ART[1][0])

    # DIE_FACE_SEPARATOR = " "

    roll = input('Roll the dice? (Yes/No): ')

    while roll.lower() == 'Yes'.lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print('Dice rolled: {} and {}'.format(dice1,dice2))
        
        print('\n'.join(DICE_ART[dice1]))
        print('\n'.join(DICE_ART[dice2]))

        roll = input('Roll again ? (Yes/No): ')



roll_dice()