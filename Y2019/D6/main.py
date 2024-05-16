from collections import defaultdict
from queue import Queue

from utils import Solver, get_data


class Solver2019Day6(Solver):
    YEAR = 2019
    DAY = 6

    def __init__(self, src):
        self.mp = defaultdict(list)
        for s in src.strip().split():
            l, r = s.split(')')
            self.mp[l].append(r)
            self.mp[r].append(l)

    def solve_part_1(self):
        ans = 0

        def dfs(u, fa, d):
            nonlocal ans
            ans += d
            for v in self.mp[u]:
                if v != fa:
                    dfs(v, u, d + 1)

        dfs("COM", "", 0)
        return ans

    def solve_part_2(self):
        q = Queue()
        d = defaultdict(int)
        st, ed = "YOU", "SAN"
        d[st] = 0
        q.put(st)
        while not q.empty():
            u = q.get()
            for v in self.mp[u]:
                if v not in d.keys():
                    d[v] = d[u] + 1
                    q.put(v)
        return d[ed] - 2


if __name__ == "__main__":
    src = get_data(Solver2019Day6.YEAR, Solver2019Day6.DAY)
    sol = Solver2019Day6(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
