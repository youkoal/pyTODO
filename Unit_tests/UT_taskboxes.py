import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

#from pyTODO.Models.one_task import one_task
from Models.taskboxes import taskboxes
from Unit_tests.mocks.UT_taskboxes_taskbox_def import *


# taskboxes = taskboxes()
# # taskboxes.add_taskbox(a_taskbox)
# # taskboxes.add_taskbox(b_taskbox)
# # taskboxes.add_taskbox(c_taskbox)
# # 
# taskboxes.load_json()



# for taskbox in taskboxes.get_taskboxes():
#     taskbox.print_console()

# taskboxes.save_json()


# tests pour GUI
taskboxes = taskboxes()
taskboxes.load_json()
for taskbox in taskboxes.get_taskboxes():
    print(f"Taskbox Title: {taskbox.get_title()}")
    for task in taskbox.get_tasks_todo() :
        print(f" - Todo Task: {task.task_name}")
        print(f" - Todo Task Description: {task.task_description}")
        print(f" - Todo Task ID: {task.task_id}")
        print(f" - Todo Task Status: {task.task_status}")
        print(f" - Todo Task Index: {task.index}")

    for task in taskbox.get_tasks_done() :
        print(f" - Done Task: {task.task_name}")
        print(f" - Done Task Description: {task.task_description}")
        print(f" - Done Task ID: {task.task_id}")
        print(f" - Done Task Status: {task.task_status}")
        print(f" - Done Task Index: {task.index}")

# reccupèrer les task box et stocker la premiere pour tests
taskbox1 = taskboxes.get_taskboxes()[0]

# récupérer les task todo du la premiere task box pour les tests
taskbox1_task_todo = taskbox1.get_tasks_todo()

# récupérer la première task todo de la première task box pour les tests
task1 = taskbox1_task_todo[0]

# modifier la task pour quelques tests
task1.task_name = "Modified Task Name"
task1.task_description = "Modified Task Description"

# save pour test
taskboxes.save_json()