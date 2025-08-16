import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

#from pyTODO.Models.one_task import one_task
from Models.one_task import one_task
from Models.taskbox import taskbox


une_tache = one_task("Un nom","Essai de la tache sur un UT")
a = une_tache.get_index()
print(a)

une_tache.print_console(20,True)


