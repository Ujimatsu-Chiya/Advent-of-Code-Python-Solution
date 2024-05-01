import copy
import re
from collections import deque
from itertools import combinations

from utils import Solver, get_data


class Item:
    def __init__(self, element: str) -> None:
        self.element = element

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.element}>"

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return repr(self) == repr(other)


class Gen(Item):
    pass


class Chip(Item):
    pass


class Floor:
    def __init__(self, generators: set, chips: set) -> None:
        self.generators = generators
        self.chips = chips

    @property
    def items(self):
        return self.generators.union(self.chips)

    def give(self, item) -> None:
        if isinstance(item, Gen):
            self.generators.remove(item)
        else:
            self.chips.remove(item)

    def get(self, item) -> None:
        if isinstance(item, Gen):
            self.generators.add(item)
        else:
            self.chips.add(item)


class State:
    def __init__(self, elevator: int, floors, steps: int) -> None:
        self.elevator = elevator
        self.floors = floors
        self.steps = steps
        self.top_floor = len(floors)

    @property
    def bottom_floor(self) -> int:
        for i in range(len(self.floors)):
            if len(self.floors[i].items) > 0:
                return i

    def __repr__(self) -> str:
        res = f"[{self.steps}]:"
        for floor in self.floors:
            res += str(floor.items) + "//"
        return res.rstrip("//")

    def __hash__(self):
        item_pair = {}
        for i, floor in enumerate(self.floors):
            for chip in floor.chips:
                item_pair[chip.element] = [i]
        for i, floor in enumerate(self.floors):
            for gen in floor.generators:
                item_pair[gen.element].append(i)
        return hash(str(sorted(item_pair.values())) + str(self.elevator))

    def __eq__(self, other):
        return hash(self) == hash(other)

    @property
    def is_complete(self) -> bool:
        return all(len(f.items) == 0 for f in self.floors[:-1])

    @property
    def is_valid(self) -> bool:
        for floor in self.floors:
            if floor.generators == set():
                continue
            for chip in floor.chips:
                if not any(chip.element == gen.element for gen in floor.generators):
                    return False
        return True

    def next_states(self):
        cur_floor = self.floors[self.elevator]
        for dir in [-1, 1]:
            if (
                    self.elevator + dir < self.bottom_floor
                    or self.elevator + dir >= self.top_floor
            ):
                continue
            for number in [1, 2]:
                for items in combinations(cur_floor.items, number):
                    state = self.generate_state(dir, items)
                    if state.is_valid:
                        yield state

    def generate_state(self, dir, items):
        new_floors = copy.deepcopy(self.floors)
        for item in items:
            new_floors[self.elevator].give(item)
            new_floors[self.elevator + dir].get(item)

        return State(
            elevator=self.elevator + dir, floors=new_floors, steps=self.steps + 1
        )


class Solver2016Day11(Solver):
    YEAR = 2016
    DAY = 11

    def parse(self, src):
        microchip_regex = re.compile(r"a (\w+)-compatible microchip")
        generator_regex = re.compile(r"a (\w+) generator")
        floors = []
        for line in src.strip().splitlines():
            chips = set(Chip(s) for s in microchip_regex.findall(line))
            generators = set(Gen(s) for s in generator_regex.findall(line))
            floors.append(Floor(generators=generators, chips=chips))
        return State(elevator=0, floors=floors, steps=0)

    def _solve(self, initial_state):
        """run simulation"""
        queue = deque([initial_state])
        visited = set([initial_state])

        while queue:
            state = queue.popleft()
            if state.is_complete:
                return state.steps

            for next_state in state.next_states():
                if next_state not in visited:
                    queue.append(next_state)
                    visited.add(next_state)

    def solve_part_1(self, src):
        st = self.parse(src)
        return self._solve(st)

    def solve_part_2(self, src):
        st = self.parse(src)
        for element in ["elerium", "dilithium"]:
            st.floors[0].chips.add(Chip(element))
            st.floors[0].generators.add(Gen(element))
        return self._solve(st)


if __name__ == "__main__":
    sol = Solver2016Day11()
    src = get_data(Solver2016Day11.YEAR, Solver2016Day11.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
