from base.container import Container

class Wall(Container):
    '''
    An impregnable barrier to the object.
    '''
    
    pic = 'X'

    def give(self, obj):
        obj.add_to_inventory(Wall())