import sys
import os

from PySide6.QtWidgets import QApplication
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from View.Interface_2 import MaFenetre



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MaFenetre()
    myWindow.show()
    sys.exit(app.exec())