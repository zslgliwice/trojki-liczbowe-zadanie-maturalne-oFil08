def zad1():
    odpowiedz = []
    with open("trojki.txt","r") as plik:
        for linijka in plik:
            arr = linijka.split(" ")
            if sum(map(int,list(arr[0]+arr[1]))) == int(arr[2]):
                odpowiedz.append(linijka)
        print(" ".join(odpowiedz))

zad1()

    