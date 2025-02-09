# top = playground::arith::adder4
 
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

    s.i.x = as_bool_array(3, 4)
    s.i.y = as_bool_array(5, 4)
    await Timer(10, units='ns')
    s.o.assert_eq(as_bool_array(8, 5))
