import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from utils.stringUtility import stringUtility
from utils.jsonUtility import JsonUtility
from Models.one_task import one_task
from Models.taskbox import taskbox


class taskboxes :
    """A class to manage multiple task boxes.
    
    Attributes:
        __task_boxes (list): A list of taskbox instances.
    
    Methods:
        add_taskbox(taskbox): Adds a new taskbox to the list.
        get_taskboxes(): Returns the list of taskboxes.
        save_json(): Saves all taskboxes to a JSON file.
        load_json(): Loads taskboxes from a JSON file.
        to_json(): Converts the taskboxes to a JSON serializable format.
    """
    
    __task_boxes = []
    __save_file_path = JsonUtility.get_save_directory()[1]

    def add_taskbox(self, taskbox):
        """Adds a new taskbox to the list."""
        self.__task_boxes.append(taskbox)

    def get_taskboxes(self):
        """Returns the list of taskboxes."""
        return self.__task_boxes

    def save_json(self):
        """Saves all taskboxes to a JSON file."""
        JsonUtility.save_json(self.to_json(), self.__save_file_path)

    def load_json(self):
        """Loads taskboxes from a JSON file."""
        data = JsonUtility.load_json(self.__save_file_path)
        for taskbox_data in data:
            a_taskbox = taskbox()
            a_taskbox.from_json(taskbox_data)
            self.add_taskbox(a_taskbox)

    def to_json(self):
        """Converts the taskboxes to a JSON serializable format."""
        return [taskbox.to_json() for taskbox in self.__task_boxes]