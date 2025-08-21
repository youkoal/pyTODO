import sys, os

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit,QPushButton

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from Models.taskbox import taskbox
from Models.one_task import one_task


class FenetreNewTask(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """
    # Création d'une variable globale
    void_task = one_task("test","test") 
    void_taskbox = taskbox()
    void_taskbox.add_new_task(void_task)
    void_secondtask = one_task("test","test")
    void_taskbox.add_new_task(void_secondtask)
    void_taskbox.check_task(void_secondtask)
    
    void_taskbox.set_title("Nouvelle Tache")

    def __init__(self):
        super().__init__()
        
        #Parametre globaux de la fenetre
        self.setWindowTitle("Nouvelle Tache")
        self.resize(300,300)

        # Layouts
        layoutNT = QVBoxLayout()
        self.setLayout(layoutNT)
        
        
        #Afichage de la tache
        text = []
        for line in self.void_taskbox.get_console():
            text = line
            message = QLabel(text)
            layoutNT.addWidget(message)
        self.Bloc_Titre = QGroupBox()
        self.Bloc_Titre.setObjectName("Bloc Titre")
        ###Titre au dessus
        self.Layout_Titre = QHBoxLayout()
        self.TaskName = QLabel("Nom de la tache :")
        self.TaskName.setObjectName("Nom tache")
        self.Layout_Titre.addWidget(self.TaskName)
        ### Zone de text et bouton en dessous
        self.layout_text = QHBoxLayout()
        
        ### Partie a propos du bouton et de ses effets
        self.Task_N = QTextEdit()

        self.Task_N.setObjectName("Champ texte Titre")
        self.Accepter_Titre = QPushButton("Accepter")
        self.Accepter_Titre.setDefault(True)
        
        

        ### On associe les deux widget de la zone texte ensemble
        self.layout_text.addWidget(self.Task_N)
        self.layout_text.addWidget(self.Accepter_Titre)
        ### On réunis tout ensemble
        self.main_layout_Titre = QVBoxLayout(self.Bloc_Titre)
        self.main_layout_Titre.addLayout(self.Layout_Titre)
        self.main_layout_Titre.addLayout(self.layout_text)
        self.main_layout_Titre.addStretch()

        # Partie text edit
        ## Bloc Nom de la tache
        self.Bloc_Desc = QGroupBox()
        self.Bloc_Desc.setObjectName("Bloc Desc")
        ###Titre au dessus
        self.Layout_Desc = QHBoxLayout()
        self.TaskDesc = QLabel("Desc de la tache :")
        self.TaskDesc.setObjectName("Nom Desc")
        self.Layout_Desc.addWidget(self.TaskDesc)
        ### Zone de text et bouton en dessous
        self.layout_text = QHBoxLayout()
        self.Task_D = QTextEdit()
        self.Task_D.setObjectName("Champ texte Desc")
        self.Accepter_Desc = QPushButton("Accepter")
        self.Accepter_Desc.setDefault(True)
        ### On associe les deux widget de la zone texte ensemble
        self.layout_text.addWidget(self.Task_D)
        self.layout_text.addWidget(self.Accepter_Desc)
        ### On réunis tout ensemble
        self.main_layout_Desc = QVBoxLayout(self.Bloc_Desc)
        self.main_layout_Desc.addLayout(self.Layout_Desc)
        self.main_layout_Desc.addLayout(self.layout_text)
        self.main_layout_Desc.addStretch()

        layoutNT.addWidget(self.Bloc_Titre)
        layoutNT.addWidget(self.Bloc_Desc)


        ### Boutons
        self.Accepter_Titre.clicked.connect(self.Sauvegarder_Nom)

    def Sauvegarder_Nom(self):
        self.void_task.task_name = self.Task_N.toPlainText()
        self.void_task.print_console
    
    
    


        

        




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
        self.ActNouveau.triggered.connect(self.BoutonNouvelleTache)
        

        self.ActOuvrir = QAction("Ouvrir une liste")
        self.ActOuvrir.setShortcut("Ctrl+O")
        self.ActOuvrir.triggered.connect(self.BoutonOuvrir)

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

    def BoutonNouvelleTache(self):

        #La nouvelle tache qui sera créée
        NewTask = taskbox()

        # Affichage de la box
        self.window1 = FenetreNewTask()
        self.window1.show()

        self.SauvegarderNewTaskBox()


    def BoutonOuvrir(self):
        print("Ouverture d'une taskbox existante")
        BoiteTache = taskbox()
        BoiteTache.load_json()
        text = []
        for line in BoiteTache.get_console():
            text = line
            message = QLabel(text)
            self.Layout_relais.addWidget(message)
        #Faire un fonction open qui va aller lire une tache dans le json et l'activer ici

    def SauvegarderNewTaskBox(self):
        pass


        







            


