from itertools import count

from tools import md5_digest
from utils import Solver, get_data


class Solver2016Day5(Solver):
    YEAR = 2016
    DAY = 5

    def __init__(self, src):
        self.s = src.strip()

    def solve_part_1(self):
        M = 8
        ans = ''
        prefix = "00000"
        for i in count(1):
            t = md5_digest(self.s + str(i))
            if t.startswith(prefix):
                ans += t[len(prefix)]
                if len(ans) == M:
                    break
        return ans

    def solve_part_2(self):
        M = 8
        ans = ['' for _ in range(M)]
        prefix = "00000"
        cnt = 0
        for i in count(1):
            t = md5_digest(self.s + str(i))
            if t.startswith(prefix):
                c1, c2 = t[len(prefix)], t[len(prefix) + 1]
                if c1.isdigit():
                    p = int(c1)
                    if p < M and ans[p] == '':
                        ans[p] = c2
                        cnt += 1
                        if cnt == M:
                            break
        return ''.join(ans)


if __name__ == "__main__":
    src = get_data(Solver2016Day5.YEAR, Solver2016Day5.DAY)
    sol = Solver2016Day5(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
