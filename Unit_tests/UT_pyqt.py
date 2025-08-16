import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtSvgWidgets import QSvgWidget
import os

def main():
	app = QApplication(sys.argv)
	window = QMainWindow()
	window.setWindowTitle("SVG Viewer Test")
	central_widget = QWidget()
	layout = QVBoxLayout(central_widget)

	# Path to the SVG icon
	svg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../View/MainWindow/static/icons/add.svg'))

	svg_widget = QSvgWidget(svg_path)
	svg_widget.setFixedSize(200, 200)
	# Set the style to make the SVG appear white
	svg_widget.setStyleSheet("background: transparent; color: white;")
	layout.addWidget(svg_widget)

	window.setCentralWidget(central_widget)
	window.resize(300, 300)
	window.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()
