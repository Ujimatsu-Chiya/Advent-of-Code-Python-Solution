import re
from math import prod

from utils import Solver, get_data


class Solver2022Day19(Solver):
    YEAR = 2022
    DAY = 19

    def __init__(self, src):
        pat = re.compile(
            r"Blueprint (\d+): Each ore robot costs (\d+) ore\. Each clay robot costs (\d+) ore\. Each obsidian robot "
            r"costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian\.")
        self.bots = [list(map(int, v))[1:] for v in pat.findall(src.strip())]

    def _run(self, tm, cost):
        ans = 0
        comb2 = [(t - 1) * t // 2 for t in range(tm + 1)]
        mx = [max(cost[0], cost[1], cost[2], cost[4]), cost[3], cost[5]]

        def dfs(tm, id, cnt, bag):
            nonlocal ans
            if id == 0 and cnt[0] >= mx[0] or \
                    id == 1 and cnt[1] >= mx[1] or \
                    id == 2 and (cnt[2] >= mx[2] or cnt[1] == 0) or \
                    id == 3 and cnt[2] == 0 or \
                    bag[3] + cnt[3] * tm + comb2[tm] <= ans:
                return
            for t in range(tm, 0, -1):
                if id == 0 and bag[0] >= cost[0]:
                    next_bag = list(b + c for b, c in zip(bag, cnt))
                    next_bag[0] -= cost[0]
                    for next_id in range(4):
                        dfs(t - 1, next_id, [cnt[0] + 1, cnt[1], cnt[2], cnt[3]], next_bag)
                    return
                if id == 1 and bag[0] >= cost[1]:
                    next_bag = list(b + c for b, c in zip(bag, cnt))
                    next_bag[0] -= cost[1]
                    for next_id in range(4):
                        dfs(t - 1, next_id, [cnt[0], cnt[1] + 1, cnt[2], cnt[3]], next_bag)
                    return
                if id == 2 and bag[0] >= cost[2] and bag[1] >= cost[3]:
                    next_bag = list(b + c for b, c in zip(bag, cnt))
                    next_bag[0] -= cost[2]
                    next_bag[1] -= cost[3]
                    for next_id in range(4):
                        dfs(t - 1, next_id, [cnt[0], cnt[1], cnt[2] + 1, cnt[3]], next_bag)
                    return
                if id == 3 and bag[0] >= cost[4] and bag[2] >= cost[5]:
                    next_bag = list(b + c for b, c in zip(bag, cnt))
                    next_bag[0] -= cost[4]
                    next_bag[2] -= cost[5]
                    for next_id in range(4):
                        dfs(t - 1, next_id, [cnt[0], cnt[1], cnt[2], cnt[3] + 1], next_bag)
                    return
                bag = list(b + c for b, c in zip(bag, cnt))
            ans = max(ans, bag[3])

        for id in range(4):
            dfs(tm, id, [1, 0, 0, 0], [0, 0, 0, 0])
        return ans

    def solve_part_1(self):
        ans = 0
        for i, cost in enumerate(self.bots):
            ans += (i + 1) * self._run(24, cost)
        return ans

    def solve_part_2(self):
        return prod(self._run(32, cost) for cost in self.bots[:3])


if __name__ == "__main__":
    src = get_data(Solver2022Day19.YEAR, Solver2022Day19.DAY)
    sol = Solver2022Day19(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
