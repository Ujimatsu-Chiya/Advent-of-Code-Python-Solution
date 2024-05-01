import hashlib
from itertools import count

from utils import Solver, get_data


class Solver2016Day14(Solver):
    YEAR = 2016
    DAY = 14

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
        cache3 = [0]
        cache5 = [0]

        def get_md5(s, x):
            if x >= len(cache3):
                md5 = hashlib.md5((s + str(x)).encode())
                t = md5.hexdigest()
                s3 = s5 = 0
                for i in range(len(t) - 2):
                    if len(set(t[i:i + 3])) == 1:
                        s3 |= 1 << int(t[i], 16)
                        break
                for i in range(len(t) - 4):
                    if len(set(t[i:i + 5])) == 1:
                        s5 |= 1 << int(t[i], 16)
                cache3.append(s3)
                cache5.append(s5)

        cnt = 0
        for i in count(1):
            get_md5(s, i)
            if cache3[i] != 0:
                for j in range(i + 1, i + 1001):
                    get_md5(s, j)
                    if cache3[i] & cache5[j]:
                        cnt += 1
                        if cnt == 64:
                            return i
                        break

    def solve_part_2(self, src):
        s = self.parse(src)
        cache3 = [0]
        cache5 = [0]

        def get_md5(s, x):
            if x >= len(cache3):
                t = s + str(x)
                for _ in range(2017):
                    md5 = hashlib.md5(t.encode())
                    t = md5.hexdigest()
                s3 = s5 = 0
                for i in range(len(t) - 2):
                    if len(set(t[i:i + 3])) == 1:
                        s3 |= 1 << int(t[i], 16)
                        break
                for i in range(len(t) - 4):
                    if len(set(t[i:i + 5])) == 1:
                        s5 |= 1 << int(t[i], 16)
                cache3.append(s3)
                cache5.append(s5)

        cnt = 0
        for i in count(1):
            get_md5(s, i)
            if cache3[i] != 0:
                for j in range(i + 1, i + 1001):
                    get_md5(s, j)
                    if cache3[i] & cache5[j]:
                        cnt += 1
                        if cnt == 64:
                            return i
                        break


if __name__ == "__main__":
    sol = Solver2016Day14()
    src = get_data(Solver2016Day14.YEAR, Solver2016Day14.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
