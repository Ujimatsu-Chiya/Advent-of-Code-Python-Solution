from utils import Solver, get_data


# class Solver2016Day12(Solver):
#     YEAR = 2016
#     DAY = 12
#
#     def __init__(self, src):
#         self.ls = []
#         for s in src.strip().split('\n'):
#             self.ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
#
#     def _run(self, val, ls):
#         pos = 0
#         while 0 <= pos < len(ls):
#             ins = ls[pos]
#             if ins[0] == 'cpy':
#                 if isinstance(ins[1], int):
#                     val[ins[2]] = ins[1]
#                 else:
#                     val[ins[2]] = val[ins[1]]
#                 pos += 1
#             elif ins[0] == 'inc':
#                 val[ins[1]] += 1
#                 pos += 1
#             elif ins[0] == 'dec':
#                 val[ins[1]] -= 1
#                 pos += 1
#             elif ins[0] == 'jnz':
#                 if isinstance(ins[1], int) and ins[1] != 0 or not isinstance(ins[1], int) and val[ins[1]] != 0:
#                     pos += ins[2]
#                 else:
#                     pos += 1
#         return val
#
#     def solve_part_1(self):
#         val = {ch: 0 for ch in 'abcd'}
#         return self._run(val, self.ls)['a']
#
#     def solve_part_2(self):
#         val = {ch: 0 for ch in 'abd'}
#         val['c'] = 1
#         return self._run(val, self.ls)['a']

class Solver2016Day12(Solver):
    YEAR = 2016
    DAY = 12

    def __init__(self, src):
        self.ls = []
        for s in src.strip().split('\n'):
            self.ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))

    def _run(self, c):
        a = b = 1
        d = 26
        if c != 0:
            d += 7
        for i in range(d):
            a, b = a + b, a
        c = self.ls[16][1]
        d = self.ls[17][1]
        a = a + d * c
        return a

    def solve_part_1(self):
        return self._run(0)

    def solve_part_2(self):
        return self._run(1)


if __name__ == "__main__":
    src = get_data(Solver2016Day12.YEAR, Solver2016Day12.DAY)
    sol = Solver2016Day12(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
