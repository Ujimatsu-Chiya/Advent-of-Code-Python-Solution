from utils import Solver, get_data


class Solver2022Day25(Solver):
    YEAR = 2022
    DAY = 25

    def __init__(self, src):
        self.queries = src.strip().split()

    def solve_part_1(self):
        mp = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
        mq = {v: k for k, v in mp.items()}

        def snafu_to_dec(s):
            s = s[::-1]
            return sum(mp[ch] * pow(5, i) for i, ch in enumerate(s))

        def dec_to_snafu(x):
            digit = [0, 1, 2, -2, -1]
            ans = []
            while x != 0:
                d = digit[x % 5]
                ans.append(d)
                x = (x - d) // 5
            return "".join(mq[d] for d in ans[::-1])

        return dec_to_snafu(sum(snafu_to_dec(s) for s in self.queries))

    def solve_part_2(self):
        pass


if __name__ == "__main__":
    src = get_data(Solver2022Day25.YEAR, Solver2022Day25.DAY)
    sol = Solver2022Day25(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
