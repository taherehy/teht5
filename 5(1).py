import random

def heita_kuutiot(arpakuutioiden_lukumaara):
    silmalukujen_summa = 0

    # For-toistorakenne käy läpi jokaisen arpakuution
    for _ in range(arpakuutioiden_lukumaara):
        # Arvotaan silmäluku väliltä 1-6 (kuution silmälukualue)
        silmaluku = random.randint(1, 6)

        # Tulostetaan heitetyn kuution silmäluku
        print(f"Heitetty silmäluku: {silmaluku}")

        # Lisätään silmäluku summaan
        silmalukujen_summa += silmaluku

    return silmalukujen_summa

def main():
    try:
        # Kysytään käyttäjältä arpakuutioiden lukumäärä
        arpakuutioiden_lukumaara = int(input("Syötä arpakuutioiden lukumäärä: "))

        # Tarkistetaan, että annettu luku on positiivinen
        if arpakuutioiden_lukumaara <= 0:
            print("Syötä positiivinen luku arpakuutioiden lukumääräksi.")
        else:
            # Suoritetaan kuutioiden heitto ja lasketaan silmälukujen summa
            summa = heita_kuutiot(arpakuutioiden_lukumaara)

            # Tulostetaan silmälukujen summa
            print(f"Silmälukujen summa: {summa}")
    except ValueError:
        print("Virheellinen syöte. Syötä positiivinen kokonaisluku.")

if __name__ == "__main__":
    main()
