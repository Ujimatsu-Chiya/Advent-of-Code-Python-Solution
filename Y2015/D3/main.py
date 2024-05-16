from tools import Point
from utils import Solver, get_data


class Solver2015Day3(Solver):
    YEAR = 2015
    DAY = 3

    def __init__(self, src):
        self.queries = src.strip()

    def _move(self, p: Point, dir: str):
        if dir == '^':
            return Point(p.x - 1, p.y)
        elif dir == 'v':
            return Point(p.x + 1, p.y)
        elif dir == '<':
            return Point(p.x, p.y - 1)
        else:
            return Point(p.x, p.y + 1)

    def solve_part_1(self):
        p = Point(0, 0)
        st = {p}
        for ch in self.queries:
            p = self._move(p, ch)
            st.add(p)
        return len(st)

    def solve_part_2(self):
        p_list = [Point(0, 0), Point(0, 0)]
        st = {p_list[0]}
        for i, ch in enumerate(self.queries):
            p_list[i % 2] = self._move(p_list[i % 2], ch)
            st.add(p_list[i % 2])
        return len(st)


if __name__ == "__main__":
    src = get_data(Solver2015Day3.YEAR, Solver2015Day3.DAY)
    sol = Solver2015Day3(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
