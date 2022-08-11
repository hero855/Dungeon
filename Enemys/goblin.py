from Enemys.metaEnemy import metaEnemy

from termcolor import colored

class Goblin(metaEnemy):
    
    des = colored('g', 'red')
    
    def __init__(self, row, elm, map_):
        self.row = row
        self.elm = elm
        self.map = map_
        super().__init__(
            self.row, 
            self.elm, 
            hlt=15, 
            dmg=5, 
            radius=4, 
            dodge_Atk=10, 
            dodge_MAtk=0, 
            chance_hit=70, 
            exp=3
        )
        self.list = ['move' for count in range(100)]