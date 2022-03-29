import numpy
import numpy as np
from numpy import ndarray
from typing import Union, Tuple, Any, Optional

# use numpy to read the text file and store the values in 'data_collected'
data_collected = np.loadtxt("fakecoin.txt", delimiter=' ', dtype=int)

# splits the array into 3 smaller arrays
coin_arrays = np.array_split(data_collected, 3)

# initialize variables to be used inside all functions
first_array_average = np.average(coin_arrays[0])  # get and store the average of the first array (index[0])
second_array_average = np.average(coin_arrays[1])  # get and store the average of the second array (index[1])
third_array_average = np.average(coin_arrays[2])  # get and store the average of the third array (index[2])


# define function to find fake coin
def find_fake_coin(coin_arrays):
    if first_array_average == second_array_average:  # if the averages are equal search the third array
        fake_coin3 = np.where(coin_arrays[2] == numpy.amin(coin_arrays[2]))
        print("The fake coin weight is ", (np.amin(coin_arrays[2])))  # prints the weight of the fake coin
        print("The index of the fake coin is in the third array at index", fake_coin3)

    if first_array_average == third_array_average:  # if the averages are equal, search the second array
        fake_coin2 = np.where(coin_arrays[1] == numpy.amin(coin_arrays[1]))
        print("The fake coin weight is ", (np.amin(coin_arrays[1])))  # prints the weight of the fake coin
        print("The index of the fake coin is in the second array at index", fake_coin2)

    if second_array_average == third_array_average:  # if the averages are equal, search the first array
        fake_coin1 = np.where(coin_arrays[0] == numpy.amin(coin_arrays[0]))
        print("The fake coin weight is ", (np.amin(coin_arrays[0])))  # Prints the weight of the fake coin
        print("The index of the fake coin is in the first array at index", fake_coin1)


# Calling Functions to check
print(coin_arrays)
find_fake_coin(coin_arrays)  # this needs to return the index of the false coin

# Dylan Sherlock (S#00355174)
#This code was written to solve the fake coin problem reading from a text file where the weights are stored.
