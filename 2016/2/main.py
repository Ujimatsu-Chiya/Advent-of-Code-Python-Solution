from utils import Solver, get_data


class Solver2016Day2(Solver):
    YEAR = 2016
    DAY = 2

    def parse(self, src):
        return src.strip().split()

    def solve_part_1(self, src):
        ls = self.parse(src)
        pad = ['123', '456', '789']
        x = y = 1
        ans = ''
        for s in ls:
            for ch in s:
                if ch == 'L' and y > 0:
                    y -= 1
                elif ch == 'R' and y < 2:
                    y += 1
                elif ch == 'U' and x > 0:
                    x -= 1
                elif ch == 'D' and x < 2:
                    x += 1
            ans += pad[x][y]
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        pad = ['  1  ', ' 234 ', '56789', ' ABC ', '  D  ']
        x = y = 2
        ans = ''
        for s in ls:
            for ch in s:
                if ch == 'L' and abs(x - 2) + abs(y - 1 - 2) <= 2:
                    y -= 1
                elif ch == 'R' and abs(x - 2) + abs(y + 1 - 2) <= 2:
                    y += 1
                elif ch == 'U' and abs(x - 1 - 2) + abs(y - 2) <= 2:
                    x -= 1
                elif ch == 'D' and abs(x + 1 - 2) + abs(y - 2) <= 2:
                    x += 1
            ans += str(pad[x][y])
        return ans


if __name__ == "__main__":
    sol = Solver2016Day2()
    src = get_data(Solver2016Day2.YEAR, Solver2016Day2.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
