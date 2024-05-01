import operator
import re

from utils import Solver, get_data, divisors_sigma


class Solver2018Day19(Solver):
    YEAR = 2018
    DAY = 19

    def rr_aux(self, reg, op, operation):
        if 0 <= min(op[1:]) and max(op[1:]) < 6:
            reg[op[3]] = int(operation(reg[op[1]], reg[op[2]]))
            return reg
        else:
            return []

    def ri_aux(self, reg, op, operation):
        if 0 <= op[1] < 6 and 0 <= op[3] < 6:
            reg[op[3]] = int(operation(reg[op[1]], op[2]))
            return reg
        else:
            return []

    def ir_aux(self, reg, op, operation):
        if 0 <= op[2] < 6 and 0 <= op[3] < 6:
            reg[op[3]] = int(operation(op[1], reg[op[2]]))
            return reg
        else:
            return []

    def op_addr(self, reg, op):
        return self.rr_aux(reg, op, operator.add)

    def op_addi(self, reg, op):
        return self.ri_aux(reg, op, operator.add)

    def op_mulr(self, reg, op):
        return self.rr_aux(reg, op, operator.mul)

    def op_muli(self, reg, op):
        return self.ri_aux(reg, op, operator.mul)

    def op_banr(self, reg, op):
        return self.rr_aux(reg, op, operator.and_)

    def op_bani(self, reg, op):
        return self.ri_aux(reg, op, operator.and_)

    def op_borr(self, reg, op):
        return self.rr_aux(reg, op, operator.or_)

    def op_bori(self, reg, op):
        return self.ri_aux(reg, op, operator.or_)

    def op_setr(self, reg, op):
        if 0 <= op[1] < 6 and 0 <= op[3] < 6:
            reg[op[3]] = reg[op[1]]
            return reg
        else:
            return []

    def op_seti(self, reg, op):
        if 0 <= op[3] < 6:
            reg[op[3]] = op[1]
            return reg
        else:
            return []

    def op_gtir(self, reg, op):
        return self.ir_aux(reg, op, operator.gt)

    def op_gtri(self, reg, op):
        return self.ri_aux(reg, op, operator.gt)

    def op_gtrr(self, reg, op):
        return self.rr_aux(reg, op, operator.gt)

    def op_eqir(self, reg, op):
        return self.ir_aux(reg, op, operator.eq)

    def op_eqri(self, reg, op):
        return self.ri_aux(reg, op, operator.eq)

    def op_eqrr(self, reg, op):
        return self.rr_aux(reg, op, operator.eq)

    op_list_run = {'addr': op_addr, 'addi': op_addi, 'mulr': op_mulr, 'muli': op_muli, 'banr': op_banr, 'bani': op_bani,
                   'borr': op_borr, 'bori': op_bori, 'setr': op_setr, 'seti': op_seti, 'gtir': op_gtir, 'gtri': op_gtri,
                   'gtrr': op_gtrr, 'eqir': op_eqir, 'eqri': op_eqri, 'eqrr': op_eqrr}

    def parse(self, src):
        pat1 = re.compile(r'(\w+) (\d+) (\d+) (\d+)')
        ls = []
        for tp in pat1.findall(src.strip()):
            ls.append([tp[0]] + list(map(int, tp[1:])))
        pat2 = re.compile(r'#ip (\d+)')
        ip = int(pat2.findall(src.strip())[0])
        return ip, ls

    def solve_part_1(self, src):
        ip, ls = self.parse(src)
        reg = [0 for _ in range(6)]
        while 0 <= reg[ip] < len(ls):
            ins = ls[reg[ip]]
            reg = self.op_list_run[ins[0]](self, reg, ins)
            reg[ip] += 1
        return reg[0]

    def solve_part_2(self, src):
        # https://dev.to/rpalo/aoc-day-19-go-with-the-flow-43ai
        ip, ls = self.parse(src)
        reg = [0 for _ in range(6)]
        reg[0] = 1
        for _ in range(100):
            ins = ls[reg[ip]]
            reg = self.op_list_run[ins[0]](self, reg, ins)
            reg[ip] += 1
        x = reg[(ip + 1) % 6]
        return divisors_sigma(x)


if __name__ == "__main__":
    sol = Solver2018Day19()
    src = get_data(Solver2018Day19.YEAR, Solver2018Day19.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
