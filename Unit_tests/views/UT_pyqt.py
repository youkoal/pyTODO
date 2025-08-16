import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)

from utils.svgUtility import *


def main():
	app = QApplication(sys.argv)
	window = QMainWindow()
	window.setWindowTitle("SVG Viewer Test")
	central_widget = QWidget()
	layout = QVBoxLayout(central_widget)

	svg_path = os.path.abspath(os.path.join(parent_dir, 'View/MainWindow/static/icons/add.svg'))
	size = (200, 200)
	color = "green"  # You can use any color name or hex code
	pixmap = svg_to_colored_pixmap(svg_path, size, color)

	label = QLabel()
	label.setPixmap(pixmap)
	layout.addWidget(label)

	window.setCentralWidget(central_widget)
	window.resize(300, 300)
	# Set gray background
	window.setStyleSheet("background-color: #888888;")
	window.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()
