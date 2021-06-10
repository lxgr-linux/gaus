#!/usr/bin/env python3

class Formular:
	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def change(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def print(self):
		print(f"{self.a}x + {self.b}y + {self.c}z = {self.d}")

	def stage(self, fac, f):
		self.change(*(eval(f"f.{i}-fac*self.{i}", {"fac": fac, "f": f, "self":self}) for i in ["a", "b", "c", "d"]))

	def first_stage(self, f1):
		self.stage(f1.a/self.a, f1)

	def second_stage(self, f2):
		self.stage(f2.b/self.b, f2)


f1 = Formular(4, -2, 2, 2)
f2 = Formular(-2, 3, -2, 0)
f3 = Formular(3, -5, 1, -7)

for i in [f1, f2, f3]:
	i.print()
print()

f1.print()
f2.first_stage(f1)
f2.print()
f3.first_stage(f1)
f3.print()
print()

f1.print()
f2.print()
f3.second_stage(f2)
f3.print()

print()
z = round(f3.d/f3.c, 10)
print(f"z = {z}")

y = round((f2.d-f2.c*z)/f2.b, 10)
print(f"y = {y}")

x = round((f1.d-f1.c*z-f1.b*y)/f1.a, 10)
print(f"x = {x}")
