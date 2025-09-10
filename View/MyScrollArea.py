from PySide6.QtWidgets import QScrollArea
from PySide6.QtGui import QPainter, QPixmap
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class MyScrollArea_TD(QScrollArea):
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        pixmap = QPixmap(os.path.join(parent_dir, "View/MainWindow/static/LofyWorking2.jpg"))
        if not pixmap.isNull():
            painter.drawPixmap(self.viewport().rect(), pixmap)


class MyScrollArea_Done(QScrollArea):
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        pixmap = QPixmap(os.path.join(parent_dir, "View/MainWindow/static/LofiDone.jpg"))
        if not pixmap.isNull():
            painter.drawPixmap(self.viewport().rect(), pixmap)