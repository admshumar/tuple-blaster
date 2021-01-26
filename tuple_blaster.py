from itertools import permutations
import string
import time

"""
A TupleBlaster is defined by a list of integers that represents a set of localities
and an adjacency matrix that indicates which of these localities are adjacent to each
other. The class locates tuples of any length for which successive entries in the tuple
are adjacent localities.
"""
class TupleBlaster:
    def __init__(self, localities, adjacency_matrix):
        self.locality_list = localities
        self.adjacency_matrix = adjacency_matrix

    def get_tuple_connectivity(self, locality_tuple):
        count = 1
        for i in range(len(locality_tuple) - 1):
            adjacency_number = self.adjacency_matrix[locality_tuple[i]][locality_tuple[i + 1]]
            count = count * adjacency_number
            if count == 0:
                break
        return count

    def get_locality_tuples(self, n):
        return list(permutations(self.locality_list, n))

    def get_connectivity_dictionary(self, permutation_list):
        dictionary = {}
        for locality_tuple in permutation_list:
            adjacency_number = self.get_tuple_connectivity(locality_tuple)
            dictionary[locality_tuple] = adjacency_number
        return dictionary

    def get_connected_tuples(self, n):
        permutation_list = self.get_locality_tuples(n)
        dictionary = self.get_connectivity_dictionary(permutation_list)
        connected_tuple_set = {key for key, value in dictionary.items() if value == 1}
        sorted_connected_tuple_list = []
        for connected_tuple in connected_tuple_set:
            connected_tuple = list(connected_tuple)
            connected_tuple.sort()
            sorted_connected_tuple_list.append(connected_tuple)
        connected_tuple_set = {tuple(l) for l in sorted_connected_tuple_list}
        return connected_tuple_set

    def print_connected_tuples(self, n):
        t0 = time.time()
        s = self.get_connected_tuples(n)
        s = list(s)
        s.sort()
        lst = ["_".join(tuple(string.ascii_uppercase[n] for n in t)) for t in s]
        print(lst)
        t1 = time.time()
        t = t1 - t0
        print("\nFinished in", t, "seconds.")


arr = list(range(10))

matrix = [[1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
          [1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
          [0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
          [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
          [0, 0, 0, 1, 1, 1, 0, 0, 1, 1]]

blaster = TupleBlaster(arr, matrix)

blaster.print_connected_tuples(3)
