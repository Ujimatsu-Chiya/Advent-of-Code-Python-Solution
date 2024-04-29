import requests
import json
from utils import Solver


class Solver15D12(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/12/input'

    def parse(self, src):
        return json.loads(src.strip())

    def solve_part_1(self, src):
        mp = self.parse(src)

        def dfs(obj):
            ans = []
            if isinstance(obj, int):
                ans.append(obj)
            elif isinstance(obj, list):
                for obj2 in obj:
                    ans += dfs(obj2)
            elif isinstance(obj, dict):
                for v in obj.values():
                    ans += dfs(v)
            return ans

        return sum(dfs(mp))

    def solve_part_2(self, src):
        mp = self.parse(src)

        def dfs(obj):
            ans = []
            if isinstance(obj, int):
                ans.append(obj)
            elif isinstance(obj, list):
                for obj2 in obj:
                    ans += dfs(obj2)
            elif isinstance(obj, dict):
                if 'red' in obj.values():
                    return []
                for v in obj.values():
                    ans += dfs(v)
            return ans

        return sum(dfs(mp))


if __name__ == "__main__":
    sol = Solver15D12()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D12.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
