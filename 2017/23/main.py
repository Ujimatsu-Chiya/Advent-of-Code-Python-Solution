from utils import Solver, get_data, is_prime


class Solver2017Day23(Solver):
    YEAR = 2017
    DAY = 23

    def parse(self, src):
        ls = []
        for s in src.strip().split('\n'):
            ls.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
        return ls

    def _solve(self, vals, ls):
        def get_val(s):
            try:
                return int(s)
            except ValueError:
                return vals[s]

        pos = 0
        cnt = 0
        while 0 <= pos < len(ls):
            ins = ls[pos]
            if ins[0] == "set":
                vals[ins[1]] = get_val(ins[2])
                pos += 1
            elif ins[0] == "sub":
                vals[ins[1]] -= get_val(ins[2])
                pos += 1
            elif ins[0] == "mul":
                vals[ins[1]] *= get_val(ins[2])
                cnt += 1
                pos += 1
            elif ins[0] == "jnz":
                if get_val(ins[1]) != 0:
                    pos += get_val(ins[2])
                else:
                    pos += 1
        return vals, cnt

    def solve_part_1(self, src):
        ls = self.parse(src)
        vals = {ch: 0 for ch in 'abcdefgh'}
        return self._solve(vals, ls)[1]

    def solve_part_2(self, src):
        # https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/
        ls = self.parse(src)
        b = ls[0][2]
        b = 100 * b + 100000
        c = b + 17000
        h = 0
        for i in range(b,c+1,17):
            if not is_prime(i):
                h += 1
        return h


if __name__ == "__main__":
    sol = Solver2017Day23()
    src = get_data(Solver2017Day23.YEAR, Solver2017Day23.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
