from collections import deque
from fractions import Fraction
from math import prod

from utils import Solver, get_data


class Solver2023Day21(Solver):
    YEAR = 2023
    DAY = 21

    def __init__(self, src):
        self.mp = src.strip().split('\n')

    def solve_part_1(self):
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        M = 64
        n, m = len(self.mp), len(self.mp[0])
        sx, sy = -1, -1
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == 'S':
                    sx, sy = i, j
        d = [[-1 for _ in range(m)] for _ in range(n)]
        q = deque([(sx, sy)])
        d[sx][sy] = 0
        while len(q) > 0:
            sx, sy = q.popleft()
            for dx, dy in dirs:
                x, y = sx + dx, sy + dy
                if 0 <= x < n and 0 <= y < m and self.mp[x][y] != '#' and d[x][y] == -1:
                    d[x][y] = d[sx][sy] + 1
                    q.append((x, y))
        ans = 0
        for i in range(n):
            for j in range(m):
                if d[i][j] != -1 and d[i][j] <= M and (M - d[i][j]) % 2 == 0:
                    ans += 1
        return ans

    def solve_part_2(self):
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n, m = len(self.mp), len(self.mp[0])
        sx, sy = -1, -1
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == 'S':
                    sx, sy = i, j
        M = 26501365

        def get_steps_general(steps, sx, sy):
            d = {(sx, sy): 0}
            q = deque([(sx, sy)])
            while len(q) > 0:
                sx, sy = q.popleft()
                if d[sx, sy] > steps:
                    break
                for dx, dy in dirs:
                    x, y = sx + dx, sy + dy
                    if self.mp[x % n][y % m] != '#' and (x, y) not in d.keys():
                        d[x, y] = d[sx, sy] + 1
                        q.append((x, y))
            return {(x, y) for (x, y), v in d.items() if ((steps - v) & 1) == 0}

        def check_diamond():
            reachable = get_steps_general(n // 2, sx, sy)
            x, y = 0, m // 2
            for dx, dy in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
                for i in range(1, n // 2 + 1):
                    x, y = x + dx, y + dy
                    if (x, y) not in reachable:
                        return False
            return True

        def walk_special():
            order = 2
            x = [i * n // 2 for i in range(1, 2 * (order + 1), 2)]
            y = [len(get_steps_general(xi, sx, sy)) for xi in x]
            a = (
                Fraction(
                    prod(M - xj for xj in x if xj != xi),
                    prod(xi - xj for xj in x if xj != xi),
                )
                for xi in x
            )
            return sum(ai * yi for ai, yi in zip(a, y))

        flag = check_diamond() and (n == m) and (n & 1) and (M - n // 2) % n == 0
        assert flag
        return walk_special()


if __name__ == "__main__":
    src = get_data(Solver2023Day21.YEAR, Solver2023Day21.DAY)
    sol = Solver2023Day21(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())