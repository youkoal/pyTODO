import sys, os

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit,QPushButton, QGridLayout

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from Models.taskbox import taskbox
from Models.one_task_copy import one_task


class FenetreNewTask(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """
    # Création d'une variable globale
    
    # On sauvegarde la nouvelle tache, si celle-ci est vide on l'effacera
    

    def __init__(self):
        super().__init__()
        
        #Parametre globaux de la fenetre
        self.setWindowTitle("Nouvelle Tache")
        self.resize(1000,1000)
        
        self.void_taskbox = taskbox()
        
        self.void_taskbox.set_title("Nouvelle Tache")
        self.void_taskbox.save_json()

        # Layouts
        
        
        #Afichage de la tache

        ###Bloc edition de tache
        self.Bloc_edit = QGroupBox()
        self.Bloc_edit.setFixedSize(200,200)
        ### Partie Titre et edition
        self.edition = QVBoxLayout()
        self.TaskName = QLabel("Nom de la tache :")
        self.Task_N = QTextEdit()
        self.TaskDesc = QLabel("Desc de la tache :")
        self.Task_D = QTextEdit()
        self.edition.addWidget(self.TaskName)
        self.edition.addWidget(self.Task_N)
        self.edition.addWidget(self.TaskDesc)
        self.edition.addWidget(self.Task_D)

        ### Partie bouton
        self.Bouton = QVBoxLayout()
        self.Accepter = QPushButton("Accepter")
        self.Accepter.setDefault(True)
        self.Bouton.addWidget(self.Accepter)

        ### On réunis tout
        self.layout_tot = QHBoxLayout(self.Bloc_edit)
        self.layout_tot.addLayout(self.edition)
        self.layout_tot.addLayout(self.Bouton)

        ## On affiche dans la fenetre 
        self.Afficher_tache()
        


        ### Boutons
        self.Accepter.clicked.connect(self.Sauvegarder_tache)
        

        ### Afficher 
    def Affichage_fenetre(self):
        _layoutNT = QVBoxLayout()
        _layoutNT.addWidget(self._layout_tache)
        _layoutNT.addWidget(self.Bloc_edit)
        self.layoutNT = _layoutNT
        self.setLayout(self.layoutNT)

    def Afficher_tache(self):
        self._layout_tache = QGroupBox()
        self._layout_tache.setFixedSize(500,500)
        self.layout_tache = QVBoxLayout()
        self.void_taskbox.load_json()
        text = []
        for line in self.void_taskbox.get_console():
            text = line
            message = QLabel(text)
            self.layout_tache.addWidget(message)
        self._layout_tache.setLayout(self.layout_tache)
        self.Affichage_fenetre()
      


    def Sauvegarder_tache(self):
        A = one_task(self.Task_N.toPlainText(),self.Task_D.toPlainText())
        self.void_taskbox.add_new_task(A)
        self.void_taskbox.save_json() 
        #Rafraichir l'affichage 

        
        self.Afficher_tache()
        
        

    
    
    
    


        

        




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


        







            


