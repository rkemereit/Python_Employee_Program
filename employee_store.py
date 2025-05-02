#!/usr/bin/env python3
#   FILE:   employee_store.py 
#   DATE:   2024-03-25
#   AUTHOR: Richard Kemereit
#   DESCRIPTION
"""
This module is for storage of the employee records

In Model-View-Controller, this is part of the Model

MOD DATE    2024-04-08
MOD BY      Your name
MOD DESCRIPTION
    For Week 11, we will store and read data from a text file.  Exception 
    handling will be added later.  Note that Python has a CSV module, but we 
    will do the work manually for better learning of the process.

""" 

FILE_NAME = 'employees.csv'
""" The name of the file where we store records. """

ID_IDX = 0
""" The index of the employee ID """
LNAME_IDX = 1
""" The index of the last name """
FNAME_IDX = 2
""" The index of the first name """
DEPT_IDX = 3
""" The index of the department name """
SALARY_IDX = 4
""" The index of the annual salary """



EMPLOYEE_LIST = []
""" A list of employee records """

def store_employee(employee: list):
    """
    Append the employee record to the file.

    INPUTS:
        employee A list representing an employee record
    """
    # Convert the employee record to a string
    line = convert_record_to_string(employee)
    # Open the file for append and add the record string
    with open(FILE_NAME, 'a') as out_file:
        out_file.write(line)

def get_employee_list() -> list:
    """
    Return the list of employee records from the file.

    RETURNS:
        list The list of employee records
    """
    employees = []
    with open(FILE_NAME, 'r') as in_file:
        for line in in_file:
            fields = line.split(',') # break into a list of fields
            id = int(fields[ID_IDX])
            last_name = fields[LNAME_IDX]
            first_name = fields[FNAME_IDX]
            dept = fields[DEPT_IDX]
            salary = round(float(fields[SALARY_IDX]),2)
            employees.append([id, last_name, first_name, dept, salary])
    return employees

def get_employee_by_id(id:int) -> list:
    """
    Loop through the list of available employees looking for one 
    that matches the supplied ID.  If the record is not found, will 
    return an empty list.

    INPUTS:
        id An integer with the desired employee ID
    RETURNS:
        list A list with the employee data or an empty list
    """
    desired = []
    employees = get_employee_list()
    for employee in employees:
        if employee[ID_IDX] == id: # Matched!
            desired = employee
            break # we are done, so leave the loop
    return desired

def update_employee_by_id(employee:list) -> bool:
    """
    Get the list of employees and loop through them looking for one with 
    the same ID as the supplied employee.  Replace that one with the 
    supplied employee.
    If the employee is found, save the list back to the file.
    Return True if the employee was found, False otherwise.

    INPUTS:
        employee An employee record to update
    RETURNS:
        bool True if updated, otherwise False
    """
    id = employee[ID_IDX]
    result = False # initialize - we have not yet found the record
    keep = []
    employees = get_employee_list()
    for emp in employees:
        if emp[ID_IDX] == id: # Found the record!
            result = True
            keep.append(employee)
        else:
            keep.append(emp)
    if result:
        save_employee_list(keep)
    return result

def remove_employee_by_id(id:int) -> bool:
    """
    Get a list of employees and copy them to a new list, excluding the 
    employee that matches the supplied ID.  Save the new list to file.
    Return True if the employee was removed, and False otherwise.

    INPUTS:
        id The ID of the employee to remove
    RETURNS:
        bool True if the employee was removed, False otherwise
    """
    result = False # initialize - we haven't found the ID yet
    keep = []
    employees = get_employee_list()
    for employee in employees:
        if employee[ID_IDX] == id: # matched!
            result = True
        else:
            keep.append(employee)
    if result:
        save_employee_list(keep)
    return result

def save_employee_list(employees:list):
    """
    Loops through the list of employees and writes them to FILE_NAME.
    This completely overwrites the existing file.

    INPUTS:
        employees A list of employee records
    """
    with open(FILE_NAME, 'w') as out_file:
        for employee in employees:
            line = convert_record_to_string(employee)
            out_file.write(line)

def convert_record_to_string(employee:list) -> str:
    """
    Takes an employee record as a list and converts it into a comma-separated
    string suitable for writing to a file.

    INPUTS:
        employee An employee record as a list
    RETURNS:
        string A comma-separated string representing the employee
    """
    line = f"{employee[ID_IDX]},{employee[LNAME_IDX]},{employee[FNAME_IDX]}" \
        f",{employee[DEPT_IDX]},{employee[SALARY_IDX]:.2f}\n"
    return line


