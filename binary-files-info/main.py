# _*_ coding: utf-8 _*_

"""This module provides binary_file_func entry point script."""

from binary_files import file_information

if __name__ == "__main__":
    #Calling the function to print the string, character at a time
    file = input("Please input full path to the file: \n")
    print(file_information(file))