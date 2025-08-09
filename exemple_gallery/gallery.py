import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
#from __future__ import annotations

"""PySide6 port of the widgets/gallery example from Qt v5.15"""

import sys

from PySide6.QtWidgets import QApplication
from exemple_gallery.widgetgallery import WidgetGallery


if __name__ == '__main__':
    app = QApplication()
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec())