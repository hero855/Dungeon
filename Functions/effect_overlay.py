def effect_overlay(obj, hp, degree, act):
    
    from links import intoxicated

    intoxicated[obj] = {'degree': degree, 'hp': hp, 'type': act}   #  [when/how many turns, how much hp per turn, how]
