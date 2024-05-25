from collections import deque
from math import prod

from utils import Solver, get_data


class Solver2021Day9(Solver):
    YEAR = 2021
    DAY = 9

    def __init__(self, src):
        self.mp = [[int(ch) for ch in s] for s in src.strip().split()]
        self.ans1 = self.ans2 = None

    def run(self):
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        n, m = len(self.mp), len(self.mp[0])
        self.ans1 = 0
        basin_list = []
        for i in range(n):
            for j in range(m):
                if not any(0 <= i + dx < n and 0 <= j + dy < m and self.mp[i + dx][j + dy] <= self.mp[i][j] for dx, dy in dirs):
                    self.ans1 += self.mp[i][j] + 1
                    st = {(i, j)}
                    q = deque([(i, j)])
                    while len(q) > 0:
                        sx, sy = q.popleft()
                        for dx, dy in dirs:
                            x, y = sx + dx, sy + dy
                            if 0 <= x < n and 0 <= y < m and self.mp[sx][sy] < self.mp[x][y] < 9 and (x, y) not in st:
                                st.add((x, y))
                                q.append((x, y))
                    basin_list.append(len(st))
        basin_list.sort(reverse=True)
        self.ans2 = prod(basin_list[:3])

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day9.YEAR, Solver2021Day9.DAY)
    sol = Solver2021Day9(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
