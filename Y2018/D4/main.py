import re
from collections import Counter, defaultdict

from utils import Solver, get_data


class Solver2018Day4(Solver):
    YEAR = 2018
    DAY = 4

    def __init__(self, src):
        pat = re.compile(
            r"\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (Guard #(\d+) begins shift|falls asleep|wakes up)")
        self.schedule = []
        for t in pat.findall("\n".join(sorted(src.strip().split('\n')))):
            self.schedule.append([int(t[4]), t[5] if len(t[6]) == 0 else int(t[6])])
        self.ans1 = self.ans2 = None

    def run(self):
        mp = defaultdict(list)
        id = -1
        pre = -1
        for tm, op in self.schedule:
            if isinstance(op, int):
                id = op
            elif op == 'falls asleep':
                pre = tm
            else:
                mp[id] += list(range(pre, tm))
        a = sorted([[len(v), k] for k, v in mp.items()], reverse=True)
        id = a[0][1]
        self.ans1 = Counter(mp[id]).most_common(1)[0][0] * id
        a = sorted([[*list(reversed(Counter(v).most_common(1)[0])), k] for k, v in mp.items()], reverse=True)
        self.ans2 = a[0][1] * a[0][2]

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day4.YEAR, Solver2018Day4.DAY)
    sol = Solver2018Day4(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
