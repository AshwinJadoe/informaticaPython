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
      "z" : "congiërge"
    }
  }, 
  "kluisjes" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "w" : "congiërge", 
      "z" : "kunst", 
      "o" : "trappenhuis2a"
    }
  }, 
  "scheikunde" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "aula", 
      "z" : "trappenhuis3a"
    }
  },
   "trappenhuis3a" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "scheikunde", 
      "b" : "trappenhuis3b"
    }
  },
   "kantine" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "o" : "aula"
    }
  },
   "gymzaal" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "z" : "aula"
    }
  },
   "handvaardigheid" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "kluisjes" 
    }
  },
   "trappenhuis2a" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "b" : "trappenhuis2b",
      "w" : "kluisjes"
    }
  },
   "trappenhuis1b" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "b" : "trappenhuis 1c" ,
      "w" : "aula balustrade", 
      "z" : "informatica", 
      "o" : "Wal", 
      "d" : "trappenhuis1a"
    }
  },
   "aula balustrade" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "Vlaam",
      "w" : "biologie", 
      "o" : "trappenhuis1b"
    }
  },
     "Vlaam" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "lerarenkamer", 
      "z" : "aula balustrade"
    }
  },
     "lerarenkamer" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "z" : "Vlaam" 
    }
  },
     "biologie" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "z" : "natuurkunde",  
      "o" : "aula balustrade"
    }
  },
     "natuurkunde" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "biologie", 
      "z" : "trappenhuis3b"
    }
  },
       "trappenhuis3b" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "natuurkunde", 
      "b" : "trappenhuis3c",
      "d" : "trappenhuis3a"
   }
  },
        "informatica" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "trappenhuis1b", 
      "z" : "mediatheek"
   }
  },
        "mediatheek" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "informatica", 
   }
  },
        "Wal" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "o" : "aardrijkskunde",
      "w" : "trappenhuis1b"
   }
  },
        "aardrijkskunde" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "o" : "trappenhuis2b",
      "w" : "Wal"
   }
  },
         "trappenhuis2b" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "z" : "geschiedenis",
      "w" : "aardrijkskunde",
      "b" : "trappenhuis2c",
      "d" : "trappenhuis2a"
   }
  },
         "geschiedenis" : { 
    "tekst": "tekst", 
    "keuzes": { 
      "n" : "trappenhuis2b"
   }
  },
}

