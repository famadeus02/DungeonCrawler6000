from time import sleep
import elements.gamelib as g
import elements.sprite as s
import random


# Dette er et tekst basert spill, hvor du har rom du navigerer deg igjennom. Du bruker "North", "South", "East", og "West" for å navigere deg.
# Målet er å få alle 5 coins. Det er ingen måte å tape, og er mest for å ha det morsomt. Derfor er hvert rom satt opp med sin egen musikk
# For å se kart over spille, kan du gå inn i mappen sketch, og se på bilde filen 'base'
# Viktig! ikke forandre på filstrukturen

# Lagrer info om spiller
player = {
    "current": "C",
    "objects": 0
}

# Definerer hva ja og nei kan være
y = "yes", "ye", "yeah", "y", "Yes"
n = "no", "n", "No"




# Definerer indivudielle rom, innhold, hva som skrives når du først går inn, og om du har vært der før eller ikke. Alle rom har de samme attributes
rooms = {
    "C": {
        "name": "Central",  # Fullt navn som skal skrives ut
        "key": "C",  # Indeks key til rommet
        "main": "music/starmaze.wav",  # Musikk som hører til rommet
        "objects": 1,  # Hvor mange coins det er i rommet
        "been": False,  # Om du har vært i rommet fra før av. Byttes til 'True' første gang du har vært der.

        # Under er rommene som er koblett opp til gjeldende rom. Spilleren skriver inn en key her, som leder til neste rom.
        "North": "N1",
        "South": "S1",
        "East": "E1",

        "West": False

    },
    "N1": {
        "name": "North 1",
        "key": "N1",
        "main": "music/deja vu.wav",
        "objects": False,
        "been": False,

        "West": "N2",
        "South": "C",

        **dict.fromkeys(["North", "East"], False)

    },
    "N2": {
        "name": "North 2",
        "key": "N2",
        "main": "music/National Anthem of USSR.wav",
        "objects": 1,
        "been": False,

        "East": "N1",

        **dict.fromkeys(["North", "South", "West"], False)

    },
    "E1": {
        "name": "East 1",
        "key": "E1",
        "main": "music/nge.wav",
        "objects": 1,
        "been": False,

        "West": "C",
        "South": "S1-E1",

        **dict.fromkeys(["North", "East"], False)

    },
    "S1": {
        "name": "South 1",
        "key": "S1",
        "main": "music/kirby runs away from king popopolice.wav",
        "objects": 1,
        "been": False,

        "North": "C",
        "East": "S1-E1",

        **dict.fromkeys(["South", "West"], False)


    },
    "S1-E1": {
        "name": "South 1, East",
        "key": "S1-E1",
        "main": "music/biggie smalls feat. thomas the tank engine.wav",
        "objects": 1,
        "been": False,

        "West": "S1",
        "North": "E1",

        **dict.fromkeys(["South", "East"], False)

    },
    "S": {
        "name": "Secret",
        "key": "S",
        "main": "music/Jebaited.wav",
        "objects": 0,
        "been" : False,

        "East": "C",

        **dict.fromkeys(["South", "North", "West"], False)
        
    }
}


# Spør om du vil ha på musikk i spillet. Kan endres på mens du spiller.
def musicOption():
    global music
    music = 0
    while music == 0:
        print("\nDo you want to play with music?")
        yn = str(input("Yes or no: "))
        if yn in y:
            music = 1
            print("\nMusic on\n\n")
        elif yn in n:
            music = 2
            print("\nMusic off\n\n")
    input("Press enter to continue")


# Introduksjons tekst som forklarer spille, og sier hvordan du kan komme tilbake til meny og instillinger
def menu():
    print("Press Esc to skip scroll\n\n")
    g.delaydprint2("You spawn in a dungeon, with a single goal...\nFind all five of the coins!\n\nTo do this you must type in directions, and navigate through the different rooms.\n\nGood luck!\n")
    
    if music == 1:
        g.delaydprint2("And enjoy the music ;)\n\nNote! its recomended to turn down the volume with the 'Volume Mixer' feature on Microsoft Windows\n")
    
    g.delaydprint2("Note! type in 'options' to turn on or off music\n      type in 'menu' to see this screen again. \n\n")
    g.delaydprint2("Note! remember to use capitalisation when typing directions\n\nValid directions are: \n'North'\n'South'\n'East'\n'West'\n\n")
    
    input("Press enter to continue")


