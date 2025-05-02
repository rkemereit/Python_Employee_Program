#!/usr/bin/env python3
# FILE      ui_helper.py
# DATE      2024-03-04
# AUTHOR    Richard Kemereit
# DESCRIPTION
"""
These are functions are for communicating with the user.
In Model-View-Controller, these are from the View.
"""

CONSOLE_WIDTH = 80
"""
The width of the console in characters.  Used to assist with layout.
"""

# #############################################################################
#   Functions for communicating with the user
#   This separates out the View from Controller and Model
# #############################################################################

def show_message(message:str):
    """
    Displays the message in a standard format.

    INPUTS:
        message A string with instructions for the user
    """
    print(message)

def show_program_title(title: str):
    """
    Display the program title in a standard manner.

    INPUTS:
        title A string with the title of the program
    """
    new_title = "*** " + title.upper() + " ***"
    print(f"\n{new_title:^{CONSOLE_WIDTH}}")

def show_section_title(title: str):
    """
    Display the section title in a consistent manner.

    INPUTS:
        title A string with the section title
    """
    print(f"\n\t-- {title} --")

def press_enter_key_to_continue():
    """
    Prompt the user to press the Enter key to continue and then wait until
    they do so.  Ignore any other input from the user.
    """
    input("\nPlease press the Enter key to continue... ")

def get_user_string(prompt: str) -> str:
    """
    Prompts the user to enter a string and then returns that string.

    INPUTS:
        prompt A string with instructions for the user
    
    RETURNS:
        str The string entered by the user
    """
    return input(prompt + " ").strip()

def get_user_int(prompt:str) -> int:
    """
    Display the prompt to the user and ask them for an int.  Return the int.

    INPUTS:
        prompt A string with instructions for the user
    RETURNS:
        int The int value entered by the user
    """
    value = 0
    needed = True
    while needed:
        user_input = input(prompt + " ")
        try:
            value = int(user_input)
            needed = False
        except ValueError:
            print(" That is not an integer. Please try again")
            press_enter_key_to_continue()
    return value

def get_user_positive_int(prompt:str) -> int:
    value = 0
    needed = True
    while needed:
        value = get_user_int(prompt)
        if value >= 0:
            needed = False
        else:
            print("The value must be greater than or equal to zero. Please try again")
            press_enter_key_to_continue()
    return value

def get_user_float(prompt:str) -> float:
    """
    Display the prompt to the user and ask them for a float.  Return the float.

    INPUTS:
        prompt A string with instructions for the user
    RETURNS:
        float The float value entered by the user
    """
    value = 0.0
    needed = True
    while needed:
        user_input = input(prompt + " ")
        try:
            value = float(user_input)
            needed = False
        except ValueError:
            print('That is not a valid number. Please try again.')
            press_enter_key_to_continue()
    return value

def get_cancellable_user_float(prompt:str) -> float:
    value = 0.0
    needed = True
    while needed:
        user_input = input(prompt + " ")
        if user_input == '':
            raise ValueError('Cancelled')
        try:
            value = float(user_input)
            needed = False
        except ValueError:
            print('That is not a valid number. Please try again.')
            press_enter_key_to_continue()
    return value

# #############################################################################
#   Functions for TABLES
# #############################################################################
def draw_table(column_defs: list, headers: list, data: list):
    """
    Draws a text-based table with the provided criteria and data.
    Note that the first two lists must be the same size and the sub-lists 
    of data must be that size.

    INPUTS:
        column_defs A list of tuples with column width and alignment
        headers A list of strings with column headers
        data A list of lists with the records to display
    """
    # determine the width of the table
    bar_size = 0
    for col in column_defs:
        bar_size += col[0]
    bar_size += len(headers) + 1
    print("")
    draw_bar(bar_size, "-")
    # Draw the table header
    print("|", end="")
    for i in range(len(column_defs)):
        draw_column(column_defs[i][0], headers[i], 'center')
        print('|', end="")
    print('')
    draw_bar(bar_size, '-')
    # Draw the table data (pick up here next time)
    for datum in data:
        print('|', end='')
        for i in range(len(datum)):
            draw_column(column_defs[i][0], datum[i], column_defs[i][1])
            print('|', end='')
        print('')
        draw_bar(bar_size, '-')

def draw_column(width: int, value:str, direction:str):
    """
    Builds a string for a column and prints it without a newline.

    INPUTS
        width The field width for the column
        value The value to display in the column
        direction The alignment for the column (left, right, center)
    """
    # Determine the alignment
    align = "<"
    if direction == "center":
        align = "^"
    elif direction == "right":
        align = ">"
    # Validate the length of the value
    output_string = str(value)
    if len(output_string) > width:
        output_string = value[:width - 3] + '...'
    # Build the string
    out = f"{output_string:{align}{width}}"
    print(out, end="")



def draw_bar(bar_size:int, bar_character:str):
    """
    Draw a horizontal line made up of the bar_character.

    INPUTS:
        bar_size The width of the line in characters
        bar_character The character to use for the line
    """
    bar = bar_character * bar_size
    print(bar)

# #############################################################################
#   Functions for menus
# #############################################################################

def get_user_choice()->str:
    """
    Display a menu and ask the user for a choice.  Return the choice as a 
    string.

    RETURNS:
    str  A string representing the user choice
    """
    menu_title = 'Main Menu'
    prompt = 'Your choice: '
    # This will be a list of strings.  A list is a set of square braces 
    # with items separated by commas.  We will cover this more in a later
    # unit.
    options = ['1) Add an Employee','2) Show All Employees','3) View an Employee'
        ,'4) Update an Employee','5) Delete an Employee','Q) Quit']
    # Call a function to display the menu
    show_menu(menu_title, options)
    # Call a function to get the user choice
    return get_user_string(prompt)

def show_menu(menu_title: str, options: list):
    """
    Displays a menu in a structured manner.  Can be used with any menu with 
    any number of options.

    INPUTS:
        menu_title A string with the title of the menu
        options A list of strings with the menu options
    """
    print(f"\n\n\t-- {menu_title} --")
    for option in options:
        print(f'\t{option}')

def confirm_quit()-> bool:
    """
    Display a message stating that the user has chosen to quit.  Ask them 
    to confirm that they really want to quit by entering Y or N.  If the 
    user enters 'Y' or 'y', then return True, otherwise return False.

    RETURNS:
        bool True if confirmed quit, False otherwise
    """
    show_message('\nYou have chosen to quit the program')
    prompt = 'Confirm quit (Y/N)'
    choice = get_user_string(prompt)
    return (choice == 'Y' or choice == 'y')




