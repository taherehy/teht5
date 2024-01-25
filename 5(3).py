def onko_alkuluku(luku):
    if luku < 2:
        return False  # 0 ja 1 eivät ole alkulukuja

    for i in range(2, int(luku**0.5) + 1):
        #-lause tarkistaa, onko luku pienempi kuin 2.
        # Jos näin on, palautetaan False, koska 0 ja 1 eivät ole alkulukuja.
        if luku % i == 0:
            return False
            # Luku ei ole alkuluku, koska se on jaollinen jollakin muulla kuin 1 ja itsellään

    return True

def main():
    try:
        syote = int(input("Syötä kokonaisluku: "))
        if onko_alkuluku(syote):
            print(f"{syote} on alkuluku.")
        else:
            print(f"{syote} ei ole alkuluku.")
    except ValueError:
        print("Virheellinen syöte. Syötä kokonaisluku.")

if __name__ == "__main__":
    main()
#Se yrittää lukea käyttäjän antaman syötteen kokonaisluvuksi.