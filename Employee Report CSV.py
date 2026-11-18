
#!/usr/bin/env python3
"""
Employee Report Generator.

This script reads employee records from a CSV file, counts the total number
of employees per department, and exports an alphabetically sorted summary
to a plain text file.
"""

import csv
import os


# =====================================================================
# FUNCTION DEFINITIONS
# =====================================================================

def validate_csv_file(csv_file_path):
    """
    Verifies that the input path refers to an existing CSV file.
    """
    if os.path.splitext(csv_file_path)[1].lower() != ".csv":
        raise ValueError(f"The input file must have a .csv extension: {csv_file_path}")
    if not os.path.isfile(csv_file_path):
        raise FileNotFoundError(f"CSV file not found: {csv_file_path}")


def read_employees(csv_file_path):
    """
    Reads an employee CSV file using a custom dialect and returns a list
    of dictionaries representing each employee record.
    """
    # Register a custom dialect to strip leading whitespace after delimiters
    csv.register_dialect("empDialect", skipinitialspace=True, strict=True)

    employee_list = []

    # Open the CSV file safely using UTF-8 encoding
    with open(csv_file_path, mode="r", encoding="utf-8") as file:
        # Parse each row into a dictionary using the first row as keys
        employee_reader = csv.DictReader(file, dialect="empDialect")

        # Convert each ordered row into a standard dictionary and append to list
        for row in employee_reader:
            employee_list.append(dict(row))

    return employee_list


def process_data(employee_list):
    """
    Aggregates employee records and returns a dictionary mapping each
    unique department name to its total employee headcount.
    """
    department_list = []

    # Extract the department value from every employee dictionary
    for employee_data in employee_list:
        department_list.append(employee_data["Department"])

    department_counts = {}

    # Use set() to iterate over unique department names and count occurrences
    for department_name in set(department_list):
        department_counts[department_name] = department_list.count(department_name)

    return department_counts


def write_report(department_counts, report_file_path):
    """
    Writes the department headcount dictionary to a text file,
    sorted alphabetically by department name.
    """
    # Open the output file in write/read mode (overwrites previous report)
    with open(report_file_path, mode="w+", encoding="utf-8") as file:
        # Sort dictionary keys alphabetically before writing each line
        for department in sorted(department_counts):
            file.write(f"{department}:{department_counts[department]}\n")


def main():
    """
    Main execution workflow: resolves file paths, validates the input CSV,
    processes records, and generates the final report.
    """
    # Dynamically resolve the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Build cross-platform file paths for input CSV and output report
    name_file = input("Enter the name of the CSV file (with .csv extension): ").strip()
    csv_file_path = os.path.join(base_dir, name_file)
    report_file_path = os.path.join(base_dir, "report.txt")

    # Step 1: Ensure the input is an existing CSV file
    validate_csv_file(csv_file_path)

    # Step 2: Read employee records from CSV
    employees = read_employees(csv_file_path)

    # Step 3: Calculate employee headcount per department
    department_summary = process_data(employees)

    # Step 4: Export formatted summary to text file
    write_report(department_summary, report_file_path)

    print(f"Report successfully generated at: {report_file_path}")


# =====================================================================
# SCRIPT ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    main()
