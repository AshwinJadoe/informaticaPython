import time
import random
from locaties import location
 


#print("Welkom bij 'The Road To The Lerarenkamer'! Het is de bedoeling dat je via verschillende locaties in de school de lerarenkamer bereikt. Je begint bij de congiërge, want je bent eens weer te laat gekomen voor het eerste uurtje Assie. Bij elke locatie kan je kiezen tussen 'n', 's', 'w' en 'o' en dan zal je weer bij een nieuwe locatie komen. Ook kan je naar de volgende verdieping via 1 van de trappenhuizen.")

inventory = [" "]
commands_list = ["n", "z", "w", "o", "b", "d"]

current_room = "congiërge"
oude_kamer = "congiërge"

def roomcheck(room):
  return location[room]["obstakel"] == "ja"

def muur(x,room):
  return (location[room]["keuzes"][x]) == "nee"

def commands(input):
  for x in commands_list:
    if x == input:
      return True
    else:
      return False



    


def engine (room):
  global current_room
  if roomcheck(room): 
    global oude_kamer
    print("je mag hier niet heen, draai om")
    engine(oude_kamer)
  else:  
    oude_kamer = room
    print (oude_kamer)
    print (location[room]["tekst"])
    actie = input("en nu? ").lower()
    if commands(actie) == False:
      print ("dit is helaas geen optie")
      engine (room)
    else:
      for x in (location[room]["keuzes"]):
        if actie == x:  
          if muur(x, current_room):
            print("Deze richting kan je niet op")
            engine(current_room)
                    
          else:   
            current_room = location[room]["keuzes"][actie]
            engine(current_room)   

            
engine(current_room)
