#!/usr/bin/env python3
# FILE      employee_handler.py
# DATE      2024-03-04
# AUTHOR    Richard Kemereit
# DESCRIPTION
"""
These are functions that handle the employee record logic.
Though the employee records are part of the Model of 
Model-View-Controller, these functions are part of the Controller.

MOD DATE    2024-03-25
MOD BY      Your Name
MOD DESCRIPTION
    Add the functionality for add_employee() and show_all_employees().
    This required two new imports: employee_store and employee_ui

"""

import employee_store
import employee_ui
import ui_helper

# #############################################################################
#   Functions for working with employee data
# #############################################################################

def add_employee():
    """
    Handles the logic for adding an employee record.
    """
    ui_helper.show_section_title('Add an Employee')
    # Get the employee data from the user
    employee = employee_ui.get_employee_data()
    try:
        # Store the employee data
        employee_store.store_employee(employee)
        # Tell the user the employee data has been stored
        ui_helper.show_message("\n\tEmployee record has been stored.")
    except IOError as err:
        ui_helper.show_message(f'ERROR: There was an error saving the record. {str(err)}')
    ui_helper.press_enter_key_to_continue()

def show_all_employees():
    """
    Handles the logic for all employee records.
    """
    ui_helper.show_section_title('Show all Employees')
    try:
        # Get the list of employee records
        employees = employee_store.get_employee_list()
        # Check if empty - if empty show message, otherwise show employees
        if len(employees) == 0: # no records
            ui_helper.show_message("There are no employee records to show.")
        else:
            employee_ui.show_employee_table(employees)
    except IOError as err:
        ui_helper.show_message(f'ERROR: There was an error reading the records. {str(err)}')
    ui_helper.press_enter_key_to_continue()

def view_an_employee():
    """
    Get a single employee ID from the user, and then get the employee
    record with the matching ID.  Display that employee.
    Handle the situation where there is no matching employee.
    I/O Exceptions will be handled in a later lab.
    """
    ui_helper.show_section_title('View an Employee')
    # Get the employee ID from the user
    id = employee_ui.get_employee_id()
    try:
        # Try to get the employee record
        employee = employee_store.get_employee_by_id(id)
        # Check for an employee and display as needed
        if len(employee) == 0:
            ui_helper.show_message(f"\nThere were no employees with ID {id}.")
        else:
            employee_ui.show_single_employee(employee)
    except IOError as err:
         ui_helper.show_message(f'ERROR: There was an error reading the record. {str(err)}')
    ui_helper.press_enter_key_to_continue()

def update_an_employee():
    """
    Get the employee ID from the user and get the matching employee 
    from the data store.  If the record exists, ask the user for 
    new values for the fields and then store the new value to the 
    data file, overwriting the old values. 
    Note, exception handling will be added later.
    """
    ui_helper.show_section_title('Update an Employee')
    # Get the employee ID
    id = employee_ui.get_employee_id()
    try:
        # Get the matching the employee record
        employee = employee_store.get_employee_by_id(id)
        # If there was match, get the new fields and store to the file
        if len(employee) == 0: # no match
            ui_helper.show_message(f"\nThere were no employees with ID {id}.")
        else:
            updated = employee_ui.get_updated_employee_data(employee)
            # Store the updated record to file
            if employee_store.update_employee_by_id(updated):
                ui_helper.show_message(f"\nUpdated employee with ID {id}.")
            else:
                ui_helper.show_message(f"\nCould not update employee with ID {id}.")
    except IOError as err:
         ui_helper.show_message(f'ERROR: There was an error reading the record. {str(err)}')

    ui_helper.press_enter_key_to_continue()

def delete_an_employee():
    """
    Gets an ID from the user, tries to find and delete that employee record.  
    If there were no matches of the record cannot be deleted, tell the user.
    """
    ui_helper.show_section_title('Delete an Employee')
    id = employee_ui.get_employee_id()
    try:

        if employee_store.remove_employee_by_id(id):
            ui_helper.show_message(f'\nDeleted employee with ID {id}.')
        else:
            ui_helper.show_message(f'\nThere was no employee with ID {id}.')
    except IOError as err:
         ui_helper.show_message(f'ERROR: There was an error reading the record. {str(err)}')

    ui_helper.press_enter_key_to_continue()









