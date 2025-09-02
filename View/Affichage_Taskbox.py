import sys, os

from PySide6.QtWidgets import QDialog, QGroupBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtWidgets import QPushButton, QCheckBox,QScrollArea, QLineEdit
from PySide6.QtCore import Qt

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from Models.taskbox import taskbox
from Models.one_task import one_task






class Affichage_Taskbox(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """
    

    def __init__(self, a_taskboxes):
        super().__init__()

        self.a_taskboxes = a_taskboxes
        
        #Parametre globaux de la fenetre
        self.setWindowTitle("Nouvelle Tache")
        self.resize(600,900)
        self.void_taskbox = taskbox()
        
        
        self.void_taskbox.set_title("")
        self.Modif = False



        # Fonctions affichage et connexions des boutons

        ## On affiche dans la fenetre , appelle aussi affichage du bloc d'edition
        self.Affichage()

        ### Boutons accepter
        

        ### Bouton pour changer entre tache a faire et tache faite
        

        ### Bouton pour supprimer une tache
        

        ### Bouton pour sauvegarder la taskbox
        



    def Affichage(self):
                # et on supprime l'ancienne pour éviter les doublons
        old_layout = self.layout()
        if old_layout is not None: 
            QWidget().setLayout(old_layout)


                ###Bloc Titre (nom de la taskbox)
        self.Titre_box = QGroupBox()

        ## Layout du titre_box
        self.Titre = QVBoxLayout(self.Titre_box)
        self.BoxName = QLabel('Nom de la liste de tâches :')
        self.NomTaskbox = QLineEdit(self.void_taskbox.get_title())
        self.Titre.addWidget(self.BoxName)
        self.Titre.addWidget(self.NomTaskbox)

        ###Bloc edition de tache (Nom et description des tâches)
        self.Bloc_edit = QGroupBox()
        self.Bloc_edit.setMinimumSize(50,15)

        ## Layout du bloc edition (nom et description de la tache)

        ### Partie edition texte
        self.Nom_Et_Desc = QVBoxLayout()
        self.TaskName = QLabel("Nom de la tache :")
        self.Task_N = QLineEdit()
        self.TaskDesc = QLabel("Desc de la tache :")
        self.Task_D = QLineEdit()
        self.Nom_Et_Desc.addWidget(self.TaskName)
        self.Nom_Et_Desc.addWidget(self.Task_N)
        self.Nom_Et_Desc.addWidget(self.TaskDesc)
        self.Nom_Et_Desc.addWidget(self.Task_D)

        ### Partie bouton
        ### Bouton nouvelle tâche
        self.Bouton = QVBoxLayout()
        self.Accepter = QPushButton("Nouvelle tâche")
        self.Accepter.setDefault(True)
        self.Bouton.addWidget(self.Accepter)
        self.Accepter.clicked.connect(self.Sauvegarder_tache)

        ### Bouton tache changer de repertoire (tache a faire <=> tache effectuées)
        self.Change = QPushButton("Check/uncheck")
        self.Change.setDefault(True)
        self.Bouton.addWidget(self.Change)
        self.Change.clicked.connect(self.Check_uncheck)


        ### Bouton tache supprimer
        self.Suppress = QPushButton("Supprimer tâche(s)")
        self.Suppress.setDefault(True)
        self.Bouton.addWidget(self.Suppress)
        self.Suppress.clicked.connect(self.Supprimer_tache)

        ###Bouton pour sauvegarder la taskbox
        self.Save = QPushButton("Sauvegarder la liste")
        self.Save.setDefault(True)
        self.Bouton.addWidget(self.Save)
        self.Save.clicked.connect(self.SauvegarderTaskbox)
        

        ### On réunis tout
        self.layout_tot = QHBoxLayout(self.Bloc_edit)
        self.layout_tot.addLayout(self.Nom_Et_Desc)
        self.layout_tot.addLayout(self.Bouton)

        
        # Creation des deux dataset
        dataTD = self.void_taskbox.get_tasks_todo()
        dataD = self.void_taskbox.get_tasks_done()

        #Longueur pour savoir si l'un est vide
        Ntask_todo = len(dataTD)
        Ntask_done = len(dataD)

        #Création des box de scroll
        self.Box_to_do = QScrollArea()
        self.Box_to_do.setMinimumSize(50,50)
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
        self.Box_check.setMinimumSize(50,50)
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

                # On regroupe tout les widget affichés dans la fenetre
        self._layoutNT = QVBoxLayout()
        self._layoutNT.addWidget(self.Titre_box)
        self._layoutNT.addWidget(self.Box_to_do)
        self._layoutNT.addWidget(self.Box_check)
        self._layoutNT.addWidget(self.Bloc_edit)
        self.layoutNT = self._layoutNT
        self.setLayout(self.layoutNT)
        

    ### Fonction des boutons
    def Sauvegarder_tache(self):
        ##Sauvegarde de la tache dans le json et rafraichit l'affichage
        if self.Task_N.text() == "":
            self.FenetreErreur("Veuillez nommer la tâche.")
        elif self.Task_D.text() == "":
            self.FenetreErreur("Veuillez décrire la tâche.")
        else:
             ##Sauvegarde de la tache dans le json et rafraichit l'affichage
            A = one_task(self.Task_N.text(),self.Task_D.text())
            self.void_taskbox.add_new_task(A)
            self.void_taskbox.save_json() 
            self.Task_N.clear()
            self.Task_D.clear()
            #Rafraichir l'affichage 
            self.Affichage()

    
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
        self.Affichage()  
    
    
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
        self.Affichage()
        
    ### Sauvegarder le travail une fois terminé    
    def SauvegarderTaskbox(self):
        #Nommer la taskbox et sauvegarder
        if self.NomTaskbox.text() != "":
            
            self.void_taskbox.set_title(self.NomTaskbox.text())

            self.a_taskboxes.add_taskbox(self.void_taskbox)
            self.a_taskboxes.save_json()
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
