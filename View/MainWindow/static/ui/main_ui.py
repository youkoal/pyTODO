import sys
import os
import json
from PySide6 import QtCore, QtGui, QtWidgets

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

class Ui_MainWindow(object):

    def setupUI(self, MainWindow):
        self.parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.icon_path = os.path.abspath(os.path.join(self.parent_dir,"icons"))
        self.static_path = self.parent_dir

        #Charge et applique les style CSS a la fenetre principale
        with open(os.path.abspath(os.path.join(self.static_path, "style.qss")), "r") as style_file:
            style_str = style_file.read()
            MainWindow.setStyleSheet(style_str)




        # Parametrage de la taille initiale de la fenetre principale et des propriétés élémentaires
        MainWindow.resize(1000,700)
        MainWindow.setObjectName("Fenetre principale")
        MainWindow.setWindowTitle("To Do List")

        #Parametrage des icones de la fenetre principale
        window_icon = QtGui.QIcon(os.path.join(self.icon_path, "list.svg"))
        MainWindow.setWindowIcon(window_icon)

        # Creer et parametre le widget central de la fenetre
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        # Creer le rendu principal pour le Widget Central

        self.main_verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.main_verticalLayout.setContentsMargins(80,50,80,50)
        self.main_verticalLayout.setSpacing(20)

        #Creer un espace pour le titre
        self.title_frame = QtWidgets.QFrame(parent= self.centralWidget)
        self.title_frame.setMaximumSize(QtCore.QSize(16777215,60))
        self.title_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_frame.setObjectName("title_frame")

        #Rendu pour la section titre, incluant une icone et une étiquette.

        self.title_horizontalLayout = QtWidgets.QHBoxLayout(self.title_frame)
        self.title_horizontalLayout.setContentsMargins(10, 10, 10, 10)

        #etiquette icone dans la section titre
        self.icon_label = QtWidgets.QLabel(parent=self.title_frame)
        self.icon_label.setMinimumSize(QtCore.QSize(40,40))
        self.icon_label.setMaximumSize(QtCore.QSize(40,40))
        self.icon_label.setPixmap(QtGui.QPixmap(os.path.join(self.icon_path, "list.svg")))
        self.icon_label.setScaledContents(True)
        self.icon_label.setObjectName("icone_label")

        #Ajouter l'icone au rendu du titre
        self.title_horizontalLayout.addWidget(self.icon_label)

        #Affichage de l'etiquette du titre de l'application
        self.title_label = QtWidgets.QLabel(parent=self.title_frame)
        self.title_label.setText("To do list")
        self.title_label.setMinimumSize(QtCore.QSize(150,40))
        self.title_label.setObjectName("title_label")

        #Ajouter l'etiquette du titre au rendu du titre
        self.title_horizontalLayout.addWidget(self.title_label)

        #Creer un espace pour la liste des taches
        self.task_frame = QtWidgets.QFrame(parent= self.centralWidget)
        self.task_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.task_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.task_frame.setObjectName("Task_frame")

        #Rendu pour les taches dans l'espace des taches
        self.task_verticalLayout = QtWidgets.QVBoxLayout(self.task_frame)
        self.task_verticalLayout.setContentsMargins(10 , 15, 15, 10)

        #Vues des listes pour afficher les taches
        self.task_listView = QtWidgets.QListView(parent=self.task_frame)
        self.task_listView.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.task_listView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.task_listView.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragOnly)
        self.task_listView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.task_listView.setMovement(QtWidgets.QListView.Movement.Free)
        self.task_listView.setObjectName("Task_listView")

        #Ajouter la liste des taches au rendu des taches
        self.task_verticalLayout.addWidget(self.task_listView)

        #Creer un espace pour ajouter des nouvelles taches
        self.add_task_frame = QtWidgets.QFrame(parent = self.centralWidget)
        self.add_task_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.add_task_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.add_task_frame.setObjectName("Ajout_espace_tache")

        #Rendu pour un bouton "ajout de tache" , ainsi qu'un ajout de texte
        self.add_horizontalLayout = QtWidgets.QHBoxLayout(self.add_task_frame)
        self.add_horizontalLayout.setContentsMargins(30,0,0,0)
        self.add_horizontalLayout.setSpacing(0)

        #Ajout de texte d'une nouvelle tache
        self.new_task = QtWidgets.QLineEdit(parent=self.add_task_frame)
        self.new_task.setObjectName("nouvelle_tache")

        #Ajout le texte au rendu "ajout nouvelle tache"
        self.add_horizontalLayout.addWidget(self.new_task)

        #Bouton ajout nouvelle tache
        self.add_btn = QtWidgets.QPushButton(parent= self.add_task_frame)
        self.add_btn.setText("Ajouter")
        font = QtGui.QFont()
        font.setBold(True)
        self.add_btn.setFont(font)
        self.add_btn.setIcon(QtGui.QIcon(os.path.join(self.icon_path, "add.svg")))
        self.add_btn.setIconSize(QtCore.QSize(30,30))
        self.add_btn.setObjectName("Bouton_Ajout")

        #ajouter le bouton au rendu ajout ajout tache
        self.add_horizontalLayout.addWidget(self.add_btn)

        #ajout du titre, liste des taches, et ajout d'une tache
        self.main_verticalLayout.addWidget(self.title_frame)
        self.main_verticalLayout.addWidget(self.task_frame)
        self.main_verticalLayout.addWidget(self.add_task_frame)


