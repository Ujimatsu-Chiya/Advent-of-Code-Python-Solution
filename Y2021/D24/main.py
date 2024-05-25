from utils import Solver, get_data
from functools import partial


# class Solver2021Day24(Solver):
#     YEAR = 2021
#     DAY = 24
#
#     def __init__(self, src):
#         self.ops = []
#         for s in src.strip().split('\n'):
#             self.ops.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
#
#     def solve_part_1(self):
#         T = self.ops.index(['inp', 'w'], 1)
#
#         def f(w, z, v0, v1, v2):
#             x = int(z % 26 + v1 != w)
#             return z // v0 * (25 * x + 1) + (w + v2) * x
#
#         f_list = []
#         for i in range(len(self.ops) // T):
#             ops = self.ops[T * i:T * i + T]
#             f = partial(f, v0=ops[4][2], v1=ops[5][2], v2=ops[15][2])
#             f_list.append(f)
#         mp = {0: 0}
#         for f in f_list:
#             mq = {}
#             for z, num in sorted(mp.items(), reverse=True):
#                 for w in range(9, 0, -1):
#                     new_num = num * 10 + w
#                     new_z = f(w, z)
#                     if new_z not in mq.keys() or new_num < mq[new_z]:
#                         mq[new_z] = new_num
#             mp = mq
#         return mp[0]
#
#     def solve_part_2(self):
#         pass

class Solver2021Day24(Solver):
    YEAR = 2021
    DAY = 24

    def __init__(self, src):
        self.ops = []
        for s in src.strip().split('\n'):
            self.ops.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
        self.ans1 = self.ans2 = None

    def run(self):
        M = 14
        a1 = [None] * M
        a2 = [None] * M
        T = self.ops.index(['inp', 'w'], 1)
        st = []
        for i in range(len(self.ops) // T):
            ops = self.ops[T * i:T * i + T]
            if ops[4][-1] == 1:
                st.append((i, ops[15][-1]))
            else:
                j, v = st.pop()
                v += ops[5][-1]
                if v > 0:
                    a1[i], a1[j] = 9, 9 - v
                    a2[i], a2[j] = v + 1, 1
                else:
                    a1[i], a1[j] = 9 + v, 9
                    a2[i], a2[j] = 1, 1 - v
        self.ans1 = "".join(str(v) for v in a1)
        self.ans2 = "".join(str(v) for v in a2)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day24.YEAR, Solver2021Day24.DAY)
    sol = Solver2021Day24(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
