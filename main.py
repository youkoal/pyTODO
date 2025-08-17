import sys
import os

parent_dir = os.path.dirname(__file__)
sys.path.append(parent_dir)

from Models.taskbox import taskbox


def main():
	#self.task_boxes = [] #future implementation
	task_box = taskbox()
	task_box.load_json()
	task_box.print_console()

    #main_windows = ...
	
    #on passe la/les taskbox en parametre pour géré les signaux
    #main_windows.init(task_box)
	



if __name__ == "__main__":
	main()
