import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from pyTODO.utils.stringUtility import stringUtility

class one_task:
    """A class to represent a single task.
    Attributes:
        task_name (str): The name of the task.
        task_description (str): A description of the task.
        task_id (int): An identifier for the task.
        task_status (bool): The status of the task, True for completed, False for not completed.
        index (int): The index of the task in a list or collection.
    Methods:
        print(): Prints a string representation of the task.
        get_index(): Returns the index of the task.
        set_index(index): Sets the index of the task.
        trigger(): Toggles the task status between completed and not completed.
        print_console(length=50, metadata=False): Prints the task details in a formatted console output.
        get_console(length, metadata=False): Returns a formatted array representation of the task for console output
    """
    def __init__(self, task_name, task_description):
        self.task_name = task_name
        self.task_description = task_description
        self.task_id = -1  # Default ID, can be set later
        self.task_status = True # Default status, can be set later
        self.index = -1  # Default index, can be set later

    def print(self):
        print (f"Task({self.task_id}, {self.task_name}, {self.task_description}, {self.task_status})")
        return f"Task({self.task_id}, {self.task_name}, {self.task_description}, {self.task_status})"
    
    def get_index(self):
        return self.index
    
    def set_index(self, index):
        self.index = index
        return self.index
    
    def trigger(self):
        """Toggles the task status between completed and not completed."""
        self.task_status = not self.task_status
        return self.task_status

    def print_console(self, length = 50 , metadata=False):
        """Prints the task details in a formatted console output.
        Args:
            length (int): The length of the console output.
            metadata (bool): If True, includes metadata in the output. (Identifier and status)
        """
        for line in self.get_console(length, metadata):
            print(line)


    def get_console(self, length, metadata=False):
        """ Returns a formatted array representation of the task for console output.
         Args:
            length (int): The length of the console output.
            metadata (bool): If True, includes metadata in the output. (Identifier and status)
        Returns:
            list: A list of strings representing the formatted task details.
        """
        lines = []
        checked = "✔" if self.task_status else "✘"

        lines.append(stringUtility.piped_separator("=",length))
        if metadata:
             lines.append (stringUtility.format_string(f"Task ID : {self.task_id}    checked : {self.task_status}"))
             lines.append (stringUtility.piped_separator("-",length))
        lines.append (stringUtility.format_string(f"{checked} {self.task_name}"))
        lines.append (stringUtility.format_string(f"{self.task_description}",length,6,6))
        lines.append (stringUtility.piped_separator("=",length))
        return lines
