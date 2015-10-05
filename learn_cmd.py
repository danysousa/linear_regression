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
			print ("D'apres nos données ... c'est une poubelle : on vous donne " + str(result * -1) + "$ pour que vous la preniez")
		else:
			print ( "Estimated price : " + str(result) + "$" )

	def estimatePrice( self, mileage ):
		result = self.t0 + ( self.t1 * mileage )
		return (result)

	def updateTheta( self, dist, prices ):
		i = 0
		x = 0
		y = 0
		vx = 0
		cov = 0

		while ( i < len(dist) ):
			x += dist[i]
			y += prices[i]
			i += 1
		x = x / len(dist)
		y = y / len(prices)
		i = 0
		while ( i < len(dist) ):
			vx += (dist[i] - x) * (dist[i] - x)
			cov += (dist[i] - x) * (prices[i] - y)
			i += 1

		vx = vx / len(dist)
		cov = cov / len(dist)
		self.t1 = cov / vx
		self.t0 = y - self.t1 * x

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
		print("Success ! t0 = " + str(self.t0) + "   |   t1 = " + str(self.t1) )

	def do_tetha0( self, line ):
		"""tetha0
		Print tetha0"""
		print(self.t0)

	def do_tetha1( self, line ):
		"""tetha1
		Print tetha1"""
		print(self.t1)



