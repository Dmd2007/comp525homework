"""
Homework 4
Dylan Durand
April 25th, 2018
"""
def count_empty_lines(source):
	"""
	Counts the iterations of empty lines in a txt file source 
	source: str (string has the name of text file)
	Returns: int
	"""
	number_line = 0 # counts the empty lines in txt file

	file_in = open(source)

	for line in file_in
		if line == '\n':
			number_line = number_line + 1
	file_in.close( )

	return number_line

def count_at_start(word, source):
	"""
	Counts the interations of lines that have a word in the begining of the line
	word: str
	source: str
	Returns: int
	"""
	count = 0

	file_in = open(source, 'r')

	for line in file_in
		list_words = line.split( )
		if list_words:
			if word == list_words[0]:
				count = count + 1
	file_in.close( )

	return count




if __name__ == '__main__':

	import doctest
	doctest.testmod()
