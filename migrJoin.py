#! /usr/bin/env python3
# coding: utf-8

import sys, subprocess, os

#variables
fileToM = './'

#main.
def main():
    print("Hello python 3")
    checkInputs()
    cleanCurDir()

#checks command line parameters.
def checkInputs():
    global fileToM
    if(len(sys.argv) < 2):
        print("Nom du fichier à migrer manquant en paramètre. EX: python migrJoin.py LBS01_A1_A35/A2.sql")
    else:
        fileToM = fileToM + sys.argv[1]

#clean current dir files for new migration.
def cleanCurDir():
    if(os.path.isfile(fileToM)):
        os.remove(fileToM)

#call program.
if __name__ == "__main__":
    main()
