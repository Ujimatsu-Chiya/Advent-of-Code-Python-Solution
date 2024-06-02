from itertools import pairwise

from utils import Solver, get_data


class Node:
    def __init__(self, x, prev=None, next=None):
        self.val = x
        self.prev = prev
        self.next = next

    def add(self, p):
        l, r = self, self.next
        l.next = r.prev = p
        p.prev = l
        p.next = r

    def pop(self):
        l, r = self.prev, self.next
        l.next = r
        r.prev = l


class Solver2022Day20(Solver):
    YEAR = 2022
    DAY = 20

    def __init__(self, src):
        self.ls = list(map(int, src.strip().split()))

    def _run(self, a, T):
        nodes = [Node(x) for x in a]
        for l, r in pairwise(nodes + [nodes[0]]):
            l.next = r
            r.prev = l
        for _ in range(T):
            for p in nodes:
                l = p.prev
                p.pop()
                step = p.val % (len(nodes) - 1)
                for _ in range(step):
                    l = l.next
                l.add(p)
        p = [node for node in nodes if node.val == 0][0]
        ans = 0
        for _ in range(3):
            for _ in range(1000):
                p = p.next
            ans += p.val
        return ans

    def solve_part_1(self):
        return self._run(self.ls, 1)

    def solve_part_2(self):
        K = 811589153
        return self._run([x * K for x in self.ls], 10)


if __name__ == "__main__":
    src = get_data(Solver2022Day20.YEAR, Solver2022Day20.DAY)
    sol = Solver2022Day20(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
