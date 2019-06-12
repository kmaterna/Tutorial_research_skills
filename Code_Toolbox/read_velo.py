import numpy as np 
import collections

velocities = collections.namedtuple("velocities",["name", "latitude", "longitude", "dNdt", "dEdt", "dUdt", "SNd", "SEd", "SUd"]);

def input (filename):
	my_file = np.loadtxt(filename, skiprows = 36, usecols = (7, 8, 19, 20, 21, 22, 23, 24), unpack = True)

	temp_file = open(filename, 'r')
	data = temp_file.readlines()[36:]
	temp_file.close()

	name_field = []

	for line in data:
	    name_field.append(line.split()[0])

	velo_field = velocities(name = name_field , latitude = my_file[0], longitude =  my_file[1], dNdt = my_file[2], dEdt = my_file[3], dUdt = my_file[4], SNd = my_file[5], SEd = my_file[6], SUd = my_file[7])
	return velo_field


if __name__ == "__main__":
	velocity_file = "../Example_data/NAM08_pbovelfile_feb2018.txt"
	velo_field = input(velocity_file)
	print(name_field)