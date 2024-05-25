from utils import Solver, get_data


class Solver2021Day10(Solver):
    YEAR = 2021
    DAY = 10

    def __init__(self, src):
        self.queries = src.strip().split()
        self.ans1 = self.ans2 = None

    def run(self):
        mp = {')': '(', ']': '[', '}': '{', '>': '<'}
        vals1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
        vals2 = {'(': 1, '[': 2, '{': 3, '<': 4}

        def solve(s):
            st = []
            for ch in s:
                if ch not in mp.keys():
                    st.append(ch)
                elif len(st) > 0 and st[-1] == mp[ch]:
                    st.pop()
                else:
                    return 0, vals1[ch]
            s = 0
            for ch in st[::-1]:
                s = s * 5 + vals2[ch]
            return 1, s

        ls = [[],[]]
        for s in self.queries:
            p, val = solve(s)
            ls[p].append(val)
        self.ans1 = sum(ls[0])
        self.ans2 = sorted(ls[1])[len(ls[1]) >> 1]

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day10.YEAR, Solver2021Day10.DAY)
    sol = Solver2021Day10(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
