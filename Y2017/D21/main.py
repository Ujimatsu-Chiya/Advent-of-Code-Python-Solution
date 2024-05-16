from utils import Solver, get_data
from tools import rotate_str


class Solver2017Day21(Solver):
    YEAR = 2017
    DAY = 21

    def __init__(self, src):
        self.rule2, self.rule3 = {}, {}
        for s in src.strip().split('\n'):
            l_str, r_str = s.split(" => ")
            mat = l_str.split('/')
            nxt = tuple(r_str.split('/'))
            rule = self.rule2 if len(mat) == 2 else self.rule3
            for _ in range(4):
                rule[tuple(mat)] = nxt
                mat = [v[::-1] for v in mat]
                rule[tuple(mat)] = nxt
                mat.reverse()
                rule[tuple(mat)] = nxt
                mat = [v[::-1] for v in mat]
                rule[tuple(mat)] = nxt
                mat.reverse()
                mat = rotate_str(mat)
        self.ans1 = self.ans2 = None

    def _trans(self, a):
        n = len(a)
        if n % 2 == 0:
            block, m, rule = n // 2, 2, self.rule2
        else:
            block, m, rule = n // 3, 3, self.rule3
        b = [['' for _ in range(n // m * (m + 1))] for _ in range(n // m * (m + 1))]
        for i in range(block):
            for j in range(block):
                t = tuple(t[m * j:m * (j + 1)] for t in a[m * i: m * (i + 1)])
                t = rule[t]
                for x in range(m + 1):
                    for y in range(m + 1):
                        b[(m + 1) * i + x][(m + 1) * j + y] = t[x][y]
        return ["".join(v) for v in b]

    def run(self):
        N, M = 5, 18
        a = ['.#.', '..#', '###']
        for _ in range(N):
            a = self._trans(a)
        self.ans1 = sum(s.count('#') for s in a)
        for _ in range(M - N):
            a = self._trans(a)
        self.ans2 = sum(s.count('#') for s in a)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2017Day21.YEAR, Solver2017Day21.DAY)
    sol = Solver2017Day21(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
