#!/usr/bin/env python3

'''
    Author: David Pruiit & Jose Eduardo Soto
    
'''
import argparse
import numpy as np

def genMatrix(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = [[value for col in range(0,size)] for row in range(0,size)]

    return matrix

def genMatrix2(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """

    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix

def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """

    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]} ' , end='')
        print('')

def writeToFile(matrix, fileName):
    """
    Writes a matrix out to a file
    """

    with open(fileName, 'w') as file:
        for row in matrix:
            for col in row:
                file.write(f'{col} ')
            file.write('\n')

def readFromFile(fileName):
    """
    Reads a matrix from a file
    """

    matrix = []

    with open(fileName, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)

    return matrix

def multiply(firstMatrix, secondMatrix):
    '''
    Returns the product of two martrixes
    '''

    '''
    1.Assert that column size of the first matrix is equal to the row size of the
    second matrix.
    '''
    print('First matrix row size:\t' + str(len(firstMatrix[0]) + '\n' +
        'Second matrix column size:\t' +
        str(len(secondMatrix))))
    if len(firstMatrix[0]) == len(secondMatrix):
        
    '''
    2. Make an empty matrix the size of (row size of the first matrix, column 
    size of the second matrix).
    '''
        matrix = np.zeros((len(firstMatrix), len(secondMatrix[0])))
        print('Product matrix is (' + len(firstMatrix) + ',' +
              len(secondMatrix[0]) + ')')
    '''
    3. Fill the product matrix with values.
    '''
        
    
    matrix = []

    
    
    return matrix

def main():
    """
    Used for running as a script
    """

    parser = argparse.ArgumentParser(description=
        'Generate a 2d matrix and save it to  a file.')
    parser.add_argument('-s', '--size', default=1024, type=int,
        help='Size of the 2d matrix to generate')
    parser.add_argument('-v', '--value', default=1, type=int,
        help='The value with which to fill the array with')
    parser.add_argument('-f', '--filename',
        help='The name of the file to save the matrix in (optional)')
    parser.add_argument('-a', '--first_matrix_filename',
        help='First multiple of multiply operation')
    parser.add_argument('-b', '--second_matrix_filename',
        help='Second multiple of multiply operation')

    args = parser.parse_args()

    mat = None
    first_matrix = None
    second_matrix = None

    if (args.first_matrix_filename is not None) and (args.second_matrix_filename):
        first_matrix = readFromFile(args.first_matrix_filename)
        second_matrix = readFromFile(args.second_matrix_filename)
        mat = multiply(first_matrix, second_matrix)
    else:
        mat = genMatrix(args.size, args.value)
    
    if args.filename is not None:
        print(f'Writing matrix to {args.filename}')
        writeToFile(mat, args.filename)

        print(f'Testing file')
        printSubarray(readFromFile(args.filename))
    else:
        printSubarray(mat)
            

if __name__ == '__main__':
    # execute only if run as a script
    main()
