from random import randint
from base.resource import Resource


class Backpack:

    def __init__(self, rarity, player):
        self.player = player
        if rarity == 'common':
            self.__items = [None for _ in range(randint( 5,  10))]
        elif rarity == 'rare':
            self.__items = [None for _ in range(randint(10,  20))]
        elif rarity == 'Epic':
            self.__items = [None for _ in range(randint(20,  50))]
        elif rarity == 'GODLY':
            self.__items = [None for _ in range(randint(50, 100))]

    def clear(self):
        for idx in range(len(self.__items)):
            if not self.__items[idx]:
                self.__items[idx] = None

    def add_to_inventory(self, *items):

        for item in items:

            base = item
            cont = True
            types = {'Helmet': 'head', 'Cuirass': 'body', 'Wings': 'wings', 'Leggings': 'feet', 'Shoes': 'shoes'}

            if item and type(item) is list:
                base = item[0]

            if hasattr(tmp, 'recipe') and not tmp.recipe in self.recipe:
                self.recipe.append(tmp.recipe)
            
            if base:
                if isinstance(base, ('Resource', 'Drug', 'Block')):
                    if not type(item) is list: item = [item]
                    for index in range(len(self.backpack)):
                        slot = self.backpack[index]
                        if type(slot) is list:
                            if type(slot[0]) == type(tmp):
                                self.backpack[index].extend(item)
                                cont = False
                    if cont and None in self.backpack:
                        self.backpack[self.backpack.index(None)] = item
                    continue

                elif tmp.type_ in tmp_dict.keys():
                    if self.get(tmp_dict[tmp.type_]) == None:
                        item.using(self)
                elif None in self.backpack:
                    self.backpack[self.backpack.index(None)] = item
                else:
                    print('inventory is full')
                    sleep(0.4)
                    break

    def remove_from_inventory(self, *items):

        for item in items:

            tmp = item
            cont = True
            tmp_dict = {'Helmet': 'head', 'Cuirass': 'body', 'Wings': 'wings', 'Leggings': 'feet', 'Shoes': 'shoes'}

            if type(item) is list:
                tmp = item[0]

            if tmp:
                if tmp.type_ in ('Resource', 'Drug', 'Block'):
                    if not type(item) is list: item = [item]
                    for idx in range(len(self.backpack)):
                        slot = self.backpack[idx]
                        if type(slot) is list:
                            if type(slot[0]) == type(tmp):
                                for _ in range(len(item)):
                                    self.backpack[idx].remove(self.backpack[idx][0])
                                cont = False
                    if cont and item in self.backpack:
                        self.backpack[self.backpack.index(item)] = None
                    continue

                elif tmp.type_ in tmp_dict.keys():
                    attr = getattr(self, tmp_dict[tmp.type_])
                    if attr == item:
                        self.__dict__[tmp_dict[tmp.type_]] = None
                elif item in self.backpack:
                    self.backpack[self.backpack.index(item)] = None

