from PySide6.QtGui import (QTextCursor)
from PySide6.QtGui import (QCloseEvent)
from PySide6.QtWidgets import (QMainWindow, QMessageBox, QDialog)

from views import Ui_MainWindow, IpDialog

class ViewMain(QMainWindow, Ui_MainWindow, IpDialog):
    def __init__(self, parent=None) -> None:
        # super().__init__(parent=parent)
        super().__init__()
        self.setupUi(self)
        self.lineEdit_username.setText("tianbot")
        self.lineEdit_password.setText("ros")
        self.lineEdit_transfer_path.setText("./Desktop")
        self.lineEdit_ip_subnet.setText("192.168.0.0/255")

    def update_log_messgae(self,message):
        """
            滑块日志组件：向文本编辑器中添加日志信息

            Args:
                text_edit: 文本编辑器
                message: 日志信息
        """
        self.text_edit_log.append(message)
        self.text_edit_log.moveCursor(QTextCursor.End)

    def show_info_message(self, message):
        """
            dump a console to show message
        """
        QMessageBox.information(self, "信息", message)

    
    def show_ip_list_dialog(self, ip_list):
        """
            show and verify the ip in list
        """
        dialog = IpDialog(ip_list)
        if dialog.exec_() == QDialog.Accepted:
            return dialog.get_selected_ips()
        return []
    
    def progess_bar_update(self, result_list):

        # get the length of progress_bar
        current_length = len(result_list)
        self.progressBar_transform.setMaximum(len(ip_list))

        # calc the value of progress follow the result modify
        progress_value = int((current_length / len(result_list)) * 100)
        
        # update the progress value
        self.progressBar_transform.setValue(progress_value)

    def closeEvent(self, event: QCloseEvent) -> None:
        """
        重写 closeEvent() 方法，在点击窗口 X 按钮时停止并退出程序
        """
        print("关闭窗口...")
        # 停止程序
        QMainWindow.close(self)

        # 接受关闭事件
        event.accept()
        
