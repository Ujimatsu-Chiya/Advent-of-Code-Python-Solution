from utils import Solver, get_data
from tools import is_prime

# class Solver2017Day23(Solver):
#     YEAR = 2017
#     DAY = 23
#
#     def __init__(self, src):
#         self.ops = []
#         for s in src.strip().split('\n'):
#             self.ops.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
#
#     def _solve(self, vals, ls):
#         def get_val(s):
#             try:
#                 return int(s)
#             except ValueError:
#                 return vals[s]
#
#         pos = 0
#         cnt = 0
#         while 0 <= pos < len(ls):
#             ins = ls[pos]
#             if ins[0] == "set":
#                 vals[ins[1]] = get_val(ins[2])
#                 pos += 1
#             elif ins[0] == "sub":
#                 vals[ins[1]] -= get_val(ins[2])
#                 pos += 1
#             elif ins[0] == "mul":
#                 vals[ins[1]] *= get_val(ins[2])
#                 cnt += 1
#                 pos += 1
#             elif ins[0] == "jnz":
#                 if get_val(ins[1]) != 0:
#                     pos += get_val(ins[2])
#                 else:
#                     pos += 1
#         return vals, cnt
#
#     def solve_part_1(self):
#         vals = {ch: 0 for ch in 'abcdefgh'}
#         return self._solve(vals, self.ops)[1]
#
#     def solve_part_2(self):
#         # https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/
#         b = self.ops[0][2]
#         b = 100 * b + 100000
#         c = b + 17000
#         h = 0
#         for i in range(b, c + 1, 17):
#             if not is_prime(i):
#                 h += 1
#         return h


class Solver2017Day23(Solver):
    YEAR = 2017
    DAY = 23

    def __init__(self, src):
        self.ops = []
        for s in src.strip().split('\n'):
            self.ops.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))

    def solve_part_1(self):
        b = self.ops[0][2]
        return (b - 2) ** 2

    def solve_part_2(self):
        b = self.ops[0][2]
        b = 100 * b + 100000
        c = b + 17000
        h = 0
        for i in range(b, c + 1, 17):
            if not is_prime(i):
                h += 1
        return h


if __name__ == "__main__":
    src = get_data(Solver2017Day23.YEAR, Solver2017Day23.DAY)
    sol = Solver2017Day23(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())