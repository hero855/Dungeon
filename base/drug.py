from Functions.effect_overlay import effect_overlay


class Drug:

	def using(self, obj):
		effect_overlay(obj, self.degree, self.num, self.ability)
		obj.backpack.remove(self)
