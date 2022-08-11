import links


class Sword:
    """
    The main class for all swords.
    Adds the swords to the dictionary items,
    using the ancestor Item.
    """

    def start_using(self, player):
        if player.selected != self:
            if player.selected:
                player.selected.stop_using(player)
            player.backpack.remove_item(self)
            player.selected = self

    def using(self, player):
        pass

    def stop_using(self, player):
        """
        If the sword does not envisage
        the cessation of the use,
        he uses it.
        """

        player.backpack.add_to_inventory(self)
        player.selected = None

    def hit(self, obj, player):
        pass
