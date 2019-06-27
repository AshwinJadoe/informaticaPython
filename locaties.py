
location = {
  "congiërge": {
    "tekst": "Je bent nu bij de conciërge. Ben je nou alweer te laat gekomen?",
     "obstakel" : "nee",
    "keuzes": {
      "n": "trappenhuis1a",
      "o": "kluisjes",
      "w": "aula",
      "z": "nee"

    }
  },

 "aula": { 
    "tekst": "Je bent nu in de aula, helaas zijn alle tafels bezet.",
    "obstakel" : "nee",
    "keuzes": {
      "z": "scheikunde",
      "w": "kantine",
      "o": "congiërge",
      "n": "gymzaal"
    }
  },
  
  "trappenhuis1a": {
    "tekst": "Je bent nu in het eerste trappenhuis op de begane grond, wil je naar boven?",
    "obstakel" : "nee",
    "keuzes": {
      "b": "trappenhuis1b",
      "z": "congiërge"
    }
  },
  "kluisjes": {
    "tekst": "Moet je boeken of je jas in je kluisje doen? Nou dit is je kans, maar welk kluisje is van jou en wat is de code van je kluisje?",
    "obstakel" : "nee",
    "keuzes": {
      "w": "congiërge",
      "z": "kunst",
      "o": "trappenhuis2a"
    }
  },
  "scheikunde": {
    "tekst": "Dit is nou het scheikundelokaal! PAS OP ONTPLOFFINGSGEVAAR! Ooh daar is Stapel. Stapel: 'Hallo, los deze reactievergelijking eens op'",
    "keuzes": {
      "n": "aula",
      "z": "trappenhuis3a"
    }
  },
  "trappenhuis3a": {
    "tekst": "Wat handig dat hier ook een trappenhuis zit. Wil je naar boven?",
    "keuzes": {
      "n": "scheikunde",
      "b": "trappenhuis3b"
    }
  },
  "kantine": {
    "tekst": "Hier is de kantine, waar je bij de 'gezonde cafetaria' hele lekkere panini's, wafels en kroketten kan halen.",
    "obstakel" : "ja",
    "keuzes": {
      "o": "aula"
    }
  },
  "gymzaal": {
    "tekst": "Lekker even sporten, want je bent nu in de gymzaal",
    "keuzes": {
      "z": "aula"
    }
  },
  "handvaardigheid": {
    "tekst": "Ben je eigenlijk een beetje creatief. Dan heeft Nobrega wel een opdracht voor jou!",
    "keuzes": {
      "n": "kluisjes"
    }
  },
  "trappenhuis2a": {
    "tekst": "Nog een trappenhuis, wil je naar boven?",
    "keuzes": {
      "b": "trappenhuis2b",
      "w": "kluisjes"
    }
  },
  "trappenhuis1b": {
    "tekst": "Je bent nu in het trappenhuis op de eerste verdieping, wil je naar boven of beneden of wil je ergens anders naartoe?",
    "keuzes": {
      "b": "trappenhuis 1c",
      "w": "aula balustrade",
      "z": "informatica",
      "o": "Wal",
      "d": "trappenhuis1a"
    }
  },
  "aula balustrade": {
    "tekst": "Zo hé, vanaf hier kan je heel de aula zien. Echt te gek!",
    "keuzes": {
      "n": "Vlaam",
      "w": "biologie",
      "o": "trappenhuis1b"
    }
  },
  "Vlaam": {
    "tekst": "Oh nee, Oh nee, daar is Vlaam snel ren weg nu het nog kan. Anders moet je misschien nablijven.",
    "keuzes": {
      "n": "lerarenkamer",
      "z": "aula balustrade"
    }
  },
  "lerarenkamer": {
    "tekst": "Ja, ja. Hier is het dan, de lerarenkamer!!!!",
    "keuzes": {
      "z": "Vlaam"
    }
  },
  "biologie": {
    "tekst": "Cellen, koolstofcirculatie en ecosystemen. Dit zijn allemaal hele interessante onderwerpen. Als je biologie kiest mag je over al deze dingen leren, geweldig toch?",
    "keuzes": {
      "z": "natuurkunde",
      "o": "aula balustrade"
    }
  },
  "natuurkunde": {
    "tekst": "Skip die Kechs ik wil Meijer!! PAS OP MISSCHIEN WORD JE GEËLEKTROCUTEERD, DOOR DEZE NATUURKUNDELERAAR!",
    "keuzes": {
      "n": "biologie",
      "z": "trappenhuis3b"
    }
  },
  "trappenhuis3b": {
    "tekst": "Je bent op de eerste verdieping in het trappenhuis, waar wil je naar toe?",
    "keuzes": {
      "n": "natuurkunde",
      "d": "trappenhuis3a"
    }
  },
  "informatica": {
    "tekst": "Het beste vak ooit is hier, namelijk Informatica",
    "keuzes": {
      "n": "trappenhuis1b",
      "z": "mediatheek"
    }
  },
  "mediatheek": {
    "tekst": "SSSSSSSSSSSSSTTTTT, stilte in de Mediatheek",
    "keuzes": {
      "n": "informatica",
    }
  },
  "Wal": {
    "tekst": "Wallieeee, hoe gaat het?",
    "keuzes": {
      "o": "aardrijkskunde",
      "w": "trappenhuis1b"
    }
  },
  "aardrijkskunde": {
    "tekst": "Dit is AK",
    "keuzes": {
      "o": "trappenhuis2b",
      "w": "Wal"
    }
  },
  "trappenhuis2b": {
    "tekst": "Je bent in een trappenhuis op de eerste verdieping.",
    "keuzes": {
      "z": "geschiedenis",
      "w": "aardrijkskunde",
      "b": "trappenhuis2c",
      "d": "trappenhuis2a"
    }
  },
  "geschiedenis": {
    "tekst": "Probeer niet in slaap te vallen. Je bent bij geschiedenis.",
    "keuzes": {
      "n": "trappenhuis2b"
    }
  },
  "trappenhuis1c": {
    "tekst": "Je bent in een trappenhuis op de tweede verdieping.",
    "keuzes": {
      "b": "trappenhuis1d",
      "o": "wiskunde",
      "d": "trappenhuis1b"
    }
  },
  "wiskunde": {
    "tekst": "De oppervlakte van een cirkel is πr^2, wiskunde.",
    "keuzes": {
      "w": "trappenhuis1c",
      "o": "nederlands"
    }
  },
  "nederlands": {
    "tekst": "Wollla doet jij goeder Nederaldns sprieken als ik?",
    "keuzes": {
      "w": "wiskunde",
      "w": "trappenhuis2c"
    }
  },
  "trappenhuis2c": {
    "tekst": "Je bent in een trappenhuis op de tweede verdieping",
    "keuzes": {
      "z": "engels",
      "w": "nederlands",
      "b": "trappenhuis2d",
      "d": "trappenhuis2b"
    }
  },
  "engels": {
    "tekst": "You Spiek verie goet Inglish",
    "keuzes": {
      "n": "trappenhuis2c",
      "w": "collegezaal"
    }
  },
  "collegezaal": {
    "tekst": "Ooh er zijn examens bezig in de collegezaal, snel weg.",
    "keuzes": {
      "o": "engels",
      "w": "Assendorp"
    }
  },
  "Assendorp": {
    "tekst": "AAAAAAAHH, Assendorp, snel rennen!",
    "keuzes": {
      "o": "collegezaal"
    }
  },
  "trappenhuis1d": {
    "tekst": "Je bent in een trappenhuis op de derde verdieping",
    "keuzes": {
      "o": "duits",
      "d": "trappenhuis1c"
    }
  },
  "duits": {
    "tekst": "Guten Tag",
    "keuzes": {
      "o": "klassieke talen",
      "w": "trappenhuis1d"
    }
  },
  "klassieke talen": {
    "tekst": "Zit jij op het gymnasium? Spreek jij toevallig Griek en Latijns? HET ANTWOORD IS NEE, JE LEERT NIET OM TE SPREKEN HET IS EEN DODE TAAL!!!!",
    "keuzes": {
      "o": "trappenhuis2d",
      "w": "duits"
    }
  },
  "trappenhuis2d": {
    "tekst": "Je bent in een trappenhuis op de derde verdieping",
    "keuzes": {
      "z": "frans",
      "w": "klassieke talen",
      "d": "trappenhuis2c"
    }
  },
  "frans": {
    "tekst": "Bonjour, je bent bij Frans",
    "keuzes": {
      "z": "tekenen",
      "n": "trappenhuis2d"
    }
  },
  "tekenen": {
    "tekst": "Je kan dit vergeten, tekenen is toch een nutteloos vak",
    "keuzes": {
      "n": "frans",
      "o": "branduitgang!!!"
    }
  },
}
