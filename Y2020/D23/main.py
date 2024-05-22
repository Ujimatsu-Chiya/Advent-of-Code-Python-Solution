from utils import Solver, get_data


class LinkList:
    def __init__(self, a):
        n = len(a)
        self.next = [0 for _ in range(n)]
        for i in range(n):
            self.next[a[i]] = a[(i + 1) % n]

    def add(self, x, y):
        z = self.next[x]
        self.next[x], self.next[y] = y, z

    def pop(self, next_x):
        y = self.next[next_x]
        self.next[next_x] = self.next[y]
        return y


class Solver2020Day23(Solver):
    YEAR = 2020
    DAY = 23

    def __init__(self, src):
        self.a = [int(ch) - 1 for ch in src.strip()]

    def _run(self, a, M):
        link = LinkList(a)
        pos = a[0]
        n = len(a)
        for _ in range(M):
            now = []
            for _ in range(3):
                now.append(link.pop(pos))
            val = (pos - 1) % n
            while val in now:
                val = (val - 1) % n
            lt = [val] + now
            for i in range(1, len(lt)):
                link.add(lt[i - 1], lt[i])
            pos = link.next[pos]
        return link

    def solve_part_1(self):
        link = self._run(self.a, 100)
        p = 0
        ans = []
        for _ in range(len(self.a) - 1):
            p = link.next[p]
            ans.append(p + 1)
        return "".join(str(x) for x in ans)

    def solve_part_2(self):
        N = 10 ** 6
        M = 10 ** 7
        a = self.a + list(range(len(self.a), N))
        link = self._run(a, M)
        x, y = link.next[0] + 1, link.next[link.next[0]] + 1
        return x * y


if __name__ == "__main__":
    src = get_data(Solver2020Day23.YEAR, Solver2020Day23.DAY)
    sol = Solver2020Day23(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
