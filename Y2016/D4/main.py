import re
from collections import Counter

from utils import Solver, get_data


class Solver2016Day4(Solver):
    YEAR = 2016
    DAY = 4

    def __init__(self, src):
        pat = re.compile(r'(.+)-(\d+)\[(.+)\]')
        ls = pat.findall(src.strip())
        self.queries = [[s[0], int(s[1]), s[2]] for s in ls]

    def solve_part_1(self):
        ans = 0
        for s, id, check_sum in self.queries:
            a = sorted((-v, k) for k, v in Counter(s.replace('-', '')).items())
            check = "".join(v[1] for v in a[:5])
            if check == check_sum:
                ans += id
        return ans

    def solve_part_2(self):
        for s, id, _ in self.queries:
            s = "".join([chr((ord(ch) - ord('a') + id) % 26 + ord('a')) if ch.isalpha() else ch for ch in s]).replace(
                '-', ' ')
            if s == 'northpole object storage':
                return id


if __name__ == "__main__":
    src = get_data(Solver2016Day4.YEAR, Solver2016Day4.DAY)
    sol = Solver2016Day4(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