# Funksjon som behandler hvordan du kommer deg mellom rom.
def walk():
    yn = 0

    while yn != 1: # Loop for om spilleren trykker feil, eller velger en av de andre valgene enn å gå. 

        print("You are in: ", rooms[player["current"]]["name"])
        g.delaydprint2("Where do you want to go?\n\n")

        # Disse printer ut tilgjengelige veier for rommet du er i. 
        if rooms[player["current"]]["North"] != False:
            print("You can go North\n")

        if rooms[player["current"]]["South"] != False:
            print("You can go South\n")

        if rooms[player["current"]]["East"] != False:
            print("You can go East\n")

        if rooms[player["current"]]["West"] != False: # !!!!!
            print("You can go West\n")

        direction = str(input("\nType direction you want to walk: "))

        # Sjekker om spiller prøver å gå inn i hemmelige rommet. 
        if direction == "West" and player["current"] == "C":
            yn = 1
            player["current"] = "S"

        # Sjekker om det spiller skrev er en av fire valg, og at valget er gyldig. 
        elif direction in ("North", "South", "East", "West") and rooms[player["current"]][direction] != False: 
            yn = 1 # Slutter loopen
            player["current"] = rooms[player["current"]][direction] # Setter spillerens gjeldende rom som det rommet de gikk til.

        # Fører spiller til options skjermen
        elif direction in ("Options", "options", "option", "Options"):
            g.clear()
            musicOption()
            if music == 2:
                g.stopS()
            elif music == 1:
                g.songS(rooms[player["current"]]["main"])
            g.clear()

        # Fører spiller til menu skjermen
        elif direction in ("Menu", "menu"):
            g.clear()
            menu()
            g.clear()

        #Spiller har skrevet feil og må prøve på nytt
        else:
            print("Type a valid direction, or use menu/options")
            input("Press enter to continue")
            g.clear()


# Funksjon for hemmelig rom
def secretRoom():
    g.delaydprint2("Congratulations! You found the secret room.\n\n You will now get\n. . .\n1000000000000000 coins.\n\n\n")
    sleep(1.7)
    g.clear()
    g.delaydprint2("Just kidding")
    sleep(0.7)
    g.loopS("music/Jebaited.wav")
    x = 0
    while x < 3:
        g.delaydprint3(s.gachiString)
        print("\n")
        x+=1
    g.clear()
    g.stopS()
    g.delaydprint2("Now find the rest of the coins.\n\nThe way out is East\n\n")
    input("Press enter to continue")



# Random generator som velger en av fire ascii tegninger som er lagt til i spillet. 
def asciiPrint():
    num = random.randint(1, 3)
    num2 = random.randint(1,20)
    if num2 == 10:
        s.gachi()
    elif num == 1:
        s.garfield()
    elif num == 2:
        s.pikachu()
    elif num == 3:
        s.tribe()


# To tekst linjer som blir brukt i main loop.
stringBeen = "You have been here before! \nContinue onwords\n\nYou have "
stringCollect = "There is ", rooms[player["current"]]["objects"], " coin/s here.\nYou pick them up.\nYou now have "


# Initialisering, spør om musikk og viser menyen. Er gjort som funkjsoner siden spiller kan få tilgang til disse under spille
musicOption()
g.clear()
menu()


# Main loop
while True:
    g.clear()
    if player["objects"] < 5:
        
        # Printer navne til romme du er i nå
        print("You are in: ", rooms[player["current"]]["name"]) 
        sleep(1.2)

        # Om spiller går til secret room, gjør den secretRoom funksjon
        if player["current"] == "S":
            g.clear()
            secretRoom()
        

        # Om spilleren ikke har vært i rommet:
        elif rooms[player["current"]]["been"] == False:
            
            # Sjekker om musikk instilligen er av eller på: 
            if music == 1:
                g.loopS(rooms[player["current"]]["main"])
            
            rooms[player["current"]]["been"] = True
            asciiPrint()
            g.delaydprint2("A new room!\n")
            sleep(2)

            # Om det er objects/coins i rommet:
            if rooms[player["current"]]["objects"] != False:
                player["objects"] += 1  # Legger til en coin
                g.delaydprint2(stringCollect)
                print(player["objects"],"coin/s\n")
                input("Press enter to continue")
            
            # Om det ikke er det:
            else:
                g.delaydprint2("There are no coins here\n\n")
                input("Press enter to continue")

            # Om spiller har funnet alle 5 coins:
            if player["objects"] == 5:
                g.clear()
                g.delaydprint2("You got five coins! Congratulations on your journey.\n\nThanks for playing the game!")
                input("\n\nPress enter to continue")
                break # Avslutter spille
        

        # Om spilleren har vært i rommet fra før av:
        else:
            g.delaydprint2(stringBeen)
            print(player["objects"],"coin/s\n")

            input("\nPress enter to continue")

        g.clear()
        walk()


    else:
        g.delaydprint("You got five coins! Congratulations on your journey.\n\nThanks for playing the game!")
        
        input("\n\nPress enter to continue")
        break


