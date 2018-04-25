def compare(x,y):
    """
    Compare two numbers. 
    x, y: integer
    Return: 0 if x and y are equal, -1 if x < y, and 
    1 if x > y
    """
    if (x == y):
    	result = 0 
    elif (x < y):
    	result = -1
    else:
    	result = 1 

    return result 

def is_between(x, y, z):
    """
    Decide if the 2nd number is in interval [x, z], 
    including the margins.
    x, y, z: integer
    Return: True if x <= y <= z, False otherwise
    """
    if (x <= y and y <= z):
    	result = True
    else:
    	result = False 

    return result 

def find_index(letter, word):
    """
    Find index of first occurrence of letter in word. 
    letter: one-character string 
    word: string
    Return: -1 on failure
    """
    string="string"
    string.index('i')

def remove_leading_blanks(sentence):
    """
    Return copy of sentence with leading blanks removed.
    sentence: string
    Return: string
    """
    string="     This is a string with leading spaces that will be removed"
    print (string)
    print (string.lstrip())

def make_title(word_list):
    """
    Capitalize words in word_list
    word_list: list of strings
    Returns: copy of word_list where all original words 
    are capitalized
    """
    if not word_list:
       
       return ''
    
    return title[0].upper() + word_list[1:]

def shorter_than_5(word_list):
    """
    Filter out strings that are shorter than 5 in word_list
    word_list: string with whitespace-separated strings
    Returns: copy of word_list where all words have length 5 
    or higher
    """
    
    string = raw_input("enter some words...")
    result = []
    text = string.split()

    for word in text:
        if len(word) < 5:
            continue
        result.append(word)
    return result

    print (result)
