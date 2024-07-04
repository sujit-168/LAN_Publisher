from PySide6.QtWidgets import QDialog, QListWidget, QListWidgetItem, QVBoxLayout, QDialogButtonBox
from PySide6.QtGui import QShortcut
from PySide6.QtCore import Qt

class IpDialog(QDialog):
    def __init__(self, ip_list):
        super().__init__()

        self.ip_list = ip_list
        self.selected_ips = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("选择 IP 地址")
        self.resize(300, 200)

        self.list_widget = QListWidget()
        for ip in self.ip_list:
            item = QListWidgetItem(ip)
            item.setCheckState(Qt.Checked)
            self.list_widget.addItem(item)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.list_widget)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.shortcut = QShortcut(Qt.Key_Enter, self)
        self.shortcut.activated.connect(self.accept)

        self.setLayout(self.layout)

    def accept(self):
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if item.checkState() == Qt.Checked:
                self.selected_ips.append(item.text())

        super().accept()

    def get_selected_ips(self):
        return self.selected_ips