import numpy as np 
import collections

velocity_file = "../Example_data/NAM08_pbovelfile_feb2018.txt"

velocities = collections.namedtuple("velocities",["name", "coords", "dNdt", "dEdt", "dUdt", "SNd", "SEd", "SUd"]);

def input (file):
	# my_file = np.loadtxt(file, skiprows = 36, usecols = (4, 5, 19, 20, 21, 22, 23), unpack = True)
	my_file = np.loadtxt(file, skiprows = 40, usecols = (7, 8, 19, 20, 21, 22, 23, 24), unpack = True)
	# my_station = velocities(name = my_file[0] , coords = [my_file[1], my_file[2]], dNdt = my_file[3], dEdt = my_file[4], dUdt = my_file[5], SNd = my_file[6], SEd = my_file[7], SUd = my_file[8])
	# my_station = velocities(coords = [my_file[0], my_file[1]], dNdt = my_file[2], dEdt = my_file[3], dUdt = my_file[4], SNd = my_file[5], SEd = my_file[6], SUd = my_file[7])
	# return my_station
	print(my_file)
	return


# with open("../Example_data/NAM08_pbovelfile_feb2018.txt") as temp_file:
    # for line in temp_file:
        # fields = line.split( )

input(velocity_file)