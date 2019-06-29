import time
import random
from locaties import location
instructies = "Bewegen door het gebouw doe je met \"n\", \"o\", \"z\", of \"w\" \nAls je bij een trappenhuis aankomt kan je met \"b\" naar boven of met \"d\" naar beneden \nVerder kan je iets(als je iets tegenkomt) in je rugzak doen met \"g\" \nDe inhoud van je rugtas bekijk je met \"i\" \nAls je het spel wilt verlaten toets je \"q\" in \nEn tenslotte, als je de instructies nog een keer wilt horen druk op \"h\" " 

def begin():
  print ("Congiërge: Goedendag, ik ben Yousef de congiërge hier op het St-Maartenscollege.")
  time.sleep(1)
  naam = input("En jij bent?  ")
  time.sleep(1.5)
  print ("Hartelijk welkom %s, welkom op het Sint-Maartenscollege " % naam)
  time.sleep(1)
  print ("Ik zal je even snel uitleggen hoe het hier op school werkt! ")
  time.sleep(1)
  print (instructies)
  time.sleep(1)
  print ("Oh en nog 1 laatste regel: \nDe lerarenkamer is voor leerlingen STRICT verboden en zal met een schorsing bestraft worden!")
  time.sleep(1)
  print ("Ik ga dr gauw weer vandoor, want ik hoor al weer een paar relschoppende bruggers. \nLater", naam)
  time.sleep(1)
  print (".\n.\n.\n.")
  time.sleep(1)
  print ("Hey!\n{0} heette je toch?\nNou beste {1} je moet iets voor me doen! \nWij van het leerlingenverzet zijn jaren geleden geschorst van deze school \nAlleen moet ik iets hier iets afleveren\nZou jij dat voor mij willen doen alsjeblief? \nJe hoeft alleen maar deze brief af te leveren in de lerarenkamer, in het postvakje van meneer Logtenberg om precies te zijn \nIk stop m alvast in je tas \nHeel erg bedankt goos! \nSucces!!!".format(naam, naam))


def spel(room):
  animatie = ["_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
        "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
        "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
        "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
        "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
        "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
        "_______\n|     |\n|\n|\n|\n|\n|\n=======",
        ]

  vier_letters = ['boom', 'deel', 'ding', 'ring', 'snel', 'ruim', 'duim', 'geel', 'eend']

  tien_letters = ['afbakbrood', 'agorafobie', 'autodeuren', 'barricades', 'paaseieren', 'xylofonist']

  vijfentwintig_letters = ['arbeidsongeschiktheidswet', 'teambuildingsactiviteiten', 'uraniumverrijkingsfabriek', 'vierentwintiguurseconomie', 'aaaaaaaaaaaaaaaaaaaaaaaaa']

  vijfendertig_letters= [
  'hippopotomonstrosesquippedaliofobie', 'landbouwmechanisatietentoonstelling', 'hottentottententententoonstellingen', 'ultravioletstralingsabsorptiefilter'
  ]


  def pick_diff():
      
      keuze_moeilijkheid = "Kies een moeilijkheidsgraad!. (Makkelijk, Medium, Moeilijk, Extreem)\n>"
      choice = ""
      while choice not in ['makkelijk', 'medium', 'moeilijk', 'extreem']:
          choice = input(keuze_moeilijkheid)
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
          woord = random.choice(vier_letters)
      elif choice == 'medium':
          woord = random.choice(tien_letters)
      elif choice == 'moeilijk':
          woord = random.choice(vijfentwintig_letters)
      elif choice == 'extreem':
          woord = random.choice(vijfendertig_letters)
      play_game(woord)

  def play_game(this_word):
      woord = list(this_word)
      blanks = "_" * len(woord)
      blanks = list(blanks)
      guessed = []
      incorrect = 6
      while incorrect > 0:
          print("\n" + animatie[incorrect]
                + "\nJij hebt nog {} kansen over.".format(incorrect)
                + "\nJouw woord: " + "".join(blanks)
                + "\nGeraden letters: " + ", ".join(guessed)
              )
          letter = input("Letter: ").lower()
          if len(letter) == 1 and letter.isalpha():
              if letter in guessed:
                  print("\n\nWolla dat heb jij al gezegd!")
                  time.sleep(2)

              elif letter in woord:
                  for index,character in enumerate(woord):
                      blanks = list(blanks)
                      if character == letter:
                          blanks[index] = letter
                          current = "".join(blanks)
                          if blanks == woord:
                              print("\n\nGEFELICITEERD, JIJ HEBT GEWONNEN!!\nJouw woord was " + ''.join(woord) + ".\n")
                              del location["nederlands"]["spel"]
                              print ("hier heb je een betoog, zou je deze bij de lerarenkamer willen inleveren")
                              inventory.append("betoog")
                              engine("nederlands")


                            
              elif letter not in woord:
                  incorrect -= 1
                  guessed.append(letter)
          else:
              print("\n\n!Potverjandriedubbeltjes, alleen enkele letters!\n\n")
              time.sleep(2)
      else:
          print(animatie[0])
          print("\nSorry , GAME OVER!\nJouw woord was " + ''.join(woord) + ".")
          briefjehalen(levens, room)          

  x= input("Heb je zin om een spelletje te spelen? \nje kan een prijs winnen die je later misschien nog nodig hebt *knipoog*\nMaar let op, als je niet wint, moet je een briefje halen. ")
  if x == "ja": 
    print("Oké, laten we beginnen met galgje, als je wint krijg je een object voor je inventory!") 
    pick_diff()
  elif x == "nee": 
    print("Dan heb je pech, want we gaan gewoon lekker een spelletje spelen!") 
    pick_diff()
  else:
    print("Je kan ja of nee invullen en niks anders.ZO MOEILIJK IS DAT TOCH NIET! Nu mag je niet meer kiezen, we gaan lekker een spelletje spelen. ")
    pick_diff



