import pyvisa as visa
from InstrumentBasics import *

#multimeter = 'USB0::0x05E6::0x6500::04446160::INSTR'
multimeter = 'TCPIP0::10.99.230.15::inst0::INSTR'
#scope = 'USB0::0x1AB1::0x0588::DS1EB144407786::INSTR'    #<-rack scope
scope = 'TCPIP0::10.99.219.40::INSTR'
generator = 'TCPIP0::10.99.250.15::INSTR'
''''
rm = visa.ResourceManager()
print(rm.list_resources())
('USB0::0x05E6::0x6500::04446160::INSTR') 
dmm = rm.open_resource('USB0::0x05E6::0x6500::04446160::INSTR')
print(dmm.query('*IDN?'))

dmm.write(":SENSE:FUNCTION 'VOLT:DC'")
dmm.write(":SENSE:VOLT:DC:RANGE 10")
dmm.write(":READ?")
print(dmm.read())
'''

identifyInstr(multimeter)
#measureDCVolt(multimeter)
measureResistance(multimeter)
#dmm.write(":SENSE:FUNCTION 'VOLT:DC'")
#dmm.write(":SENSE:VOLT:DC:RANGE 10")
#dmm.write(":READ?")
#print(dmm.read())
