def set(automat,indeksy):

    j=0;
    for i in range(0,len(automat)):
        if j< len(indeksy) and i == indeksy[j]:
            automat[i] = 1
            j +=1
