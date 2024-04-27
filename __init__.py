from joulescope_ui.plugins import *
from PySide6 import QtCore, QtGui, QtWidgets


@register
@styled_widget(N_('Simple Widget Example'))
class SimpleWidgetExampleWidget(QtWidgets.QWidget):

    CAPABILITIES = ['widget@']
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._layout = QtWidgets.QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.addWidget(QtWidgets.QLabel(N_('Hello World!')))

    def on_pubsub_register(self):
        pass

    def mousePressEvent(self, event):
        event.accept()
        if event.button() == QtCore.Qt.RightButton:
            menu = QtWidgets.QMenu(self)
            settings_action_create(self, menu)
            context_menu_show(menu, event)
