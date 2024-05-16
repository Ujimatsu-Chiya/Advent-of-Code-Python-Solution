import re
from collections import defaultdict
from queue import PriorityQueue

from utils import Solver, get_data


class Solver2018Day7(Solver):
    YEAR = 2018
    DAY = 7

    def __init__(self, src):
        pat = re.compile(r"Step (\w) must be finished before step (\w) can begin\.")
        mp = defaultdict(list)
        nodes = set()
        for s, t in pat.findall(src.strip()):
            mp[s].append(t)
            nodes |= {s, t}
        self.queries = nodes, mp

    def solve_part_1(self):
        nodes, mp = self.queries
        deg = defaultdict(int)
        for v in mp.values():
            for s in v:
                deg[s] += 1
        ans = ''
        q = PriorityQueue()
        for ch in nodes:
            if deg[ch] == 0:
                q.put(ch)
        while q.qsize() > 0:
            u = q.get()
            ans += u
            for v in mp[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.put(v)
        return ans

    def solve_part_2(self):
        nodes, mp = self.queries
        deg = defaultdict(int)
        for v in mp.values():
            for s in v:
                deg[s] += 1
        cost = {}
        for ch in nodes:
            cost[ch] = ord(ch) - ord('A') + 60
        q = PriorityQueue()
        for ch in nodes:
            if deg[ch] == 0:
                q.put(ch)
        running = PriorityQueue()
        tm = 0
        M = 5
        while q.qsize() > 0 or running.qsize() > 0:
            while running.qsize() > 0 and running.queue[0][0] <= tm:
                t, u = running.get()
                for v in mp[u]:
                    deg[v] -= 1
                    if deg[v] == 0:
                        q.put(v)
            while running.qsize() < M and q.qsize() > 0:
                ch = q.get()
                running.put((tm + cost[ch] + 1, ch))
            if running.qsize() > 0:
                tm = running.queue[0][0]
        return tm


if __name__ == "__main__":
    src = get_data(Solver2018Day7.YEAR, Solver2018Day7.DAY)
    sol = Solver2018Day7(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
