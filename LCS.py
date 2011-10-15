# -*- coding: utf-8 -*-

from sys import argv
import codecs


def main(inpargv):
    f = codecs.open(str(inpargv[1]), 'r', encoding='utf-16')
    for line in f:
        line = line.replace('\n','')
        print repr(line)


if __name__ == "__main__":
    main(argv)
