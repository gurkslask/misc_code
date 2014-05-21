#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alexander.svensson
#
# Created:     25-07-2013
# Copyright:   (c) alexander.svensson 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
def main():
    def tFram():
        t.fd(10)
    def tLeft():
        t.left(60)
    def tRight():
        t.right(120)
    t = turtle.Turtle()
    t.showturtle
    t.speed=0

    def tEtta():
        tFram()
        t.left(60)
        tFram()
        t.right(120)
        tFram()
        t.left(60)
        tFram()

    tEtta()

    tLeft()
    tEtta()
    tRight()
    tEtta()
    tLeft()

    tEtta()

    tLeft()
    tEtta()
    tLeft()
    tEtta()
    tRight()
    tEtta()


    tLeft()
    tEtta()
    tRight()
    tEtta()
    tLeft()

    tLeft()
    tEtta()
    tLeft()
    tEtta()
    tRight()
    tEtta()

    tEtta()

if __name__ == '__main__':
    main()
