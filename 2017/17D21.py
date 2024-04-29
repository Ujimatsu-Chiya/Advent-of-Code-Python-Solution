import requests

from utils import Solver, rotate


class Solver17D21(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/21/input'

    def parse(self, src):
        rule2, rule3 = {}, {}
        for s in src.strip().split('\n'):
            l_str, r_str = s.split(" => ")
            mat = l_str.split('/')
            nxt = tuple(r_str.split('/'))
            rule = rule2 if len(mat) == 2 else rule3
            for _ in range(4):
                rule[tuple(mat)] = nxt
                mat = [v[::-1] for v in mat]
                rule[tuple(mat)] = nxt
                mat.reverse()
                rule[tuple(mat)] = nxt
                mat = [v[::-1] for v in mat]
                rule[tuple(mat)] = nxt
                mat.reverse()
                mat = rotate(mat)
        return rule2, rule3

    def _trans(self, rule2, rule3, a):
        n = len(a)
        if n % 2 == 0:
            block, m, rule = n // 2, 2, rule2
        else:
            block, m, rule = n // 3, 3, rule3
        b = [['' for _ in range(n // m * (m + 1))] for _ in range(n // m * (m + 1))]
        for i in range(block):
            for j in range(block):
                t = tuple(t[m * j:m * (j + 1)] for t in a[m * i: m * (i + 1)])
                t = rule[t]
                for x in range(m + 1):
                    for y in range(m + 1):
                        b[(m + 1) * i + x][(m + 1) * j + y] = t[x][y]
        return ["".join(v) for v in b]

    def solve_part_1(self, src):
        rule2, rule3 = self.parse(src)
        a = ['.#.', '..#', '###']
        for _ in range(5):
            a = self._trans(rule2, rule3, a)
        return sum(s.count('#') for s in a)

    def solve_part_2(self, src):
        rule2, rule3 = self.parse(src)
        a = ['.#.', '..#', '###']
        for _ in range(18):
            a = self._trans(rule2, rule3, a)
        return sum(s.count('#') for s in a)

if __name__ == "__main__":
    sol = Solver17D21()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D21.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
