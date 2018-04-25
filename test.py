def double_dictionary {num_dict}
"""
>>>double_dictionary({1:2, 3:4, 5:6})
{1:4, 2:8, 5:12}
"""
result = {}

for num in num_dict:
	result[num] = num_dict[num] * 2
return result



if __name__ == '__main__':

	import doctest
	doctest.testmod()