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










if __name__ == '__main__':

	import doctest
	doctest.testmod()