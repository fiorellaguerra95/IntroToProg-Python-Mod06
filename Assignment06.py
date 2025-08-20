# --------------------------------------------------------------------------- #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Fiorella Guerra, 08/19/2025, Updated Script
# --------------------------------------------------------------------------- #

import json  # import code from Python's JSON module into my script

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 

'''

# Define the Data Variables
# Holds the first name of a student entered by the user.
student_first_name: str = ''
# Holds the last name of a student entered by the user.
student_last_name: str = ''
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

# Processing --------------------------------------- #


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    FGuerra,8.19.2025,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(
                "Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list) -> None:

        try:
            file = open(FILE_NAME, "w")
            json.dump(student_data, file)
            file.close()
            for student in student_data:
                print()
                print("Student", student['FirstName'], student['LastName'],
                      "is enrolled in", student['CourseName'])
        except TypeError as e:
            IO.output_error_messages(
                "Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    FGuerra, 8/19/2025, Created Class
    FGuerra, 8/19/2025, Added menu output and input functions
    FGuerra, 8/19/2025, Added a function to display the data
    FGuerra, 8/19/2025, Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ 
        This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        FGuerra, 8/19/2025, Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str) -> None:
        """ 
        This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        FGuerra, 8/19/2025, Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice() -> str:
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            # Not passing e to avoid the technical message
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def input_student_data(student_data: list) -> list:
        """ 
        This function gets the first name, last name, and course name from user

        ChangeLog: (Who, When, What)
        FGuerra,8/19/2025, Created function

        :return: list  
        """

        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages(
                "That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return student_data

    @staticmethod
    def output_student_data(student_data: list) -> None:
        """
        This function displays student data in comma separated values

        ChangeLog: (Who, When, What)
        FGuerra, 8/19/2025, Created function

        :return: None
        """
        # Process the data to create a comma separated value for each row
        print("-"*50)
        for student in student_data:
            print(",".join(student.values()))
        print("-"*50)

#  End of function definitions


# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(
    file_name=FILE_NAME, student_data=students)

# Repeat the following tasks
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue
    elif menu_choice == "2":
        IO.output_student_data(student_data=students)
        continue
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(
            file_name=FILE_NAME, student_data=students)
        continue
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended. Goodbye!")
