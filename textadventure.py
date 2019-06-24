import time
import random
from locaties import location
 


#print("Welkom bij 'The Road To The Lerarenkamer'! Het is de bedoeling dat je via verschillende locaties in de school de lerarenkamer bereikt. Je begint bij de congiërge, want je bent eens weer te laat gekomen voor het eerste uurtje Assie. Bij elke locatie kan je kiezen tussen 'n', 's', 'w' en 'o' en dan zal je weer bij een nieuwe locatie komen. Ook kan je naar de volgende verdieping via 1 van de trappenhuizen.")

inventory = [" "]
commands_list = ["n", "z", "w", "o", "b", "d"]

current_room = "congiërge"
oude_kamer = "congiërge"

def roomcheck(room):
   for x in location[room]:
    if x == "obstakel":
      return True

def muur(x,room):
  return (location[room]["keuzes"][x]) == "nee"

def commands(input):
  for x in commands_list:
    if x == input:
      return True



    


def engine (room):
  global current_room
  if roomcheck(room): 
    global oude_kamer
    print(location[room]["obstakel"]["obstakel_tekst"])
    engine(oude_kamer)
  else:  
    oude_kamer = room
    print (oude_kamer)
    print (location[room]["tekst"])
    actie = input("en nu? ").lower()
    print (commands(actie))
    if commands(actie) == True:
      for x in (location[room]["keuzes"]):
        if actie == x:  
          if muur(x, current_room):
            print("Deze richting kan je niet op")
            engine(current_room)
                    
          else:   
            current_room = location[room]["keuzes"][actie]
            engine(current_room)  
    elif commands(actie) == None:
      print ("dit is helaas geen optie")
      engine (room) 


engine(current_room)
