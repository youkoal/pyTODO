import sys, os, json

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QDialog, QMainWindow, QGroupBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit,QPushButton, QCheckBox,QScrollArea, QLineEdit
from PySide6.QtCore import Qt

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from Models.taskbox import taskbox
from Models.one_task import one_task
from Models.taskboxes import taskboxes


## Chargement de la base de donnée
a_taskboxes = taskboxes()
a_taskboxes.load_json()

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
        self.resize(600,900)
        self.void_taskbox = taskbox()
        
        
        self.void_taskbox.set_title("Nouvelle Tache")
        self.Modif = False

        self.Titre_box = QGroupBox()
        self.Titre = QVBoxLayout(self.Titre_box)
        self.BoxName = QLabel('Nom de la liste de tâches :')
        self.NomTaskbox = QLineEdit()
        self.Titre.addWidget(self.BoxName)
        self.Titre.addWidget(self.NomTaskbox)

        ###Bloc edition de tache
        self.Bloc_edit = QGroupBox()
        self.Bloc_edit.setFixedSize(600,220)
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

        ### Bouton tache changer de repertoire (tache a faire <=> tache effectuées)
        self.Change = QPushButton("Check/uncheck")
        self.Change.setDefault(True)
        self.Bouton.addWidget(self.Change)


        ### Bouton tache supprimer
        self.Sup = QPushButton("Supprimer tâche(s)")
        self.Sup.setDefault(True)
        self.Bouton.addWidget(self.Sup)

        ###Bouton pour sauvegarder la taskbox
        self.Save = QPushButton("Sauvegarder la liste")
        self.Save.setDefault(True)
        self.Bouton.addWidget(self.Save)
        

        ### On réunis tout
        self.layout_tot = QHBoxLayout(self.Bloc_edit)
        self.layout_tot.addLayout(self.edition)
        self.layout_tot.addLayout(self.Bouton)

        ## On affiche dans la fenetre , appelle aussi affichage du bloc d'edition
        self.Afficher_tache()

        ### Boutons accepter
        self.Accepter.clicked.connect(self.Sauvegarder_tache)

        ### Bouton pour changer entre tache a faire et tache faite
        self.Change.clicked.connect(self.Check_uncheck)

        ### Bouton pour supprimer une tache
        self.Sup.clicked.connect(self.Supprimer_tache)

        ### Bouton pour sauvegarder la taskbox
        self.Save.clicked.connect(self.SauvegarderTaskbox)


        

        ### Afficher 
    def Affichage_fenetre(self):
        # On regroupe tout les widget affichés dans la fenetre
        self._layoutNT = QVBoxLayout()
        self._layoutNT.addWidget(self.Titre_box)
        self._layoutNT.addWidget(self.Box_to_do)
        self._layoutNT.addWidget(self.Box_check)
        self._layoutNT.addWidget(self.Bloc_edit)
        self.layoutNT = self._layoutNT
        self.setLayout(self.layoutNT)
        self._layoutNT.deleteLater()


    def Afficher_tache(self):

        
        # Creation des deux dataset
        dataTD = self.void_taskbox.get_tasks_todo()
        dataD = self.void_taskbox.get_tasks_done()

        #Longueur pour savoir si l'un est vide
        Ntask_todo = len(dataTD)
        Ntask_done = len(dataD)

        #Création des box de scroll
        self.Box_to_do = QScrollArea()
        self.Box_to_do.setFixedSize(500,320)
        self.widget_TODO = QWidget()
        self.List_to_do = QVBoxLayout()
        # Boucle de lecture du fichier json et création des checkboxs TODO
        self.Checked_todo = []
        if Ntask_todo !=0:

            for tache in dataTD:

                self.task = QCheckBox(tache.task_name)
                self.desc = QLabel(tache.task_description)
                self.Checked_todo.append(self.task)
                

                self.List_to_do.addWidget(self.task)
                self.List_to_do.addWidget(self.desc)
        else:
            self.List_to_do.addWidget(QLabel("Aucune tâche en cours"))

        self.widget_TODO.setLayout(self.List_to_do)

        # Idem pour DONE
        self.Box_check = QScrollArea()
        self.Box_check.setFixedSize(500,320)
        self.widget_check = QWidget()
        self.List_check = QVBoxLayout()

        #Idem pour DONE

        self.Checked_done = []
        if Ntask_done !=0:
            for i in dataD:

                self.task = QCheckBox(i.task_name)
                self.desc = QLabel(i.task_description)
                self.Checked_done.append(self.task)

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

        #Une fois le fichier lu , on déclenche la création de la fenetre
        # et on supprime l'ancienne pour éviter les doublons
        self.Affichage_fenetre()

    ### Fonction des boutons
    def Sauvegarder_tache(self):
        ##Sauvegarde de la tache dans le json et rafraichit l'affichage
        if self.Task_N.toPlainText() == "":
            self.FenetreErreur("Veuillez nommer la tâche.")
        elif self.Task_D.toPlainText() == "":
            self.FenetreErreur("Veuillez décrire la tâche.")
        else:
             ##Sauvegarde de la tache dans le json et rafraichit l'affichage
            A = one_task(self.Task_N.toPlainText(),self.Task_D.toPlainText())
            self.void_taskbox.add_new_task(A)
            self.void_taskbox.save_json() 
            self.Task_N.clear()
            self.Task_D.clear()
            #Rafraichir l'affichage 
            self.Afficher_tache()

    
    def Check_uncheck(self):
        #Fonction pour le bouton check/uncheck
        toute_tache = self.Checked_todo + self.Checked_done
        toute_tache_objet = self.void_taskbox.get_all_tasks_flat()
        transition = []

        for tache in toute_tache:

            position = toute_tache.index(tache)

            if tache.isChecked():
                transition.append(toute_tache_objet[position])

        for tache in transition:
            self.void_taskbox.Zcheck_task(tache)

        self.void_taskbox.save_json()
        self.Afficher_tache()  
    
    
    def Supprimer_tache(self):
        #Fonction pour le bouton supprimer tache
        toute_tache = self.Checked_todo + self.Checked_done
        toute_tache_objet = self.void_taskbox.get_all_tasks_flat()
        trashbin =[]
        for tache in toute_tache:
            

            position = toute_tache.index(tache)

            if tache.isChecked():
                trashbin.append(toute_tache_objet[position])
            
        for tache in trashbin:
            self.void_taskbox.erase_task(tache)

        self.void_taskbox.save_json()
        self.Afficher_tache()
        
    ### Sauvegarder le travail une fois terminé    
    def SauvegarderTaskbox(self):
        #Nommer la taskbox et sauvegarder
        if self.NomTaskbox.text() != "":
            
            self.void_taskbox.set_title(self.NomTaskbox.text())

            a_taskboxes.add_taskbox(self.void_taskbox)
            a_taskboxes.save_json()
            self.Task_N.clear()
            self.Task_D.clear()
            self.NomTaskbox.clear()
            self.close()
        else:
            self.FenetreErreur("Veuillez nommer la liste de tâches avant de sauvegarder.")


    def FenetreErreur(self, message):
        

        dlg = QDialog(self)
        dlg.setWindowTitle("Erreur")
        dlg.resize(200,100)
        dlg_layout = QVBoxLayout()
        dlg_label = QLabel(message)
        dlg_button = QPushButton("OK")
        dlg_button.clicked.connect(dlg.accept)
        dlg_layout.addWidget(dlg_button)
        dlg_layout.addWidget(dlg_label)
        dlg.setLayout(dlg_layout)
        dlg.exec()

        
        

    


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

        #Creation des actions du menu
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
        #Creation du menu
        BarreMenu = self.menuBar()

        Fichier = BarreMenu.addMenu("&Fichier")
        Fichier.addAction(self.ActNouveau)
        Fichier.addSeparator()
        Fichier.addAction(self.ActOuvrir)
        Fichier.addSeparator()
        Fichier.addAction(self.ActFuite)

    def BoutonNouvelleTache(self):


        # Affichage de la box
        self.window1 = FenetreNewTask()
        self.window1.show()



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
    
    