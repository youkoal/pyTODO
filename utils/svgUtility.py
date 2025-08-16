from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import Qt


def svg_to_colored_pixmap(svg_path, size, color):
	""" Make it easy to change SVG colors """
	renderer = QSvgRenderer(svg_path)
	pixmap = QPixmap(size[0], size[1])
	pixmap.fill(Qt.GlobalColor.transparent)
	painter = QPainter(pixmap)
	renderer.render(painter)
	painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
	painter.fillRect(pixmap.rect(), QColor(color))
	painter.end()
	return pixmap