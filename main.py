import sys
import os
#Necessaire pour lancer la QApplication pour la fenetre
from PySide6.QtWidgets import QApplication


parent_dir = os.path.dirname(__file__)
sys.path.append(parent_dir)

from Models.taskbox import taskbox
#Interface
from View.Interface import MaFenetre


def main():
	#self.task_boxes = [] #future implementation
	#task_box = taskbox()
	#task_box.load_json()
	#task_box.print_console()

    #main_windows = ...
	app = QApplication(sys.argv)
	myWindow = MaFenetre()
	myWindow.show()
	sys.exit(app.exec())
	
    #on passe la/les taskbox en parametre pour géré les signaux
    #main_windows.init(task_box)
	



if __name__ == "__main__":
	main()
