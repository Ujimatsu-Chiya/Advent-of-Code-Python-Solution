import re
from copy import deepcopy
from dataclasses import dataclass
from enum import auto, Enum
from itertools import count
from typing import FrozenSet

from utils import Solver, get_data


class Army(Enum):
    IMMUNE_SYSTEM = auto()
    INFECTION = auto()


class Damage(Enum):
    COLD = auto()
    FIRE = auto()
    SLASHING = auto()
    RADIATION = auto()
    BLUDGEONING = auto()


@dataclass
class Unit:
    army: Army
    count: int
    hp: int
    damage: int
    attack: Damage
    initiative: int
    weaknesses: FrozenSet[Damage] = frozenset()
    immunities: FrozenSet[Damage] = frozenset()

    def __hash__(self):
        return id(self)

    @property
    def effective_power(self):
        return self.count * self.damage

    def damage_dealt(self, other):
        if self.attack in other.immunities:
            return 0
        elif self.attack in other.weaknesses:
            return self.effective_power * 2
        else:
            return self.effective_power


class Solver2018Day24(Solver):
    YEAR = 2018
    DAY = 24

    def round(self, armies):
        targets = set()
        attacking = {}

        for unit in sorted(armies, key=lambda unit: (unit.effective_power, unit.initiative), reverse=True):
            if unit.count <= 0:
                continue
            enemies = [enemy for enemy in armies if enemy.army != unit.army]
            enemies = sorted(enemies,
                             key=lambda enemy: (unit.damage_dealt(enemy), enemy.effective_power, enemy.initiative),
                             reverse=True)
            target = next(
                (enemy for enemy in enemies if enemy.count > 0 and unit.damage_dealt(enemy) and enemy not in targets),
                None)
            if target:
                targets.add(target)
                attacking[unit] = target

        stalemate = True

        for unit in sorted(armies, key=lambda group: group.initiative, reverse=True):
            if unit.count > 0 and attacking.get(unit):
                target = attacking[unit]
                killed = min(unit.damage_dealt(target) // target.hp, target.count)

                if killed:
                    target.count -= killed
                    stalemate = False

        if stalemate:
            raise AttributeError

        return armies

    def fight(self, armies, boost=0):
        armies = deepcopy(armies)
        for group in armies:
            if group.army == Army.IMMUNE_SYSTEM:
                group.damage += boost
        while all(any(group.count for group in armies if group.army == army) for army in Army):
            armies = self.round(armies)
            armies = [unit for unit in armies if unit.count > 0]
        return armies

    def __init__(self, src):
        pat = re.compile(r'(\d+) units each with (\d+) hit points(?: \((.*?)\))?'
                         r' with an attack that does (\d+) (\w+) damage at initiative (\d+)')
        self.armies = []
        for group in src.strip().split('\n\n'):
            name, *units = group.splitlines()
            army = Army[name.replace(':', '').replace(' ', '_').upper()]
            for unit in units:
                count, hp, mods, damage, attack, initiative = pat.match(unit).groups()
                kwargs = {}
                if mods:
                    for mod in mods.split('; '):
                        modifier, _, types = mod.split(' ', 2)
                        damages = frozenset(Damage[damage.upper()] for damage in types.split(', '))
                        if modifier == 'weak':
                            kwargs['weaknesses'] = damages
                        elif modifier == 'immune':
                            kwargs['immunities'] = damages
                self.armies.append(Unit(army=army, count=int(count), hp=int(hp), damage=int(damage),
                                        attack=Damage[attack.upper()], initiative=int(initiative), **kwargs))

    def solve_part_1(self):
        result = self.fight(self.armies)
        return sum(group.count for group in result if group.army == Army.INFECTION)

    def solve_part_2(self):
        for boost in count(1):
            try:
                result = self.fight(self.armies, boost=boost)
            except AttributeError:
                continue
            else:
                if all(group.count == 0 for group in result if group.army == Army.INFECTION):
                    break
        return sum(group.count for group in result if group.army == Army.IMMUNE_SYSTEM)


if __name__ == "__main__":
    src = get_data(Solver2018Day24.YEAR, Solver2018Day24.DAY)
    sol = Solver2018Day24(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
