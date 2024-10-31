# ```python
# # hill encryption algorithm
from numpy import *
import cipher


def oned_matrix_ptext(plain_text, key_matrix):
    # takes plain_text and key_matrix
    # passes 1d-array of indexes of plain text to matrix_operations()

    key_matrix = key_matrix.copy()  # deep copy
    upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowerCase = 'abcdefghijklmnopqrstuvwxyz'

    arr1 = list()  # arr1 list to store indexes of plain_text

    for i in plain_text:
        if i.isupper():
            for j in upperCase:
                if i == j:
                    arr1.append(upperCase.index(j))
                    break
        else:
            for j in lowerCase:
                if i == j:
                    arr1.append(lowerCase.index(j))
                    break

    matrix_dim = key_matrix.shape[0]
    arr1 = array(arr1)
    arr1 = arr1.reshape((matrix_dim, -1), order='F').T  # Convert to correct shape for multiplication

    encrypted_segment = matrix_operations(arr1, key_matrix)
    return index_to_letter(encrypted_segment)


def index_to_letter(index_list_ctext):
    index_list_ctext = index_list_ctext.copy()  # deep copy
    upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res_cy_text = list()
    for i in index_list_ctext:
        res_cy_text.append(upperCase[i])
    return "".join(res_cy_text)


def matrix_operations(matrix, key_matrix):
    # take 1d array of plain text as a argument from oned_matrix_ptext()
    # return 1d array of indexes of parse text

    matrix = matrix.copy()  # deep copy
    key_matrix = key_matrix.copy()  # deep copy

    res_matrix = dot(matrix, key_matrix)  # perform matrix multiplication(dot operation)
    res_matrix = res_matrix.flatten()
    res_matrix = list(map(lambda a: a % 26, res_matrix))  # perform mod 26 operations on res_matrix list

    return res_matrix  # return the ciphertext indexes


def encry_hill_impl(p_text, key_matrix):
    key_matrix = key_matrix.copy()  # deep copy
    a = key_matrix.shape[0]  # assigning the value of rows
    len_ptext = len(p_text)
    #global len_ptext# length of plain text
    num_extra_char = len_ptext % a  # extra characters at the end
    i = (len_ptext // a) + 1  # i segments of size a in plain text
    b, c = 0, a  # b,c will be used to fetch a string
    result_cypher = list()

    for j in range(i):
        if j == i - 1 and num_extra_char == 0 or j != i - 1:
            # j==i-1 and num_extra_char==0 -> indicates it is last segment and no extra characters
            # j!=i-1 -> indicates it is not last segment

            temp1 = p_text[b:c]
        else:  # else is for last segment which may or may not contain a characters

            temp1 = p_text[b:c]

            if num_extra_char != 0:
                for k in range(a - num_extra_char):
                    temp1 += 'x'
        b = c
        c += a
        cypher_str = oned_matrix_ptext(temp1, key_matrix)
        d,e=0,0#to print the characters instead of printing extra characters
        if not j==i-1:
            print(cypher_str)
        else:
            print(cypher_str[:num_extra_char])
        result_cypher.append(
            cypher_str)  # list of cypher text of a plaintext segment, which  will be passed to a oned_matrix_ptext()

    print(f"cipher text by using hill algorithm is {' '.join(result_cypher)}")


def adjoin_matrix(matrix):
    matrix = matrix.copy()

    pass


def determinant(matrix):
    matrix = matrix.copy()
    det = round(linalg.det(matrix))
    print(f" determinant of key1 : {det}")
    return det


key1 = array([[17, 17, 5],
              [21, 18, 21],
              [2, 2, 19]
              ])
# key1=matrix(key_matrix)
print(key1.shape)
print(f"key1 : {key1} ; id(key1) {type(key1)}  ")
p_text = list(input("enter the plain text :"))
encry_hill_impl(p_text, key1)


