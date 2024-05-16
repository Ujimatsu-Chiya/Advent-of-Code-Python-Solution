from itertools import count

from utils import Solver, get_data


class Solver2016Day25(Solver):
    YEAR = 2016
    DAY = 25

    def __init__(self, src):
        self.ls = [list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())) for s in src.strip().split('\n')]

    # def _solve(self, vals, ls):
    #     def get_val(s):
    #         try:
    #             return int(s)
    #         except ValueError:
    #             return vals[s]
    #
    #     pos = 0
    #     pre_val = 1
    #     cnt = 0
    #     while 0 <= pos < len(ls):
    #         if pos == 20:
    #             print(vals)
    #             return False
    #         ins = ls[pos]
    #         if ins[0] == "inc":
    #             vals[ins[1]] += 1
    #             pos += 1
    #         elif ins[0] == "dec":
    #             vals[ins[1]] -= 1
    #             pos += 1
    #         elif ins[0] == "cpy":
    #             vals[ins[2]] = get_val(ins[1])
    #             pos += 1
    #         elif ins[0] == "jnz":
    #             if get_val(ins[1]) != 0:
    #                 pos += get_val(ins[2])
    #             else:
    #                 pos += 1
    #         elif ins[0] == "out":
    #             v = get_val(ins[1])
    #             if v != 0 and v != 1:
    #                 return False
    #             if pre_val == v:
    #                 return False
    #             pre_val = v
    #             cnt += 1
    #             if cnt == 1000:
    #                 return True
    #             pos += 1
    #         else:
    #             assert False

    # def solve_part_1(self):
    #     for i in count():
    #         if self._solve({'a': i}, self.ls):
    #             return i
    def solve_part_1(self):
        x = self.ls[1][1] * self.ls[2][1]
        for i in count(1):
            y = int("10" * i, 2)
            if y > x:
                return y - x

    def solve_part_2(self):
        pass


if __name__ == "__main__":
    src = get_data(Solver2016Day25.YEAR, Solver2016Day25.DAY)
    sol = Solver2016Day25(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
