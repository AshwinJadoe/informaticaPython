import time 
import random 

""""print("Welkom bij 'The Road To The Lerarenkamer'! Het is de bedoeling dat je via verschillende locaties in de school de lerarenkamer bereikt. Je begint bij de congiërge, want je bent eens weer te laat gekomen voor het eerste uurtje Assie. Bij elke locatie kan je kiezen tussen 'n', 's', 'w' en 'o' en dan zal je weer bij een nieuwe locatie komen. Ook kan je naar de volgende verdieping via 1 van de trappenhuizen.")


location = {
  "congiërge" : {
    "tekst": "Hallo allemaal.",
    "keuzes": {
      "n" : "trappenhuis1a", 
      "o" : "kluisjes",
      "w" : "aula"
  }
  },
  "aula" : { 
    "tekst": "Je bent nu in de aula, helaas zijn alle tafels bezet.", 
    "keuzes": { 
      "s" : "scheikunde", 
      "w" : "kantine", 
      "o" : "congiërge",
      "n" : "gymzaal"
    } 
  },
  "trappenhuis1a" : { 
    "tekst": "Je bent nu in het eerste trappenhuis op de begane grond, wil je naar boven?", 
    "keuzes": { 
      "b" : "trappenhuis1b", 
      "s" : "congiërge"
    }
  }, 
}"""



current_room = "congiërge"


def engine (room):
  print (location[room]["tekst"])
  actie = input("en nu? ").lower()
  for x in (location[room]["keuzes"]):
    if actie == x:
      current_room = location[room]["keuzes"][actie]
      engine(current_room)   

engine(current_room)







