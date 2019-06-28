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


#Program Functions
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

def play_game(this_word):
   
    word = list(this_word)
    blanks = "_" * len(word)
    blanks = list(blanks)
    guessed = []
    incorrect = 6
    while incorrect > 0:
        print("\n" + gallows[incorrect]
              + "\nJij hebt nog {} kansen over.".format(incorrect)
              + "\nJouw woord: " + "".join(blanks)
              + "\nGeraden letters: " + ", ".join(guessed)
             )
        letter = input("Letter: ").lower()
        if len(letter) == 1 and letter.isalpha():
            if letter in guessed:
                print("\n\nWolla dat heb jij al gezegd!")
                time.sleep(2)

            elif letter in word:
                for index,character in enumerate(word):
                    blanks = list(blanks)
                    if character == letter:
                        blanks[index] = letter
                        current = "".join(blanks)
                        if blanks == word:
                            print("\n\nGEFELICITEERD, JIJ HEBT GEWONNEN!!\nJouw woord was " + ''.join(word) + ".\n")
                           
                            
                          
            elif letter not in word:
                incorrect -= 1
                guessed.append(letter)
        else:
            print("\n\n!Potverjandriedubbeltjes, alleen enkele letters!\n\n")
            time.sleep(2)
    else:
        print(gallows[0])
        print("\nSorry " + player + ", GAME OVER!\nJouw woord was " + ''.join(word) + ".")
        
        

name= input("Hallo, je bent bij Nederlands. Wat is jouw naam: ")
time.sleep(1)
print("Welkom,", name)
time.sleep(1.4)
age= input("En hoe oud ben je eingelijk: ")
print("AAAH WOLLAH ben jij %s. JIJ BENT tering OUD NEEEEFF" % age)
time.sleep(2.3)
x= input("Heb jij zin om een spelletje te spelen, %s: [ja/nee]" %name)
if x == "ja": 
  print("Oké, laten we beginnen met galgje, als je wint krijg je een object voor je inventory!") 
  difficulty = pick_diff()
elif x == "nee": print("Dan heb je pech, want we gaan gewoon lekker een spelletje spelen!") 
else: print("Je kan ja of nee invullen en niks anders.ZO MOEILIJK IS DAT TOCH NIET! Nu mag je niet meer kiezen, we gaan lekker een spelletje spelen. ")
print("Maar let op, als je niet wint, moet je een briefje halen")
