# Student Name: Sakshi Luchoo
# Student ID: 23314771
#
# main.py - execution of the main program tasks
#
from frequency_colours import *
from data_calculation import *
from stone_and_music_notes import *
import os

# For bold text and resetting it back to normal font 
BOLD = '\033[1m'
RESET = '\033[0m'
def start_up_menu():

    print(f'{BOLD}\nWelcome to the Electromagnetic Spectrum colour analysis!\n')
    print(f'{BOLD}\nHere are the options available for the analysis: {RESET}\n')

    print('1. Select a color to calculate its frequency upper and lower bound')
    print('2. Enter a frequency(THz) to calculate its wavelength')
    print('3. Enter a wavelength(nm) to calculate its frequency')
    print('4. Enter a frequency(THz) to find its appropriate corresponding range')
    print('5. Enter a frequency(THz) to find its colour produced')
    print('6. Enter two frequency values(both in THz) to check their colour representation')
    print('7. Color analysis')
    print('8. Exit')
     
def main():
    while True:
        start_up_menu()
        choice = (input(f'{BOLD}\nPlease choose from the available options (1-8): {RESET}\n'))
        if not('1'<= choice <= '8'):
            print(f'\nInvalid choice {choice}. Please choose from the options available (1-8)\n')
            
        match choice:
             case '1':
                print(f'{BOLD}\nOption 1 selected!{RESET}\n')
                while True:
                    colour_choice = input('Enter a colour available in the visible light spectrum range (violet, blue, cyan, green, yellow, orange, red): ')
                    try:
                        lower_bound, upper_bound = get_colour_freq(colour_choice)
                        print(f'Frequency bounds for {colour_choice} is: {lower_bound}THz to {upper_bound}THz')
                        break    # Exit loop after valid input and process

                    except ValueError:
                        print('\nColour frequency not found! Please enter an available colour\n')

             case '2':
                print(F'{BOLD}\nOption 2 selected!{RESET}\n')
                while True:
                    try:
                        freq_value = int(input('Enter a frequency value in THz to calculate its wavelength(1-39,999): '))
                        if (0 < freq_value < 40000):
                            print(f'Wavelength is: {calculate_wavelength_of_freq(freq_value)}nm')
                            break
                        else:
                            print('\nInvalid frequency! Out of bound. Please enter a frequency value between 1 and 39,999: \n')

                    except ValueError:
                        print('\nInvalid input! Please enter a valid frequency\n')
                        
             case '3':
                print(F'{BOLD}\nOption 3 selected!{RESET}\n')

                while True:
                    try:
                        wavelength_value = int(input('Enter a wavelength value in nm to calculate its frequency(1-7,499): '))
                        if (0 < wavelength_value < 7500):
                            print(f'Wavelength is: {calculate_freq_of_wavelength(wavelength_value)}THz')
                            break
                        else:
                            print('\nOut of bound! Please enter a wavelength value between 0 and 7500\n')

                    except ValueError:
                        print('\nInvalid input! Please enter a valid wavelength\n')
                         
             case '4':
                print(F'{BOLD}\nOption 4 selected!{RESET}\n')

                while True:
                    try:
                        freq_in_THz = int(input('Enter a frequency value in THz to find if it is within the Visible Light, IR and UV range or not(1-39,999): '))

                        if freq_in_THz <= 0 or freq_in_THz >= 40000:
                                print('\nInvalid frequency! Frequency must be between 1 and 39,999THz range\n')
                        else:
                            if freq_in_THz >= 400 and freq_in_THz <= 790:
                                print(f'{freq_in_THz}THz is in the {BOLD}Visible Light{RESET} range')
                                break
                            if freq_in_THz > 790:
                                print(f'{freq_in_THz}THz is in the {BOLD}UltraViolet(UV){RESET} range')
                                break
                            if freq_in_THz < 400:
                                print(f'{freq_in_THz}THz is in the {BOLD}InfraRed(IR){RESET} range')
                                break

                    except ValueError:
                        print('\nInvalid input! Please input a valid frequency\n')
                        
             case '5':  
                print(F'{BOLD}\nOption 5 selected!{RESET}\n')

                while True:
                    try:
                        freq_value = int(input('Enter a frequency value in THz to find the its colour(400-790THz): '))
                        find_colour = freq_colours(freq_value)
                        print(f'{find_colour}')
                        break
                       
                    except ValueError:
                        print('\nInvalid input! Please enter a valid frequency\n') 
                
             case '6':
                print(f'{BOLD}\nOption 6 selected!{RESET}\n')
                print('Enter two frequency values to compare their colour(s)(400-790THz)')

                while True:
                        try:
                            freq_val1 = int(input('First frequency value: '))
                            freq_val2 = int(input('Second frequency value: '))

                            comparison = compare_two_freq(freq_val1, freq_val2)
                            print('Comparison results are:\n', comparison)
                            break

                        except ValueError:
                            print('\nInvalid input! Please enter two valid frequencies\n')

             case '7':
                print(f'{BOLD}\nOption 7 selected!{RESET}\n')
                print(f'\n COLOUR ANALYSIS\n')
                print('These are the following colours available: violet, blue, cyan, green, yellow, orange, red')

                while True:
                        try:
                            choice = input('Select a colour: ')
                            details = get_colour_facts(choice)
                            if details is None:
                                print('Sorry, this colour is not available')
                            else:
                                print('Stone association:', details['Matching Stone'])
                                print('Musical note association:', details['Matching Music note'])
                                print('Emotion association:', details['Matching Emotion'])
                                break
                          
                        except ValueError:    
                            print('\nUnavailable colour option! Please try again\n')

             case '8':
                print('Thank you for participating! Farewell!')
                break 

if __name__ == '__main__':
    main()