## General Functions for all Test Instruments ##

import pyvisa as visa

rm = visa.ResourceManager()

def identifyInstr(address):
    instr = rm.open_resource(address)  ## Add Error Checking
    print(instr.query('*IDN?\n'))
    

## Multimeter Functions ##
def measureDCVolt(address,range = "AUTO", inp = "AUTO", azer = "ON", nplc = "5", avgFilterType = "MOV", filterCount = "100", filterEnable = "ON" ):
    
    dmm = rm.open_resource(address)
    dmm.clear()
    dmm.write('*RST')
    dmm.write(":SENSE:FUNCTION 'VOLT:DC'")
    dmm.write(":SENSE:VOLT:DC:RANGE " + range)
    dmm.write(":SENSE:VOLT:DC:INP " + inp)
    dmm.write(":SENSE:VOLT:DC:AZER " + azer)
    dmm.write(":SENSE:VOLT:DC:NPLC " + nplc)
    dmm.write(":SENSE:VOLT:DC:AVER:TCON " + avgFilterType)
    dmm.write(":SENSE:VOLT:DC:AVER:COUN " + filterCount)
    dmm.write(":SENSE:VOLT:DC:AVER " + filterEnable)
    dmm.write(":READ?")
    print(dmm.read())

def returnDCVolt(address,range = "AUTO ON", inp = "AUTO", azer = "ON", nplc = "5", avgFilterType = "MOV", filterCount = "100", filterEnable = "ON" ):
    
    dmm = rm.open_resource(address)
    dmm.clear()
    dmm.write('*RST')
    dmm.write(":SENSE:FUNCTION 'VOLT:DC'")
    dmm.write(":SENSE:VOLT:DC:RANGE " + range)
    dmm.write(":SENSE:VOLT:DC:INP " + inp)
    dmm.write(":SENSE:VOLT:DC:AZER " + azer)
    dmm.write(":SENSE:VOLT:DC:NPLC " + nplc)
    dmm.write(":SENSE:VOLT:DC:AVER:TCON " + avgFilterType)
    dmm.write(":SENSE:VOLT:DC:AVER:COUN " + filterCount)
    dmm.write(":SENSE:VOLT:DC:AVER " + filterEnable)
    dmm.write(":READ?")
    voltage = dmm.read()
    return voltage

def measureResistance(address, range = "AUTO ON", offset = "ON", azer = "ON", nplc = "1"):
    dmm = rm.open_resource(address)
    dmm.clear()
    dmm.write('*RST')
    dmm.write(":SENSE:FUNCTION 'FRES'")
    dmm.write(":SENSE:FRES:RANG:  " + range)
    dmm.write(":SENSE:FRES:OCOM " + offset)
    dmm.write(":SENSE:FRES:AZER " + azer)
    dmm.write(":SENSE:FRES:NPLC " + nplc)
    dmm.write(":READ?")
    print(dmm.read())
