from random import randint
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key
from os import system

from Functions.smart_input import smart_input
from Functions.choice_of import choice_of
from Generations.rooms import Room, Rooms, Corridor
import links
from items import Board
from Blocks.air import Air
from Blocks.Functional.posthumous_chest import PosthumousChest
from Blocks.Functional.workbench import Workbench
from Blocks.Containers.ground_block import GroundBlock
from base.creation_wand import CreationWand
from backpack import Backpack
from Generations.vector import Vector3


class Player(object):

    def __init__(self, area, room=True):
        self.selected = None
        self.focused_utility_block = None
        self.idx = 0
        self.col = 0

        self.status = list()
        self.used_items = list()
        self.recipe = [Workbench().recipe, Board().recipe]
        self.count = dict()  # {'self.name': [start, stop, stat(on/off), self]}
        self.chance = dict()  # {'event': chance}
        self.choices = None

        self.gold = 0

        self.pic = '0'

        self.full_hp = 10
        self.full_mp = 0

        self.mid_dmg = 2
        self.mid_m_dmg = 1

        self.dodge_Atk = 5
        self.dodge_MAtk = 1

        self.hit = 1
        self.armor = 0

        self.power = 1

        self.Atk = 1
        self.MAtk = 1
        self.Agi = 1
        self.Vit = 1
        self.Int = 1
        self.Dcs = 1
        self.Luc = 1

        self.Lvl = 1

        self.exp = 0
        self.exp_limit = 20

        self.Skill_points = 0

        self.crit = 0

        self.hp = self.full_hp
        self.mp = self.full_mp
        self.dmg = randint(self.mid_dmg - 1, self.mid_dmg + 1)
        self.m_dmg = randint(self.mid_m_dmg - 1, self.mid_m_dmg + 1)

        self.area = area
        self.map = self.area.map

        self.chance['dodge Atk'] = 100 - self.dodge_Atk
        self.chance['dodge MAtk'] = 100 - self.dodge_MAtk
        self.chance['hit'] = 100 - self.hit

        self.count['Source'] = [40, 0, 'on', None]

        self.z = 0
        self.y = 0
        self.x = 0

        # if room:
        #   Rooms(

        #     ['the initial room', 'room with the chest'],
        #     WIDTH=5, HEIGHT=5

        #     ).spawn(
        #         0,
        #       - 1, 
        #       - 1, 
        #       self.map
        #       )

        self.select = None
        self.head = None
        self.torso = None
        self.wings = None
        self.feet = None
        self.shoes = None
        self.rings = []

        self.backpack = Backpack('common', self)

        self.fall_var = False

        self.idx = 0

    def update(self):
        """
        Checks to see if all is in order with avatar
        """

        self.map[self.z][self.y][self.x] = self

        if self.exp >= self.exp_limit:
            self.Lvl += 1
            self.Skill_points += 3
            self.skill_up()
            if self.exp > self.exp_limit:
                exp = self.exp - self.exp_limit
            else:
                exp = 0
            self.exp = 0
            self.exp_limit = self.exp_limit * 2 + exp
            exp = 0

        for item in self.used_items:
            item.using(self)

        if self.hp <= 0:
            links.game = 'Game over'
            self.reset()

    def chk_walk(self, obj):
        return True

    @property
    def location(self):
        return Vector3(self.x, self.y, self.z)

    def fall(self):
        if self.fall_var and type(self.map[self.z - 1][self.y][self.x]) is Air:
            self.map[self.z][self.y][self.x] = Air()
            self.z -= 1
            self.fall_var = False
            self.map[self.z][self.y][self.x] = self

        if type(self.map[self.z - 1][self.y][self.x]) is Air:
            self.fall_var = True

    def reset(self):
        """
        Restart the level and Avatar
        """
        if self.selected:
            self.selected.use = False
        self.map[self.z][self.y][self.x] = PosthumousChest(self)
        self.z = 0
        self.y = 0
        self.x = 0
        for slot in self.backpack:
            slot = None
        self.hp = self.full_hp
        self.armor = self.full_armor
        self.mp = self.full_mp
        if self in links.intoxicated:
            del links.intoxicated[self]

    def open_inventory(self):
        """
        Shows the contents of the inventory,
        allows the player to view the data on the desired item,
        as well as to use this item
        """

        idx = 0
        slot = None

        while True:
            item, idx, col, esc = choice_of(self.backpack, idx=idx, slot=slot, obj=self, inv=True)

            self.slots()

            if esc:
                break

            if type(item) is list:
                item[0].start_using(self)
            elif item:
                item.start_using(self)
            elif self.select:
                self.select.stop_using(self)

    def stat(self):
        print(f'level:  {self.Lvl}')

        if self in links.intoxicated:
            print(*list(set(self.status)))

        print(f'''hp:     {self.hp}
            armor:  {self.armor}
            mp:     {self.mp}
            gold:   {self.gold}
            
              
            exp: {self.exp}/{self.exp_limit}
             
            ''')

    def recovery(self):
        if self.mp < self.full_mp:
            self.mp += 1
        for para in list(self.count):
            if self.count[para][3]:
                if self.count[para][2] == 'on':
                    if self.count[para][0] < self.count[para][1]:
                        self.count[para][0] += 1
                    elif self.count[para][0] > self.count[para][1]:
                        self.count[para][0] -= 1
                    elif self.count[para][0] == self.count[para][1]:
                        self.count[para][2] = 'off'

    def skill_tree(self, idx=False):

        skl_nams = ['Atk', 'MAtk', 'Agi', 'Vit', 'Int', 'Dcs', 'Luc']
        skls = [self.Atk, self.MAtk, self.Agi, self.Vit, self.Int, self.Dcs, self.Luc]

        count = 0

        for skl in skl_nams:
            dub_dot = ': ' if len(skl) == 3 else ':  '
            mark = ' <' if count == idx else ''

            print(f'{skl}{dub_dot}{skls[skl_nams.index(skl)]}{mark}')

            count += 1

        if not idx:
            smart_input({Key.enter: None})

    def skill_up(self):

        system('cls')

        skl_nams = ['Atk', 'MAtk', 'Agi', 'Vit', 'Int', 'Dcs', 'Luc']
        skls = [self.Atk, self.MAtk, self.Agi, self.Vit, self.Int, self.Dcs, self.Luc]

        idx = 0

        while self.Skill_points > 0:

            print(f'Skill points: {self.Skill_points}')

            self.skill_tree(idx)

            choices = {Key.up: 'up', Key.down: 'down', Key.enter: 'select', Key.esc: 'esc'}
            choice = smart_input(choices)

            if choice == 'esc':
                break

            elif choice == 'up':
                if idx > 0:
                    idx -= 1

            elif choice == 'down':
                if idx < len(skl_nams) - 1:
                    idx += 1

            elif choice == 'select':

                choice = skl_nams[idx]

                if choice == 'Atk':
                    self.Atk += 1
                    if self.Atk % 10 == 0:
                        self.mid_dmg += 20
                elif choice == 'MAtk':
                    self.MAtk += 1
                    self.mid_m_dmg += 100
                elif choice == 'Agi':
                    self.Agi += 1
                elif choice == 'Vit':
                    self.Vit += 1
                    if self.Vit % 10 == 0:
                        self.hp += 10
                elif choice == 'Int':
                    self.Int += 1
                    if self.Int % 10 == 0:
                        self.mid_m_dmg += 5
                elif choice == 'Dcs':
                    self.Dcs += 1
                elif choice == 'Luc':
                    self.Luc += 1

                self.Skill_points -= 1

            system('cls')

        system('cls')

        self.skill_tree()

        system('cls')

    def locate(self, dir_):

        if self.select:

            row = self.y
            elm = self.x

            if dir_ == 'up':
                row -= 1
            elif dir_ == 'right':
                elm += 1
            elif dir_ == 'down':
                row += 1
            elif dir_ == 'left':
                elm -= 1

            if self.select.type_ == 'Trigger':
                if type(self.select) is list:
                    self.map[row][elm] = self.select[0]
                    if len(self.select) > 1:
                        del self.select[0]
                    else:
                        self.select = None
                else:
                    self.map[row][elm] = self.select
                    self.select = None

    def crity(self):
        if self.select and randint(1, 100) in range(self.crit):
            self.dmg = 2 * randint(self.mid_dmg - 1, self.mid_dmg + 1)
        else:
            self.dmg = randint(self.mid_dmg - 1, self.mid_dmg + 1)

    def get_hit(self, dmg):
        if randint(1, 100) in range(self.chance['dodge Atk']) and self.armor < dmg:
            self.hp -= dmg - self.armor
            print(f'get damage: {dmg - self.armor}')
            smart_input({Key.enter: None})
        else:
            print('miss')
            smart_input({Key.enter: None})

    def give_hit(self, obj, lay, row, elm):
        if isinstance(self.selected, CreationWand):
            self.selected.locate(lay, row, elm, self.map)

        elif randint(1, 100) in range(self.chance['hit']):
            self.selected.hit(obj, self)

        else:
            print('miss')
            sleep(0.3)
