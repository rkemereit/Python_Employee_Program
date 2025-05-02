#!/usr/bin/env python3
# FILE      employee_program.py
# DATE      2024-02-12
# AUTHOR    Richard Kemereit
# DESCRIPTION
"""
This program allows the user to interact with Employee records.
The primary logic uses a loop for the menu to repeat activities 
until the user chooses to quit.
In the Week 06 Lab, we split the program into functions.
"""

# Needed for command line arguments
import sys
import employee_handler
import ui_helper


VERSION = "1.0.3"
"""
This is the current version of this program.
"""


def main(argv:list):
    """
    The main() function is the starting point for the program.
    Based on command line arguments, the program will accomplish
    different tasks.

    INPUTS:
        argv A list of command line arguments

    """
    # Check the length of the argument list.  The first item is the program
    #print(argv)
    if len(argv) == 1:
        do_program_logic()
    elif len(argv) == 2:
        # Are they asking for help or for the version?
        if argv[1] == '-?' or argv[1] == '-h' or argv[1] == '--help':
            show_help()
        elif argv[1] == '-v' or argv[1] == '--version':
            show_version()
        else:
            show_error(f'Invalid command line argument: {argv[1]}')
    else:
        show_error(f"Invalid number of command line arguments: {argv}")

# #############################################################################
#   Functions to handle command line arguments
# #############################################################################

def show_error(message: str):
    """
    Display an error message related to the command line arguments.  Then show 
    the help message and exit with a non-zero error code.

    INPUTS:
        message A string with the error message
    """
    ui_helper.show_message(f'\nERROR: {message}')
    show_help()
    sys.exit(1) # non-zero value means there was an error

def show_version():
    """
    Display the current version number and then exit with an OK status.
    """
    ui_helper.show_message(f'\nemployee_program {VERSION}')
    sys.exit(0) # exit with an OK status

def show_help():
    """
    Display a usage message for the user telling how to use the program.
    When done, exit the program with an OK status.
    """
    ui_helper.show_message('\nUSAGE:')
    ui_helper.show_message('python employee_program.py')
    ui_helper.show_message('python employee_program.py [-? | -h | --help]')
    ui_helper.show_message('python employee_program.py [-v | --version]\n')

def do_program_logic():
    """
    This function will print a menu of options for the user.  Then it will
    prompt the user for a menu choice.  Using an if-elif-else structure, 
    it will print a message related to the user's choice.
    This will continue until the user chooses to quit.
    """
    program_title = "EMPLOYEE PROGRAM"
    ui_helper.show_program_title(program_title)
    invalid_choice_message = "\nYour choice was not recognized.  Please try again."
    # Define the loop variable
    done = False
    # Start the loop
    while not done:
        user_choice = ui_helper.get_user_choice()
        # Decide what to do with the choice
        if user_choice == '1':
            employee_handler.add_employee()
        elif user_choice == '2':
            employee_handler.show_all_employees()
        elif user_choice == '3':
            employee_handler.view_an_employee()
        elif user_choice == '4':
            employee_handler.update_an_employee()
        elif user_choice == '5':
            employee_handler.delete_an_employee()
        elif user_choice == 'Q' or user_choice == 'q':
            done = ui_helper.confirm_quit()
        else:
            ui_helper.show_message(invalid_choice_message)
    # Tell the user the program is finished
    print("\nProgram complete.\n")

# #############################################################################
#   Call the main() function
# #############################################################################
if __name__ == "__main__":
    main(sys.argv)


# #############################################################################
#                              END OF FILE
# #############################################################################











