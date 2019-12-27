#!/usr/bin/env python3

import sly
import argparse
import os, sys

class ExcellonLexer(sly.Lexer):
    tokens = {LETTER, INTEGER, FLOAT, REWIND, XCOORD, YCOORD}

    ignore = ' \t\n\r'

    #Regex definitions for tokens
    LETTER  =   r'[a-zA-Z]'
    FLOAT   =   r'\d*\.\d+'
    INTEGER =   r'\d+'
    REWIND  =   r'%'

    LETTER['X'] = XCOORD
    LETTER['Y'] = YCOORD
    LETTER['x'] = XCOORD
    LETTER['y'] = YCOORD

    #Token action triggers
    @_(r'\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\d*\.\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

argparser = argparse.ArgumentParser()

argparser.add_argument("-i", help="Input file", type=argparse.FileType('r'))
argparser.add_argument("-o", help="Output file", type=argparse.FileType('w'))
argparser.add_argument("-d", help="Tool diameter in mm", type=float, default=0.8)

args = argparser.parse_args()

lexer = ExcellonLexer()

print(args)

infile = args.i.read()

for tok in lexer.tokenize(infile):
    print('type=%r, value=%r' % (tok.type, tok.value))
