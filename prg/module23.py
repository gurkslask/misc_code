#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alexander.svensson
#
# Created:     26-07-2013
# Copyright:   (c) alexander.svensson 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print('Hello World')
    a = ('a','b','c')
    b = (1, 4, 8)
    c= []
    for i in b:
        c.append(i*2)

    print(c)
    print(b)


if __name__ == '__main__':
    main()
