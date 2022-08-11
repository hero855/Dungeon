class CreationWand:
	
	def using(self, player):
		if player.selected != self:
			if player.selected:
				player.selected.stop_using(obj)
			player.backpack.remove_item(self)
			player.selected = self


	def locate(self, lay, row, elm, map_):
		map_[row][elm] = self.block()
		

	def stop_using(self, obj):
		obj.add_to_inventory(self)
		obj.selected = None
		self.use = False

