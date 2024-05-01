from collections import defaultdict
from queue import Queue

from utils import Solver, get_data


class Solver2017Day18(Solver):
    YEAR = 2017
    DAY = 18

    def parse(self, src):
        ls = []
        for s in src.strip().split('\n'):
            ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
        return ls

    def solve_part_1(self, src):
        ls = self.parse(src)
        vals = defaultdict(int)

        def get_val(s):
            try:
                return int(s)
            except ValueError:
                return vals[s]

        pre_sound = 0
        pos = 0
        while 0 <= pos < len(ls):
            ins = ls[pos]
            if ins[0] == "set":
                vals[ins[1]] = get_val(ins[2])
                pos += 1
            elif ins[0] == "add":
                vals[ins[1]] += get_val(ins[2])
                pos += 1
            elif ins[0] == "mul":
                vals[ins[1]] *= get_val(ins[2])
                pos += 1
            elif ins[0] == "mod":
                vals[ins[1]] %= get_val(ins[2])
                pos += 1
            elif ins[0] == "jgz":
                if get_val(ins[1]) > 0:
                    pos += get_val(ins[2])
                else:
                    pos += 1
            elif ins[0] == 'snd':
                pre_sound = get_val(ins[1])
                pos += 1
            elif ins[0] == 'rcv':
                if get_val(ins[1]) != 0:
                    return pre_sound
                pos += 1

    def solve_part_2(self, src):
        ls = self.parse(src)
        q = [Queue(), Queue()]
        vals = [defaultdict(int), defaultdict(int)]
        vals[0]['p'] = 0
        vals[1]['p'] = 1

        def get_val(id, s):
            try:
                return int(s)
            except ValueError:
                return vals[id][s]

        pos = [0, 0]
        cnt = [0, 0]
        id = 0
        while 0 <= pos[0] < len(ls) or 0 <= pos[1] < len(ls):
            if not (0 <= pos[id] < len(ls)):
                id ^= 1
            if q[0].qsize() == q[1].qsize() == 0 and \
                    0 <= pos[0] < len(ls) and ls[pos[0]][0] == "rcv" and \
                    0 <= pos[1] < len(ls) and ls[pos[1]][0] == "rcv":
                break
            ins = ls[pos[id]]
            if ins[0] == "rcv" and q[id ^ 1].qsize() == 0 and not (0 <= pos[id ^ 1] < len(ls)):
                break
            if ins[0] == "set":
                vals[id][ins[1]] = get_val(id, ins[2])
                pos[id] += 1
            elif ins[0] == "add":
                vals[id][ins[1]] += get_val(id, ins[2])
                pos[id] += 1
            elif ins[0] == "mul":
                vals[id][ins[1]] *= get_val(id, ins[2])
                pos[id] += 1
            elif ins[0] == "mod":
                vals[id][ins[1]] %= get_val(id, ins[2])
                pos[id] += 1
            elif ins[0] == "jgz":
                if get_val(id, ins[1]) > 0:
                    pos[id] += get_val(id, ins[2])
                else:
                    pos[id] += 1
            elif ins[0] == 'snd':
                q[id ^ 1].put(get_val(id, ins[1]))
                cnt[id] += 1
                pos[id] += 1
            elif ins[0] == 'rcv':
                if q[id].qsize() == 0:
                    id ^= 1
                else:
                    val = q[id].get()
                    vals[id][ins[1]] = val
                    pos[id] += 1
        return cnt[1]


if __name__ == "__main__":
    sol = Solver2017Day18()
    src = get_data(Solver2017Day18.YEAR, Solver2017Day18.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
