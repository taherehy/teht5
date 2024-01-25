def lue_luvut():
    numerot = []

    while True:
        syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")

        # Tarkistetaan, onko syöte tyhjä
        if not syote:
            break  # Tyhjä syöte lopettaa ohjelman suorituksen

        try:
            luku = float(syote)
            numerot.append(luku)
        except ValueError:
            print("Virheellinen syöte. Syötä desimaaliluku tai tyhjä merkkijono.")

    return numerot

def main():
    numerot = lue_luvut()

    if numerot:
        # Lajitellaan numerot suurimmasta pienimpään
        numerot.sort(reverse=True)

        # Tulostetaan viisi suurinta lukua
        print("Viisi suurinta lukua suuruusjärjestyksessä:")
        for i in range(min(5, len(numerot))):  # Otetaan huomioon, ettei listassa välttämättä ole viittä lukua
            print(numerot[i])
    else:
        print("Et syöttänyt yhtään lukua.")

if __name__ == "__main__":
    main()
