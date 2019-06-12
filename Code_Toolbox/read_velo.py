import numpy as np 
import collections

velocity_file = "../Example_data/NAM08_pbovelfile_feb2018.txt"

velocities = collections.namedtuple("velocities",["name", "coords", "dNdt", "dEdt", "dUdt", "SNd", "SEd", "SUd"]);

def input (filename):
	my_file = np.loadtxt(filename, skiprows = 36, usecols = (7, 8, 19, 20, 21, 22, 23, 24), unpack = True)

	temp_file = open(filename, 'r')
	data = temp_file.readlines()[35:]
	temp_file.close()

	name_field = []

	for line in data:
	    name_field.append(line.split()[1])
	name = name_field

	my_station = velocities(name = name , coords = [my_file[0], my_file[1]], dNdt = my_file[2], dEdt = my_file[3], dUdt = my_file[4], SNd = my_file[5], SEd = my_file[6], SUd = my_file[7])
	return

input(velocity_file)
print(name_field)