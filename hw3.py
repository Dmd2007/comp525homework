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

def opposite_of_sum(numbers_list):
    """
    Sums up the numbers in numbers_list and finds the oppisite of the sum
    numbers_list: list of numbers
    Returns: the oppisite of the sum of the numbers in the numbers_list

    >>> opposite_of_sum([4,6,8,10,12,14])
    -54
    >>> opposite_of_sum([100,1000,10000,100000])
    -111100
    >>> opposite_of_sum([1234123,12341234123,1235123451324,134652341,2345623451,6785673465])
    -1256731868827
    """
    if not numbers_list:

        return None

    users_nums = 0

    for numbers in numbers_list:

        users_nums= users_nums + numbers
        opposite_sum = users_nums * -1

    return opposite_sum

    def opposite_keys(nums_dict):
    """
    Maps out the key values in a dictionary (num_dict) and finds the opposite of the
    numbers the user entered in the corresponding dictionary.
    num_list: list of numbers
    Returns: the average of the numbers in num_list. 
    If num_list is empty, return None

    >>> opposite_keys({1:2, 2:4, 3:6})
    {-1:2, -2:4, -3:6}
    >>> opposite_keys({10:20, 20:40, 30:60})
    {-10:20, -20:40, -30:60}
    >>> opposite_keys({100:200, 200:400, 300:600})
    {-100:200, -200:400, -300:600}
    """
    user_num = { }

    for nums in nums_dict:
        user_num[nums] = nums_dict[nums] * -1

    return 
    user_num








if __name__ == '__main__':

	import doctest
	doctest.testmod()