import re
from math import prod

from utils import Solver, get_data


class Solver2022Day11(Solver):
    YEAR = 2022
    DAY = 11

    def __init__(self, src):
        pat = re.compile(
            r'Monkey (\d+):\n\s+Starting items: ([\d, ]+)\n\s+Operation: (.+?)\n\s+Test: divisible by (\d+)\n\s+If true: throw to monkey (\d+)\n\s+If false: throw to monkey (\d+)')
        self.info = []
        for match in pat.findall(src.strip()):
            mp = {'start': list(map(int, match[1].split(', ')))}
            s = "lambda old: {}".format(match[2][6:])
            mp['func'] = eval(s)
            mp['div'] = int(match[3])
            mp['tran'] = (int(match[5]), int(match[4]))
            self.info.append(mp)

    def solve_part_1(self):
        items = [mp['start'].copy() for mp in self.info]
        n = len(items)
        cnt = [0 for _ in range(n)]
        T = 20
        for t in range(T):
            for i, info in enumerate(self.info):
                cnt[i] += len(items[i])
                for x in items[i]:
                    y = info['func'](x) // 3
                    items[info['tran'][y % info['div'] == 0]].append(y)
                items[i] = []
        return prod(sorted(cnt)[-2:])

    def solve_part_2(self):
        items = [mp['start'].copy() for mp in self.info]
        mod = prod(mp['div'] for mp in self.info)
        n = len(items)
        cnt = [0 for _ in range(n)]
        T = 10000
        for t in range(T):
            for i, info in enumerate(self.info):
                cnt[i] += len(items[i])
                for x in items[i]:
                    y = info['func'](x) % mod
                    items[info['tran'][y % info['div'] == 0]].append(y)
                items[i] = []
        return prod(sorted(cnt)[-2:])


if __name__ == "__main__":
    src = get_data(Solver2022Day11.YEAR, Solver2022Day11.DAY)
    sol = Solver2022Day11(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
