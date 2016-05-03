from fractions import Fraction
from random import randint


def gerarmatrizaleatoria(numlinhas, numcolunas, varval):
    aum = []
    for i in range(numlinhas):
        aum.append([])
        for j in range(numcolunas):
            aum[i].append(randint(-varval, varval))
            if aum[i][j] == 0:
                aum[i].insert(j, randint(-varval, varval))
    return aum


def exibir(aum, numcolunas, l, frac):
    print(2 * numcolunas * "----", "\n")
    a = 0
    for aum in aum:
        for i in range(numcolunas):
            if aum[i] == -0:
                aum[i] = 0
            elif float(aum[i]).is_integer():
                aum[i] = int(aum[i])
            if frac == False:
                print(Fraction(round(aum[i], 2)), sep='', end='    ')
            else:
                print(round(aum[i], 2), sep='', end='    ')
        if l != "":
            print(l[a], end='')
        print("\n")
        a += 1
    print(2 * numcolunas * "----")


def esc(aum):
    numlinhas = len(aum)
    numcolunas = len(aum[0])

    l = []
    l.insert(0, "L{0}=L{0}".format(1))

    exibir(aum, numcolunas, "", "")

    for k in range(numlinhas - 1):
        for i in range(k + 1, numlinhas):
            x = aum[i][k]
            for j in range(k, numcolunas):
                aum[i][j] = aum[i][j] - x / aum[k][k] * aum[k][j]
            if i != k:
                l.insert(i, "L{0}=L{0}-({1}/{2})L{3}".format(i + 1, round(x, 2), round(aum[k][k], 2), k + 1))
            else:
                l.insert(i, "L{0}=L{0}".format(i))

        print("\nk = ", k, " i = ", i, " j = ", j, "\n")
        exibir(aum, numcolunas, l, "")
        l.insert(i - 1, "L{0}=L{0}".format(i))


def escr(aum, frac):
    numlinhas = len(aum)
    numcolunas = len(aum[0])

    l = []

    exibir(aum, numcolunas, "", "")

    for k in range(numlinhas):
        pivo = aum[k][k]
        for j in range(numcolunas):
            aum[k][j] = aum[k][j] / pivo

        for i in range(numlinhas):
            if i != k:
                x = aum[i][k]
                l.insert(i, "L{0}=L{0}-({1}L{2})".format(i + 1, round(x, 2), k + 1))
                for j in range(numcolunas):
                    aum[i][j] = aum[i][j] - x * aum[k][j]
            else:
                l.insert(i, "L{0}=L{0}/{1}".format(i + 1, round(pivo, 2)))

        print("\nk = ", k, " i = ", i, " j = ", j, "\n")
        exibir(aum, numcolunas, l, frac)


aum = gerarmatrizaleatoria(3, 4, 10)
escr(aum, True)
