from random import randint

from base.container import Container


class GroundBlock(Container):
    """
    On the ground you can walk,
    of course, if it's not spike.
    """

    pic = '■'
    type_ = 'Block'
    name = 'ground'

    def give(self, obj):
        obj.add_to_inventory([GroundBlock()])
