"""In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?"""

tablica = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

lista1 = tablica.split("\n")
lista = []

for x in lista1:
    lista.append(x.split(" "))

# print(lista)

wartosc = 0
wynik_czterech_w_wierszu = 1


for wiersz in lista:
    indexstart = 0
    indexstop = 3
    while indexstop < 20:
        cztery_liczby = wiersz[indexstart: indexstop + 1]
        # print(cztery_liczby)
        for i in cztery_liczby:
            wynik_czterech_w_wierszu *= int(i)
        # print(f'Wynik czterech kolejnych: {wynik_czterech_w_wierszu}')
        if wynik_czterech_w_wierszu > wartosc:
            wartosc = wynik_czterech_w_wierszu
            najwieksze_liczby = cztery_liczby
            print(f'WYNIK PO PIERWSZYM: {wartosc}, cztery_liczby: {najwieksze_liczby}')
        wynik_czterech_w_wierszu = 1
        indexstart += 1
        indexstop += 1
    # print("Nowy wiersz!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# print(f'WYNIK PO PIERWSZYM: {wartosc}, cztery_liczby: {najwieksze_liczby}')

index_start = 0
index_stop = 3
iloczyn = 1
nowa_kolumna = 0
licznik_w_kolumnach = 0
lista_do_printu = []

while licznik_w_kolumnach < 20:
    while index_stop < 23:
        lista_czterech = lista[index_start:index_stop + 1]
        # print(lista_czterech)
        for x in lista_czterech:
            # print(f'index {index_start}: {x[nowa_kolumna]}')
            iloczyn *= int(x[nowa_kolumna])
            lista_do_printu.append(x[nowa_kolumna])
            # print(iloczyn)
        lista_czterech = None
        if iloczyn > wartosc:
            wartosc = iloczyn
            najwieksze_liczby1 = lista_do_printu
            print(f'WYNIK PO DRUGIM: {wartosc}, najwieksze liczby: {najwieksze_liczby1}')
        lista_do_printu = []
        iloczyn = 1
        index_start += 1
        index_stop += 1
    nowa_kolumna += 1
    index_start = 0
    index_stop = 3
    licznik_w_kolumnach += 1

# print(f'WYNIK PO DRUGIM: {wartosc}, najwieksze liczby: {najwieksze_liczby1}')

index_kolumna = 3
index_start1 = 0
index_stop1 = 3
index_x = 0
index_x_kolejne_kolumny = 0
wynik = 1
lista_do_printu1 = []

while index_kolumna < 20:  # dopóki index_kolumna nie będzie w ostatnim wierszu
    while index_stop1 < 20:  # dopóki index_wiersz nie będzie w ostatniej kolumnie
        # while index_x1 < 4: # dopóki index_x będzie mniejszy od 4
        index_x += index_x_kolejne_kolumny
        lista_czterech1 = lista[index_start1:index_stop1 + 1]  # lista czterech wierszy. Od indeksu 0 do 3
        for wiersz in lista_czterech1:  # dla każdego wiersza w liscie czterech wierszy:
            wynik *= int(wiersz[index_x])  # wynik równa się każdy kolejny wiersz z czterech wierszy *
            # print(f'{index_x}:--- {wiersz[index_x]}')
            # print(wynik)
            lista_do_printu1.append(wiersz[index_x])
            index_x += 1
        if wynik > wartosc:
            # print(f'WYNIK W IFIE: {wynik}')
            wartosc = wynik
            najwieksze_liczby2 = lista_do_printu1
            print(f'WYNIK PO TRZECIM: {wartosc}, najwieksze liczby: {najwieksze_liczby2}')
        lista_do_printu1 = []
        # print("Kamil!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        wynik = 1
        index_start1 += 1
        index_stop1 += 1
        index_x = 0
    # print('###########################################################')
    index_start1 = 0
    index_stop1 = 3  # tutaj cos nie tak: było: index_stop1 = 3
    index_x_kolejne_kolumny += 1
    index_kolumna += 1

# print(f'WYNIK PO TRZECIM: {wartosc}, najwieksze liczby: {najwieksze_liczby2}')

index_kolumna1 = 3
index_start11 = 0
index_stop11 = 3
index_x1 = 3
index_x_kolejne_kolumny1 = 0
wynik1 = 1
lista_do_printu11 = []

while index_kolumna1 < 20:  # dopóki index_kolumna nie będzie w ostatnim wierszu
    while index_stop11 < 20:  # dopóki index_wiersz nie będzie w ostatniej kolumnie
        # while index_x1 < 4: # dopóki index_x będzie mniejszy od 4
        index_x1 += index_x_kolejne_kolumny1
        lista_czterech11 = lista[index_start11:index_stop11 + 1]  # lista czterech wierszy. Od indeksu 0 do 3
        for wiersz in lista_czterech11:  # dla każdego wiersza w liscie czterech wierszy:
            wynik1 *= int(wiersz[index_x1])  # wynik równa się każdy kolejny wiersz z czterech wierszy *
            print(f'{index_x1}:--- {wiersz[index_x1]}')
            print(wynik1)
            lista_do_printu1.append(wiersz[index_x1])
            index_x1 -= 1
        if wynik1 > wartosc:
            print(f'WYNIK W IFIE: {wynik1}')
            wartosc = wynik1
            najwieksze_liczby21 = lista_do_printu11
            print(f'WYNIK PO CZWARTYM: {wartosc}, najwieksze liczby: {najwieksze_liczby21}')
        lista_do_printu11 = []
        print("Kamil!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        wynik1 = 1
        index_start11 += 1
        index_stop11 += 1
        index_x1 = 3
    print('###########################################################')
    index_start11 = 0
    index_stop11 = 3  # tutaj cos nie tak: było: index_stop1 = 3
    index_x_kolejne_kolumny1 += 1
    index_kolumna1 += 1

print(wartosc)
