# import des bibliothèques nécessaire pour IUG, creation de fichier et systeme

import sys
import os 
import json

#Import des composants de Pyside pour construire l'application

from PySide6.QtCore import QSize, Signal, Qt
from PySide6.QtGui import QStandardItemModel,QStandardItem,QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from ui.task_ui import UI_Taskform
from ui.main_ui import Ui_MainWindow

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

#La classe FenetrePrincipale est la fenetre principale de l'application


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        # Chargement de la fentre principale
        self.ui = Ui_MainWindow()
        self.ui.setupUI(self)

        # Attribut des element de l'UI a des variables
        self.list_view = self.ui.task_listView
        self.add_btn = self.ui.add_btn
        self.task_input = self.ui.new_task

        self.list_model = QStandardItemModel()
        self.init_ui()


        self.task_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"task.json"))
        self.task_list = self.get_task()
        self.show_task(self.task_list)




    #initialisation
    def init_ui(self):
        #parametre le model pour la liste et personalise l'apparence
        self.list_view.setModel(self.list_model)
        self.list_view.setSpacing(5)
        self.list_view.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        #Icone du bouton et signal
        self.add_btn.setIcon(QIcon(os.path.join(parent_dir, "icons/bouton.svg")))
        self.add_btn.clicked.connect(self.add_new_task)

    def add_new_task(self):
        new_task = self.task_input.text().strip()
        if new_task:
            self.task_list.append([new_task,False])
            self.show_task(self.task_list)
            self.task_input.clear()

    def remove_item(self, position):
        self.list_model.removeRow(position)
        self.task_list.pop(position)
        self.get_all_tasks()
        self.show_task(self.task_list)



    def get_task(self):
        with open(self.task_file_path, "r") as f:
            tasks_data_str = f.read()
            if tasks_data_str :
                tasks = json.loads(tasks_data_str)
                return tasks["tasks"]
            else : 
                return list() #liste vide si le fichier n'existe pas
            


    def show_task(self, task_list):
        self.list_model.clear()
        if task_list:
            for i, task in enumerate(task_list):
                item = QStandardItem()
                self.list_model.appendRow(item)
                widget = UI_Taskform(task[0], task[1], i)
                widget.closeClicked.connect(self.remove_item)
                item.setSizeHint(widget.sizeHint())
                self.list_view.setIndexWidget(self.list_model.indexFromItem(item),widget)


    def get_all_tasks(self):

        self.task_list = []
        for row in range(self.list_model.rowCount()):
            item = self.list_model.item(row, 0)
            widget = self.list_view.indexWidget(item.index())
            if isinstance(widget,UI_Taskform):
                self.task_list.append([widget.Get_CheckBox_Text(),widget.Get_CheckBox_State()])            

    def closeEvent(self, event):
        self.get_all_tasks()
        with open(self.task_file_path, "w") as f: 
            f.write(json.dumps({"tasks": self.task_list}))   

if __name__== "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
