from erozja import erozja
from dylatacja import dylatacja
def domkniecie(obraz,filtr):
    temp = dylatacja(obraz,filtr)
    return erozja(temp,filtr)