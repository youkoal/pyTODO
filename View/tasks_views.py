from PySide6.QtWidgets import QWidget, QHBoxLayout,QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap
from Models.taskbox import taskbox
from Models.one_task import one_task
import sys,os
from utils.svgUtility import *

static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'MainWindow/static/'))
circle_icon = os.path.join(static_dir, 'icons/circle.min.svg')
checkcircle_icon = os.path.join(static_dir, 'icons/circle.min.svg')
# circle_icon = circle_icon.replace('\\', '/')  # Ensure the path is in the correct format for Qt  
print(circle_icon)
sys.path.append(static_dir)


def create_task_view(task):
    # Create a QWidget to represent the task
    task_widget = QWidget()
    task_layout = QHBoxLayout()
    check_icon = svg_to_colored_pixmap(checkcircle_icon, (18, 18), "green") if task.task_status else svg_to_colored_pixmap(circle_icon, (18, 18), "blue")
    check_icon_label = QLabel()
    check_icon_label.setPixmap(check_icon)
    check_icon_label.setStyleSheet("width:18px;margin:0;padding:0;border:0;")  # Add some space between icon and text
    check_icon_label.setFixedSize(18, 18) #thx copilote

    # Create a QLabel for the task title
    tasklabel = QLabel("<b>" + task.task_name + "</b><br>" + task.task_description)

    tasklabel.setStyleSheet("padding: 5px; color: black; border: 0; margin: 0;")
    tasklabel.setWordWrap(True)
    task_layout.addWidget(check_icon_label)
    task_layout.addWidget(tasklabel)

    # Set the layout for the task widget
    task_widget.setLayout(task_layout)
    task_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum) # thx Copilot

    return task_widget


def create_taskbox_view(taskbox):
    # Create a QWidget to represent the task box
    taskbox_widget = QWidget()
    taskbox_layout = QVBoxLayout()

    taskbox_title = QLabel("<h3>" + taskbox.get_title() + "</h3>")
    taskbox_title.setStyleSheet("padding: 5px; color: black; border: 0; margin: 0;")
    taskbox_title.setWordWrap(True)
    taskbox_title.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
    taskbox_layout.addWidget(taskbox_title)

    # add a separator between todo and done tasks
    separator = QLabel("<b><hr/></b>")
    separator.setStyleSheet("margin: 0;padding: 0; color: black; border: 0;")
    separator.setWordWrap(True)
    separator.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
    taskbox_layout.addWidget(separator)

    for task in taskbox.get_tasks_todo():
        task_view = create_task_view(task)
        taskbox_layout.addWidget(task_view)


    # add a separator between todo and done tasks
    separator = QLabel("<b><hr/></b>")
    separator.setStyleSheet("margin: 0;padding: 0; color: white; border: 0;")
    separator.setWordWrap(True)
    separator.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
    taskbox_layout.addWidget(separator)


    for task in taskbox.get_tasks_done():
        task_view = create_task_view(task)
        taskbox_layout.addWidget(task_view)

    taskbox_widget.setLayout(taskbox_layout)
    taskbox_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

    return taskbox_widget