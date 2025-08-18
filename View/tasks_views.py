from PySide6.QtWidgets import QWidget, QHBoxLayout,QVBoxLayout, QLabel, QSizePolicy, QFormLayout, QGroupBox, QLineEdit, QPushButton
from PySide6.QtGui import QPixmap
from Models.taskbox import taskbox
from Models.one_task import one_task
import sys,os
from utils.svgUtility import *

static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'MainWindow/static/'))
circle_icon = os.path.join(static_dir, 'icons/circle.min.svg')
checkcircle_icon = os.path.join(static_dir, 'icons/check_circle.min.svg')
# circle_icon = circle_icon.replace('\\', '/')  # Ensure the path is in the correct format for Qt  
print(circle_icon)
sys.path.append(static_dir)


def create_task_view(task):
    # Create a QWidget to represent the task
    task_widget = QWidget()
    task_layout = QHBoxLayout()
    check_icon = svg_to_colored_pixmap(circle_icon, (18, 18), "#30a141") if task.task_status else svg_to_colored_pixmap(checkcircle_icon, (18, 18), "#6F1D1B")
    check_icon_label = QLabel()
    check_icon_label.setPixmap(check_icon)
    check_icon_label.setStyleSheet("width:18px;margin:0;padding:0;border:0;")  # Add some space between icon and text
    check_icon_label.setFixedSize(18, 18) #thx copilote

    # Create a QLabel for the task title
    tasklabel = QLabel("<b>" + task.task_name + "</b><br>" + task.task_description)

    # tasklabel.setStyleSheet("padding: 5px; color: white; border: 0; margin: 0;")
    tasklabel.setStyleSheet("border: 0;")
    tasklabel.setWordWrap(True)
    task_layout.addWidget(check_icon_label)
    task_layout.addWidget(tasklabel)

    # Set the layout for the task widget
    task_widget.setLayout(task_layout)
    task_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum) # thx Copilot

    return task_widget


def create_taskbox_view(taskboxes,taskbox):
    # Create a QWidget to represent the task box
    taskbox_widget = QWidget()
    taskbox_layout = QVBoxLayout()

    insert_task_form = insert_task_form_view(taskboxes, taskbox)

    taskbox_title = QLabel("<h2>" + taskbox.get_title() + "</h2>")
    taskbox_title.setStyleSheet("padding: 5px; border: 0; margin: 0;")
    taskbox_title.setWordWrap(True)
    taskbox_title.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
    taskbox_layout.addWidget(taskbox_title)

    # add a separator between todo and done tasks
    separator = QLabel("<b><hr/></b>")
    separator.setStyleSheet("margin: 0;padding: 0; color: #FFE6A7; border: 0; font-size: 14px;")
    separator.setWordWrap(True)
    separator.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
    taskbox_layout.addWidget(separator)
    taskbox_layout.addWidget(insert_task_form)


    todo = taskbox.get_tasks_todo()
    if len(todo) > 0:
        # add a separator between todo and done tasks
        separator = QLabel("<b><hr/></b>")
        separator.setStyleSheet("margin: 0;padding: 0; color: #FFE6A7; border: 0; font-size: 14px;")
        separator.setWordWrap(True)
        separator.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        taskbox_layout.addWidget(separator)

    for task in todo:
        task_view = create_task_view(task)
        task_view.setStyleSheet("background-color: #FFE6A7; color: #432818; border: 2px solid #BB9457;padding: 5px; margin: 0; font-size: 14px;")
        taskbox_layout.addWidget(task_view)


    done = taskbox.get_tasks_done()
    if len(done) > 0:
        # add a separator between todo and done tasks
        separator = QLabel("<b><hr/></b>")
        separator.setStyleSheet("margin: 0;padding: 0; color: #FFE6A7; border: 0; font-size: 14px;")
        separator.setWordWrap(True)
        separator.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        taskbox_layout.addWidget(separator)


    for task in done:
        task_view = create_task_view(task)
        task_view.setStyleSheet("background-color: #BB9457; color: #432818; border: 2px solid #FFE6A7;padding: 5px; margin: 0; font-size: 14px;")
        taskbox_layout.addWidget(task_view)

        

    taskbox_widget.setLayout(taskbox_layout)
    taskbox_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

    return taskbox_widget


def insert_task_form_view(taskboxes,taskbox):

    input_wrapper = QWidget()
    new_task_widget = QWidget()
    layout = QFormLayout()
    new_task_widget.setLayout(layout)

    new_task_groupbox = QGroupBox('Personal Information')
    form_layout = QFormLayout()
    new_task_groupbox.setLayout(form_layout)

    Task_title_input = QLineEdit(new_task_groupbox)
    form_layout.addRow('Tache:', Task_title_input)

    Task_description_input = QLineEdit(new_task_groupbox)
    form_layout.addRow('Description:', Task_description_input)

    layout.addWidget(new_task_groupbox)
    btn = QPushButton('+')
    btn.clicked.connect(lambda: add_task_to_taskbox(taskboxes,taskbox, Task_title_input.text(), Task_description_input.text()))
    layout.addWidget(btn)


    return new_task_widget

def add_task_to_taskbox(taskboxes, taskbox, task_name, task_description):
    task = one_task(task_name, task_description)
    taskbox.add_new_task(task)
    taskboxes.save_json()