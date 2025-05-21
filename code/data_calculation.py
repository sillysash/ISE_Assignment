# Student Name: Sakshi Luchoo
# Student ID: 23314771
#
# data_calculation.py - To calculate given frequency's wavelength and given wavelength's frequency
#

# Function to find the wavelength of the frequency given
def calculate_wavelength_of_freq(freq_in_THz):
    conversion = 300000000   # c = 3 * 10^8 m/s (conversion forumla)
    wavelength = conversion / freq_in_THz   # Calculating wavelength 
    return wavelength

# Function to find the frequency of the wavelength given
def calculate_freq_of_wavelength(wavelength_in_nm):
    conversion = 300000000 
    freq_in_Hz = conversion / wavelength_in_nm    # Calculating frequency
    return freq_in_Hz
