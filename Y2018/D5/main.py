from utils import Solver, get_data


class Solver2018Day5(Solver):
    YEAR = 2018
    DAY = 5

    def __init__(self, src):
        self.s =  src.strip()

    def _solve(self, ls):
        st = []
        M = 32
        for x in ls:
            if len(st) > 0 and st[-1] == x ^ M:
                st.pop()
            else:
                st.append(x)
        return len(st)

    def solve_part_1(self):
        ls = [ord(ch) for ch in self.s]
        return self._solve(ls)

    def solve_part_2(self):
        char_set = set(self.s.lower())
        ans = min(self._solve([ord(ch) for ch in self.s.replace(ch, "").replace(ch.upper(), "")]) for ch in char_set)
        return ans


if __name__ == "__main__":
    src = get_data(Solver2018Day5.YEAR, Solver2018Day5.DAY)
    sol = Solver2018Day5(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
