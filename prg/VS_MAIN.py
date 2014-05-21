class Kompensering:
    '''Kompensering är en klass som används
    för utekompensering. Man får sätta lite olika
    brytpunkter med SetVarden metoden, sätta MinMax
    och sen kör CountSP med utetemperaturen för att få
    tillbaka ett börvärde
    '''
    def __init__(self):
        self.DictVarden = {}
        self.SortedDictVarden = {}
        self.IterValue = 0

    def SetVarden(self, GraderUte, GraderFram):
        if isinstance(GraderUte, (int, float, complex)) and isinstance(GraderFram, (int, float, complex)):
            self.DictVarden[GraderUte] = GraderFram
        else:
            print('Fel vÃ¤rde')

    def SetMin(self, Min):
        self.Min = Min

    def SetMax(self, Max):
        self.Max = Max

    def MinMax(self, Value):
        return max(self.Min, min(self.Max, Value))
    
    def CountSP(self, PV):
        self.SortedList = sorted(self.DictVarden.keys())#Sortera värden
        for i in sorted(self.DictVarden.keys()):#Loopa igenom alla utetemp-värden
            if i > PV:#Hitta ett värde som är större än nuvarande utetemp
                self.UpperValueKomp = i#sätt det värdet
                self.LowValueKomp = self.SortedList[self.IterValue-1]#och ta värdet under det
                break#avbryt loopen4
            self.IterValue += 1
            if self.IterValue == len(self.DictVarden):
                return self.MinMax(self.DictVarden[self.SortedList[-1]])
        if self.UpperValueKomp == self.LowValueKomp:
            return self.MinMax(self.DictVarden[self.UpperValueKomp])#Om dessa är lika anta att nedre skalan nåddes
        self.y2 = self.DictVarden[self.UpperValueKomp]#sätt lite variabler
        self.y1 = self.DictVarden[self.LowValueKomp]
        self.x2 = self.UpperValueKomp
        self.x1 = self.LowValueKomp
        self.k =  (self.y2 - self.y1) / (self.x2 - self.x1)#utför räta linjens ekvation
        self.m =  self.y1 - (self.x1 * self.k)
        self.SP = (PV * self.k) + self.m
        return self.MinMax(self.SP), self.x2, self.x1
class PID:
    """ Simple Pid1 control.

        This class implements a simplistic Pid1 control algorithm. When first
        instantiated all the gain variables are set to zero, so calling
        the method GenOut will just return zero.
    """
    def __init__(self):
        # initialze gains
        self.Kp = 0
        self.Kd = 0
        self.Ki = 0
        self.OutMax = 100.0
        self.OutMin = 0.0

        self.Initialize()

    def SetKp(self, invar):
        """ Set proportional gain. """
        self.Kp = invar

    def SetKi(self, invar):
        """ Set integral gain. """
        self.Ki = invar

    def SetKd(self, invar):
        """ Set derivative gain. """
        self.Kd = invar

    def SetPrevErr(self, preverr):
        """ Set previous error value. """
        self.prev_err = preverr

    def Initialize(self):
        # initialize delta t variables
        self.currtm = time.time()
        self.prevtm = self.currtm

        self.prev_err = 0

        # term result variables
        self.Cp = 0
        self.Ci = 0
        self.Cd = 0


    def GenOut(self, error):
        """ Performs a Pid1 computation and returns a control value based on
            the elapsed time (dt) and the error signal from a summing junction
            (the error parameter).
        """
        self.currtm = time.time()               # get t
        dt = self.currtm - self.prevtm          # get delta t
        de = error - self.prev_err              # get delta error

        self.Cp = self.Kp * error               # proportional term
        self.Ci += error * dt                   # integral term

        self.Cd = 0
        if dt > 0:                              # no div by zero
            self.Cd = de/dt                     # derivative term

        self.prevtm = self.currtm               # save t for next pass
        self.prev_err = error                   # save t-1 error

        # sum the terms and return the result
        return min(self.OutMax, max(self.OutMin, self.Cp + (self.Ki * self.Ci) + (self.Kd * self.Cd)))



