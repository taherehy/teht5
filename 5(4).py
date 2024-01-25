def main():
    # Luodaan tyhjä lista kaupungeille
    kaupungit = []

    # Kysytään käyttäjältä viiden kaupungin nimet
    for i in range(5): #for i in range(5):
        # Tämä for-toistorakenne pyytää käyttäjältä 5
        # kaupungin nimeä käyttäen muuttujaa i indeksinumerona.
        # Jokainen kaupunki tallennetaan listalle.


        kaupunki = input(f"Syötä kaupunki {i + 1}: ")
        kaupungit.append(kaupunki)

    # Tulostetaan kaupungit yksi kerrallaan
    print("Syötetyt kaupungit:")
    for kaupunki in kaupungit:
        #for kaupunki in kaupungit: Toinen for-toistorakenne
        # käy läpi kaikki tallennetut kaupungit listalta ja tulostaa ne yksi kerrallaan.

        print(kaupunki)

if __name__ == "__main__":
    main()
