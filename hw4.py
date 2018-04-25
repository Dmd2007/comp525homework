"""
lab 7
Dylan Durand
April 4th, 2018

"""
def all_greetings_greater_3(greeting_histogram):
""" 
reduces greeting_histogram by summing up frequencies of greetings
of greater than 3
greeting _histogram: dictionary with greeting strings as keys
and numerical frequencies as values

Returns: (integer) sum of frequencies of greetings greater than 3

>>>all_greeting_greater_3 ({'hi': 5, 'bye': 10,'hola':23,'good morning':0})
>>>all_greeting_greater_3(d)
>>>d
"""
	total = 0
	for k in greeting_histogram:
		if len(k) > 3:
			total = total + greeting_histogram[k]
	return total


if __name__ == '__main__':

	import doctest
	doctest.testmod()
