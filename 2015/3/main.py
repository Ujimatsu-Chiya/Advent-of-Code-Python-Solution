from utils import Solver, Point, get_data


class Solver2015Day3(Solver):
    YEAR = 2015
    DAY = 3

    def parse(self, src):
        return src.strip()

    def _move(self, p: Point, dir: str):
        if dir == '^':
            return Point(p.x - 1, p.y)
        elif dir == 'v':
            return Point(p.x + 1, p.y)
        elif dir == '<':
            return Point(p.x, p.y - 1)
        else:
            return Point(p.x, p.y + 1)

    def solve_part_1(self, src):
        p = Point(0, 0)
        st = {p}
        for ch in self.parse(src):
            p = self._move(p, ch)
            st.add(p)
        return len(st)

    def solve_part_2(self, src):
        p_list = [Point(0, 0), Point(0, 0)]
        st = {p_list[0]}
        for i, ch in enumerate(self.parse(src)):
            p_list[i % 2] = self._move(p_list[i % 2], ch)
            st.add(p_list[i % 2])
        return len(st)


if __name__ == "__main__":
    sol = Solver2015Day3()
    src = get_data(Solver2015Day3.YEAR, Solver2015Day3.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
