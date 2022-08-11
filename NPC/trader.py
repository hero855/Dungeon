from os import system
from pynput.keyboard import Key

from meta.npc import NPC
from links import items
from Functions.smart_input import smart_input

class Trader(NPC):
    
    stat = False
    des = '$'

    items = [None for _ in range(10)]
    
    # def __init__(self):
    #   self.generator()

    # def generator(self):

    def choice_item(self, obj):

        idx = 0

        while True:

            clear()

            choice = choice_of(obj.backpack, self.items, idx=idx)

            if choice == 'esc': break

            if lst == 'sec':

                if type(item) is list:
                    item[0].print_details()

                elif item:
                    item.print_details()

                else: continue

                print('\nGet?')

                choices = {Key.enter: True, 
                             Key.esc:   False}

                answer = smart_input(choices)
                
                if answer:
                    obj.add_to_inventory(item)
                    self.items[index-len(obj.backpack)-1] = None

            elif lst == 'fst':

                if None in self.items:
                    self.items[self.items.index(None)] = item
                    obj.backpack[index-1] = None
                    obj.gold += item.cost

    def act(self, obj):

        index = 0

        while True:
            system('cls')
            print('Здравствуй, одинокий путник! С чем ты ко мне пожаловал?')
            questions = ['Что у тебя есть на продажу?', 'Есть ли для меня задание?']
            for qun in questions:
                if index == questions.index(qun):
                    mark = ' <'
                else:
                    mark = str()
                print(f'{qun}{mark}')

            choices = {Key.up:    'up', 
                         Key.down:  'down', 
                         Key.enter: 'select', 
                         Key.esc:   'esc'}

            choice = smart_input(choices)

            if choice == 'esc': break
            elif choice == 'up':
                if index > 0:
                    index -= 1
            elif choice == 'down':
                if index < len(questions)-1:
                    index += 1
            elif choice == 'select':
                if index == 0:
                    pass
