import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from pyTODO.utils.stringUtility import stringUtility
from pyTODO.Models.one_task import one_task

class taskbox:
    """A class to represent a task box containing tasks.
    Attributes:
        __tasks_todo (list): A list of tasks that are yet to be completed.
        __tasks_done (list): A list of tasks that have been completed.
        __title (str): The title of the task box.
        Methods:
            add_new_task(task): Adds a new task to the task box.
            check_task(task): Marks a task as completed and moves it to the done list.
            uncheck_task(task): Marks a task as not completed and moves it back to the todo list.
            set_title(title): Sets the title of the task box.
            get_tasks_todo(): Returns the list of tasks that are yet to be completed.
            get_tasks_done(): Returns the list of tasks that have been completed.
            get_all_tasks(): Returns both todo and done tasks.
            get_console(length=60, metadata=False): Returns a formatted array representation of the task box
            print_console(): Prints the task box details in a formatted console output.
        """

    __tasks_todo = []
    __tasks_done = []
    __title = "New task Box"

    def __init__(self):
        """Initializes a new task box with empty todo and done lists."""
        self.__tasks_todo = []
        self.__tasks_done = []

    def add_new_task(self, task):
        task.set_index(len(self.__tasks_todo))
        self.__tasks_todo.append(task)

    #todo : decrement index of all tasks after the removed task 
    def check_task(self, task):
        """Marks a task as completed and moves it to the done list."""
        task.trigger()
        self.__tasks_todo.pop(task.get_index())

        task.set_index(len(self.__tasks_done))
        self.__tasks_done.append(task)

    def uncheck_task(self, task):
        """Marks a task as not completed and moves it back to the todo list."""
        task.trigger()
        self.__tasks_done.pop(task.get_index())

        task.set_index(len(self.__tasks_todo))
        self.__tasks_todo.append(task)
    

    def set_title(self, title):
        self.__title = title
        return self.__title


    def get_tasks_todo(self):
        return self.__tasks_todo
    
    def get_tasks_done(self):
        return self.__tasks_done

    def get_all_tasks(self):
        return (self.__tasks_todo,self.__tasks_done)

    def __repr__(self):
        return f"TaskBox({self.__title}, Todo: {len(self.__tasks_todo)}, Done: {len(self.__tasks_done)})"
    




    def get_console(self, length=60, metadata=False):
        """ Returns a formatted array representation of the task box for console output. """
        lines = []

        lines.append(stringUtility.piped_separator("■", length))
        lines.append(stringUtility.format_string(f"{self.__title}", length, 1 , 1 , 1 , 2))
        lines.append(stringUtility.piped_separator("⬞", length))
        
        if len(self.__tasks_todo) > 0:
            lines.append(stringUtility.format_string("Tasks to do:", length, 1, 1,1,1))
            for task in self.__tasks_todo:
                lines.extend(self.get_console_extended(task, 50,length, metadata))
        else:
            lines.append(stringUtility.format_string("No tasks to do", length, 1, 1,1,1))

        if len(self.__tasks_done) > 0:
            lines.append(stringUtility.format_string("Tasks done:", length, 1, 1,1,1))
            for task in self.__tasks_done:
                lines.extend(self.get_console_extended(task, 50,length, metadata))
        else:
            lines.append(stringUtility.format_string("No tasks done", length, 1, 1,1,1))

        lines.append(stringUtility.piped_separator("■", length))
        return lines
    
    def get_console_extended(self, task, length=54, content_length =54, metadata=False):
        """ 
        Returns a formatted array representation of the task box for console output with extended space for task details. and centered "boxes"
        Args:
            task (one_task): The task to format.
            length (int): The length of the console output.
            content_length (int): The length of the content inside the box.
            metadata (bool): If True, includes metadata in the output. (Identifier and status)  
        Returns:
            list: A list of strings representing the formatted task.
        """
        
        lines = task.get_console(length, metadata)
        for i in range(len(lines)):
            lines[i] = stringUtility.add_spaces(lines[i], length)     
            lines[i] = lines[i].center(content_length, ' ')       
            lines[i] = stringUtility.add_pipes(lines[i])

            
        return lines

    def print_console(self):
        """Prints the task box details in a formatted console output."""
        for line in self.get_console():
            print(line)