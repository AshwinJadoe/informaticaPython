import time
import random
import sys

#Gallow printouts
gallows = ["_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
       "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
       "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
       "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
       "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
       "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
       "_______\n|     |\n|\n|\n|\n|\n|\n=======",
      ]

# Lists containing the words for the game
four_letters = ['boom', 'deel', 'ding', 'ring', 'snel', 'ruim', 'duim', 'geel', 'eend']

ten_letters = ['afbakbrood', 'agorafobie', 'autodeuren', 'barricades', 'paaseieren', 'xylofonist']

twenty_five_letters = ['arbeidsongeschiktheidswet', 'teambuildingsactiviteiten', 'uraniumverrijkingsfabriek', 'vierentwintiguurseconomie', 'aaaaaaaaaaaaaaaaaaaaaaaaa']

thirty_five_letters= [
 'hippopotomonstrosesquippedaliofobie', 'landbouwmechanisatietentoonstelling', 'hottentottententententoonstellingen', 'ultravioletstralingsabsorptiefilter'
]

def pick_diff():
    
    prompt = "Kies een moeilijkheidsgraad!. (Makkelijk, Medium, Moeilijk, Extreem)\n>"
    choice = ""
    while choice not in ['makkelijk', 'medium', 'moeilijk', 'extreem']:
        choice = input(prompt)
        choice = choice.lower()
    change_diff(choice)

def change_diff(level):
    
    message = "\nJij hebt deze moeilijkheidsgraad gekozen: " + level + ". Wil je het veranderen? [J/N]\n>"
    answer = ""
    while answer not in ['j', 'n']:
        answer = input(message)
        answer = answer.lower()
    if answer == 'j':
        pick_diff()
    if answer == 'n':
        print("\nSucces!\n")
        choose_word(level)

def choose_word(choice):
    
    if choice == 'makkelijk':
        word = random.choice(four_letters)
    elif choice == 'medium':
        word = random.choice(ten_letters)
    elif choice == 'moeilijk':
        word = random.choice(twenty_five_letters)
    elif choice == 'extreem':
        word = random.choice(thirty_five_letters)
    play_game(word)
