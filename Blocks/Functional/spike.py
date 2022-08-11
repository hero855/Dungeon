from random import randint
from termcolor import colored

from Blocks.air import Air
from base.functional import Functional
from Functions.effect_overlay import effect_overlay


class Spike(Functional):
    
    pic = Air.pic

    def __init__(self):
        self.name = 'Spike'
        self.type_ = 'Triger'
        self.desc = 'Something'
        self.activate = False

    def walk(self, choice, player):

        dmg = randint(1, 3)
        degree = randint(1, 15)

        if not self.activate:
            self.pic = colored('^', 'red')
            self.activate = True
        
        player.get_hit(dmg)
        
        if randint(0, 100) in range(20):
            effect_overlay(player, dmg, degree, 'spike hlt down')

    def act(self, player, dir_):
        """
        Breaks the block
        """

        row = player.row
        elm = player.elm

        if dir_ == 'up':
            row -= 1
        elif dir_ == 'right':
            elm += 1
        elif dir_ == 'down':
            row += 1
        elif dir_ == 'left':
            elm -= 1

        player.map[row][elm] = ()
