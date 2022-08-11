from base.functional import Functional


class Door(Functional):
    """open-close-open-close"""

    def __init__(self, stat=False):
        self.name = 'Door'
        self.type_ = 'Triger'
        self.desc = 'Something'
        self.stat = stat
        if not self.stat:
            self.pic = '<'
        else:
            self.pic = '>'

    def act(self, player):
        if not self.stat:
            self.stat = True
            self.pic = '>'
        else:
            self.stat = False
            self.pic = '<'

    def walk(self, choice, player):
        """
        Helps the subject walk on it.
        """

        if self.stat:

            location = player.location
            player.area.map[location['row']][location['elm']] = player.memo()
            player.memo = type(self)
            if choice == 'up':
                player.row -= 1
            elif choice == 'right':
                player.elm += 1
            elif choice == 'down':
                player.row += 1
            elif choice == 'left':
                player.elm -= 1
