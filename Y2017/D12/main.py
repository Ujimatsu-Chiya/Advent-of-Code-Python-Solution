from queue import Queue

from utils import Solver, get_data


class Solver2017Day12(Solver):
    YEAR = 2017
    DAY = 12

    def __init__(self, src):
        self.mp = {}
        for s in src.strip().split('\n'):
            l_str, r_str = s.split(' <-> ')
            self.mp[int(l_str)] = list(map(int, r_str.split(', ')))

    def _bfs(self, mp, s):
        st = {s}
        q = Queue()
        q.put(s)
        while q.qsize() > 0:
            u = q.get()
            for v in mp[u]:
                if v not in st:
                    st.add(v)
                    q.put(v)
        return st

    def solve_part_1(self):
        return len(self._bfs(self.mp, 0))

    def solve_part_2(self):
        st = set()
        ans = 0
        for s in self.mp.keys():
            if s not in st:
                st |= self._bfs(self.mp, s)
                ans += 1
        return ans


if __name__ == "__main__":
    src = get_data(Solver2017Day12.YEAR, Solver2017Day12.DAY)
    sol = Solver2017Day12(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
