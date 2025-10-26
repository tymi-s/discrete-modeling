from erozja import erozja
from dylatacja import dylatacja
def otwarcie(obraz,filtr):
    temp = erozja(obraz,filtr)
    return dylatacja(temp,filtr)
