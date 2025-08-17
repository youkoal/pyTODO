import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Models.one_task import one_task
from Models.taskbox import taskbox


a_task          = one_task("TB 1 Test Task"     , "TB 1 This is a test task") 
a_second_task   = one_task("TB 1 Second Task"   , "TB 1 This is another test task")
a_third_task    = one_task("TB 1 Third Task"    , "TB 1 This is yet another test task with a verry long description that should be truncated in the console output")  
a_fourth_task   = one_task("TB 1 a task"        , "TB 1 Just for guigui")  

a_taskbox = taskbox()
a_taskbox.set_title("My Task Box 1")
a_taskbox.add_new_task(a_task)
a_taskbox.add_new_task(a_second_task)
a_taskbox.add_new_task(a_third_task)

a_taskbox.check_task(a_second_task)
a_taskbox.uncheck_task(a_second_task)
a_taskbox.check_task(a_task)
a_taskbox.check_task(a_second_task)
a_taskbox.add_new_task(a_fourth_task)


b_task          = one_task("TB 2 Test Task"     , "TB 2 This is a test task") 
b_second_task   = one_task("TB 2 Second Task"   , "TB 2 This is another test task")
b_third_task    = one_task("TB 2 Third Task"    , "TB 2 This is yet another test task with a verry long description that should be truncated in the console output")  
b_fourth_task   = one_task("TB 2 a task"        , "TB 2 Just for guigui")  

b_taskbox = taskbox()
b_taskbox.set_title("My Task Box 2")
b_taskbox.add_new_task(b_task)
b_taskbox.add_new_task(b_second_task)
b_taskbox.add_new_task(b_third_task)
b_taskbox.add_new_task(b_fourth_task)

b_taskbox.check_task(b_second_task)
b_taskbox.uncheck_task(b_second_task)
b_taskbox.check_task(b_task)
b_taskbox.check_task(b_second_task)
b_taskbox.add_new_task(b_fourth_task)


c_task          = one_task("TB 3 Test Task"     , "TB 3 This is a test task") 
c_second_task   = one_task("TB 3 Second Task"   , "TB 3 This is another test task")
c_third_task    = one_task("TB 3 Third Task"    , "TB 3 This is yet another test task with a verry long description that should be truncated in the console output")  
c_fourth_task   = one_task("TB 3 a task"        , "TB 3 Just for guigui")  

c_taskbox = taskbox()
c_taskbox.set_title("My Task Box 3")
c_taskbox.add_new_task(c_task)
c_taskbox.add_new_task(c_second_task)
c_taskbox.add_new_task(c_third_task)
c_taskbox.add_new_task(c_fourth_task)

c_taskbox.check_task(c_second_task)
c_taskbox.uncheck_task(c_second_task)
c_taskbox.check_task(c_task)
c_taskbox.check_task(c_second_task)
c_taskbox.add_new_task(c_fourth_task)


