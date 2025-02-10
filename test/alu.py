# top = alu::alu
 
import cocotb
from spade import SpadeExt
from cocotb.triggers import Timer

@cocotb.test()
async def test(dut):
    s = SpadeExt(dut) 

    s.i.x = 3
    s.i.y = 5
    s.i.op = "Operation::Add"
    await Timer(10, units='ns')
    s.o.assert_eq(8)

    s.i.x = 3
    s.i.y = 5
    s.i.op = "Operation::Sub"
    await Timer(10, units='ns')
    s.o.assert_eq(- 2)

    s.i.x = 3
    s.i.y = 5
    s.i.op = "Operation::Sub"
    await Timer(10, units='ns')
    s.o.assert_eq(-2)

    s.i.x = 3
    s.i.y = 5
    s.i.op = "Operation::And"
    await Timer(10, units='ns')
    s.o.assert_eq(0b1)

    s.i.x = 3
    s.i.y = 5
    s.i.op = "Operation::Or"
    await Timer(10, units='ns')
    s.o.assert_eq(0b111)

    s.i.x = 3
    s.i.y = 5
    s.i.op = "Operation::Xor"
    await Timer(10, units='ns')
    s.o.assert_eq(0b110)

    s.i.x = 3
    s.i.y = 5
    s.i.op = "Operation::Sll"
    await Timer(10, units='ns')
    s.o.assert_eq(3 << 5)

    s.i.x = 3
    s.i.y = 5
    s.i.op = "Operation::Srl"
    await Timer(10, units='ns')
    s.o.assert_eq(3 >> 5)

    s.i.x = -3
    s.i.y = 5
    s.i.op = "Operation::Sra"
    await Timer(10, units='ns')
    s.o.assert_eq(-3 >> 5)

    s.i.x = -3
    s.i.y = 5
    s.i.op = "Operation::Slt"
    await Timer(10, units='ns')
    s.o.assert_eq(1)

    s.i.x = -3
    s.i.y = 5
    s.i.op = "Operation::Sltu"
    await Timer(10, units='ns')
    s.o.assert_eq(0)

    s.i.x = 3
    s.i.y = 5
    s.i.op = "Operation::Xnor"
    await Timer(10, units='ns')
    s.o.assert_eq(~(0b110))

