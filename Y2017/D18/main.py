from collections import defaultdict
from queue import Queue

from utils import Solver, get_data


# class Solver2017Day18(Solver):
#     YEAR = 2017
#     DAY = 18
#
#     def __init__(self, src):
#         self.ls = []
#         for s in src.strip().split('\n'):
#             self.ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
#
#     def solve_part_1(self):
#         a = 2 ** 31 - 1
#         p = self.ls[9][2]
#         for i in range(127):
#             p = (p * 8505 * 129749 + 12345) % a
#             b = p % 10000
#         return b
#
#     def solve_part_2(self):
#         ls = self.ls
#         q = [Queue(), Queue()]
#         vals = [defaultdict(int), defaultdict(int)]
#         vals[0]['p'] = 0
#         vals[1]['p'] = 1
#
#         def get_val(id, s):
#             try:
#                 return int(s)
#             except ValueError:
#                 return vals[id][s]
#
#         pos = [0, 0]
#         cnt = [0, 0]
#         id = 0
#         while 0 <= pos[0] < len(ls) or 0 <= pos[1] < len(ls):
#             if not (0 <= pos[id] < len(ls)):
#                 id ^= 1
#             if q[0].qsize() == q[1].qsize() == 0 and \
#                     0 <= pos[0] < len(ls) and ls[pos[0]][0] == "rcv" and \
#                     0 <= pos[1] < len(ls) and ls[pos[1]][0] == "rcv":
#                 break
#             ins = ls[pos[id]]
#             if ins[0] == "rcv" and q[id ^ 1].qsize() == 0 and not (0 <= pos[id ^ 1] < len(ls)):
#                 break
#             if ins[0] == "set":
#                 vals[id][ins[1]] = get_val(id, ins[2])
#                 pos[id] += 1
#             elif ins[0] == "add":
#                 vals[id][ins[1]] += get_val(id, ins[2])
#                 pos[id] += 1
#             elif ins[0] == "mul":
#                 vals[id][ins[1]] *= get_val(id, ins[2])
#                 pos[id] += 1
#             elif ins[0] == "mod":
#                 vals[id][ins[1]] %= get_val(id, ins[2])
#                 pos[id] += 1
#             elif ins[0] == "jgz":
#                 if get_val(id, ins[1]) > 0:
#                     pos[id] += get_val(id, ins[2])
#                 else:
#                     pos[id] += 1
#             elif ins[0] == 'snd':
#                 q[id ^ 1].put(get_val(id, ins[1]))
#                 cnt[id] += 1
#                 pos[id] += 1
#             elif ins[0] == 'rcv':
#                 if q[id].qsize() == 0:
#                     id ^= 1
#                 else:
#                     val = q[id].get()
#                     vals[id][ins[1]] = val
#                     pos[id] += 1
#         return cnt[1]

class Solver2017Day18(Solver):
    YEAR = 2017
    DAY = 18

    def __init__(self, src):
        self.ls = []
        for s in src.strip().split('\n'):
            self.ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
        self.ans1 = self.ans2 = None

    def run(self):
        a = 2 ** 31 - 1
        p = self.ls[9][2]
        ls = []
        for i in range(127):
            p = (p * 8505 * 129749 + 12345) % a
            b = p % 10000
            ls.append(b)
        self.ans1 = ls[-1]
        cnt = 0
        while True:
            cnt += 1
            tmp = []
            ok = True
            k = ls[0]
            for i in range(1, len(ls)):
                if ls[i] > k:
                    tmp.append(ls[i])
                    ok = False
                else:
                    tmp.append(k)
                    k = ls[i]
            tmp.append(k)
            if ok:
                break
            ls = tmp
        self.ans2 = (cnt + 1) // 2 * len(ls)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2017Day18.YEAR, Solver2017Day18.DAY)
    sol = Solver2017Day18(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
