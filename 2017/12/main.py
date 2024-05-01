from queue import Queue

from utils import Solver, get_data


class Solver2017Day12(Solver):
    YEAR = 2017
    DAY = 12

    def parse(self, src):
        mp = {}
        for s in src.strip().split('\n'):
            l_str, r_str = s.split(' <-> ')
            mp[int(l_str)] = list(map(int, r_str.split(', ')))
        return mp

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

    def solve_part_1(self, src):
        mp = self.parse(src)
        return len(self._bfs(mp, 0))

    def solve_part_2(self, src):
        mp = self.parse(src)
        st = set()
        ans = 0
        for s in mp.keys():
            if s not in st:
                st |= self._bfs(mp, s)
                ans += 1
        return ans


if __name__ == "__main__":
    sol = Solver2017Day12()
    src = get_data(Solver2017Day12.YEAR, Solver2017Day12.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
