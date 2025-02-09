# top = playground::arith::full_adder
 
import cocotb
from spade import SpadeExt
from cocotb.triggers import Timer

@cocotb.test()
async def test(dut):
    s = SpadeExt(dut) 

    s.i.x = False
    s.i.y = False
    s.i.z = False
    await Timer(10, units='ns')
    s.o.sum.assert_eq(False)
    s.o.carry.assert_eq(False)

    s.i.x = True
    s.i.y = False
    s.i.z = False
    await Timer(10, units='ns')
    s.o.sum.assert_eq(True)
    s.o.carry.assert_eq(False)

    s.i.x = False
    s.i.y = True
    s.i.z = False
    await Timer(10, units='ns')
    s.o.sum.assert_eq(True)
    s.o.carry.assert_eq(False)

    s.i.x = False
    s.i.y = False
    s.i.z = True
    await Timer(10, units='ns')
    s.o.sum.assert_eq(True)
    s.o.carry.assert_eq(False)

    s.i.x = True
    s.i.y = True
    s.i.z = False
    await Timer(10, units='ns')
    s.o.sum.assert_eq(False)
    s.o.carry.assert_eq(True)

    s.i.x = True
    s.i.y = False
    s.i.z = True
    await Timer(10, units='ns')
    s.o.sum.assert_eq(False)
    s.o.carry.assert_eq(True)

    s.i.x = False
    s.i.y = True
    s.i.z = True
    await Timer(10, units='ns')
    s.o.sum.assert_eq(False)
    s.o.carry.assert_eq(True)

    s.i.x = True
    s.i.y = True
    s.i.z = True
    await Timer(10, units='ns')
    s.o.sum.assert_eq(True)
    s.o.carry.assert_eq(True)

 
