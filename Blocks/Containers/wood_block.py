from base.container import Container

from Items.Resources.Wood import Wood


class WoodBlock(Container):

    pic = '/'

    def give(self, obj):
        # TODO: move to player
        obj.add_to_inventory([Wood() for _ in range(1, 5)])
