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
    for line in table:
        print line
    


def main(inpargv):
    f = codecs.open(str(inpargv[1]), 'r', encoding='utf-16')
    lines = []
    for line in f:
        line = line.replace('\n','')
        lines.append(line)
    #getLCSTable(lines[0], lines[1])
    getLCSTable(u'ABCBDAB', u'BDCABA')


if __name__ == "__main__":
    main(argv)
