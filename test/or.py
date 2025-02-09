# top = playground::logic::or
 
import cocotb
from spade import SpadeExt
from cocotb.triggers import Timer

@cocotb.test()
async def test(dut):
    s = SpadeExt(dut) 

    s.i.x = False
    s.i.y = False
    await Timer(10, units='ns')
    s.o.assert_eq(False)
    
    s.i.x = True
    s.i.y = False
    await Timer(10, units='ns')
    s.o.assert_eq(True)
    
    s.i.x = False
    s.i.y = True
    await Timer(10, units='ns')
    s.o.assert_eq(True)
    
    s.i.x = True
    s.i.y = True
    await Timer(10, units='ns')
    s.o.assert_eq(True)
 
