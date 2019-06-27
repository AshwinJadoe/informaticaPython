import time
import random
from locaties import location
instructies = "Bewegen door het gebouw doe je met \"n\", \"o\", \"z\", of \"w\" \nAls je bij een trappenhuis aankomt kan je met \"b\" naar boven of met \"d\" naar beneden \nVerder kan je iets(als je iets tegenkomt) in je rugzak doen met \"g\" \nDe inhoud van je rugtas bekijk je met \"i\" \nAls je het spel wilt verlaten toets je \"q\" in \nEn tenslotte, als je de instructies nog een keer wilt horen druk op \"h\" " 

def begin():
  print ("Congiërge: Goedendag, ik ben Youseff de congiërge hier op het St-Maartenscollege.")
  naam = input("En jij bent?  ")
  print ("Hartelijk welkom %s, welkom op het Sint-Maartenscollege " % naam)
  print ("Ik zal je even snel uitleggen hoe het hier op school werkt! ")
  print (instructies)
  print ("Oh en nog 1 laatste regel: \nDe lerarenkamer is voor leerlingen STRICT verboden en zal met een schorsing bestraft worden!")
  print ("Ik ga dr gauw weer vandoor, want ik hoor al weer een paar relschoppende bruggers. \nLater", naam)
  print (".\n.\n.\n.")
  print ("Hey!\n{0} heette je toch?\nNou beste {1} je moet iets voor me doen! \nZou jij deze brief af voor mij af willen leveren in de lerarenkamer? \nIk stop m alvast in je tas \nHeel erg bedankt goos! \nSucces!!!".format(naam, naam))


begin()
inventory = ["check", "zaklamp"]
commands_list = ["n", "z", "w", "o", "b", "d", "i", "q", "h"]

current_room = "congiërge"
begin_kamer = "congiërge"
levens = 2


def roomcheck(room):
  global levens
  if "obstakel" in location[room]:
      print (location[room]["obstakel"]["obstakel_tekst"])
      if location[room]["obstakel"]["obstakel_object"] in inventory:
        print (location[room]["obstakel"]["obstakel_bezit"])
        return False
      else:
        levens -= 1
        print (location[room]["obstakel"]["obstakel_niet"])
        engine (begin_kamer)
          
  else:
      return False


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
    print(', '.join(inventory))
    return True
  elif input == "q":
    quit()
    return True
  elif input == "h":
    print ("Youseff: Hallo daar ben ik weer, ik zal je de instructies nog een keer uitleggen!\n" + instructies)
    return True
  else:
    return False
  



    


def engine (room):
  while levens > 0:
    print ("")
    print (room)
    global current_room
    if roomcheck(room): 
        engine (begin_kamer)
      
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
              if muur(x, current_room):
                print("Deze richting kan je niet op")
                engine(current_room)
            
              else:   
                current_room = location[room]["keuzes"][actie]
                engine(current_room)  
      elif commands(room,actie) == None:
        print ("dit is helaas geen optie")
        engine (room) 

  else:
    print ("game over")
    quit()
  


engine(current_room)
