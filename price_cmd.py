import cmd
import sys

class PriceCmd(cmd.Cmd):

	def __init__(self):
		super(PriceCmd, self).__init__()
		self.prompt = "$>"
		self.t0 = 0
		self.t1 = 0
		self.max = 1
		if ( len(sys.argv) == 3 ):
			self.t0 = float(sys.argv[1])
			self.t1 = float(sys.argv[2])
		else :
			self.read_file()

	def do_exit( self, arg ):
		exit(0)

	def read_file(self):
		f = open(".tmpFile", 'r')
		self.t0 = float(f.readline())
		self.t1 = float(f.readline())
		self.max = float(f.readline())

	def default( self, mileage ):
		# super(PriceCmd, self).default(mileage)
		if ( mileage.isdigit() == False ):
			print ("I don't understand your language")
			return

		m = float(mileage) / self.max
		result = self.t0 + ( self.t1 * m )
		print ( "Estimated price : " + str(result) + "$" )
