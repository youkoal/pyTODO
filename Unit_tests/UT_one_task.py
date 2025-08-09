import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

from pyTODO.Models.one_task import one_task


a_task = one_task("Test Task", "This is a test task") 
a_task.print()  # Should return a string representation of the task
print(a_task.get_index())   # Should return -1 as index is not set
print(a_task.set_index(0))  # Set index to 0
print(a_task.get_index())   # Should now return 0

print("\n default pretty print with methadata :")
a_task.print_console(50,1)  # Should print the task details in a formatted console output
print("\n default pretty print :")
a_task.print_console()  # Should print the task details in a formatted console output

print("\n pretty print with status triggered ✘ :")
a_task.trigger()  # Toggle task status
a_task.print_console()

print("\n pretty print with status triggered again ✔ :")
a_task.trigger()  # Toggle task status
a_task.print_console()