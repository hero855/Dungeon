from termcolor import colored
from pynput.keyboard import Key

from Functions.smart_input import smart_input
from base.functional import Functional
import links


class Simulator(Functional):
    
    pic = colored('{', 'yellow')

    name = 'Simulator'
    desc = 'Something'
    
    def get_hit(self, dmg, player):
        print('Taked domage:', dmg)
        smart_input({Key.enter: None})
