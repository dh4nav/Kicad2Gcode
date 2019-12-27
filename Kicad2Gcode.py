#!/usr/bin/env python3

import sly
import argparse
import os, sys

class ExcellonLexer(sly.Lexer):
    tokens = {LETTER, INTEGER, FLOAT, REWIND}

    ignore = ' \t\n\r'

    #Regex definitions for tokens
    LETTER  =   r'[a-zA-Z]'
    FLOAT   =   r'\d*\.\d+'
    INTEGER =   r'\d+'
    REWIND  =   r'%'



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
