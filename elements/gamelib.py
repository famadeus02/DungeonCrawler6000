import winsound, sys
from time import sleep as s
import msvcrt as m 

# Funksjon for å ta vek alt fra skjermen
def clear(): 
    print("\n" * 100)



# En print funksjon som printer ting saktere
def delaydprint(string):
    for char in string:
        print(char, end="")
        sys.stdout.flush()
        if char != " ":
            s(0.08)


# Igjen en print funksjon som printer ord for ord, med litt flere variasjoner på hvor lenge den skal vente, angående tegne. Også lagt inn at spiller kan trykke på 'Esc' for å printe ut alt med en gang. 
def delaydprint2(string): 
    c = 0
    while m.kbhit(): m.getwch()
    for char in string: # Loop som printer hver enkelt bokstav i string
        if m.kbhit() and c != 27: # Sjekker keyboard er trykket på, og om Esc ikke har blitt trykket på tidligere.
        
            if ord(m.getch().decode("utf-8")) == 27: # Sjekker om det som ble trykka på var Esc, altså key nr. 27 i utf-8 sette 
                c = 27
        
        if c != 27: # Print med delay for hver bokstav. Skjer ikke hvis Esc er trykket
            print(char, end="")
            sys.stdout.flush()
            if char == ".":
                s(0.8)
            elif char == ",":
                s(0.4)
            elif char == "!":
                s(0.6)
            elif char != " ":
                s(.05)

        else: # Print uten delay mellom hver bokstav
            print(char, end="")
            sys.stdout.flush()


# Print med delay for hver new line
def delaydprint3(string): 
    c = 0
    while m.kbhit(): m.getwch()
    for char in string: # Loop som printer hver enkelt bokstav i string
        if m.kbhit() and c != 27: # Sjekker keyboard er trykket på, og om Esc ikke har blitt trykket på tidligere.
        
            if ord(m.getch().decode("utf-8")) == 27: # Sjekker om det som ble trykka på var Esc, altså key nr. 27 i utf-8 sette 
                c = 27
        
        if c != 27: # Print med delay for hver bokstav. Skjer ikke hvis Esc er trykket
            print(char, end="")
            sys.stdout.flush()
            if char == "\n":
                s(0.4)

        else: # Print uten delay mellom hver bokstav
            print(char, end="")
            sys.stdout.flush()

# Funksjoner for å spille av lyd filer.
def songS(songname):
    winsound.PlaySound(songname, winsound.SND_FILENAME|winsound.SND_NODEFAULT|winsound.SND_ASYNC)


def loopS(songname):
    winsound.PlaySound(songname, winsound.SND_FILENAME|winsound.SND_NODEFAULT|winsound.SND_ASYNC|winsound.SND_LOOP)


# Siden det ikke er en funksjon i 'winsound' modulen for å stoppe spilling av musikk, lagde jeg en som spilte et lite lyd klipp med ingen lyd i seg. 
def stopS():
    winsound.PlaySound("empty.wav", winsound.SND_FILENAME|winsound.SND_NODEFAULT|winsound.SND_ASYNC)



