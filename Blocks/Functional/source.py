from termcolor import colored


class Source(object):
    
    pic = colored('£', 'blue')

    def act(self, player):

        if type(player) is Avatar:
            if player.count['Source'][0] == 40:
                player.hlt = player.full_hlt
                player.count['Source'][0] = 0
                player.mana = player.full_mana
                
                if player in intoxicated:
                    del intoxicated[player]