class oneThing:
	pass

class twoThing:
	def func1(self):
		self.one = 1
		two = 2
		print('ran')


a = oneThing()
b = twoThing()
print(a)
print(b)

c = {oneThing:3,twoThing:4}
print(c)
print(c.keys())

b.func1()
print(b.one)


