from collections import defaultdict, deque
from itertools import count
from math import lcm

from utils import Solver, get_data

from copy import deepcopy


class Solver2023Day20(Solver):
    YEAR = 2023
    DAY = 20

    def __init__(self, src):
        self.g = {}
        self.flip_flop = {}
        self.memory = {}
        for s in src.strip().split('\n'):
            key, val_str = s.split(' -> ')
            vals = val_str.split(', ')
            id = key.lstrip('%&')
            self.g[id] = vals
            if key[0] == '%':
                self.flip_flop[id] = 0
            elif key[0] == '&':
                self.memory[id] = {}
        for pre, now in self.g.items():
            for c in now:
                if c in self.memory.keys():
                    self.memory[c][pre] = 0

    def solve_part_1(self):
        main = 0
        begin = 'broadcaster'
        T = 1000
        flip_flop, memory = deepcopy(self.flip_flop), deepcopy(self.memory)
        cnt = [0, 0]
        for _ in range(T):
            cnt[0] += 1
            q = deque([[begin, ip, main] for ip in self.g[begin]])
            while len(q) > 0:
                pre, now, val = q.popleft()
                cnt[val] += 1
                if now in flip_flop.keys() and val == 0:
                    flip_flop[now] ^= 1
                    new_val = flip_flop[now]
                elif now in memory.keys():
                    memory[now][pre] = val
                    new_val = int(0 in memory[now].values())
                else:
                    continue
                q.extend([[now, future, new_val] for future in self.g[now]])
        return cnt[0] * cnt[1]

    def solve_part_2(self):
        main = 0
        begin = 'broadcaster'
        flip_flop, memory = deepcopy(self.flip_flop), deepcopy(self.memory)
        l1 = [pre for pre in self.g.keys() if 'rx' in self.g[pre]]
        assert len(l1) == 1 and l1[0] in memory.keys()
        l2 = {pre for pre in self.g.keys() if l1[0] in self.g[pre]}
        cycles = []
        for T in count(1):
            q = deque([[begin, ip, main] for ip in self.g[begin]])
            while len(q) > 0:
                pre, now, val = q.popleft()
                if now in flip_flop.keys() and val == 0:
                    flip_flop[now] ^= 1
                    new_val = flip_flop[now]
                elif now in memory.keys():
                    memory[now][pre] = val
                    new_val = int(0 in memory[now].values())
                    if now in l2 and new_val == 1:
                        cycles.append(T)
                        l2.remove(now)
                else:
                    continue
                q.extend([[now, future, new_val] for future in self.g[now]])
            if len(l2) == 0:
                break
        return lcm(*cycles)


if __name__ == "__main__":
    src = get_data(Solver2023Day20.YEAR, Solver2023Day20.DAY)
    sol = Solver2023Day20(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
