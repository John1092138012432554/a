"""
Filename: parser.py
Author: Henry Holtslander
Created: 09/16/2024
Version: 1.0.0
Description:
    For use in the Python Programming Class at Osbourn High School
    This Python file defines a class Parser that facilitates reading
    and printing the contents of text files. It includes functionality
    to insert variables into the text and add a delay to the print.
Dependencies: time
"""

# Import statements
from time import sleep


class Parser:
    def __init__(self, path=None):
        """
        Facilitates reading and printing the contents of text files

        :param path: The path to the file you want to print from
        """
        self.path = path

        # Check to see if a path argument was passed
        if path is not None:
            self.file = open(self.path, 'r')
        else:
            self.file = None


    # Close any open files
    def __unload(self):
        if self.file is not None:
            self.file.close()


    # Open a new file with read access
    def  __load(self, path):
        # Close any open files before loading a new one
        if self.file is not None:
            self.__unload()

        # Open file at path
        self.path = path
        self.file = open(self.path, "r")


    # Helper function to print each char with a delay
    def __pprint(self, text, pause):
        for c in text:
            print(c, end="", flus=True)
            sleep(pause)
        print("\n", end="", flush=True)


    def print(self, path_to_file, *args, pause=0):
        """
        Prints the text file to stdout using an indefinite number of arguments.
        Pause can optionally be included to print the files one letter at a time
        with a delay.

        :param path_to_file: The path to the text file
        :param args: An array of arguments to insert into the text upon printing.
        :param pause: The amount of time in seconds to wait before printing the next
                        character.
        """
        # Load the text file
        self.__load(path_to_file)

        # If there are variables and pause
        if pause != 0 and args is not None:
            text = self.file.read().format(*args)
            self.__pprint(text, pause)

        # If there are variables, but no pause
        elif pause == 0 and args is not None:
            print(self.file.read().format(*args))

        # If there are no variables, but pause
        elif pause != 0 and args is None:
            text = self.file.read()
            self.__pprint(text, pause)

        # If there are no variables or pause, print the file normally
        else:
            print(self.file.read())


    def dprint(self, path_to_file, keys=None, pause=0):
        """
        Prints the text file to stdout using a dictionary to insert values into
        the text that correspond with the keys written in the text file.
        Pause can optionally be included to print the files one letter at a time
        with a delay.

        :param path_to_file: The path to the text file
        :param keys: A dictionary containing key/value pairs to insert into the text
                        upon printing.
        :param pause: The amount of time in seconds to wait before printing the next
                        character.
        """
        # Load the text file
        self.__load(path_to_file)

        # If there are variables and pause
        if pause != 0 and keys is not None:
            text = self.file.read().format(**keys)
            self.__pprint(text, pause)

        # If there are variables, but no pause
        elif pause == 0 and keys is not None:
            print(self.file.read().format(**keys))

        # If there are no variables, but pause
        elif pause != 0 and keys is None:
            text = self.file.read()
            self.__pprint(text, pause)

        # If there are no variables or pause, print the file normally
        else:
            print(self.file.read())


    def destroy(self):
        """
        A clean-up function to close any open files. After running destroy,
        the variable that points to the Parser should be set to None.
        """
        self.__unload()