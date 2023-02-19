# Importowanie biblioteki math i random
import math
import random
# Inicjalizacja listy a i wypełnienie jej 10 losowymi wartościami z zakresu od 1 do 99
a = []
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
# Pętla for powtarza się 10 razy
for i in range(10):
    # Program prosi użytkownika o podanie liczby z zakresu od 1 do 99 i zapisuje 
    g = int(input("Enter an integer from 1 to 99: "))
    # Pętla while sprawdza, czy liczba podana przez użytkownika zgadza się z wartością na i-tej pozycji w liście a
    while a[i] != g:
        # Jeśli liczba jest mniejsza niż wartość na i-tej pozycji w liście a, program wypisuje "guess is low"
        # i prosi użytkownika o ponowne podanie liczby z zakresu od 1 do 99
        if g < a[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 99: "))
            # Jeśli liczba jest większa niż wartość na i-tej pozycji w liście a, program wypisuje "guess is high"
            # i prosi użytkownika o ponowne podanie liczby z zakresu od 1 do 99
        elif g > a[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: "))
            # Jeśli liczba zgadza się z wartością na i-tej pozycji w liście a, program wypisuje "you guessed it!"
            # i przechodzi do kolejnego przebiegu pętli for
        else:
            break
    print("you guessed it!")
# Inicjalizacja listy b i wypełnienie jej 10 losowymi wartościami z zakresu od 1 do 49
b = []
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
# pętla for powtarza się 10 razy
for i in range(10):
    # Program prosi użytkownika o podanie liczby z zakresu od 1 do 49 i zapisuje 
    g = int(input("Enter an integer from 1 to 49: "))
    # Pętla while sprawdza, czy liczba podana przez użytkownika zgadza się
    while b[i] != g:
        if g < b[i]:
             # Jeśli liczba jest mniejsza niż wartość na i-tej pozycji w liście a, program wypisuje "guess is low"
            # i prosi użytkownika o ponowne podanie liczby z zakresu od 1 do 49
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
            # Jeśli liczba jest większa niż wartość na i-tej pozycji w liście a, program wypisuje "guess is high"
            # i prosi użytkownika o ponowne podanie liczby z zakresu od 1 do 49
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
            # Jeśli liczba zgadza się z wartością na i-tej pozycji w liście a, program wypisuje "you guessed it!"
        else:
            break
    print("you guessed it!")

    # Program losuje 10 liczb z zakresu od 1 do 99 i 
    # od 1 do 49, a następnie w pętli while sprawdza, czy liczba podana przez użytkownika zgadza się z którą
    # W kodzie wykorzystywana jest biblioteka random, która generuje losowe liczby całkowite z określonego przedziału.
