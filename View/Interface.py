import sys, os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QLabel, QVBoxLayout, QWidget
from Models.taskbox import taskbox
from Models.taskboxes import taskboxes
from utils.stringUtility import stringUtility
from View.tasks_views import *


class MaFenetre(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ToDoListe')
        self.resize(1000,1000)

        ## Appelle des fonctions initiales
        self.CreerAction()

        self.CreerMenu()
        self.Layout_central = QWidget()
        self.setCentralWidget(self.Layout_central)
        
        self.Layout_relais = QVBoxLayout()
        self.Layout_central.setLayout(self.Layout_relais)

    def CreerAction(self):

        self.ActNouveau = QAction("Nouvelle liste")
        self.ActNouveau.setShortcut('ctrl+N')
        self.ActNouveau.triggered.connect(self.BoutonNouveau)

        self.ActOuvrir = QAction("Ouvrir une liste")
        self.ActOuvrir.setShortcut("Ctrl+O")

        self.ActFuite = QAction("Quitter")
        self.ActFuite.setShortcut("Alt+F4")
        self.ActFuite.triggered.connect(self.close)

            

    def CreerMenu(self):
        BarreMenu = self.menuBar()

        Fichier = BarreMenu.addMenu("&Fichier")
        Fichier.addAction(self.ActNouveau)
        Fichier.addSeparator()
        Fichier.addAction(self.ActOuvrir)
        Fichier.addSeparator()
        Fichier.addAction(self.ActFuite)

    def BoutonNouveau(self):
        print("Creation d'une nouvelle liste")
        boxes = taskboxes()
        boxes.load_json()

        tasksLayout = QVBoxLayout()
        tasks = QWidget()
        tasks.setLayout(tasksLayout)

        for box in boxes.get_taskboxes():
            box_view = create_taskbox_view(box)
            box_view.setStyleSheet("background-color: lightgray; padding: 10px; border-radius: 5px; border: 1px solid black")
            tasksLayout.addWidget(box_view)

        self.Layout_relais.addWidget(tasks)




        







            


