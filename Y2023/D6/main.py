from utils import Solver, get_data


class Solver2023Day6(Solver):
    YEAR = 2023
    DAY = 6

    def __init__(self, src):
        time_str, distance_str = src.strip().split('\n')
        self.time_list = list(map(int, time_str[time_str.find(':') + 1:].strip().split()))
        self.distance_list = list(map(int, distance_str[distance_str.find(':') + 1:].strip().split()))

    def cal(self, tm, dis):
        l = 0
        r = (tm + 1) // 2 + 1
        while l < r:
            mid = (l + r) >> 1
            if mid * (tm - mid) > dis:
                r = mid
            else:
                l = mid + 1
        k = tm - l
        return 0 if l > k else k - l + 1

    def solve_part_1(self):
        ans = 1
        for tm, dis in zip(self.time_list, self.distance_list):
            ans *= self.cal(tm, dis)
        return ans

    def solve_part_2(self):
        tm = int(''.join(str(x) for x in self.time_list))
        dis = int(''.join(str(x) for x in self.distance_list))
        return self.cal(tm, dis)


if __name__ == "__main__":
    src = get_data(Solver2023Day6.YEAR, Solver2023Day6.DAY)
    sol = Solver2023Day6(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
