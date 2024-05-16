from Y2015.D1.main import Solver2015Day1
from Y2015.D2.main import Solver2015Day2
from Y2015.D3.main import Solver2015Day3
from Y2015.D4.main import Solver2015Day4
from Y2015.D5.main import Solver2015Day5
from Y2015.D6.main import Solver2015Day6
from Y2015.D7.main import Solver2015Day7
from Y2015.D8.main import Solver2015Day8
from Y2015.D9.main import Solver2015Day9
from Y2015.D10.main import Solver2015Day10
from Y2015.D11.main import Solver2015Day11
from Y2015.D12.main import Solver2015Day12
from Y2015.D13.main import Solver2015Day13
from Y2015.D14.main import Solver2015Day14
from Y2015.D15.main import Solver2015Day15
from Y2015.D16.main import Solver2015Day16
from Y2015.D17.main import Solver2015Day17
from Y2015.D18.main import Solver2015Day18
from Y2015.D19.main import Solver2015Day19
from Y2015.D20.main import Solver2015Day20
from Y2015.D21.main import Solver2015Day21
from Y2015.D22.main import Solver2015Day22
from Y2015.D23.main import Solver2015Day23
from Y2015.D24.main import Solver2015Day24
from Y2015.D25.main import Solver2015Day25
from Y2016.D1.main import Solver2016Day1
from Y2016.D2.main import Solver2016Day2
from Y2016.D3.main import Solver2016Day3
from Y2016.D4.main import Solver2016Day4
from Y2016.D5.main import Solver2016Day5
from Y2016.D6.main import Solver2016Day6
from Y2016.D7.main import Solver2016Day7
from Y2016.D8.main import Solver2016Day8
from Y2016.D9.main import Solver2016Day9
from Y2016.D10.main import Solver2016Day10
from Y2016.D11.main import Solver2016Day11
from Y2016.D12.main import Solver2016Day12
from Y2016.D13.main import Solver2016Day13
from Y2016.D14.main import Solver2016Day14
from Y2016.D15.main import Solver2016Day15
from Y2016.D16.main import Solver2016Day16
from Y2016.D17.main import Solver2016Day17
from Y2016.D18.main import Solver2016Day18
from Y2016.D19.main import Solver2016Day19
from Y2016.D20.main import Solver2016Day20
from Y2016.D21.main import Solver2016Day21
from Y2016.D22.main import Solver2016Day22
from Y2016.D23.main import Solver2016Day23
from Y2016.D24.main import Solver2016Day24
from Y2016.D25.main import Solver2016Day25
from Y2017.D1.main import Solver2017Day1
from Y2017.D2.main import Solver2017Day2
from Y2017.D3.main import Solver2017Day3
from Y2017.D4.main import Solver2017Day4
from Y2017.D5.main import Solver2017Day5
from Y2017.D6.main import Solver2017Day6
from Y2017.D7.main import Solver2017Day7
from Y2017.D8.main import Solver2017Day8
from Y2017.D9.main import Solver2017Day9
from Y2017.D10.main import Solver2017Day10
from Y2017.D11.main import Solver2017Day11
from Y2017.D12.main import Solver2017Day12
from Y2017.D13.main import Solver2017Day13
from Y2017.D14.main import Solver2017Day14
from Y2017.D15.main import Solver2017Day15
from Y2017.D16.main import Solver2017Day16
from Y2017.D17.main import Solver2017Day17
from Y2017.D18.main import Solver2017Day18
from Y2017.D19.main import Solver2017Day19
from Y2017.D20.main import Solver2017Day20
from Y2017.D21.main import Solver2017Day21
from Y2017.D22.main import Solver2017Day22
from Y2017.D23.main import Solver2017Day23
from Y2017.D24.main import Solver2017Day24
from Y2017.D25.main import Solver2017Day25
from Y2018.D1.main import Solver2018Day1
from Y2018.D2.main import Solver2018Day2
from Y2018.D3.main import Solver2018Day3
from Y2018.D4.main import Solver2018Day4
from Y2018.D5.main import Solver2018Day5
from Y2018.D6.main import Solver2018Day6
from Y2018.D7.main import Solver2018Day7
from Y2018.D8.main import Solver2018Day8
from Y2018.D9.main import Solver2018Day9
from Y2018.D10.main import Solver2018Day10
from Y2018.D11.main import Solver2018Day11
from Y2018.D12.main import Solver2018Day12
from Y2018.D13.main import Solver2018Day13
from Y2018.D14.main import Solver2018Day14
from Y2018.D15.main import Solver2018Day15
from Y2018.D16.main import Solver2018Day16
from Y2018.D17.main import Solver2018Day17
from Y2018.D18.main import Solver2018Day18
from Y2018.D19.main import Solver2018Day19
from Y2018.D20.main import Solver2018Day20
from Y2018.D21.main import Solver2018Day21
from Y2018.D22.main import Solver2018Day22
from Y2018.D23.main import Solver2018Day23
from Y2018.D24.main import Solver2018Day24
from Y2018.D25.main import Solver2018Day25
from time import time

