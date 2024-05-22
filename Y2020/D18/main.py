import re

from utils import Solver, get_data


class Solver2020Day18(Solver):
    YEAR = 2020
    DAY = 18

    def __init__(self, src):
        pat = re.compile(r"(\d+|\+|\-|\*|/|\(|\))")
        self.queries = []
        for expr in src.strip().split('\n'):
            expr = " ".join(pat.split(expr)).replace("  ", " ").strip()
            ls = ['('] + expr.split() + [')']
            self.queries.append([int(s) if s.isdigit() else s for s in ls])

    def solve_part_1(self):
        def solve(tokens):
            st = []
            for token in tokens:
                if token == ')':
                    a = []
                    while len(st) > 0 and st[-1] != '(':
                        a.append(st.pop())

                    st.pop()
                    a.reverse()
                    for i in range(1, len(a), 2):
                        if a[i] == '+':
                            a[0] += a[i + 1]
                        else:
                            a[0] *= a[i + 1]
                    st.append(a[0])
                else:
                    st.append(token)
            return st[-1]

        return sum(solve(tokens) for tokens in self.queries)

    def solve_part_2(self):
        def solve(tokens):
            precedence = {'+': 2, '*': 1, '(': 0}
            st = []
            output = []
            for token in tokens:
                if isinstance(token, int):
                    output.append(token)
                elif token == '(':
                    st.append(token)
                elif token == ')':
                    while len(st) > 0 and st[-1] != '(':
                        output.append(st.pop())
                    st.pop()
                else:
                    while len(st) > 0 and precedence[st[-1]] >= precedence[token]:
                        output.append(st.pop())
                    st.append(token)
            while len(st) > 0:
                output.append(st.pop())
            for token in output:
                if isinstance(token, int):
                    st.append(token)
                else:
                    x, y = st.pop(), st.pop()
                    st.append(x * y if token == '*' else x + y)
            return st[0]

        return sum(solve(tokens) for tokens in self.queries)


if __name__ == "__main__":
    src = get_data(Solver2020Day18.YEAR, Solver2020Day18.DAY)
    sol = Solver2020Day18(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
