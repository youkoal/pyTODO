import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils.stringUtility import stringUtility


a_string = "Example string to demonstrate the utility function.  This will be split into multiple lines if it exceeds the specified length."
a_smoll_string = "Short string."

print("\nFormatted String with Pipes and Indentation as an array :")
print (stringUtility.format_string(a_string,50,2,8,0))  # Example usage of the utility function

print("\nFormatted String with specified 2 Indent and 8 dedent as a string :")
print (stringUtility.format_string(a_string,70,2,8,1))  # Example usage of the utility function

print("\nFormatted String with (default) 4 Indent and 2 dedent as a string :")
print (stringUtility.format_string(a_string,50))  # Example usage of the utility function

print("\nFormatted String with specified 2 Indent and 2 dedent as a string :")
print (stringUtility.format_string(a_string,50,2,2))  # Example usage of the utility function


print("\nFormatted smoll String:")
print (stringUtility.format_string(a_smoll_string,50,2,2,1,2))  # Example usage of the utility function
