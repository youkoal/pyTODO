import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

#from pyTODO.Models.one_task import one_task
from pyTODO.Models.one_task import one_task
from pyTODO.Models.taskbox import taskbox


a_task = one_task("Test Task", "This is a test task") 
a_second_task = one_task("Second Task", "This is another test task")
a_third_task = one_task("Third Task", "This is yet another test task")  

a_taskbox = taskbox()
a_taskbox.set_title("My Task Box")
a_taskbox.add_new_task(a_task)
a_taskbox.add_new_task(a_second_task)
a_taskbox.add_new_task(a_third_task)


print("Initial Task Box with second task checked:")
a_taskbox.check_task(a_second_task)
a_taskbox.print_console()  # Should print the task box details with tasks


print("Initial Task Box with NO task checked:")
a_taskbox.uncheck_task(a_second_task)
a_taskbox.print_console()  # Should print the task box details with tasks


print("Initial Task Box with first and second task checked:")
a_taskbox.check_task(a_task)
a_taskbox.check_task(a_second_task)
a_taskbox.print_console()  # Should print the task box details with tasks


print("Initial Task Box with ALL checked:")
a_taskbox.set_title("Finished Task Box")
a_taskbox.check_task(a_third_task)
a_taskbox.print_console()  # Should print the task box details with tasks