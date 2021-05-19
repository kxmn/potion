
class Tester :
	pass

class A :
	value = 1

	@staticmethod
	def add () :
		"""
		@staticmethod, avoid the instance argument to be passed on call
		"""
		A.value +=1

	def __init__ (Self) :
		pass

class B :
	value = 1

	@classmethod
	def add ( Self ) :
		Self.value +=1

	def __new__ ( Cls ) :
		"""
		Triggered on class execution before __init__
		Cls refers to static class. Automattically passed
		"""
		return Cls

	def __init__ ( Self ) :
		"""
		Triggered on class execution, after __new__
		Self refers to instance ( differently of Cls of __new__  )
		"""
		pass



# With iA.add() the instance changes his own static class
iA = A()
iA.add()
print (A.value, iA.value)

# With iB.add() The instance changes only his own instance
iB = B()
iB.add()
print (B.value, iB.value)
