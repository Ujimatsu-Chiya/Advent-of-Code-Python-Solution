from utils import Solver, get_data
from collections import defaultdict


class Solver2021Day4(Solver):
    YEAR = 2021
    DAY = 4

    def __init__(self, src):
        ls_str, *mats = src.strip().split("\n\n")
        self.queries = list(map(int, ls_str.split(',')))
        self.mats = [[[int(x) for x in s.split()] for s in t.split('\n')] for t in mats]
        self.ans1 = self.ans2 = None

    def run(self):
        M = 5
        cnt = [[[M for _ in range(M)], [M for _ in range(M)]] for _ in range(len(self.mats))]
        vis = [False for _ in range(len(self.mats))]
        s = []
        pos = defaultdict(list)
        for i, mat in enumerate(self.mats):
            for j in range(M):
                for k in range(M):
                    pos[mat[j][k]].append((i, j, k))
            s.append(sum(sum(v) for v in mat))
        for x in self.queries:
            for i, j, k in pos[x]:
                cnt[i][0][j] -= 1
                cnt[i][1][k] -= 1
                s[i] -= x
                if (cnt[i][0][j] == 0 or cnt[i][1][k] == 0) and not vis[i]:
                    v = s[i] * x
                    if self.ans1 is None:
                        self.ans1 = v
                    self.ans2 = v
                    vis[i]=True

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day4.YEAR, Solver2021Day4.DAY)
    sol = Solver2021Day4(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
