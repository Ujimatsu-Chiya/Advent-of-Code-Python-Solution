from utils import Solver, get_data


class Solver2023Day4(Solver):
    YEAR = 2023
    DAY = 4

    def parse(self, src):
        ls = src.strip().split('\n')
        lt = []
        for line in ls:
            card, nums = line.split(':')
            winning_numbers_str, numbers_str = nums.split('|')
            winning_numbers = set(winning_numbers_str.split())
            numbers = set(numbers_str.split())
            lt.append((winning_numbers, numbers))
        return lt

    def solve_part_1(self, src):
        ans = 0
        for winning_numbers, numbers in self.parse(src):
            cnt = len(winning_numbers & numbers)
            ans += 1 << (cnt - 1) if cnt > 0 else 0
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        n = len(ls)
        f = [1 for _ in range(n)]
        for i, tp in enumerate(ls):
            winning_numbers, numbers = tp
            cnt = len(winning_numbers & numbers)
            for k in range(1, cnt + 1):
                if i + k < n:
                    f[i + k] += f[i]
        return sum(f)


if __name__ == "__main__":
    sol = Solver2023Day4()
    src = get_data(Solver2023Day4.YEAR, Solver2023Day4.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
