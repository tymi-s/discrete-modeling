def regula2(automat):
    nowy = automat.copy()
    n = len(automat)

    for i in range(n):
        # i=0  wiec -1%30 = 29
        lewa = automat[(i - 1) % n]
        prawa = automat[(i + 1) % n]

        if lewa == prawa:
            nowy[i] = 0
        else:
            nowy[i] = 1

    for i in range(n):
        automat[i] = nowy[i]