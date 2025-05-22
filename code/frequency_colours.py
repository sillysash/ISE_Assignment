# Student Name: Sakshi Luchoo
# Student ID: 23314771
#
# frequency_colours.py - Details about colour names and their frequencies
#

# Dictionary containing colour options and their upper and lower bound frequency values
colour_freq_bounds = {'violet': (670, 790),       
                          'blue': (620, 669),
                          'cyan': (600, 619),
                          'green': (530, 599),
                          'yellow': (510, 529),
                          'orange': (480, 509),
                          'red': (400, 479)}
min_visible_light = 400
max_visible_light = 790

# Function to return colour from colours available 
def get_colour_freq(colour):
    colour = colour.lower()
    if colour not in colour_freq_bounds:
        raise ValueError(f'Unavailable colour: {colour}')     # Raises an error if the user has input an invalid colour choice
    return colour_freq_bounds[colour]

# Function to find and return colour produced by frequency given by user
def freq_colours(freq_value):
    if freq_value < min_visible_light:
        return 'Frequency value is below the Visible Light range (lower than frequency of Red)'
    elif freq_value > max_visible_light:
         return 'Frequency value is above the Visible Light range (higher than frequency of Violet)'
    
    # For loop created to access color name, min and max boundary values for frequency(in the dictionary)     
    for colour, (min, max) in colour_freq_bounds.items():  
        if min <= freq_value <= max:         # Freq value is user input value for frequency
           return f'Corresponding colour is: {colour}'
    

# Function to return visible colour names
def get_visible_colours(freq_value):
    for colour, (min, max) in colour_freq_bounds.items():  
        if min <= freq_value <= max:  
            return colour     # Colour is visible so colour name is returned
    return None       # Colour is not in the Visible Light range

# Function to compare the two frequency values to find if both represent a single colour or two different colours
def compare_two_freq(freq_val1, freq_val2):
    val1_visible = get_visible_colours(freq_val1)     # Get colour frequencies(min and max) for comparison process
    val2_visible = get_visible_colours(freq_val2)

    if not val1_visible and not val2_visible:
        return (f'Neither frequencies are visible: {freq_val1}THz, {freq_val2}THz')
    if not val1_visible:
        return (f'Frequency {freq_val1}THz is not within the Visible Light range')
    if not val2_visible:
        return (f'Frequency {freq_val2}THz is not within the Visible Light range')
    
    colour1 = get_visible_colours(freq_val1)
    colour2 = get_visible_colours(freq_val2)

    # Find if both represent the same colour or not
    if colour1 == colour2:
        return 'Both frequencies represent the same colour'
    else:
        return 'Both frequencies represent different colours'