import re

from utils import Solver, get_data


class Solver2017Day7(Solver):
    YEAR = 2017
    DAY = 7

    def parse(self, src):
        pattern = re.compile(r"^(\w+)\s+\((\d+)\)(?:\s+->\s+(.*))?", re.M)
        ls = pattern.findall(src.strip())
        mp = {}
        for t in ls:
            mp[t[0]] = [int(t[1]), t[2].split(', ') if t[2] else []]
        return mp

    def solve_part_1(self, src):
        mp = self.parse(src)
        s1 = set(mp.keys())
        s2 = set()
        for _, v in mp.values():
            s2 |= set(v)
        return list(s1 - s2)[0]

    def solve_part_2(self, src):
        mp = self.parse(src)
        root = self.solve_part_1(src)
        ans = []

        def dfs(u):
            val = mp[u][0]
            ls = [dfs(v) for v in mp[u][1]]
            if len(set(ls)) == 2:
                for i in range(len(ls)):
                    if ls.count(ls[i]) == 1:
                        aim = (sum(ls) - ls[i]) // (len(ls) - 1)
                        ans.append(mp[mp[u][1][i]][0] + aim - ls[i])
                        ls[i] = aim
                        break
            return val + sum(ls)

        dfs(root)
        return ans[0]

if __name__ == "__main__":
    sol = Solver2017Day7()
    src = get_data(Solver2017Day7.YEAR, Solver2017Day7.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
