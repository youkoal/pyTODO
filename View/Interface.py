import sys, os, json

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QGroupBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit,QPushButton, QCheckBox,QScrollArea
from PySide6.QtCore import Qt

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
        self.resize(500,800)
        
        self.void_taskbox = taskbox()
        
        self.void_taskbox.set_title("Nouvelle Tache")

        self.void_taskbox.save_json()


        self.Modif = False
        

        ###Bloc edition de tache
        self.Bloc_edit = QGroupBox()
        self.Bloc_edit.setFixedSize(500,120)
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
        ### Bouton nouvelle tâche
        self.Bouton = QVBoxLayout()
        self.Accepter = QPushButton("Nouvelle tâche")
        self.Accepter.setDefault(True)
        self.Bouton.addWidget(self.Accepter)

        ### Bouton tache check
        self.Acheve = QPushButton("Tâche achevés")
        self.Acheve.setDefault(True)
        self.Bouton.addWidget(self.Acheve)
        

        ### On réunis tout
        self.layout_tot = QHBoxLayout(self.Bloc_edit)
        self.layout_tot.addLayout(self.edition)
        self.layout_tot.addLayout(self.Bouton)

        ## On affiche dans la fenetre , appelle aussi affichage du bloc d'edition
        self.Afficher_tache()

        ### Boutons accepter
        self.Accepter.clicked.connect(self.Sauvegarder_tache)

        ### Bouton tache achevée
        self.Acheve.clicked.connect(self.Achever_tache)
        

        ### Afficher 
    def Affichage_fenetre(self):
        self._layoutNT = QVBoxLayout()
        self._layoutNT.addWidget(self.Box_to_do)
        self._layoutNT.addWidget(self.Box_check)
        self._layoutNT.addWidget(self.Bloc_edit)
        self.layoutNT = self._layoutNT
        self.setLayout(self.layoutNT)
        self._layoutNT.deleteLater()

    # def clearTache(self):
        ## Efface les layout contenu dans layout_tache, pour refraichir l'affichage
        # Tache = []
        # for i in range(self.layout_tache.count()):
            # T = self.layout_tache.itemAt(i).widget()
            # if T:
                # Tache.append(T)
        # for T in Tache:
            # T.deleteLater()
        
    def Afficher_tache(self):
        ## Fonction affichage de la tache, appelé au début et a chaque màj
        #### Chargement des taches dans la taskbox


        f = open('Data/tasks.json')
        data = json.load(f)
        Ntask_todo = len(data['tasks_todo'])
        Ntask_done = len(data['tasks_done'])


        self.Box_to_do = QScrollArea()
        self.Box_to_do.setFixedSize(500,300)
        self.widget_TODO = QWidget()
        self.List_to_do = QVBoxLayout()

        self.Checked_todo = []
        if Ntask_todo !=0:

            for i in data['tasks_todo']:

                self.task = QCheckBox(str(str(i).split(",")[0]).split(":")[1])
                #self.task.stateChanged.connect(self.Todo2done)
                self.desc = QLabel(str(str(i).split(",")[1]).split(":")[1])
                self.Checked_todo.append(self.task)

                self.List_to_do.addWidget(self.task)
                self.List_to_do.addWidget(self.desc)
        else:
            self.List_to_do.addWidget(QLabel("Aucune tâche en cours"))

        self.widget_TODO.setLayout(self.List_to_do)

        self.Box_check = QScrollArea()
        self.Box_check.setFixedSize(500,300)
        self.widget_check = QWidget()
        self.List_check = QVBoxLayout()
        if Ntask_done !=0:
            for i in data['tasks_done']:

                self.task = QCheckBox(str(str(i).split(",")[0]).split(":")[1])
                self.desc = QLabel(str(str(i).split(",")[1]).split(":")[1])

                self.List_check.addWidget(self.task)
                self.List_check.addWidget(self.desc)
        else:
            self.List_check.addWidget(QLabel("Aucune tâche en cours"))

        self.widget_check.setLayout(self.List_check)


        

        #Parametre scroll area
        self.Box_to_do.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Box_to_do.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Box_to_do.setWidgetResizable(True)
        self.Box_to_do.setWidget(self.widget_TODO)

        self.Box_check.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Box_check.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Box_check.setWidgetResizable(True)
        self.Box_check.setWidget(self.widget_check)

        f.close()
        self.Affichage_fenetre()


    def Sauvegarder_tache(self):
        ##Sauvegarde de la tache dans le json et rafraichit l'affichage
        A = one_task(self.Task_N.toPlainText(),self.Task_D.toPlainText())
        self.void_taskbox.add_new_task(A)
        self.void_taskbox.save_json() 
        #Rafraichir l'affichage 
        #self.clearTache()
        self.Afficher_tache()
    
    def Achever_tache(self):
        pass

        
        

    


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
    
    