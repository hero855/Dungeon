from base.resource import Resource
from base.ore import Ore
from base.drug import Drug
from base.creation_wand import CreationWand
from base.sword import Sword
from Blocks.Functional.workbench import Workbench
from Blocks.Containers.stone_block import StoneBlock
from Blocks.Containers.gold_ore_block import GoldOreBlock
from Functions.effect_overlay import effect_overlay


class SmallHealthDrug(Drug):
    name = 'Small health drug'
    num = 5
    degree = 3
    ability = 'drug hlt up'
    coast = 150
    rarity = 'common'


class MediumHealthDrug(Drug):
    name = 'Medium health drug'
    num = 15
    degree = 4
    ability = 'drug hlt up'
    coast = 500
    rarity = 'common'


class BrokenBoard(Resource):
    name = 'Broken Board'
    rarity = 'common'


class Board(Resource):
    name = 'Board'
    rarity = 'common'
    recipe = {BrokenBoard: 2,
              'num': 1,
              'place': Workbench}


class IronBar(Resource):
    name = 'Iron bar'
    rarity = 'rare'


class IronOre(Resource, Ore):
    name = 'Iron ore'
    rarity = 'rare'
    out = IronBar


class GoldBar(Resource):
    name = 'Gold bar'
    rarity = 'rare'


class GoldOre(Resource, Ore):
    name = 'Gold ore'
    rarity = 'rare'
    out = GoldBar


class RawStone(Resource):
    name = 'Raw stone'
    rarity = 'common'


class Stone(Resource):
    name = 'Stone'
    rarity = 'common'
    recipe = {RawStone: 6,
              'num': 1,
              'place': Workbench}


class StoneCreationWand(CreationWand):
    name = 'stone creation wand'
    rarity = 'Epic'
    block = StoneBlock


class GoldOreCreationWand(CreationWand):
    name = 'gold ore creation wand'
    rarity = 'GODLY'
    block = GoldOreBlock


class BrokenSword(Sword):
    name = 'Broken sword'
    dmg = 2
    rarity = 'common'
    critical = 0
    # TODO: BREAK


class FierySword(Sword):
    name = 'Fiery sword'
    dmg = 5
    critical = 0
    rarity = 'common'

    def effect(self, obj):
        effect_overlay(obj, 2, 'WS', 'set fire')


class RustyBlade(Sword):
    name = 'Rusty Blade'
    dmg = 2
    critical = 0
    rarity = 'common'
    effect = None


class IronSword(Sword):
    name = 'IronSword'
    recipe = {Board: 2, IronBar: 4, 'num': 1, 'place': Workbench}
    dmg = 10
    critical = 5
    rarity = 'common'
    effect = None


IronSword.recipe['out'] = IronSword


class SwordRecovery1(Sword):
    name = 'Sword recovery 1'
    desc = 'For each enemy killed restores 5 HP'
    dmg = 2
    critical = 0
    rarity = 'rare'
    effect = 'recovery'
