from utils import Solver, get_data


class Solver2023Day4(Solver):
    YEAR = 2023
    DAY = 4

    def __init__(self, src):
        self.queries = []
        for line in src.strip().split('\n'):
            card, nums = line.split(':')
            winning_numbers_str, numbers_str = nums.split('|')
            winning_numbers = set(winning_numbers_str.split())
            numbers = set(numbers_str.split())
            self.queries.append((winning_numbers, numbers))

    def solve_part_1(self):
        ans = 0
        for winning_numbers, numbers in self.queries:
            cnt = len(winning_numbers & numbers)
            ans += 1 << (cnt - 1) if cnt > 0 else 0
        return ans

    def solve_part_2(self):
        n = len(self.queries)
        f = [1 for _ in range(n)]
        for i, (winning_numbers, numbers) in enumerate(self.queries):
            cnt = len(winning_numbers & numbers)
            for k in range(1, cnt + 1):
                if i + k < n:
                    f[i + k] += f[i]
        return sum(f)


if __name__ == "__main__":
    src = get_data(Solver2023Day4.YEAR, Solver2023Day4.DAY)
    sol = Solver2023Day4(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
