import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

#from pyTODO.Models.one_task import one_task
from Models.taskboxes import taskboxes
from Unit_tests.mocks.UT_taskboxes_taskbox_def import *


taskboxes = taskboxes()
taskboxes.add_taskbox(a_taskbox)
taskboxes.add_taskbox(b_taskbox)
taskboxes.add_taskbox(c_taskbox)

# taskboxes.load_json()



for taskbox in taskboxes.get_taskboxes():
    taskbox.print_console()

taskboxes.save_json()