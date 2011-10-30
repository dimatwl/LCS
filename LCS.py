# -*- coding: utf-8 -*-
from sys import argv
import codecs

def getLCSTable(inpFirstString, inpSecondString):
    X = inpFirstString
    Y = inpSecondString
    m = len(X)
    n = len(Y)
    table = [[0] for i in range(m+1)]
    for line in table:
        for char in Y:
            line.append(0)
    c = table
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return c

def getSTRTable(inpFirstString, inpSecondString):
    X = inpFirstString
    Y = inpSecondString
    m = len(X)
    n = len(Y)
    table = [[0] for i in range(m+1)]
    for line in table:
        for char in Y:
            line.append(0)
    c = table
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = 0 
    return c


def getLCSFromTable(inpLCSTable, inpFirstString, inpSecondString):
    c = inpLCSTable
    X = inpFirstString
    Y = inpSecondString
    i = len(X)
    j = len(Y)
    LCS = u''
    while i != 0 and j != 0:
        if X[i-1] == Y[j-1]:
            LCS = LCS + X[i-1]
            i -= 1
            j -= 1
        elif c[i][j-1] > c[i-1][j]:
            j -= 1
        else:
            i -= 1
    return LCS[::-1]


def getLCS(inpFirstString, inpSecondString):
    LCSTable = getLCSTable(inpFirstString,inpFirstString)
    LCS = getLCSFromTable(LCSTable,inpFirstString,inpSecondString)
    return LCS


def main(inpargv):
    f = codecs.open(str(inpargv[1]), 'r', encoding='utf-16')
    lines = []
    for line in f:
        line = line.replace('\n','')
        line = line.lower()
        lines.append(line)
    for line in getSTRTable(lines[0],lines[1]):
        print line


if __name__ == "__main__":
    main(argv)
