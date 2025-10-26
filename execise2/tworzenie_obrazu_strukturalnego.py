import numpy as np
def tworzenie_obrazu_strukturalnego(rozmiar,ksztalt):

    if ksztalt == "kwadrat":
        return np.ones((rozmiar,rozmiar),dtype=np.uint8)

    elif ksztalt == "krzyz":
        element = np.zeros((rozmiar,rozmiar),dtype= np.uint8)

        mid = rozmiar // 2 # rozmiar sąsiedztwa
        element[mid,:]=1
        element[:,mid]=1
        return element

    elif ksztalt == "gauss":
        sigma = rozmiar /6.0
        mid = rozmiar // 2
        element = np.zeros((rozmiar,rozmiar),dtype=np.float32)

        #wzor na filtr gaussa
        for i in range(rozmiar):
            for j in range(rozmiar):
                x = i - mid
                y = j - mid
                element[i, j] = np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))

        element = element / np.max(element)
        return element
    elif ksztalt == "upperpass":
        element = np.ones((rozmiar,rozmiar),dtype=np.float32) * -1
        mid = rozmiar // 2

        #element środkowy
        element[mid,mid] = rozmiar * rozmiar -1
        return element

    else:
        print("\n BŁĄD! WPISANO NIE OBSŁUGIWANY KSZTAŁT FILTRA!")
        return np.ones((rozmiar,rozmiar),dtype=np.uint8)

