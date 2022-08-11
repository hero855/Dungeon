from termcolor import colored
from pynput.keyboard import Key

from Functions.smart_input import smart_input
from base.functional import Functional
import links


class Table(Functional):
    """
    Plaque with the inscription
    """

    pic = colored('=', 'yellow')

    def __init__(self, text=None):
        self.name = 'Table'
        self.type_ = 'Triger'
        self.text = text or input('Text: ')

    def act(self, player):
        """
        Shows the inscription on the plate
        """
        print(self.text)
        smart_input({
            Key.enter: '',
            Key.esc: ''
        })
