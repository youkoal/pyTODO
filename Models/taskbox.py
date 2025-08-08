import sys
sys.path.append(r'd:\Codes')

from pyTODO.utils.stringUtility import stringUtility
from pyTODO.Models.one_task import one_task

class taskbox:

    __tasks_todo = []
    __tasks_done = []
    __title = "New task Box"

    def __init__(self):
        self.__tasks_todo = []
        self.__tasks_done = []

    def add_new_task(self, task):
        task.set_index(len(self.__tasks_todo))
        self.__tasks_todo.append(task)

    def check_task(self, task):
        task.trigger()
        self.__tasks_todo.pop(task.get_index())

        task.set_index(len(self.__tasks_done))
        self.__tasks_done.append(task)

    def uncheck_task(self, task):
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
    
    def get_console(self, length=54, metadata=False):
        """ Returns a formatted array representation of the task box for console output. """
        lines = []

        lines.append(stringUtility.piped_separator("■", length))
        lines.append(stringUtility.format_string(f"{self.__title}", length, 1 , 1 , 1 , 2))
        lines.append(stringUtility.piped_separator("⬞", length))
        
        if len(self.__tasks_todo) > 0:
            lines.append(stringUtility.format_string("Tasks to do:", length, 1, 1,1,1))
            for task in self.__tasks_todo:
                lines.extend(self.get_console_extended(task, 50, metadata))
        else:
            lines.append(stringUtility.format_string("No tasks to do", length, 1, 1,1,1))

        if len(self.__tasks_done) > 0:
            lines.append(stringUtility.format_string("Tasks done:", length, 1, 1,1,1))
            for task in self.__tasks_done:
                lines.extend(self.get_console_extended(task, 50, metadata))
        else:
            lines.append(stringUtility.format_string("No tasks done", length, 1, 1,1,1))

        lines.append(stringUtility.piped_separator("■", length))
        return lines
    
    def get_console_extended(self, task, length=54, metadata=False):
        """ Returns a formatted array representation of the task box for console output with extended details. """
        lines = task.get_console(length, metadata)
        for i in range(len(lines)):
            lines[i] = stringUtility.indent_string(lines[i], 2)
            lines[i] = stringUtility.add_spaces(lines[i], length)
            lines[i] = stringUtility.add_pipes(lines[i])
        return lines

    def print_console(self):
        for line in self.get_console():
            print(line)

        #print (stringUtility.piped_separator("■",52))
        #print (stringUtility.format_string(f"{self.__title}"),52)
        #print (stringUtility.piped_separator("⬞",52))
        #
        #if len(self.__tasks_todo) > 0:
        #    print (stringUtility.format_string("Tasks to do:",52,1,1))
        #    for task in self.__tasks_todo:
        #        task.print_console()
        #else:
        #    print (stringUtility.format_string("No tasks to do",52,1,1))
        #
        #if len(self.__tasks_done) > 0:
        #    print (stringUtility.format_string("Tasks done:",52,1,1))
        #    for task in self.__tasks_done:
        #        task.print_console()
        #else:
        #    print (stringUtility.format_string("No tasks done",52,1,1))
        #
        #print (stringUtility.piped_separator("■",52))