'''
#!#!#!#!#! Här nedan följer ett modbus exempel
#---------------------------------------------------------------------------# 
# configure the client logging
#---------------------------------------------------------------------------# 
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#---------------------------------------------------------------------------# 
# choose the client you want
#---------------------------------------------------------------------------# 
# make sure to start an implementation to hit against. For this
# you can use an existing device, the reference implementation in the tools
# directory, or start a pymodbus server.
#---------------------------------------------------------------------------# 
client = ModbusClient('127.0.0.1')

#---------------------------------------------------------------------------# 
# example requests
#---------------------------------------------------------------------------# 
# simply call the methods that you would like to use. An example session
# is displayed below along with some assert checks. Note that some modbus
# implementations differentiate holding/input discrete/coils and as such
# you will not be able to write to these, therefore the starting values
# are not known to these tests. Furthermore, some use the same memory
# blocks for the two sets, so a change to one is a change to the other.
# Keep both of these cases in mind when testing as the following will
# _only_ pass with the supplied async modbus server (script supplied).
#---------------------------------------------------------------------------# 
rq = client.write_coil(1, True)
rr = client.read_coils(1,1)
assert(rq.function_code < 0x80)     # test that we are not an error
assert(rr.bits[0] == True)          # test the expected value

rq = client.write_coils(1, [True]*8)
rr = client.read_coils(1,8)
assert(rq.function_code < 0x80)     # test that we are not an error
assert(rr.bits == [True]*8)         # test the expected value

rq = client.write_coils(1, [False]*8)
rr = client.read_discrete_inputs(1,8)
assert(rq.function_code < 0x80)     # test that we are not an error
assert(rr.bits == [True]*8)         # test the expected value

rq = client.write_register(1, 10)
rr = client.read_holding_registers(1,1)
assert(rq.function_code < 0x80)     # test that we are not an error
assert(rr.registers[0] == 10)       # test the expected value

rq = client.write_registers(1, [10]*8)
rr = client.read_input_registers(1,8)
assert(rq.function_code < 0x80)     # test that we are not an error
assert(rr.registers == [17]*8)      # test the expected value

arguments = {
    'read_address':    1,
    'read_count':      8,
    'write_address':   1,
    'write_registers': [20]*8,
}
rq = client.readwrite_registers(**arguments)
rr = client.read_input_registers(1,8)
assert(rq.function_code < 0x80)     # test that we are not an error
assert(rq.registers == [20]*8)      # test the expected value
assert(rr.registers == [17]*8)      # test the expected value

#---------------------------------------------------------------------------# 
# close the client
#---------------------------------------------------------------------------# 
client.close()
'''

import time
#from pymodbus.client.sync import ModbusTcpClient

def main():
	#Kompensering
	Komp = Kompensering()
	Komp.SetVarden(20, 17)
	Komp.SetVarden(10, 30)
	Komp.SetVarden(0, 55)
	Komp.SetVarden(-10, 60)
	Komp.SetVarden(-20, 65)

	Komp.SetMax(65)
	Komp.SetMin(20)
	#Pid1

	Pid1 = PID()
	Pid1.SetKp(10)
	Pid1.SetKi(1)
	Pid1.SetKd(1)
	#Initiering för program
	akt_time1 = time.time()
	akt_time2 = time.time()
	akt_time3 = time.time()


	#for i in range(100):
		#print(Pid1.GenOut(2.2))
		#time.sleep(0.4)

	
	while True:
		if akt_time1 <= time.time()-5:
			#Loop var 5:e sekund
			print('nu har det gatt 5 sekunder')
			akt_time1 = time.time()
		if akt_time2 <= time.time()-10:
			#SP = Komp.CountSP(UTEGIVAREN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
			print('nu har det gatt 10 sekunder')
			#Loop var 10:e sekund
			akt_time2 = time.time()
		if akt_time3 <= time.time()-1:
			#Loop varje sekund
			print('nu har det gatt 1 sekunder')
			#Pid1.GenOut(SP-FRAMLEDNING!!!!!!!!!!!!!!!!!!!!!!!!)
			akt_time3 = time.time()



if __name__ == '__main__':
	main()