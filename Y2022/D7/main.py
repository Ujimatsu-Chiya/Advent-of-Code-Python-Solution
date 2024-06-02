from utils import Solver, get_data
from collections import defaultdict


class Solver2022Day7(Solver):
    YEAR = 2022
    DAY = 7

    def __init__(self, src):
        path = []
        self.files = defaultdict(set)
        self.system = defaultdict(set)
        ls = src.strip().split('\n')
        for i, s in enumerate(ls):
            if not s.startswith('$'):
                continue
            vals = s.split()[1:]
            if vals[0] == 'cd':
                param = vals[1]
                if param == "..":
                    if len(path) > 0:
                        path.pop()
                elif param == '/':
                    path = []
                else:
                    path.append(param)
            else:
                j = i + 1
                while j < len(ls) and not ls[j].startswith('$'):
                    tp, name = ls[j].split()
                    if tp == 'dir':
                        self.system[tuple(path)].add(tuple(path + [name]))
                    else:
                        self.files[tuple(path)].add((int(tp), name))
                    j += 1
        self.ans1 = self.ans2 = None

    def run(self):
        self.ans1 = 0
        M = 100000
        sz_list = []

        def dfs(path):
            sz = sum(v[0] for v in self.files[path]) + sum(dfs(next_path) for next_path in self.system[path])
            if sz <= M:
                self.ans1 += sz
            sz_list.append(sz)
            return sz

        cost = dfs(tuple())
        total = 70000000
        need = 30000000
        self.ans2 = min(x for x in sz_list if total - cost + x >= need)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2022Day7.YEAR, Solver2022Day7.DAY)
    sol = Solver2022Day7(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
