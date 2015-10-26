import cmd
import sys

class LearnCmd(cmd.Cmd):

	def __init__(self):
		super(LearnCmd, self).__init__()
		self.prompt = "$>"
		self.t0 = 0
		self.t1 = 0
		self.prices = []
		self.dist = []
		self.max = 0

	def do_exit( self, arg ):
		"""exit
		Exit the program"""
		exit(0)

	def do_price( self, mileage ):
		"""price [mileage]
		Print the estimate price for the given mileage"""
		if ( mileage.isdigit() == False ):
			print ("Usage : price [mileage]")
			return

		result = self.estimatePrice(float(mileage))
		if ( result == -1 ):
			print ("I don't understand your language")
			return
		if ( result < 0 ):
			print ("D'apres nos données ... c'est une poubelle : " + str(result) + "$")
		else:
			print ( "Estimated price : " + str(result) + "$" )

	def estimatePrice( self, mileage ):
		result = self.t0 + ( self.t1 * self.normalize(mileage) )
		return (result)

	def setMax(self, l):
		tmp = 0
		i = 0
		while (i < len(l)):
			tmp = l[i] if l[i] > tmp else tmp
			i += 1
		self.max = tmp

	def normalize(self, value):
		return (value / self.max)

	def updateTheta( self, dist, prices ):
		tmp = None
		self.setMax(dist)
		alpha = 0.01
		while 42 :
			i = 0
			X = 0
			Y = 0
			while (i < len(dist)):
				Y += (self.estimatePrice(dist[i]) - prices[i])
				X += ((self.estimatePrice(dist[i]) - prices[i]) * (self.normalize(dist[i])))
				i += 1
			X = X / len(dist)
			Y = Y / len(dist)
			print (X)
			if (tmp != None and abs(tmp) < abs(X)):
				alpha /= 10
			elif (tmp != None and abs(tmp) > abs(X)):
				alpha *= 2
			self.t0 = self.t0 - (alpha * Y)
			self.t1 = self.t1 - (alpha * X)
			tmp = X
			if (abs(X) < 0.001):
				break

	def do_import( self, filename ):
		"""import [file]
		Import dataset and update tetha0 & tetha1"""
		try:
			fd = open(filename, 'r')
		except Exception:
			print("Error with " + filename + " file")
			return

		firstLine = True
		for line in fd:
			line = line.rstrip('\n')
			if ( firstLine == True and line != "km,price" ):
				print ("Your file isn't supported")
				firstLine = False
				return
			if ( firstLine == True ):
				firstLine = False
				continue
			tmp = line.split(",")
			if ( len(tmp) != 2 or tmp[0].isdigit() == False or tmp[1].isdigit() == False ):
				print ("Parse error, check your file")
				return
			self.dist.append( float(tmp[0]) )
			self.prices.append( float(tmp[1]) )
		self.updateTheta( self.dist, self.prices )
		print("Success ! t0 = " + str(self.t0) + "   |   t1 = " + str(self.t1) + "\nWith max = " + str(self.max) )
		self.save_in_file()

	def save_in_file(self):
		f = open('.tmpFile', 'w')
		f.write(str(self.t0) + "\n")
		f.write(str(self.t1) + "\n")
		f.write(str(self.max) + "\n")


	def do_tetha0( self, line ):
		"""tetha0
		Print tetha0"""
		print(self.t0)

	def do_tetha1( self, line ):
		"""tetha1
		Print tetha1"""
		print(self.t1)



