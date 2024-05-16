import os

import requests


class Solver:
    def solve_part_1(self):
        raise NotImplementedError()

    def solve_part_2(self):
        raise NotImplementedError()

    def run(self):
        pass


def get_data(year: int, day: int) -> str:
    root = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(root, 'Y{}/D{}/input.txt'.format(year, day))
    if not os.path.exists(input_path):
        session = open(os.path.join(root, '.session')).read().strip()
        input_url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
        cookies = {'session': session}
        src = requests.get(input_url, cookies=cookies).text
        with open(input_path, 'w+') as fp:
            fp.write(src)
    return open(input_path).read()


if __name__ == "__main__":
    current_path = os.path.abspath(__file__)
