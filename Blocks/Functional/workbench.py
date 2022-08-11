from time import sleep

from Items.Resources.Wood import Wood
from base.functional import Functional
from Functions.choice_of import choice_of
import links


class Workbench(Functional):

    pic = 'W'

    def __init__(self):
        self.recipe = {Wood: 10, 'result': Workbench, 'place': Workbench}
        self.name = 'Workbench'
        self.type_ = 'Triger'
        self.desc = 'Something'

    def act(self, player):

        self.recipe = []

        player.in_the_process = self
        player.slots()

        item, player.idx, player.col, esc = choice_of(player.backpack, self.gen_strings(player), player.idx, player.col)

        if esc:
            player.in_the_process = None
            player.idx = 0

        selected_recipe = self.recipe[index-len(player.backpack)-1]

        chk = True

        for key in selected_recipe.keys():
            try:
                if not key in ('place', 'out'):
                    if self.resources_in_backpack[key] < selected_recipe[key]:
                        chk = False
            except KeyError:
                chk = False

        if chk:
            for resource in selected_recipe.keys():
                var = True
                for slot in player.backpack:
                    if type(slot) is list and var:
                        if type(slot[0]) == resource:
                            for _ in range(selected_recipe[resource]):
                                del slot[0]
                            var = False
                            break

            player.add_to_inventory(selected_recipe['out'])

        else:
            print('\nyou don\'t have enough resources')
            sleep(0.8)

    def gen_strings(self, player):

        self.resources_in_backpack = {}
        for slot in player.backpack:
            if slot:
                if type(slot) is list:
                    if slot[0].type_ == 'Resource':
                        if not type(slot[0]) in self.resources_in_backpack.keys():
                            self.resources_in_backpack[type(slot[0])] = len(slot)
                else:
                    if slot.type_== 'Resource':
                        if not type(slot) in self.resources_in_backpack.keys():
                            self.resources_in_backpack[type(slot)] = 1

        resources_in_player_recipes = {}
        for recipe in player.recipes:
            for resource in recipe.keys():
                if not resource in ('place', 'result'):
                    if not resource in resources_in_player_recipes.keys():
                        if recipe['place'] == type(self):
                            resources_in_player_recipes[resource] = player.recipes.index(recipe)

        recipes = []
        strings = []

        for res_b in self.resources_in_backpack.keys():
            if res_b in resources_in_player_recipes.keys():
                recipe = player.recipes[resources_in_player_recipes[res_b]]
                if not recipe in self.recipe:
                    self.recipe.append(recipe)

        for recipe in self.recipe:
            string = '' 
            var = False
            for key in recipe:
                if key == 'result':
                    result = recipe['result']
                    string += f' = {result.name}'
                    break
                elif not key == 'place':
                    if var:
                        plus = ' + '
                    else:
                        var = True
                        plus = ''
                    num = recipe[key]
                    string += f'{plus}{key.name} x{num}'
            if not string in strings:
                strings.insert(self.recipe.index(recipe), string)

        return strings

