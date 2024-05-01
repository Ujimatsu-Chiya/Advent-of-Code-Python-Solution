import operator
import re

from utils import Solver, get_data


class Solver2018Day16(Solver):
    YEAR = 2018
    DAY = 16

    def rr_aux(self, reg, op, operation):
        if 0 <= min(op[1:]) and max(op[1:]) < 4:
            reg[op[3]] = int(operation(reg[op[1]], reg[op[2]]))
            return reg
        else:
            return []

    def ri_aux(self, reg, op, operation):
        if 0 <= op[1] < 4 and 0 <= op[3] < 4:
            reg[op[3]] = int(operation(reg[op[1]], op[2]))
            return reg
        else:
            return []

    def ir_aux(self, reg, op, operation):
        if 0 <= op[2] < 4 and 0 <= op[3] < 4:
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
        if 0 <= op[1] < 4 and 0 <= op[3] < 4:
            reg[op[3]] = reg[op[1]]
            return reg
        else:
            return []

    def op_seti(self, reg, op):
        if 0 <= op[3] < 4:
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

    op_list_run = [op_addr, op_addi, op_mulr, op_muli, op_banr, op_bani, op_borr, op_bori, op_setr, op_seti,
                   op_gtir, op_gtri, op_gtrr, op_eqir, op_eqri, op_eqrr]

    def parse(self, src):
        pat1 = re.compile(r"Before: \[([0-9, ]+)\]\n([0-9 ]+)\nAfter:  \[([0-9, ]+)\]")
        ls = []
        for t in pat1.findall(src.strip()):
            ls.append([eval('[' + t[0] + ']'), list(map(int, t[1].split())), eval('[' + t[2] + ']')])
        pat2 = re.compile(r'(\d+) (\d+) (\d+) (\d+)')
        s = src
        while "After" in s:
            s = s[s.find("After") + 1:]
        ops = [list(map(int, match)) for match in pat2.findall(s)]
        return ls, ops

    def solve_part_1(self, src):
        ls, _ = self.parse(src)
        ans = 0
        for before, op, after in ls:
            cnt = 0
            for sim in self.op_list_run:
                if sim(self, before.copy(), op) == after:
                    cnt += 1
            if cnt >= 3:
                ans += 1
        return ans

    def solve_part_2(self, src):
        ls, ops = self.parse(src)
        M = 16
        st_list = [set(self.op_list_run) for _ in range(M)]
        for before, op, after in ls:
            for sim in self.op_list_run:
                if sim(self, before.copy(), op) != after and sim in st_list[op[0]]:
                    st_list[op[0]].remove(sim)
        while not all(len(st) == 1 for st in st_list):
            tmp = set()
            for st in st_list:
                if len(st) == 1:
                    tmp |= st
            for st in st_list:
                for f in tmp:
                    if len(st) > 1 and f in st:
                        st.remove(f)
        mp = [None] * M
        for i in range(M):
            mp[i] = list(st_list[i])[0]

        reg = [0, 0, 0, 0]
        for op in ops:
            reg = mp[op[0]](self, reg, op)
        return reg[0]


if __name__ == "__main__":
    sol = Solver2018Day16()
    src = get_data(Solver2018Day16.YEAR, Solver2018Day16.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
