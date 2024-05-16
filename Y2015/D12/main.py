import json

from utils import Solver, get_data


class Solver2015Day12(Solver):
    YEAR = 2015
    DAY = 12

    def __init__(self, src):
        self.mp = json.loads(src.strip())

    def solve_part_1(self):
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

        return sum(dfs(self.mp))

    def solve_part_2(self):
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

        return sum(dfs(self.mp))


if __name__ == "__main__":
    src = get_data(Solver2015Day12.YEAR, Solver2015Day12.DAY)
    sol = Solver2015Day12(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
