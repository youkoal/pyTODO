import sys
import os
from PySide6.QtWidgets import QApplication

from View.Interface import MaFenetre



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MaFenetre()
    myWindow.show()
    sys.exit(app.exec())