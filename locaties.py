location = {
  "congiërge": {
    "tekst": "We zijn nu bij de congierge",
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
      "w": "nee",
    }
  },
  "kluisjes": {
    "tekst": "Oh hier zijn de kluisjes, goed om te weten",
    "object" : {
      "object_tekst" : "Hey hier dit kluisje staat open, er ligt een rekenmachine in. Die kan vast later van pas komen ;)",
      "object_soort" : "rekenmachine"

    },

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
    "tekst": "Welkom bij Scheikunde, het beste vak op aarde",
    "obstakel" : {
      "obstakel_tekst" : "Stapel: Hé, jij zou verf voor mij meenemen voor het practicum. Je komt dit lokaal niet binnen totdat je verf hebt voor mij!",
      "obstakel_object" : "verf",
      "obstakel_bezit" : "Oh je hebt het al? Mooizo, nu hoef je je niet meer te melden",
      "obstakel_niet" : "Zie ik nou dat je het nog niet heb gehaald? Ik heb je minstens het drie keer gevraagd.\nGa je maar melden!\nEn volgende keer als je komt heb je verf bij je hè"
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
    "tekst": "Ben je eigenlijk een beetje creatief. Dan zit je hier bij meneer Nobrega goed. ",
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
      "b": "trappenhuis1c",
      "w": "aula balustrade",
      "z": "informatica",
      "o": "Wal",
      "d": "trappenhuis1a",
      "n": "nee"
    }
  },
  "aula balustrade": {
    "tekst": "Zo hé, vanaf hier kan je heel de aula zien. Echt te gek!",
    "obstakel" : { 
      "obstakel_tekst" : "Zeg jongeman, er is een viering gaande, alleen de TTC mag hierboven komen op de aula balustrade.",
      "obstakel_object" : "TTC pasje",
      "obstakel_bezit" : "Oh, je hebt een TTC pasje, nou in dat geval mag je hier gewoon komen. Toch kan ik me niet herinneren dat ik jou eerder gezien heb",
      "obstakel_niet" : "Zoals ik al had vermoed heb jij geen TTC pasje en mag jij hier dus nu niet zijn. Ga je maar even melden"
    },
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
    "tekst": "Vlaam: Niet vergeten he, telefoons zijn ten strengste verboden. Als ik er een zie kan je hem om half vijf op komen halen!",
    "obstakel" : {
      "obstakel_tekst" : "Vlaam: Zeg jongeman, waar denk jij heen te gaan...\nDe lerarenkamer is UITERST verboden voor leerlingen!!",
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
    "victory" : "JA",
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
    "tekst": "Neutronen, elektronen, iets met krachten. Dat kan je hier allemaal leren. ",
    "object" : {
      "object_tekst" : "Hey hier ligt een pasje. Er staat TTC op.",
      "object_soort" : "TTC pasje"
    },
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
      "w": "Logtenberg",
      "b": "nee",
      "d": "nee"
    }
  },
  "mediatheek": {
    "tekst": "SSSSSSSSSSSSSTTTTT, stilte in de Mediatheek",
    "object" : {
      "object_tekst" : "IK WIL DAT HET NU STIL IS!,Oh goedendag, wil je een boek lenen. Ik heb hier nog een woordenboek Grieks voor de liefhebber!",
      "object_soort" : "woordenboek"
    },
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
    "tekst": "Dit is AK. Ook al hebben we tegenwoordig Google Maps, is het nog steeds handig om AK te kiezen",
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
    "obstakel" : {
      "obstakel_tekst" : "Welkom bij het beste vak op aarde: Wiskunde. A^2 + b^2 = C^2! Maar dit wist je natuurlijk al lang! Wat veel interessanter is is de binomiale verdeling! Dit kan echt heel gemakkelijk met je GR",
      "obstakel_object" : "rekenmachine",
      "obstakel_niet" : "Wil je me nou vertellen dat je je rekenmachine NIET bij je hebt? Oh hij zat wel in je tas? Ja dat zeggen ze allemaal. Ga je maar even melden\nEn volgende keer niet zo bijdehand hè ",
      "obstakel_bezit" : "En uiteraard heb je er een bij je! Geef maar hier ik laat je wel even zien hoe dat moet!"
    },
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
    "tekst": "Je bent bij Nederlands. Hier kunnen wij jou alles leren over grammatica, spelling en literatuur. Maar eerst een belangrijke vraag: ",
    "spel" : "ja", 
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
    "tekst": "You are now at English .",
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
    "tekst": "Guten Tag! Dit is Duits, een zeer mooie taal.",
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
    "tekst": "Grieks en latijn zijn helemaal geen nutteloze talen, als je er op let zie je dat ze vaak terugkomen in onze huidige leefomgeving. Hier bij Grieks en Latijn leren we je dit soort dingen!",
    "obstakel" : {
      "obstakel_tekst" : "Ah hallo, welkom bij Latijn en Grieks. Je kan niet vertalen zonder woordenboek, ik neem aan dat je er een bij je hebt...",
      "obstakel_object" : "woordenboek",
      "obstakel_bezit" : "Zie je wel, je hebt er gewoon aan gedacht, chapeau",
      "obstakel_niet" : "Erg zonde dit, had dit niet van jou verwacht. Ga je maar even melden bij de congiërge, je vergeet het bijna elke les"
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
    "tekst": "Dit is tekenen, een lokaal vol verf en mooie kunstwerken van bruggers.",
    "object" : {
      "object_tekst" : "Hey, daar ligt een potje verf. Had je die niet ergens voor nodig?" ,
      "object_soort" : "verf"
    },
    "keuzes": {
      "n": "frans",
      "o": "nee",
      "w": "nee",
      "z": "nee",
      "b": "nee",
      "d": "nee"
    }
  },
  "Logtenberg" : {
    "tekst" : "Logtenberg: Hallo, ik ben de informatica docent hiero. Ik zal magister ff hacken en je briefjes kwijtschenden, begin je weer lekker met een schone lei. Fijn toch!",
    "briefjes" : "JA",
     "keuzes": {
      "b": "trappenhuis2b",
      "w": "kluisjes",
       "d": "nee",
       "n": "nee",
       "o": "nee",
       "z": "nee"
      }
}  
}
