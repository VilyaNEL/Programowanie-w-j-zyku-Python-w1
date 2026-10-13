
# Program proszący o imię i nazwisko oraz ich wyświetlenie #

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

print(f"Imię i nazwisko: {imie} {nazwisko}")

# Program obliczający sumę, różnicę, iloczyn i iloraz dwóch liczb w pythonie

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

suma = a + b
roznica = a - b
iloczyn = a * b

if b == 0:
    print("Suma:", suma)
    print("Różnica:", roznica)
    print("Iloczyn:", iloczyn)
    print("Iloraz: nie można dzielić przez zero")
else:
    iloraz = a / b
    print("Suma:", suma)
    print("Różnica:", roznica)
    print("Iloczyn:", iloczyn)
    print("Iloraz:", iloraz)

# Program przeliczający temperaturę z Celsjusza na Fahrenheita

celsjusz = float(input("Podaj temperaturę w stopniach Celsjusza: "))
fahrenheit = celsjusz * 9 / 5 + 32

print(f"{celsjusz}°C to {fahrenheit}°F")

# Suma dwóch liczb z komentarzami opisującymi kroki

# Krok 1: Pobierz pierwszą liczbę od użytkownika i zamień ją na liczbę dziesiętną
pierwsza_liczba = float(input("Podaj pierwszą liczbę: "))

# Krok 2: Pobierz drugą liczbę i zamień ją na liczbę dziesiętną
druga_liczba = float(input("Podaj drugą liczbę: "))

# Krok 3: Dodaj obie liczby
suma = pierwsza_liczba + druga_liczba

# Krok 4: Wyświetl wynik dodawania
print("Suma:", suma)

# Obliczanie pola prostokąta z komentarzami

# Krok 1: Pobierz długość prostokąta od użytkownika
dlugosc = float(input("Podaj długość prostokąta: "))

# Krok 2: Pobierz szerokość prostokąta
szerokosc = float(input("Podaj szerokość prostokąta: "))

# Krok 3: Oblicz pole, mnożąc długość przez szerokość
pole = dlugosc * szerokosc

# Krok 4: Wyświetl wynik
print("Pole prostokąta:", pole)

# Pobranie imienia i nazwiska, format "Nazwisko, Imię" oraz walidacja danych

def pobierz_dane(etykieta):
    while True:
        dane = input(f"Podaj {etykieta}: ").strip()
        # Dozwolone są litery, spacje, łączniki i apostrofy
        if dane and any(znak.isalpha() for znak in dane) and all(
            znak.isalpha() or znak in " -'’" for znak in dane
        ):
            return " ".join(dane.split())  # Usuń nadmiarowe spacje
        print("Nieprawidłowe dane. Użyj liter; dozwolone są też spacje, łączniki i apostrofy.")

imie = pobierz_dane("imię")
nazwisko = pobierz_dane("nazwisko")

# Wyświetl dane w formacie „Nazwisko, Imię”
print(f"{nazwisko}, {imie}")