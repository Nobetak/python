def wpisywanie():
    rozmiar = int(input("podaj rozmiar tablicy: "))
    tablica = []
    for _ in range(rozmiar):
        tablica.append(int(input("wpisz cyfre: ")))
    return tablica


def mnozenie(tablica):
    wynik = 1
    for element in tablica:
        wynik *= element
    return wynik


def dodawanie(tablica):
    wynik = 1
    for element in tablica:
        wynik += element
    return wynik


def odejmowanie(tablica):
    wynik = 1
    for element in tablica:
        wynik -= element
    return wynik


def dzielenie(tablica):
    wynik = 1
    for element in tablica:
        wynik / element
    return wynik


tablica = wpisywanie()
wynik_mnozenia = mnozenie(tablica)

print("wynik mnozenia z "f"{tablica}" " wynosi "f"{wynik_mnozenia} ")
