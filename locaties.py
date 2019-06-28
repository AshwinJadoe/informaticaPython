location = {
  "congiërge": {
    "tekst": "",
    "keuzes": {
      "n": "trappenhuis1a",
      "o": "kluisjes",
      "w": "aula",
      "z": "nee",
      "b": "nee",
      "d": "nee"
    }
  },

 "aula": { 
    "tekst": "Je bent nu in de aula, helaas zijn alle tafels bezet.",
    "obstakel" : {
      "obstakel_tekst" : "wollah je hebt zaklamp nodig",
      "obstakel_object" : "zaklamp",
      "obstakel_bezit" : "aight je hebt dees gewoon",
      "obstakel_niet" : "nope je hebt m niet je moet terug"
    },
    "object" : {
      "object_tekst" : "er ligt een banaan",
      "object_soort" : "banaan"
    },
    "keuzes": {
      "z": "scheikunde",
      "w": "kantine",
      "o": "congiërge",
      "n": "gymzaal",
      "b": "nee",
      "d": "nee",
      
    }
  },
  
  "trappenhuis1a": {
    "tekst": "Je bent nu in het eerste trappenhuis op de begane grond, wil je naar boven?",
    "keuzes": {
      "b": "trappenhuis1b",
      "z": "congiërge",
      "n": "nee",
      "o": "nee",
      "z": "nee",
      "w": "nee",
    }
  },
  "kluisjes": {
    "tekst": "Moet je boeken of je jas in je kluisje doen? Nou dit is je kans, maar welk kluisje is van jou en wat is de code van je kluisje?",

    "keuzes": {
      "w": "congiërge",
      "z": "kunst",
      "o": "trappenhuis2a",
      "n": "nee",
      "b": "nee",
      "d": "nee"
      
    }
  },
  "scheikunde": {
    "tekst": "Dit is nou het scheikundelokaal! PAS OP ONTPLOFFINGSGEVAAR! Ooh daar is Stapel. Stapel: 'Hallo, los deze reactievergelijking eens op'",
    "obstakel" : {
      "obstakel_tekst" : "Hé, jij zou verf voor mij meenemen voor het practicum. Je komt dit lokaal niet binnen totdat je verf hebt voor mij!",
      "obstakel_object" : "verf",
      "obstakel_bezit" : "Gelukkig heb je deze al en hoef je niet helemaal terug",
      "obstakel_niet" : "Je moet de verf halen, want je hebt het nog niet in je inventory staan"
    },
    "keuzes": {
      "n": "aula",
      "z": "trappenhuis3a",
      "o": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
      
    }
  },
  "trappenhuis3a": {
    "tekst": "Wat handig dat hier ook een trappenhuis zit. Wil je naar boven?",
    "keuzes": {
      "n": "scheikunde",
      "b": "trappenhuis3b",
      "o": "nee",
      "z": "nee",
      "w": "nee",
      "d": "nee"
    }
  },
  "kantine": {
    "tekst": "Hier is de kantine, waar je bij de 'gezonde cafetaria' hele lekkere panini's, wafels en kroketten kan halen.",
    "keuzes": {
      "o": "aula",
      "n": "nee",
      "w": "nee",
      "z": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "gymzaal": {
    "tekst": "Lekker even sporten, want je bent nu in de gymzaal",
    "keuzes": {
      "z": "aula",
      "o": "nee",
      "n": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "handvaardigheid": {
    "tekst": "Ben je eigenlijk een beetje creatief. Dan heeft Nobrega wel een opdracht voor jou!",
    "keuzes": {
      "n": "kluisjes",
      "o": "nee",
      "z": "nee",
      "w": "nee",
      "d": "nee",
      "b": "nee"
    }
  },
  "trappenhuis2a": {
    "tekst": "Nog een trappenhuis, wil je naar boven?",
    "keuzes": {
      "b": "trappenhuis2b",
      "w": "kluisjes",
      "d": "nee",
      "n": "nee",
      "o": "nee",
      "z": "nee"
    }
  },
  "trappenhuis1b": {
    "tekst": "Je bent nu in het trappenhuis op de eerste verdieping, wil je naar boven of beneden of wil je ergens anders naartoe?",
    "keuzes": {
      "b": "trappenhuis 1c",
      "w": "aula balustrade",
      "z": "informatica",
      "o": "Wal",
      "d": "trappenhuis1a",
      "n": "nee"
    }
  },
  "aula balustrade": {
    "tekst": "Zo hé, vanaf hier kan je heel de aula zien. Echt te gek!",
    "keuzes": {
      "n": "Vlaam",
      "w": "biologie",
      "o": "trappenhuis1b",
      "z": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "Vlaam": {
    "tekst": "Oh nee, Oh nee, daar is mevrouw Vlaam snel ren weg nu het nog kan. Anders moet je misschien nablijven.",
    "obstakel" : {
      "obstakel_tekst" : "Zeg jongeman, waar denk jij heen te gaan...\nDe lerarenkamer is UITERST verboden voor leerlingen!!",
      "obstakel_object" : "betoog",
      "obstakel_bezit" : "Oh ik zie dat je een betoog  hebt \nDie wil je zeker even in een postvakje van je docent leggen..\nIn dat geval loop maar even door.",
      "obstakel_niet" : "IEDERE LEERLING WEET DAT JE HIER NIET MAG KOMEN \nMELDEN\nNU!!!!"
    },
    "keuzes": {
      "n": "lerarenkamer",
      "z": "aula balustrade",
      "o": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "lerarenkamer": {
    "keuzes": {
      "z": "Vlaam",
      "o": "nee",
      "n": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "biologie": {
    "tekst": "Cellen, koolstofcirculatie en ecosystemen. Dit zijn allemaal hele interessante onderwerpen. Als je biologie kiest mag je over al deze dingen leren, geweldig toch?",
    "keuzes": {
      "z": "natuurkunde",
      "o": "aula balustrade",
      "n": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "natuurkunde": {
    "tekst": "Skip die Kechs ik wil Meijer!! PAS OP MISSCHIEN WORD JE GEËLEKTROCUTEERD, DOOR DEZE NATUURKUNDELERAAR!",
    "keuzes": {
      "n": "biologie",
      "z": "trappenhuis3b",
      "o": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "trappenhuis3b": {
    "tekst": "Je bent op de eerste verdieping in het trappenhuis, waar wil je naar toe?",
    "keuzes": {
      "n": "natuurkunde",
      "d": "trappenhuis3a",
      "o": "nee",
      "z": "nee",
      "w": "nee",
      "b": "nee"
    }
  },
  "informatica": {
    "tekst": "Het beste vak ooit is hier, namelijk Informatica",
    "keuzes": {
      "n": "trappenhuis1b",
      "z": "mediatheek",
      "o": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "mediatheek": {
    "tekst": "SSSSSSSSSSSSSTTTTT, stilte in de Mediatheek",
    "keuzes": {
      "n": "informatica",
      "o": "nee",
      "w": "nee",
      "z": "nee",
      "b": "nee",
      "d": "nee"

    }
  },
  "Wal": {
    "tekst": "Wallieeee, hoe gaat het?",
    "keuzes": {
      "o": "aardrijkskunde",
      "w": "trappenhuis1b",
      "n": "nee",
      "z": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "aardrijkskunde": {
    "tekst": "Dit is AK",
    "keuzes": {
      "o": "trappenhuis2b",
      "w": "Wal",
      "n": "nee",
      "z": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "trappenhuis2b": {
    "tekst": "Je bent in een trappenhuis op de eerste verdieping.",
    "keuzes": {
      "z": "geschiedenis",
      "w": "aardrijkskunde",
      "b": "trappenhuis2c",
      "d": "trappenhuis2a",
      "n": "nee",
      "o": "nee",
    }
  },
  "geschiedenis": {
    "tekst": "Probeer niet in slaap te vallen. Je bent bij geschiedenis.",
    "keuzes": {
      "n": "trappenhuis2b",
      "o": "nee",
      "z": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "trappenhuis1c": {
    "tekst": "Je bent in een trappenhuis op de tweede verdieping.",
    "keuzes": {
      "b": "trappenhuis1d",
      "n": "nee",
      "o": "wiskunde",
      "z": "nee",
      "w": "nee",
      "d": "trappenhuis1b"
    }
  },
  "wiskunde": {
    "tekst": "De oppervlakte van een cirkel is πr^2, wiskunde.",
    "keuzes": {
      "w": "trappenhuis1c",
      "o": "nederlands",
      "n": "nee",
      "z": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "nederlands": {
    "tekst": "Wollla doet jij goeder Nederaldns sprieken als ik?",
    "keuzes": {
      "w": "wiskunde",
      "o": "trappenhuis2c",
      "n": "nee",
      "z": "nee",
      "b": "nee",
      "d": "nee"
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
      "w": "collegezaal",
      "o": "nee",
      "z": "nee",
      "b": "nee",
      "d": "nee",
    }
  },
  "collegezaal": {
    "tekst": "Ooh er zijn examens bezig in de collegezaal, snel weg.",
    "keuzes": {
      "o": "engels",
      "w": "Assendorp",
      "z": "nee",
      "n": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "Assendorp": {
    "tekst": "AAAAAAAHH, Assendorp, snel rennen!",
    "keuzes": {
      "o": "collegezaal",
      "n": "nee",
      "z": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "trappenhuis1d": {
    "tekst": "Je bent in een trappenhuis op de derde verdieping",
    "keuzes": {
      "o": "duits",
      "d": "trappenhuis1c",
      "n": "nee",
      "z": "nee",
      "w": "nee",
      "b": "nee"
    }
  },
  "duits": {
    "tekst": "Guten Tag",
    "keuzes": {
      "o": "klassieke talen",
      "n": "nee",
      "z": "nee",
      "w": "trappenhuis1d",
      "b": "nee",
      "d": "nee"
    }
  },
  "klassieke talen": {
    "tekst": "Zit jij op het gymnasium? Spreek jij toevallig Griek en Latijns? HET ANTWOORD IS NEE, JE LEERT NIET OM TE SPREKEN HET IS EEN DODE TAAL!!!!",
    "obstakel" : {
      "obstakel_tekst" : "Je kan je huiswerk niet maken zonder een woordenboek. Ga maar even een woordenboek halen",
      "obstakel_object" : "woordenboek",
      "obstakel_bezit" : "aight je hebt dees gewoon",
      "obstakel_niet" : "nope je hebt m niet je moet terug"
    },
    "keuzes": {
      "o": "trappenhuis2d",
      "w": "duits",
      "n": "nee",
      "z": "nee",
      "d": "nee",
      "b": "nee",
      "n": "nee"
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
      "n": "trappenhuis2d",
      "o": "nee",
      "w": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "tekenen": {
    "tekst": "Je kan dit vergeten, tekenen is toch een nutteloos vak",
    "keuzes": {
      "n": "frans",
      "o": "nee",
      "w": "nee",
      "z": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
}
