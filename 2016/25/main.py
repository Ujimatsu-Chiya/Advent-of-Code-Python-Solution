from itertools import count

from utils import Solver, get_data


class Solver2016Day25(Solver):
    YEAR = 2016
    DAY = 25

    def parse(self, src):
        ls = []
        for s in src.strip().split('\n'):
            ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
        return ls

    def _solve(self, vals, ls):
        def get_val(s):
            try:
                return int(s)
            except ValueError:
                return vals[s]

        pos = 0
        pre_val = 1
        cnt = 0
        while 0 <= pos < len(ls):
            # print(pos,vals)
            ins = ls[pos]
            if ins[0] == "inc":
                vals[ins[1]] += 1
                pos += 1
            elif ins[0] == "dec":
                vals[ins[1]] -= 1
                pos += 1
            elif ins[0] == "cpy":
                vals[ins[2]] = get_val(ins[1])
                pos += 1
            elif ins[0] == "jnz":
                if get_val(ins[1]) != 0:
                    pos += get_val(ins[2])
                else:
                    pos += 1
            elif ins[0] == "out":
                v = get_val(ins[1])
                if v != 0 and v != 1:
                    return False
                if pre_val == v:
                    return False
                pre_val = v
                cnt += 1
                if cnt == 10000:
                    return True
                pos += 1
            else:
                assert False

    def solve_part_1(self, src):
        ls = self.parse(src)
        for i in count():
            if self._solve({'a': i}, ls):
                return i

    def solve_part_2(self, src):
        pass


if __name__ == "__main__":
    sol = Solver2016Day25()
    src = get_data(Solver2016Day25.YEAR, Solver2016Day25.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
