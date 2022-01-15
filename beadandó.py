print("Üdvözöllek!")

while 1:
    print("Mit szeretnél?:")
    print("1. Összeadni")
    print("2. Kivonni")
    print("3  Szorozni")
    print("4. Osztani")
    print("5. Kilépni")

    választás = int(input("Ide írd a választásod: "))
    if választás == 1:
        szam1 = int(input("Írd be az első számot: "))
        szam2 = int(input("Írd be a másik számot: "))
        print("Eredmény: ", szam1+szam2)

    elif választás == 2:
        szam1 = int(input("Írd be az első számot: "))
        szam2 = int(input("Írd be a másik számot: "))
        print("Eredmény: ", szam1-szam2)

    elif választás == 3:
        szam1 = int(input("Írd be az első számot: "))
        szam2 = int(input("Írd be a másik számot: "))
        print("Eredmény: ", szam1*szam2)

    elif választás == 4:
        szam1 = int(input("Írd be az első számot: "))
        szam2 = int(input("Írd be a másik számot: "))
        print("Eredmény: ", szam1/szam2)

    elif választás == 5:
        print("Kilépés...")
        break
    print()