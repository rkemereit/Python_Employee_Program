#!/usr/bin/env python3
#   FILE:   employee_ui.py 
#   DATE:   2024-03-25
#   AUTHOR: Richard Kemereit
#   DESCRIPTION
"""
This module is for the user interface for employee-specific interactions.

In Model-View-Controller, this is part of the view
""" 

import employee_store
import ui_helper

def get_employee_data() ->list:
    """
    Asks the user for the data needed for an employee record and returns
    that data as a list. 
    The record format is:
        employee ID, last name, first name, department, salary
    
    RETURNS:
        list A list with employee data
    """
    id = ui_helper.get_user_int("Please enter the employee ID:")
    last_name = ui_helper.get_user_string("Please enter the last name:")
    first_name = ui_helper.get_user_string("Please enter the first name:")
    dept = ui_helper.get_user_string("Please enter the department name:")
    salary = ui_helper.get_user_float("Please enter the annual salary:")
    employee = [id, last_name, first_name, dept, salary]
    return employee


def show_employee_table(employees:list):
    """
    Display a list of employee records as a table.

    INPUTS:
        employees A list of employee records
    """
    widths = [(5, "center"), (40,"left"), (20,"left"), (20,"right")]
    headers = ["ID","NAME", "DEPARTMENT", "SALARY"]
    emp_list = []
    for employee in employees:
        current = []
        current.append(employee[0]) # ID
        current.append(employee[1] + ", " + employee[2]) # full name
        current.append(employee[3]) # department
        current.append(f'{employee[4]:.2f}') # salary
        emp_list.append(current)
    ui_helper.draw_table(widths, headers, emp_list)


def get_employee_id() -> int:
    """
    Gets an employee ID from the user.  This is used when the user wants
    to view, update, or delete a single employee record.

    RETURNS:
        int The ID entered by the user
    """
    id = ui_helper.get_user_positive_int("Please enter the Employee ID:")
    return id

def show_single_employee(employee:list):
    """
    Display the single employee record in a table.

    INPUTS:
        employee The employee record to display
    """
    show_employee_table([employee])

def get_updated_employee_data(employee:list) -> list:
    """
    Ask the user for replacement values for the attributes of the supplied
    employee record.  The entered values are used to create a new list which
    gets returned.  This does not allow for updates to the ID value.
    The code displays the current value for the benefit of the user.
    
    
    INPUTS:
        employee A list representing an employee record
    RETURNS:
        list An updated employee record
    """
    ui_helper.show_message("\nPress Enter to keep the existing value.")
    id = employee[employee_store.ID_IDX]
    # Get Last Name
    prompt = f"Please enter the last name ({employee[employee_store.LNAME_IDX]}): "
    last_name = ui_helper.get_user_string(prompt)
    if last_name == '': # the user pressed Enter
        last_name = employee[employee_store.LNAME_IDX]
    # Get First Name
    prompt = f"Please enter the first name ({employee[employee_store.FNAME_IDX]}): "
    first_name = ui_helper.get_user_string(prompt)
    if first_name == '': # the user pressed Enter
        first_name = employee[employee_store.FNAME_IDX]
    # Get Department
    prompt = f"Please enter the department ({employee[employee_store.DEPT_IDX]}): "
    dept = ui_helper.get_user_string(prompt)
    if dept == '': # the user pressed Enter
        dept = employee[employee_store.DEPT_IDX]
    # Get the salary
    
    prompt = f"Please enter the annual salary ({employee[employee_store.SALARY_IDX]}): "
    try:
        salary = ui_helper.get_cancellable_user_float(prompt)
    except ValueError:
        salary = employee[employee_store.SALARY_IDX]
    # return the updated employee values as a list
    return [id, last_name, first_name, dept, salary]
