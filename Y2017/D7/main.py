import re

from utils import Solver, get_data


class Solver2017Day7(Solver):
    YEAR = 2017
    DAY = 7

    def __init__(self, src):
        pattern = re.compile(r"^(\w+)\s+\((\d+)\)(?:\s+->\s+(.*))?", re.M)
        ls = pattern.findall(src.strip())
        self.mp = {t[0]: [int(t[1]), t[2].split(', ') if t[2] else []] for t in ls}
        self.ans1 = self.ans2 = None

    def run(self):
        s1 = set(self.mp.keys())
        s2 = set()
        for _, v in self.mp.values():
            s2 |= set(v)
        self.ans1 = root = list(s1 - s2)[0]
        ans = []

        def dfs(u):
            val = self.mp[u][0]
            ls = [dfs(v) for v in self.mp[u][1]]
            if len(set(ls)) == 2:
                for i in range(len(ls)):
                    if ls.count(ls[i]) == 1:
                        aim = (sum(ls) - ls[i]) // (len(ls) - 1)
                        ans.append(self.mp[self.mp[u][1][i]][0] + aim - ls[i])
                        ls[i] = aim
                        break
            return val + sum(ls)

        dfs(root)
        self.ans2 = ans[0]

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2017Day7.YEAR, Solver2017Day7.DAY)
    sol = Solver2017Day7(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
