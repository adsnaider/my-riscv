# top = playground::logic::not
 
import cocotb
from spade import SpadeExt
from cocotb.triggers import Timer

@cocotb.test()
async def test(dut):
    s = SpadeExt(dut) 

    s.i.x = False
    await Timer(10, units='ns')
    s.o.assert_eq(True)

    s.i.x = True
    await Timer(10, units='ns')
    s.o.assert_eq(False)
    
