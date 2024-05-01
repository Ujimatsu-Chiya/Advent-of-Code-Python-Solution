import hashlib
from itertools import count

from utils import Solver, get_data


class Solver2016Day5(Solver):
    YEAR = 2016
    DAY = 5

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
        ans = ''
        prefix = "00000"
        for i in count(1):
            md5 = hashlib.md5((s + str(i)).encode())
            t = md5.hexdigest()
            if t.startswith(prefix):
                ans += t[len(prefix)]
                if len(ans) == 8:
                    break
        return ans

    def solve_part_2(self, src):
        s = self.parse(src)
        M = 8
        ans = ['' for _ in range(M)]
        prefix = "00000"
        cnt = 0
        for i in count(1):
            md5 = hashlib.md5((s + str(i)).encode())
            t = md5.hexdigest()
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
    sol = Solver2016Day5()
    src = get_data(Solver2016Day5.YEAR, Solver2016Day5.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))