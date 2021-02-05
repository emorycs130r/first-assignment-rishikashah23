
'''

This file contains the functions that you need for completing this assignment. 

1. append_two_strings() --> Function to append a string2 to string1. -- 30%
2. append_character() --> Function to append a character to the end of string. -- 30% 
3. append_num_to_string() --> Function to append a number to the end of a string. -- 40%

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def append_two_strings(string_1, string_2):

    result = string_1 + string_2
    return result


def append_character(string_1, char_1):

    result = string_1 + char_1
    return result


def append_num_to_string(string_1, num_1):

    result = string_1 + num_1
    return result


if __name__ == "__main__":
    
    val_11 = input("Enter a string: ")
    val_12 = input("Enter another string: ")
    val_1 = append_two_strings(val_11, val_12)
    print(val_1)

    val_21 = input("Enter a string: ")
    val_22 = input("Enter character: ")
    val_2 = append_character(val_21, val_22)
    print(val_2)

    val_31 = input("Enter a string: ")
    val_32 = input("Enter a number: ")
    val_3 = append_num_to_string(val_31, val_32)
    print(val_3)
