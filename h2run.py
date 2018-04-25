"""
	Homework2run
	Dylan Durand
	3/21/18
"""
import hw2

def run_compare( ):
	"""
	test cases if x == y, x < y, x > y
	"""
	result = hw2.compare(1,2)
	print('compare({}, {} --> {}'.format(1,2, result))

	result = hw2.compare(2,1)
	print('compare({}, {} --> {}'.format(2,1, result))

	result = hw2.compare(1,1)
	print('compare({}, {} --> {}'.format(2,1, result))


