#jak działa automat komórkowy 2D
# mamy planszę jak w szachach i rozmieszczamy na niej kropki na samym początku
import random

#gra w życie składa się z dwuch rund:
#1 - nowe kropki pojawiają się na polach  które w obrębie swojego sąsiedztwa (1 pole w każdym możliwym kierunku) mają dokładnie 3 sąsiadów.
#2 - kropki które w swoim sąsiedztwie nie mają 2 lub 3 sąsiadów znikają


# automat komórkowy 1D
# tutaj mamy tablicę gdzie mamy jedynki i zera
from set import *
from regula2 import *
from regula1 import *
from wyswietl_kolorowo import *
try:
    rozmiar = int(input("Podaj rozmiar automatu komórkowego: "))
except ValueError:
    print("Podaj liczbę całkowitą!")
    exit(0)

if rozmiar == 0:
    print("Rozmiar nie może być równy 0!")
    exit(0)

try:
    iteracje = int(input("Podaj ilość interacji do wykonania: "))
except ValueError:
    print("Podaj liczbę całkowitą!")
    exit(0)

if iteracje == 0:
    print("Rozmiar nie może być równy 0!")
    exit(0)

indeksy = random.sample(range(0,rozmiar-1), rozmiar //2)
indeksy.sort()
print("indeksy które na początku mają być żywe: ",indeksy)

automat=[0]*rozmiar
set(automat,indeksy)

print(f"\n{'^'*50}\nAutomat początkowy:", automat,"\n\n")


for i in range(iteracje):
    regula2(automat)
    wyswietl_kolorowo(automat,i)


