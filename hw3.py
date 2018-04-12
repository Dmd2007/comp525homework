"""
Homework 3
Dylan Durand
April 3rd, 2018
"""
def double_numbers(number_list):
    """
    Maps numbers in the number_list to double the value of original number.
    number_list: list of numbers.
    Returns: Double the values of the list of original numbers.

    >>> double_numbers([4,6,8])
    [8, 12, 16]

    >>> double_numbers([10,20,30])
    [20, 40, 60]

    >>> double_numbers([100,150,151])
    [200, 300, 302]
    """
    double_number = [ ]

    for number in number_list:

        double_number.append(2 * number)

    return double_number

def leave_lowercase_words(lowerwords_list):
    """
    Filters out words out of a list of strings that have uppercase
    letters.
    word_list: list of strings
    Returns: (strings) list of lowercase words with any words 
    with uppercase removed.  

    >>> leave_lowercase_words(['Hello','how','World','are','yEs','you'])
    ['how', 'are', 'you']

    >>> leave_lowercase_words(['Blue','blue','is','CooL','cooL','cool'])
    ['blue', 'is', 'cool']

    >>> leave_lowercase_words(['I','i ',' will','not','nO','NOT'])
    ['i ', ' will', 'not']
    """
    newwords = [ ]

    for lowerwords in lowerwords_list:

        if lowerwords.islower( ):

            newwords.append(lowerwords)

    return newwords









if __name__ == '__main__':

	import doctest
	doctest.testmod()