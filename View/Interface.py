import sys, os

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QLabel, QVBoxLayout, QWidget
from Models.taskbox import taskbox


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
        BoiteTache = taskbox()
        BoiteTache.load_json()
        text = []
        for line in BoiteTache.get_console():
            text = line
            message = QLabel(text)
            self.Layout_relais.addWidget(message)
        #Faire un fonction open qui va aller lire une tache dans le json et l'activer ici



        







            


