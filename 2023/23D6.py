import requests

from utils import Solver


class Solver23D6(Solver):
    INPUT_URL = 'https://adventofcode.com/2023/day/6/input'

    def parse(self, src):
        time_str, distance_str = src.strip().split('\n')
        time_list = list(map(int, time_str[time_str.find(':') + 1:].strip().split()))
        distance_list = list(map(int, distance_str[distance_str.find(':') + 1:].strip().split()))
        return time_list, distance_list

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

    def solve_part_1(self, src):
        time_list, distance_list = self.parse(src)
        ans = 1
        for tm, dis in zip(time_list, distance_list):
            ans *= self.cal(tm, dis)
        return ans

    def solve_part_2(self, src):
        time_list, distance_list = self.parse(src)
        tm = int(''.join(str(x) for x in time_list))
        dis = int(''.join(str(x) for x in distance_list))
        return self.cal(tm, dis)


if __name__ == "__main__":
    sol = Solver23D6()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver23D6.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))