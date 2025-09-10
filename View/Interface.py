import sys, os, json

from PySide6.QtGui import  QAction, QPainter, QPixmap
from PySide6.QtWidgets import  QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtWidgets import QPushButton, QCheckBox,QScrollArea,  QGridLayout


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


from Models.taskboxes import taskboxes
from View.Affichage_Taskbox import Affichage_Taskbox



class MaFenetre(QMainWindow):



    def __init__(self):
            ## Chargement des taskboxes
        self.a_taskboxes = taskboxes()
        self.a_taskboxes.load_json()

        super().__init__()
        qss_path = os.path.join(os.path.dirname(__file__), "MainWindow", "static", "style.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r") as f:
                self.setStyleSheet(f.read())
        else:
            print("QSS file not found:", qss_path)
        

        #Parametre de la fenetre
        self.setWindowTitle('ToDoListe')
        self.resize(1200,800)
        

        ### Afficher un background
        qss_path = os.path.join(parent_dir, "View/MainWindow/static/style.qss")
        with open(qss_path, "r") as f:
            self.setStyleSheet(f.read())
        

        ## Appelle des fonctions initiales
        self.CreerAction()

        self.CreerMenu()
        self.AfficherFenetre()


    def AfficherFenetre(self):
        # Creation du layout central

        self.Layout_central = QWidget()
        self.setCentralWidget(self.Layout_central)


        #Creer le widget qui sera utilisé dans le layout central
        self.Layout_relais = QVBoxLayout()
        self.Layout_central.setLayout(self.Layout_relais)
        
        

    def CreerAction(self):

        #Creation des actions du menu
        ## Creation d'une nouvelle fenetre pour creer une nouvelle taskbox
        self.ActNouveau = QAction("Nouvelle liste")
        self.ActNouveau.setShortcut('ctrl+N')
        self.ActNouveau.triggered.connect(self.BoutonNouvelleTache)
        
        ## Affichage d'une taskbox existante dans la fenetre principale
        self.ActOuvrir = QAction("Ouvrir une liste")
        self.ActOuvrir.setShortcut("Ctrl+O")
        self.ActOuvrir.triggered.connect(self.BoutonOuvrir)

        ## Quitter l'application
        self.ActFuite = QAction("Quitter")
        self.ActFuite.setShortcut("Alt+F4")
        self.ActFuite.triggered.connect(self.close)

            
    def CreerMenu(self):
        #Creation du menu
        BarreMenu = self.menuBar()

        #Partie fichier (nouvelle, ouvrir, quitter)
        Fichier = BarreMenu.addMenu("&Fichier")
        Fichier.addAction(self.ActNouveau)
        Fichier.addSeparator()
        Fichier.addAction(self.ActOuvrir)
        Fichier.addSeparator()
        Fichier.addAction(self.ActFuite)

    def BoutonNouvelleTache(self):


        # Affichage de la box
        self.window1 = Affichage_Taskbox(self.a_taskboxes)
        self.window1.show()



    def BoutonOuvrir(self):
        # Selection de la taskbox a ouvrir dans une liste
        ## Chargement de la liste des taskbox
        Liste_Box = self.a_taskboxes.get_taskboxes()
        


        #Creation du menu de selection
        MenuSelect = QHBoxLayout()
        
        Choixselect = QScrollArea()
        Choixselect.setFixedSize(200,200)
        Selectwidget = QWidget()
        Layoutselect = QVBoxLayout()
        self.Checked_taskbox = []
        ##Taskbox disponible
        for i in Liste_Box:
            Choix = QCheckBox(i.get_title())
            self.Checked_taskbox.append(Choix)
        
            Layoutselect.addWidget(Choix)
        

        Selectwidget.setLayout(Layoutselect)
        Choixselect.setWidget(Selectwidget)
        #Bouton de selection
        Bouton = QVBoxLayout()
        Boutonselection = QPushButton("OK")
        Boutonselection.setFixedSize(100,30)
        Boutonselection.setDefault(True)
        BoutonAnnuler = QPushButton("Annuler")
        BoutonAnnuler.setFixedSize(100,30)
        BoutonAnnuler.setDefault(True)
        Bouton.addWidget(Boutonselection)
        Bouton.addWidget(BoutonAnnuler)


        #On regroupe tout
        MenuSelect.addLayout(Layoutselect)
        MenuSelect.addWidget(Choixselect)
        MenuSelect.addLayout(Bouton)

        #On affiche le menu
        
        self.Layout_relais.deleteLater()

        self.AfficherFenetre()
        self.Layout_relais.addLayout(MenuSelect)  
        


        

            
        #Fonction des boutons
        Boutonselection.clicked.connect(lambda: self.OuvrirTaskbox(Liste_Box, Layoutselect, MenuSelect))
        BoutonAnnuler.clicked.connect(lambda: self.AnnulerSelection(Layoutselect, MenuSelect))

    def OuvrirTaskbox(self, Liste_Box, Layoutselect, MenuSelect):
        self.Layout_relais.deleteLater()

        Layout_taskbox = QGridLayout()
        Layout_taskbox.setSizeConstraint
        
        

        Taskbox_selectionnee = []
        for box in self.Checked_taskbox:
            position = self.Checked_taskbox.index(box)
            if box.isChecked():
                Taskbox_selectionnee.append(Liste_Box[position])
                



        #On affiche la taskbox selectionnée
        i=0
        j=0
        z=0


        for box in Taskbox_selectionnee:
            
            widget = Affichage_Taskbox(self.a_taskboxes)
            
            widget.void_taskbox = box
            widget.NomTaskbox.setText(box.get_title())
            widget.Modif = False
            widget.Affichage()
            

            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setMinimumSize(200,200)
            scroll.setMaximumSize(400,400)
            scroll.setWidget(widget)
            Layout_taskbox.addWidget(scroll,i,z)
            if z == 1 :
                i+=1
                j-=2
            
            j += 1
            z = j % 2
            


                
        self.AfficherFenetre()
        self.Layout_relais.addLayout(Layout_taskbox)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        pixmap = QPixmap(os.path.join(parent_dir, "View/MainWindow/static/test.jpg"))
        painter.drawPixmap(self.rect(), pixmap)

