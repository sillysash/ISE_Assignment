# Student Name: Sakshi Luchoo
# Student ID: 23314771
#
# unit_test.py - Verify that the colours 'red' and 'violet' are correctly identified in the Visible Light range
#
from frequency_colours import *

#Upper and lower boundary values for Visible Light range
min_visible_light = 400
max_visible_light = 790

colour_freq_bounds = {'violet': (670, 790),       
                          'blue': (620, 669),
                          'cyan': (600, 619),
                          'green': (530, 599),
                          'yellow': (510, 529),
                          'orange': (480, 509),
                          'red': (400, 479)}
# Function to test in the two colours are visible
def test_visible_range():
    # Testing red edge in visible light range
    assert freq_colours(400) == "red is visible" # Min red freq
    assert freq_colours(479) == "red is visible" # Max red freq
    # Testing violet edge in visible light range
    assert freq_colours(670) == "violet is visible" # Min violet freq
    assert freq_colours(790) == "violet is visible" # Max violet freq

# Function to test the two colours going out of range
def  test_visible_outrange():
    # Above visibility range
    assert freq_colours(791) == "Above Visible Light range"  # Upper boundary is 790
    # Below visibility range
    assert freq_colours(399) == "Below Visible Light range"  # Lower boundary is 400

# Run the tests
test_visible_range()
test_visible_outrange()