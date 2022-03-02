from typing import List

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v,w)]
assert add([1,2,3], [4,5,6])== [5,7,9]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v,w)]
assert subtract([5,7,9], [4,5,6])== [1,2,3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2], [3,4], [5,6]])== [3,4]


def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v,w))
assert dot([1,2,3], [4,5,6])== 32 #1 * 4 + 2 * 5 + 3 * 6 


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)
assert sum_of_squares([1,2,3])== 14 # 1 * 1 + 2 * 2 + 3 * 3

import math

def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))   # math.sqrt is square root function
assert magnitude([3,4])== 5

def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))


def distance(v: Vector, w: Vector) -> float:  # type: ignore
    return magnitude(subtract(v, w))

#Another type alias
Matrix = List[List[float]]

A = [[1,2,3],
     [4,5,6]]
B = [[1,2],
     [3,4],
     [5,6]]

from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 #number of elements in first row
    return num_rows, num_cols

def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]

def get_column(A: Matrix, j:int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return[A_i[j]
           for A_i in A]

from typing import Callable 

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i,j)
    """
    return [[entry_fn(i,j)
             for j in range(num_cols)]
            for i in range(num_rows)]

def identity_matriz(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matriz(n, n, lambda i, j: 1 if i == j else 0)
assert identity_matrix(5) == [[1,0,0,0,0],
                              [0,1,0,0,0],
                              [0,0,1,0,0],
                              [0,0,0,1,0],
                              [0,0,0,0,1]]


assert add([1, 2, 3], [10,9,8]) == [11,11,11], "something wrong with add()"
assert subtract([11,11,11], [1, 2, 3]) == [10,9,8], "trouble with subtract()"
assert vector_sum([[3,4], [5,6], [7,8]]) == [15, 18], "vector_sum() problem"
assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4], "oopsie vector_mean()"
assert dot([1, 2, 3], [4, 5, 6]) == 32, "dot() issue"  # 1 * 4 + 2 * 5 + 3 * 6

# Add these tests to the end of your linear_algebra.py file
# commit and push the update to GitHub

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Extra assert statements to test all of the functions you will need
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6
assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3
assert magnitude([3, 4]) == 5
assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns
assert distance([1,1],[4,1]) == 3.0
assert squared_distance([1,2,3],[2,3,4]) == 3
assert scalar_multiply(2, [1,2,3]) == [2,4,6]
assert magnitude([0,0,4,3]) == 5.0

# Work on an Identity Matrix
id = [  [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1] ]

assert get_column(id,2) == [0, 0, 1, 0, 0]
assert get_row(id,2) == [0, 0, 1, 0, 0]
assert get_column(id,2) == get_row(id,2)
assert identity_matrix(5) == id
assert make_matrix(5,5, lambda i,j: 1 if i == j else 0) == id
assert shape(id) == (5,5)

