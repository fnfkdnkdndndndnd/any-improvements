import math

print("=================rekenmachine=================")

machten = input("Wil je werken met machten? (ja/nee): ").strip().lower()

if machten == "ja":
    g1 = float(input("Geef getal: "))
    macht = float(input("Exponent: "))
    uitkomst = g1 ** macht

elif machten == "nee":
    g1 = float(input("Geef getal 1: "))
    optie = input("Welke bewerking wil je uitvoeren? (+, -, *, /): ").strip()
    g2 = float(input("Geef getal 2: "))

    if optie == "+":
        uitkomst = g1 + g2
    elif optie == "-":
        uitkomst = g1 - g2
    elif optie == "*":
        uitkomst = g1 * g2
    elif optie == "/":
        uitkomst = g1 / g2
    else:
        print("Ongeldige optie")

else:
    print("Ongeldige invoer voor machten. Voer 'ja' of 'nee' in.")

# geen regel hiervoor zetten 
print("de uitkomst is:", uitkomst)