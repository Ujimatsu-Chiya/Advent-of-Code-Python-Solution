from utils import Solver, get_data


class Solver2018Day5(Solver):
    YEAR = 2018
    DAY = 5

    def parse(self, src):
        return src.strip()

    def _solve(self, ls):
        st = []
        M = 32
        for x in ls:
            if len(st) > 0 and st[-1] == x ^ M:
                st.pop()
            else:
                st.append(x)
        return len(st)

    def solve_part_1(self, src):
        ls = [ord(ch) for ch in self.parse(src)]
        return self._solve(ls)

    def solve_part_2(self, src):
        s = self.parse(src)
        char_set = set(s.lower())
        ans = min(self._solve([ord(ch) for ch in s.replace(ch, "").replace(ch.upper(), "")]) for ch in char_set)
        return ans


if __name__ == "__main__":
    sol = Solver2018Day5()
    src = get_data(Solver2018Day5.YEAR, Solver2018Day5.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
