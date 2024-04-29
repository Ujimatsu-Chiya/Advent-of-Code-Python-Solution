import requests

from utils import Solver, transpose


class Solver23D13(Solver):
    INPUT_URL = 'https://adventofcode.com/2023/day/13/input'

    def parse(self, src):
        ls = []
        t = src.strip().split('\n')
        i = 0
        while i < len(t):
            if len(t[i]) > 0:
                j = i
                while j < len(t) and len(t[j]) > 0:
                    j += 1
                ls.append(t[i:j])
                i = j
            else:
                i += 1
        return ls

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for mp in ls:
            n, m = len(mp), len(mp[0])
            for i in range(1, n):
                sz = min(i, n - i)
                if mp[i - sz:i] == list(reversed(mp[i:i + sz])):
                    ans += i * 100
            mp = transpose(mp)
            for i in range(1, m):
                sz = min(i, m - i)
                if mp[i - sz:i] == list(reversed(mp[i:i + sz])):
                    ans += i
        return ans

    def solve_part_2(self, src):
        def check(m1, m2):
            ans = 0
            for i in range(len(m1)):
                for j in range(len(m1[0])):
                    if m1[i][j] != m2[i][j]:
                        ans += 1
            return ans == 1

        ls = self.parse(src)
        ans = 0
        for mp in ls:
            n, m = len(mp), len(mp[0])
            for i in range(1, n):
                sz = min(i, n - i)
                if check(mp[i - sz:i], list(reversed(mp[i:i + sz]))):
                    ans += i * 100
            mp = transpose(mp)
            for i in range(1, m):
                sz = min(i, m - i)
                if check(mp[i - sz:i], list(reversed(mp[i:i + sz]))):
                    ans += i
        return ans


if __name__ == "__main__":
    sol = Solver23D13()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver23D13.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
