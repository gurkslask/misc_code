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

class Pid():

    def __init__(self, pv, bv):
        super(Pid, self).__init__()
        self.bv = bv
        self.pv = pv
        self.Out = 0.0
        self.EnableP = True
        self.Gain = 5

    def Preg(self):
        return (self.pv - self.bv) * self.Gain

    def Treg(self):


    def PidLoop(self):
        if self.EnableP:
            self.Out = self.Preg()
        return self.Out





def main():
    PID = Pid(23,20)
    print(PID.PidLoop())



if __name__ == '__main__':
    main()