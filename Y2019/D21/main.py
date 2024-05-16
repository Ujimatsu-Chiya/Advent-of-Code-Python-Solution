from tools import IntCodeComputer
from utils import Solver, get_data
from itertools import count


class Solver2019Day21(Solver):
    YEAR = 2019
    DAY = 21

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))

    def solve_part_1(self):
        p = IntCodeComputer(self.ops)
        queries = ['NOT C J', 'AND D J', 'NOT A T', 'OR T J', 'WALK']
        '''
          notes:
          -------------------------------
          1. droid jumps 4 steps at a time
          2. always check to see that tile D (4th tile) is solid (for landing)
          3. if you want to land on an island (###.##..####), jump 2 tiles before the first
             hole: so basically jump whenever C (3rd tile ahead) is a hole. 

        '''
        s = "\n".join(queries) + "\n"
        p.add_ascii_input(s)
        return p.get_all_output()[-1]

    def solve_part_2(self):
        p = IntCodeComputer(self.ops)
        queries = [
            # |  @  CD   H      |
            # |#####.##.##.#.###|
            'NOT C J', 'AND D J', 'AND H J',
            # |      @ B D      |
            # |#####.##.##.#.###|
            'NOT B T', 'AND D T', 'OR T J',
            # |          @A     |
            # |#####.##.##.#.###|
            'NOT A T', 'OR T J', 'RUN'
        ]
        '''
        notes:
        -------------------------------
        1. droid stills jumps 4 steps at a time
        2. always check to see that tile D (4th tile) is solid (for landing)
        3. if you want to land on an island (###.##..####), jump 2 tiles before the first
           hole: so basically jump whenever C (3rd tile ahead) is a hole. 
        4. watch where you landing next after leaving the island.
        '''
        s = "\n".join(queries) + "\n"
        p.add_ascii_input(s)
        return p.get_all_output()[-1]


if __name__ == "__main__":
    src = get_data(Solver2019Day21.YEAR, Solver2019Day21.DAY)
    sol = Solver2019Day21(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
