import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils.stringUtility import stringUtility
from utils.jsonUtility import JsonUtility
from Models.one_task import one_task

class taskbox:
    """A class to represent a task box containing tasks.
    Attributes:
        __tasks_todo (list): A list of tasks that are yet to be completed.
        __tasks_done (list): A list of tasks that have been completed.
        __title (str): The title of the task box.
        Methods:
            add_new_task(task): Adds a new task to the task box.
            erase_task(task) : Remove the selected task.
            check_task(task): Marks a task as completed and moves it to the done list.
            uncheck_task(task): Marks a task as not completed and moves it back to the todo list.
            Zcheck_task(task) : Marks a task as completed and moves it to the done list.
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

    def erase_task(self,task):
        src_list = self.__tasks_done
        if task.task_status :
            src_list = self.__tasks_todo
        
        current_index = task.get_index()
        src_list.pop(current_index)
        for i in range(current_index, len(src_list)):
            src_list[i].set_index(src_list[i].get_index() - 1)
        

        
        

    
    def _move_task_between_lists(self, task, src_list, dst_list):
        """Helper to move a task between lists and update indices."""
        task.trigger()
        current_index = task.get_index()
        src_list.pop(current_index)
        for i in range(current_index, len(src_list)):
            src_list[i].set_index(src_list[i].get_index() - 1)
        task.set_index(len(dst_list))
        dst_list.append(task)

    def check_task(self, task):
        """Marks a task as completed and moves it to the done list."""
        self._move_task_between_lists(task, self.__tasks_todo, self.__tasks_done)

    def uncheck_task(self, task):
        """Marks a task as not completed and moves it back to the todo list."""
        self._move_task_between_lists(task, self.__tasks_done, self.__tasks_todo)
    
    def Zcheck_task(self, task):
        """Marks a task as completed and moves it to the done list."""
        if task.task_status:
            self._move_task_between_lists(task, self.__tasks_todo, self.__tasks_done)
        else:
            self._move_task_between_lists(task, self.__tasks_done, self.__tasks_todo)

    def set_title(self, title):
        self.__title = title
        return self.__title
    
    def get_title(self):
        return self.__title


    def get_tasks_todo(self):
        return self.__tasks_todo
    
    def get_tasks_done(self):
        return self.__tasks_done

    def get_all_tasks(self):
        return (self.__tasks_todo,self.__tasks_done)

    def get_all_tasks_flat(self):
        return self.__tasks_todo + self.__tasks_done

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
            lines[i] = stringUtility.format_string(lines[i], content_length, 1, 1, 1, 2)
            # lines[i] = stringUtility.add_spaces(lines[i], length)     
            # lines[i] = lines[i].center(content_length, ' ')       
            # lines[i] = stringUtility.add_pipes(lines[i])
        return lines

    def print_console(self):
        """Prints the task box details in a formatted console output."""
        for line in self.get_console():
            print(line)

    def to_json(self):
        """Converts the task box to a JSON serializable dictionary."""
        return {
            "title": self.__title,
            "tasks_todo": [task.to_json() for task in self.__tasks_todo],
            "tasks_done": [task.to_json() for task in self.__tasks_done]
        }
    
    def save_json(self):
        """Saves the task box to a JSON file."""
        complete_save_file_path = JsonUtility.get_save_directory()[0]
        if complete_save_file_path:
            JsonUtility.save_json(self.to_json(), complete_save_file_path)
        else:
            print("Error: Could not save task box. Save directory is not set.")

    def get_saved_json(self):
        """Loads the task box from a JSON file."""
        complete_save_file_path = JsonUtility.get_save_directory()[0]
        if complete_save_file_path:
            return JsonUtility.load_json(complete_save_file_path)
        else:
            print("Error: Could not load task box. Save directory is not set.")
            return None

    def load_json(self, json_data=None):
        """Loads the task box from a JSON serializable dictionary."""
        if json_data is None:
            json_data = self.get_saved_json()

        self.__title = json_data.get("title", "New task Box")
        self.__tasks_todo = [one_task.from_json(task) for task in json_data.get("tasks_todo", [])]
        self.__tasks_done = [one_task.from_json(task) for task in json_data.get("tasks_done", [])]
        
        # Update indices after loading tasks
        for i, task in enumerate(self.__tasks_todo):
            task.set_index(i)
        for i, task in enumerate(self.__tasks_done):
            task.set_index(i)
        return self.__tasks_todo
    
    def from_json(self, json_data):
        self.__title = json_data.get("title", "New task Box")
        self.__tasks_todo = [one_task.from_json(task) for task in json_data.get("tasks_todo", [])]
        self.__tasks_done = [one_task.from_json(task) for task in json_data.get("tasks_done", [])]

        # Update indices after loading tasks
        for i, task in enumerate(self.__tasks_todo):
            task.set_index(i)
        for i, task in enumerate(self.__tasks_done):
            task.set_index(i)
