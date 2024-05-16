import re

from utils import Solver, get_data


class Solver2015Day14(Solver):
    YEAR = 2015
    DAY = 14

    def __init__(self, src):
        pat = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds")
        self.reindeers = [[int(spd), int(t1), int(t2)] for _, spd, t1, t2 in pat.findall(src.strip())]

    def solve_part_1(self):
        M = 2503
        return max((M // (t1 + t2) * t1 + min(M % (t1 + t2), t1)) * spd for spd, t1, t2 in self.reindeers)

    def solve_part_2(self):
        M = 2503
        n = len(self.reindeers)
        score = [0 for _ in range(n)]
        dis = [0 for _ in range(n)]
        for i in range(M):
            for j in range(n):
                if i % (self.reindeers[j][1] + self.reindeers[j][2]) < self.reindeers[j][1]:
                    dis[j] += self.reindeers[j][0]
            mx = max(dis)
            score = [score[i] + 1 if dis[i] == mx else score[i] for i in range(n)]
        return max(score)


if __name__ == "__main__":
    src = get_data(Solver2015Day14.YEAR, Solver2015Day14.DAY)
    sol = Solver2015Day14(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
