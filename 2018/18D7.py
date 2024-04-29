import re
from collections import Counter, defaultdict
from queue import Queue, PriorityQueue

import numpy as np
import requests

from utils import Solver


class Solver18D7(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/7/input'

    def parse(self, src):
        pat = re.compile(r"Step (\w) must be finished before step (\w) can begin\.")
        mp = defaultdict(list)
        nodes = set()
        for s, t in pat.findall(src.strip()):
            mp[s].append(t)
            nodes |= {s, t}
        return nodes, mp

    def solve_part_1(self, src):
        nodes, mp = self.parse(src)
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

    def solve_part_2(self, src):
        nodes, mp = self.parse(src)
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

        tm = 0
        M = 5
        workers = [0 for _ in range(M)]
        job = [None for _ in range(M)]
        while q.qsize() > 0 or max(workers) > 0:
            workers = [max(w - 1, 0) for w in workers]
            nxt = []
            for i in range(len(workers)):
                if workers[i] == 0:
                    if job[i] is not None:
                        for v in mp[job[i]]:
                            deg[v] -= 1
                            if deg[v] == 0:
                                nxt.append(v)
                        job[i] = None
                    if q.qsize() > 0:
                        u = q.get()
                        job[i] = u
                        workers[i] = cost[u]
            for ch in nxt:
                q.put(ch)
            tm += 1
        return tm


if __name__ == "__main__":
    sol = Solver18D7()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D7.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
