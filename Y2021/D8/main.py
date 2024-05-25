from utils import Solver, get_data
from functools import reduce
import operator


class Solver2021Day8(Solver):
    YEAR = 2021
    DAY = 8

    def __init__(self, src):
        self.queries = []
        cal = lambda s: reduce(operator.or_, [1 << (ord(ch) - ord('a')) for ch in s])
        for s in src.strip().split('\n'):
            l_str, r_str = s.split(' | ')
            l = [cal(s) for s in l_str.split()]
            r = [cal(s) for s in r_str.split()]
            self.queries.append((l, r))

    def solve_part_1(self):
        return sum(sum(1 for x in v if x.bit_count() in {2, 3, 4, 7}) for _, v in self.queries)

    def solve_part_2(self):
        def solve(dg, vals):
            to_line = [-1 for _ in range(7)]
            to_digit = [-1 for _ in range(10)]
            for st in dg:
                match st.bit_count():
                    case 2:
                        to_digit[1] = st
                    case 3:
                        to_digit[7] = st
                    case 4:
                        to_digit[4] = st
                    case 7:
                        to_digit[8] = st
            to_line[0] = to_digit[1] ^ to_digit[7]
            t = to_line[0] | to_digit[4]
            for st in dg:
                if st.bit_count() == 6 and (t & st) == t:
                    to_line[6] = t ^ st
                    to_digit[9] = st
                if st.bit_count() == 5 and (st & to_digit[7]) == to_digit[7]:
                    to_digit[3] = st
            to_line[4] = to_digit[8] ^ to_digit[9]
            for st in dg:
                if st.bit_count() == 5 and (st & to_digit[9]) != st:
                    to_digit[2] = st
                if st.bit_count() == 6 and st != to_digit[9] and (st & to_digit[1]) == to_digit[1]:
                    to_digit[0] = st
            for x in dg:
                for y in dg:
                    if x != y and x != to_digit[9] and (x | to_line[4]) == y:
                        to_digit[5] = x
                        to_digit[6] = y
            to_line[3] = to_digit[8] ^ to_digit[0]
            to_line[2] = to_digit[8] ^ to_digit[6]
            to_line[5] = to_digit[1] ^ to_line[2]
            to_line[1] = to_digit[3] ^ to_digit[9]
            ans = 0
            for st in vals:
                ans = ans * 10 + to_digit.index(st)
            return ans

        return sum(solve(*q) for q in self.queries)


if __name__ == "__main__":
    src = get_data(Solver2021Day8.YEAR, Solver2021Day8.DAY)
    sol = Solver2021Day8(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
