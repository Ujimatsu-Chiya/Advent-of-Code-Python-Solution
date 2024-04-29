import requests

from utils import Solver


class Solver17D6(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/6/input'

    def parse(self, src):
        return list(map(int, src.strip().split()))

    def solve_part_1(self, src):
        a = self.parse(src)
        n = len(a)
        st = set(tuple(a))
        cnt = 0
        while True:
            cnt += 1
            p = a.index(max(a))
            x = a[p]
            a[p] = 0
            q, r = divmod(x, n)
            for i in range(n):
                a[(p + i + 1) % n] += q + int(i < r)
            t = tuple(a)
            if t in st:
                break
            else:
                st.add(t)
        return cnt

    def solve_part_2(self, src):
        a = self.parse(src)
        n = len(a)
        mp = {tuple(a): 0}
        cnt = 0
        while True:
            cnt += 1
            p = a.index(max(a))
            x = a[p]
            a[p] = 0
            q, r = divmod(x, n)
            for i in range(n):
                a[(p + i + 1) % n] += q + int(i < r)
            t = tuple(a)
            if t in mp.keys():
                return cnt - mp[t]
            else:
                mp[t] = cnt


if __name__ == "__main__":
    sol = Solver17D6()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D6.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
