import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

#from pyTODO.Models.one_task import one_task
from Models.one_task import one_task
from Models.taskbox import taskbox


a_task = one_task("Test Task", "This is a test task for saves tests") 
a_second_task = one_task("Second Task", "This is another test task for saves tests")
a_third_task = one_task("Third Task", "This is yet another test task for saves tests")  
a_fourth_task = one_task("a task", "for saves tests")  


a_taskbox = taskbox()
a_taskbox.load_json()




#a_taskbox.add_new_task(a_task)
#a_taskbox.add_new_task(a_second_task)
#a_taskbox.add_new_task(a_third_task)
#a_taskbox.add_new_task(a_fourth_task)
#a_taskbox.check_task(a_fourth_task)
#a_taskbox.save_json()

#a_taskbox.uncheck_task(a_taskbox.get_tasks_done()[2])
#a_taskbox.uncheck_task(a_taskbox.get_tasks_done()[2])

# print("Initial Task Box with ALL checked:")
# a_taskbox.set_title("Finished Task Box")
# a_taskbox.check_task(a_third_task)
a_taskbox.print_console()  # Should print the task box details with tasks