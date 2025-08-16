import sys,os
from PySide6 import QtCore, QtWidgets, QtGui

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

class UI_Taskform(QtWidgets.QWidget) :
    

    #Signal pour indiquer si le bouton de tache à été cliqué
    #Un parametre entier est utilisé
    closeClicked = QtCore.Signal(int)


    #Style CSS pour les taches vérifié et non vérifié
    #Ces styles sont basé sur la complétion ou non des taches

    checked_style = "text-decoration: line-through;"
    unchecked_style = "text-decoration: none;"




    def __init__(self, text, state, position, *args, **kwargs) :
        super().__init__()

        #Position de la tache dans la liste, pour l'identification de celle-ci, spécialement la suppression

        self.position = position
        self.parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.icon_path = os.path.abspath(os.path.join(self.parent_dir,"icons"))
        self.static_path = self.parent_dir
        # Initialise les composants UI

        self.init_ui()

        #Fixe le parametre initial des taches
        self.task_check_box.setText(text)
        self.task_check_box.setChecked(state)

        #applique la style approprié en fonction de l'etat
        if state:
            self.task_check_box.setStyleSheet(self.checked_style)

        ## Connecte le signal à son emplacement correspondant
        # QUand la tâche change, màj de son style 
        self.task_check_box.stateChanged.connect(self.Update_style)
        self.remove_btn.clicked.connect(self.emitCloseSignal)



    def init_ui(self):
        # Parametre la geometrie de la tache
        self.setGeometry(0,0, 1000, 100) # x, y , largeur, hauteur

        # Chargement et application du CSS à partir d'un fichier
        with open(os.path.join(self.static_path, "style.qss"), "r") as style_file:
            style_str = style_file.read()
            # print(style_str)

        bg_path =  os.path.join(self.static_path, "background.jpg")
        bg_path = bg_path.replace("\\", "/")
        print(f"Background image path: {bg_path}")
        style_str = style_str.replace("background.jpg", bg_path)
        self.setStyleSheet(style_str)


        #Creer un rendu de grille
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setSpacing(0)

        #Creation de la tache principal et son rendu
        self.task_widget =QtWidgets.QWidget(parent=self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.task_widget)

        #Ajout d'une case pour vérifier la complétion d'une tache
        self.task_check_box = QtWidgets.QCheckBox(self.task_widget)
        self.horizontalLayout.addWidget(self.task_check_box)

        #Ajout Bouton pour retirer la tache
        self.remove_btn = QtWidgets.QPushButton(self.task_widget)
        self.remove_btn.setIcon(QtGui.QIcon(os.path.join(self.icon_path, "bouton.svg")))
        self.remove_btn.setIconSize(QtCore.QSize(20,20))
        self.horizontalLayout.addWidget(self.remove_btn)

        #Ajout du widge de la tache sur un rendu de grille
        self.gridLayout.addWidget(self.task_widget, 0, 0, 1, 1)

    #MàJ du visu de la tache fonction de sa co^mplétion
    def Update_style(self, state) :

        self.task_check_box.setStyleSheet(self.checked_style if state else self.unchecked_style)

    #Emet un signal si la tache doit etre fermée
    #Passes sa position en tant qu'argument
    def emitCloseSignal(self):
        self.closeClicked.emit(self.position)
        
    #Récupération de l'etat actuel et du texte de la tâche

    def Get_CheckBox_State(self):
        return self.task_check_box.isChecked()
    
    def Get_CheckBox_Text(self):
        return self.task_check_box.text()
    
