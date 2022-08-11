from links import intoxicated


def effect():
    for obj in intoxicated.keys():

        degree = intoxicated[obj]['degree']
        type_ = intoxicated[obj]['type']
        hp = intoxicated[obj]['hp']

        if degree == 'WS':  # WTS - while selected
            try:
                if obj.selected == intoxicated[obj]['item']:
                    pass
                else:
                    del intoxicated[obj]
                    break
            except KeyError:
                intoxicated[obj]['item'] = obj.selected

        elif degree > 0:
            intoxicated[obj]['degree'] -= 1

        else:
            del intoxicated[obj]

        if type_ == 'spike hp down':
            obj.hp -= hp
            if 'intoxicated' not in obj.status:
                obj.status.append('intoxicated')
        elif type_ == 'potion hp up' and obj.hp < obj.full_hp:
            if obj.hp + hp < obj.full_hp:
                obj.hp += hp
            else:
                for count in range(hp):
                    if obj.hp < obj.full_hp:
                        obj.hp += 1
                    else:
                        break
            if 'regenerated' not in obj.status:
                obj.status.append('regenerated')
        elif type_ == 'set fire':
            obj.hp -= hp
            if 'set on fire' not in obj.status:
                obj.status.append('set on fire')
