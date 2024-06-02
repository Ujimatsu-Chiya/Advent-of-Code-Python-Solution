from utils import Solver, get_data
from typing import NamedTuple
from heapq import heappush, heappop


class State(NamedTuple):
    rooms: tuple
    hallway: tuple = (-1,) * 11

    def is_complete(self):
        return all(h == -1 for h in self.hallway) and all(
            all(a == i for a in room) for i, room in enumerate(self.rooms)
        )


class Solver2021Day23(Solver):
    YEAR = 2021
    DAY = 23

    def __init__(self, src):
        mp = []
        ls = src.strip('\n').split('\n')[::-1]
        for j in range(len(ls[0])):
            lt = tuple(ord(ls[i][j]) - ord('A') for i in range(len(ls)) if ls[i][j].isupper())
            if lt:
                mp.append(lt)
        self.mp = tuple(mp)

    def _run(self, mp):
        out_idx = [2, 4, 6, 8]
        mx = max(max(u) for u in mp)
        room_size = len(mp[0])
        pw10 = [10 ** i for i in range(mx + 1)]

        def replace(tp, i, new):
            return tp[:i] + (new,) + tp[i + 1:]

        def gen_state(st: State):
            for room_i, room in enumerate(st.rooms):
                if all(x == room_i for x in room):
                    continue
                x = room[-1]
                for gen in (range(out_idx[room_i] + 1, 11, 1), range(out_idx[room_i] - 1, -1, -1)):
                    for hall_i in gen:
                        if hall_i in out_idx:
                            continue
                        if st.hallway[hall_i] != -1:
                            break
                        yield (room_size - len(room) + 1 + abs(out_idx[room_i] - hall_i)) * pw10[x], \
                              State(replace(st.rooms, room_i, room[:-1]), replace(st.hallway, hall_i, x))
            for hall_i, x in enumerate(st.hallway):
                if x == -1:
                    continue
                if hall_i < out_idx[x] and any(t >= 0 for t in st.hallway[hall_i + 1: out_idx[x]]) or \
                        hall_i > out_idx[x] and any(t >= 0 for t in st.hallway[out_idx[x] + 1: hall_i]):
                    continue
                if any(t != x for t in st.rooms[x]):
                    continue
                yield (room_size - len(st.rooms[x]) + abs(out_idx[x] - hall_i)) * pw10[x], \
                      State(replace(st.rooms, x, st.rooms[x] + (x,)), replace(st.hallway, hall_i, -1))

        vis = set()
        start = State(mp)
        q = []
        heappush(q, (0, start))
        while len(q) > 0:
            cost, st = heappop(q)
            if st in vis:
                continue
            if st.is_complete():
                return cost
            vis.add(st)
            for pay, new_st in gen_state(st):
                if new_st not in vis:
                    heappush(q, (cost + pay, new_st))

    def solve_part_1(self):
        return self._run(self.mp)

    def solve_part_2(self):
        mp = (
            (self.mp[0][0], 3, 3, self.mp[0][1]),
            (self.mp[1][0], 1, 2, self.mp[1][1]),
            (self.mp[2][0], 0, 1, self.mp[2][1]),
            (self.mp[3][0], 2, 0, self.mp[3][1])
        )
        return self._run(mp)


if __name__ == "__main__":
    src = get_data(Solver2021Day23.YEAR, Solver2021Day23.DAY)
    sol = Solver2021Day23(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