inventory = []
commands_list = ["n", "z", "w", "o", "b", "d", "i", "q", "h"]

current_room = "congiërge"
begin_kamer = "congiërge"
levens = 0


def roomcheck(room):
  global levens
  print (location[room]["obstakel"]["obstakel_tekst"])
  if location[room]["obstakel"]["obstakel_object"] in inventory:
    print (location[room]["obstakel"]["obstakel_bezit"])
    del location[room]["obstakel"]
    engine(room)
  else:
    levens += 1
    print (location[room]["obstakel"]
    ["obstakel_niet"])
    briefjehalen (levens,room)

      


def muur(x,room):
  return (location[room]["keuzes"][x]) == "nee"

def commands(room,input):
  if input == "g":
    if "object" in location[room]:
      oppakken(room)
      return True

    else: 
      print ("dit is helaas op het moment geen mogelijkheid")
      engine(room)
      return False
  else:
    for x in commands_list:
      
      if x == input:
        return True

def oppakken(room):
    inventory.append(location[room]["object"]["object_soort"])
    del location[room]["object"]

def object_check(room):
  return "object" in location[room]

def andere_commands (input):
  if input == "i":
    print("Je rugzak bevat hetvolgende: " +', '.join(inventory))
    return True
  elif input == "q":
    quit()
    return True
  elif input == "h":
    print ("Youseff: Hallo daar ben ik weer, ik zal je de instructies nog een keer uitleggen!\n" + instructies)
    return True
  else:
    return False
  

def victory():
  print("Je bent aangekomen bij de befaamde lerarenkamer, een plek waar alleen de elite mag komen!")
  nombre = ("Elsakkers: Goedendag, Ik ben de rector van het St-Maartenscollege. En wie ben jij? ") 
  print("Oh jij bent {0}, ik heb goede dingen over jou gehoord!\nKan ik iets voor je doen? \nHet vakje van meneer Logtenberg zei je? \nUiteraard, komt voor de bakker!".format(nombre))
  print("")
  time.sleep(2)
  print("*biep biep biep*\nJa hallo met het leerlingenverzet, ik bel je om te vragen of de opdracht voltooid is. \nJa?\nBedankt gozer, je staat bij me in het krijt.\nFijne avond nog, ik hoop je nog eens te spreken")
  quit()

def briefjehalen(levens, room):
  print("\nYousef: Tjongejonge ben je daar nu al weer?\nHier heb je nog een briefje, dat wordt morgen 8uur melden\nJe hebt nu %s briefje(s), bij 10 word je geschorst! onthoud dat goed!" % levens)  
  engine("congiërge")


def engine (room):
  global levens
  while levens < 10:
    print ("")
    global current_room
    if "obstakel" in location[room]: 
        roomcheck(room)   
    elif "victory" in location[room]:
      print ("gelukt")
      victory()
    elif "briefjes" in location[room]:
      print (location[room]["tekst"])
      levens = 0
      engine("informatica")
    elif "spel" in location[room]:
      spel(room)
    else:  
      if object_check(room):
        print (location[room]["tekst"])
        print (location[room]["object"]["object_tekst"])
      else:
        print (location[room]["tekst"])
      actie = input("en nu? ").lower()
      if commands(room,actie) == True:
        if andere_commands(actie) == True:
          engine(room)
     
        elif andere_commands(actie) == False:
          for x in (location[room]["keuzes"]):
            if actie == x:  
              if muur(x, room):
                print("Deze richting kan je niet op, je keert terug naar waar je was")
                engine(room)
            
              else:   
                current_room = location[room]["keuzes"][actie]
                engine(current_room)  
      elif commands(room,actie) == None:
        print ("dit is helaas geen optie")
        engine (room) 

  else:
    print ("game over")
    quit()
  



  

begin()
engine(begin_kamer)
