class one_task:
    def __init__(self, task_id, task_name, task_description, task_status):
        self.task_id = -1  # Default ID, can be set later
        self.task_name = task_name
        self.task_description = task_description
        self.task_status = task_status
        self.index = -1  # Default index, can be set later

    def print(self):
        print (f"Task({self.task_id}, {self.task_name}, {self.task_description}, {self.task_status})")
        return f"Task({self.task_id}, {self.task_name}, {self.task_description}, {self.task_status})"
    
    def get_index(self):
        return self.index
    
    def set_index(self, index):
        self.index = index
        return self.index