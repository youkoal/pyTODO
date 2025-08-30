import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.one_task import one_task
from Models.taskbox import taskbox



a_task = one_task("Test Task", "This is a test task") 
a_second_task = one_task("Second Task", "This is another test task")
a_third_task = one_task("Third Task", "This is yet another test task with a verry long description that should be truncated in the console output")  
a_fourth_task = one_task("a task", "Just for guigui")  

a_taskbox = taskbox()
a_taskbox.set_title("My Task Box")
a_taskbox.add_new_task(a_task)
a_taskbox.add_new_task(a_second_task)
a_taskbox.add_new_task(a_third_task)

a_taskbox.check_task(a_second_task)
a_taskbox.print_console()

a_taskbox.Zcheck_task(a_second_task)
a_taskbox.print_console()

a_taskbox.Zcheck_task(a_second_task)
a_taskbox.print_console()




a_taskbox.save_json()

print("\nAfter checking second task:")
a_taskbox.print_console()

all_tasks = a_taskbox.get_all_tasks_flat()
print("\nAll Tasks 1by 1:")
for task in all_tasks:
    task.print_console()
    print(all_tasks.index(task))

print("\nInitial Task Box:")
a_taskbox.print_console()

a_taskbox.erase_task(all_tasks[0])

print("\nAfter erasing first task:")
a_taskbox.print_console()
#a_taskbox.print_console()


# print("Initial Task Box with ALL checked:")
# a_taskbox.set_title("Finished Task Box")
# a_taskbox.check_task(a_third_task)
# a_taskbox.print_console()  # Should print the task box details with tasks