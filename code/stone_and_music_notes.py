# Student Name: Sakshi Luchoo
# Student ID: 23314771
#
# stone_and_music_notes.py - Contains colour facts details(verifies if user colour input matches available colours)
#

# Outer dictionary(colour names) containing inner dictionaries(colour facts)
colour_notes = {'violet':{'Matching Stone':'Amethyst',
                          'Matching Music note':'B',
                          'Matching Emotion':'Bravery'},

                'blue':{'Matching Stone':'Opal',
                        'Matching Music note':'A',
                        'Matching Emotion':'Calm'}, 

                'cyan':{'Matching Stone':'Turquoise',
                        'Matching Music note':'G',
                        'Matching Emotion':'Calm'},

                'green':{'Matching Stone':'Emerald',
                        'Matching Music note':'F',
                        'Matching Emotion':'Peaceful'},  

                'yellow':{'Matching Stone':'Topaz',
                        'Matching Music note':'E',
                        'Matching Emotion':'Happy'}, 

                'orange':{'Matching Stone':'Moonstone',
                        'Matching Music note':'D',
                        'Matching Emotion':'Happy'}, 

                'red':{'Matching Stone':'Garnet',
                        'Matching Music note':'C',
                        'Matching Emotion':'Confidence'}}

# Function to check whether user has entered a colour that is available in the dictionary
def get_colour_facts(colour):
    colour = colour.lower()
    if colour not in colour_notes:
        raise ValueError(f'Colour {colour} is not available to obtain facts')
    return colour_notes[colour]

