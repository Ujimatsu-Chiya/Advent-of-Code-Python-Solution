from utils import Solver, get_data


class Solver2016Day1(Solver):
    YEAR = 2016
    DAY = 1
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, src):
        ls = src.strip().split(', ')
        self.queries = [[s[0], int(s[1:])] for s in ls]

    def solve_part_1(self):
        x = y = p = 0
        for d, dis in self.queries:
            if d == 'L':
                p = (p - 1) % 4
            else:
                p = (p + 1) % 4
            x += self.dirs[p][0] * dis
            y += self.dirs[p][1] * dis
        return abs(x) + abs(y)

    def solve_part_2(self):
        st = {(0, 0)}
        x = y = p = 0
        for d, dis in self.queries:
            if d == 'L':
                p = (p - 1) % 4
            else:
                p = (p + 1) % 4
            for k in range(dis):
                x += self.dirs[p][0]
                y += self.dirs[p][1]
                if (x, y) in st:
                    return abs(x) + abs(y)
                st.add((x, y))
        return None


if __name__ == "__main__":
    src = get_data(Solver2016Day1.YEAR, Solver2016Day1.DAY)
    sol = Solver2016Day1(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
