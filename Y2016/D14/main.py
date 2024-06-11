from itertools import count

from tools import md5_digest
from utils import Solver, get_data


class Solver2016Day14(Solver):
    YEAR = 2016
    DAY = 14

    def __init__(self, src):
        self.s = src.strip()

    def _run(self, f):
        cache3 = [0]
        cache5 = [0]

        def get_md5(s, x):
            if x >= len(cache3):
                t = f(s + str(x))
                s3 = s5 = 0
                for i in range(len(t) - 2):
                    if len(set(t[i:i + 3])) == 1:
                        s3 |= 1 << int(t[i], 16)
                        break
                for i in range(len(t) - 4):
                    if len(set(t[i:i + 5])) == 1:
                        s5 |= 1 << int(t[i], 16)
                        break
                cache3.append(s3)
                cache5.append(s5)

        cnt = 0
        for i in count(1):
            get_md5(self.s, i)
            if cache3[i] != 0:
                for j in range(i + 1, i + 1001):
                    get_md5(self.s, j)
                    if cache3[i] & cache5[j]:
                        cnt += 1
                        if cnt == 64:
                            return i
                        break

    def solve_part_1(self):
        return self._run(md5_digest)

    def solve_part_2(self):

        def iterate2017(s):
            for _ in range(2017):
                s = md5_digest(s)
            return s

        return self._run(iterate2017)


if __name__ == "__main__":
    from time import time
    st = time()
    src = get_data(Solver2016Day14.YEAR, Solver2016Day14.DAY)
    sol = Solver2016Day14(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
    print(time() - st)