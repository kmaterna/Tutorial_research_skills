import numpy as np
import matplotlib.pyplot as plt
import read_catalog
import datetime as dt

# practice with matrix math

a = [0.557, 0.557, -0.557]
b = [1.114, -1.114, 1.114]

a_dot_b = np.dot(a,b)

print(a_dot_b)

a_cross_b = np.cross(a,b)

print(a_cross_b)

filename = "../Example_Data/USGS_catalog_MTJ.txt"
[myCatalog] = read_catalog.input(filename)

# # making histograms of magnitudes, etc

# mag_plot = plt.hist(myCatalog.magnitude)
# plt.xlabel("Earthquake Magnitude")
# plt.savefig('mag_plot.png', bbox_inches='tight')


# plotting earthquake frequency rates, as earthquakes per day vs time
# datetime to strings, truncating
def configure_dates(datetime_array):
	days = []
	for idate in datetime_array:
		day = idate.strftime("%Y.%m.%d")
		days.append(day)
	return days

# counting intances of eqs
def compute_eq_rate(time_array):
	eq_rates = []
	for iday in time_array:
		num_eq = time_array.count(iday)
		eq_rates.append(num_eq)
	return eq_rates

# removing duplicated counts of same eqs, etc
def remove_duplicates(old_array):
	new_array = old_array[:1]
	for elem in old_array:
		if elem == 1:
			new_array.append(elem)
		elif elem != new_array[-1]:
			new_array.append(elem)
	return new_array

# converting dates back to datetimes, plotting
def output_eq_rates(days, eq_rates):
	days = remove_duplicates(my_days)
	eq_rates = remove_duplicates(my_eq_rates)
	dt_days = []
	for iday in days:
		dt_day = dt.datetime.strptime(iday, "%Y.%m.%d")
		dt_days.append(dt_day)

	eq_rate_plot = plt.plot_date(dt_days, eq_rates, linestyle='solid', marker='None')
	plt.xlabel("Time")
	plt.ylabel("Earthquakes per Day")
	plt.savefig('eq_rate_plot.png', bbox_inches='tight')
	return eq_rate_plot

# plotting magnitude vs time to compare w eq frequency
def output_mag_plot(days, magnitude):
	plt.figure()
	mag_plot = plt.plot_date(days, magnitude, linestyle='solid', marker='None')
	plt.xlabel("Time")
	plt.ylabel("Earthquakes Magnitude")
	plt.savefig('magnitude_plot.png', bbox_inches='tight')
	return mag_plot

# pseudo driver
my_days = configure_dates(myCatalog.dtarray)
my_eq_rates = compute_eq_rate(my_days)
my_eq_rate_plot = output_eq_rates(my_days, my_eq_rates)
my_mag_plot = output_mag_plot(myCatalog.dtarray, myCatalog.magnitude)


# plotting the vector field associated with strain rates

import read_velo

filename = "../Example_data/NAM08_pbovelfile_feb2018.txt"
velo_field = read_velo.input(filename)

y = velo_field.latitude
x = velo_field.longitude
xvel = velo_field.dEdt
yvel = velo_field.dNdt

def build_field(x, y, xvel, yvel):
	field = plt.figure()
	plt.quiver(x, y, xvel, yvel, pivot='middle')
	plt.title("Strain Velocities of the Western US")
	plt.ylim(35, 45)
	plt.xlim(234, 240)
	plt.xlabel("Longitude")
	plt.ylabel("Latitude")
	plt.savefig('velo_plot.png', bbox_inches='tight')
	return field

my_field = build_field(x, y, xvel, yvel)
