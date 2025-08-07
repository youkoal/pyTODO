import one_task

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
        self.__tasks_todo.pop(task.get_index())

        task.set_index(len(self.__tasks_done))
        self.__tasks_done.append(task)

    def uncheck_task(self, task):
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