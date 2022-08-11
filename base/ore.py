class Ore (object):

    def melting(self, oven, player, index):

        player.backpack[index].remove(self)

        for slot in oven.slots:
            if len(slot) == 0:
                slot.append(self.out())
                break
            elif type(slot[0]) is GoldBar:
                slot.append(self.out())
                break