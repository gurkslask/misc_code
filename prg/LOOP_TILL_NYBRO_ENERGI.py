#-------------------------------------------------------------------------------
# Name:        Filflyttningsloop åt Nybro Energi
# Purpose:     Flyttar filer för visning på dator vid foaje
#
# Author:      Alexander Svensson @ Bitcon
#
# Created:     13-09-2013
# 
# Kopierar filer från det ena stället till det andra ink. felhantering
#-------------------------------------------------------------------------------
import time, shutil
def main():
    akt_tid = time.time()

    while True == True:
        if akt_tid <= time.time() - 2:
            try:
                shutil.copy(r'C:\temp4\test.txt', r'C:\temp5\test.txt')
                #print('Success!')
            except IOError:
                print('Could not read file!')
            except:
                print('Error occured!')
            akt_tid = time.time()

if __name__ == '__main__':
    main()