from utils import get_data

st = time()
class_list = [Solver2015Day1, Solver2015Day2, Solver2015Day3, Solver2015Day4, Solver2015Day5, Solver2015Day6,
              Solver2015Day7, Solver2015Day8, Solver2015Day9, Solver2015Day10, Solver2015Day11, Solver2015Day12,
              Solver2015Day13, Solver2015Day14, Solver2015Day15, Solver2015Day16, Solver2015Day17, Solver2015Day18,
              Solver2015Day19, Solver2015Day20, Solver2015Day21, Solver2015Day22, Solver2015Day23, Solver2015Day24,
              Solver2015Day25, Solver2016Day1, Solver2016Day2, Solver2016Day3, Solver2016Day4, Solver2016Day5,
              Solver2016Day6, Solver2016Day7, Solver2016Day8, Solver2016Day9, Solver2016Day10, Solver2016Day11,
              Solver2016Day12, Solver2016Day13, Solver2016Day14, Solver2016Day15, Solver2016Day16, Solver2016Day17,
              Solver2016Day18, Solver2016Day19, Solver2016Day20, Solver2016Day21, Solver2016Day22, Solver2016Day23,
              Solver2016Day24, Solver2016Day25, Solver2017Day1, Solver2017Day2, Solver2017Day3, Solver2017Day4,
              Solver2017Day5, Solver2017Day6, Solver2017Day7, Solver2017Day8, Solver2017Day9, Solver2017Day10,
              Solver2017Day11, Solver2017Day12, Solver2017Day13, Solver2017Day14, Solver2017Day15, Solver2017Day16,
              Solver2017Day17, Solver2017Day18, Solver2017Day19, Solver2017Day20, Solver2017Day21, Solver2017Day22,
              Solver2017Day23, Solver2017Day24, Solver2017Day25, Solver2018Day1, Solver2018Day2, Solver2018Day3,
              Solver2018Day4, Solver2018Day5, Solver2018Day6, Solver2018Day7, Solver2018Day8, Solver2018Day9,
              Solver2018Day10, Solver2018Day11, Solver2018Day12, Solver2018Day13, Solver2018Day14, Solver2018Day15,
              Solver2018Day16, Solver2018Day17, Solver2018Day18, Solver2018Day19, Solver2018Day20, Solver2018Day21,
              Solver2018Day22, Solver2018Day23, Solver2018Day24, Solver2018Day25]
for clazz in class_list:
    if not (clazz.YEAR, clazz.DAY) >= (2018, 1):
        continue
    src = get_data(clazz.YEAR, clazz.DAY)
    sol = clazz(src)
    sol.run()
    print(clazz.YEAR, clazz.DAY)
    print(sol.solve_part_1(), sol.solve_part_2())
print(time() - st)
