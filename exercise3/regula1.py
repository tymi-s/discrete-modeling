def regula1(automat):
    nowy = automat.copy()
    for i in range(0,len(automat)):

        if i ==0:
            lewa = 0
            prawa = automat[i+1]
        elif i == len(automat)-1:
            prawa = 0
            lewa = automat[i-1]

        else:
            lewa = automat[i-1]
            prawa = automat[i+1]

        if lewa == prawa:
            nowy[i] = 0
        else:
            nowy[i] = 1

    for i in range(0,len(automat)):
        automat[i] = nowy[i]
# jeśli dokładnie jeden sąsiad będzie żywy to komórka zostaje lub staje się żywa, w innym przypadku staje się martwa