from Blocks.air import Air

class Container:

	def destroy(self, obj, lay, row, elm):
		self.give(obj)
		obj.map[lay][row][elm] = Air()

