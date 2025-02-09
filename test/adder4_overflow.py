# top = playground::arith::adder4_overflow
 
import cocotb
from spade import SpadeExt
from cocotb.triggers import Timer

def as_bool_array(num: int, length: int) -> list[bool]:
    binary = bin(num)[2:]
    out = []
    for bit in binary:
        out.insert(0, bit == '1')

    extension = length - len(out)
    out += [False] * extension
    print(out)
    return out

@cocotb.test()
async def test(dut):
    s = SpadeExt(dut) 

    s.i.x = 3
    s.i.y = 5
    await Timer(10, units='ns')
    s.o.result.assert_eq(8)
    s.o.overflow.assert_eq(False)

    s.i.x = 12
    s.i.y = 14
    await Timer(10, units='ns')
    s.o.result.assert_eq(10)
    s.o.overflow.assert_eq(True)
