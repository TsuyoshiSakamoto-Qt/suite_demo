# -*- coding: utf-8 -*-

import names
import sys

def main():

    print(sys.stdout.encoding)
    # sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
    print("print:テストログの出力".encode('utf_8').decode('cp932', errors="surrogateescape"))
    print("print:テストログの出力")
    test.log("test.log:テストログの出力")
   
