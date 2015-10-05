import cmd
import sys

class PriceCmd(cmd.Cmd):

	def __init__(self):
		super(PriceCmd, self).__init__()
		self.prompt = "$>"
		self.t0 = 0
		self.t1 = 0
		if ( len(sys.argv) == 3 ):
			self.t0 = float(sys.argv[1])
			self.t1 = float(sys.argv[2])

	def do_exit( self, arg ):
		exit(0)

	def default( self, mileage ):
		# super(PriceCmd, self).default(mileage)
		if ( mileage.isdigit() == False ):
			print ("I don't understand your language")
			return

		m = float(mileage)
		result = self.t0 + ( self.t1 * m )
		print ( "Estimated price : " + str(result) + "$" )