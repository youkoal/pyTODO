import sys
sys.path.append(r'd:\Codes')

from pyTODO.utils.stringUtility import stringUtility

class one_task:
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
        self.task_status = not self.task_status
        return self.task_status

    def print_console(self, length = 50 , metadata=False):
        #checked = "✔" if self.task_status else "✘"
        #print (stringUtility.piped_separator("=",50))
        #if metadata:
        #    print (stringUtility.format_string(f"Task ID : {self.task_id}    checked : {self.task_status}"))
        #    print (stringUtility.piped_separator("-",50))
        #print (stringUtility.format_string(f"{checked} {self.task_name}"))
        #print (stringUtility.format_string(f"{self.task_description}",50,6,6))
        #print (stringUtility.piped_separator("=",50))
        for line in self.get_console(length, metadata):
            print(line)


    def get_console(self, length, metadata=False):
        """ Returns a formatted array representation of the task for console output. """
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
