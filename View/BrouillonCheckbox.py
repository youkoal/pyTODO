import sys
from PySide6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel, QVBoxLayout


class CountingSelectedCheckboxes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Counting selected checkboxes')
        self.resize(800, 1000)

        main_layout = QVBoxLayout()

        self.checked_boxes = []

        for i in range(5):
            self.checkbox_name = QCheckBox(f'checkbox_{i + 1}')
            self.checkbox_name.stateChanged.connect(self.update_count)
            self.checked_boxes.append(self.checkbox_name)

        for cb in self.checked_boxes:
            main_layout.addWidget(cb)

        self.label = QLabel()

        main_layout.addWidget(self.label)

        self.setLayout(main_layout)

    def update_count(self):
        count = sum(cb.isChecked() for cb in self.checked_boxes)
        self.label.setText(f'Selected: {count}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CountingSelectedCheckboxes()
    window.show()
    app.exec()