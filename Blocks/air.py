from termcolor import colored

class Air:
    colors = ['white', 'yellow', 'green', 'red', 'blue', 'magenta', 'cyan']

    # TODO: Remove Air and replace with None object
    def pic(self, z, y, x, map_):
        for count in range(1, 10):
            cell = map_[z - count, y, x]
            if isinstance(cell, type(None)):
                return ' '
            if not isinstance(cell, Air) and count < len(self.colors):
                if count < len(self.colors):
                    return colored(cell.pic, self.colors[count - 1])
                else:
                    return colored(cell.pic, 'grey')
            

    def walk(self, player, z, y, x):

        player.map[player.z, player.y, player.x] = self

        player.z = z
        player.y = y
        player.x = x
