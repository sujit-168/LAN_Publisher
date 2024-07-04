# -*- coding: utf-8 -*-
# controller_main.py

import os
from PySide6.QtWidgets import  QFileDialog, QMessageBox

from views import ViewMain
from models import ModelMain

class ControllerMain:

    def __init__(self):
        self.view = ViewMain()
        self.model = ModelMain()

        # show UI
        self.view.show()

        # bind button event
        self.view.pushButton_scan_ip.clicked.connect(self.scan_ip_list_operate)
        self.view.pushButton_save.clicked.connect(self.save_ip_list_operate)

        self.view.pushButton_add.clicked.connect(self.add_file_operate)
        self.view.pushButton_del.clicked.connect(self.del_file_operate)
        
        self.view.pushButton_zip.clicked.connect(self.zip_files_operate)
        self.view.pushButton_send.clicked.connect(self.send_files_operate)

        self.model.target_ip_subnet = self.view.lineEdit_ip_subnet.text()
        self.model.username = self.view.lineEdit_username.text()

    def add_file(self):
        """
            add file or folder in ListItem
        """

        file_paths, _ = QFileDialog.getOpenFileNames(
            self.view, "Select Files or Folders to Zip", "", "All Files (*)"
        )
        for file_path in file_paths:
            if os.path.isfile(file_path):
                file_name = os.path.basename(file_path)
                self.view.listWidget_file.addItem(file_name)
                self.model.file_list.append(file_path)
            elif os.path.isdir(file_path):
                for root, dirs, files in os.walk(file_path):
                    for file in files:
                        full_file_path = os.path.join(root, file)
                        file_name = os.path.basename(full_file_path)
                        self.view.listWidget_file.addItem(file_name)
                        self.model.file_list.append(full_file_path)
            self.view.update_log_messgae(f"已添加 {file_paths[-1]} 成功！")

    def add_folder(self):
        """
            add file or folder in ListItem
        """

        dir_path = QFileDialog.getExistingDirectory(
            self.view, "Select Directory to Zip", "", QFileDialog.ShowDirsOnly
        )
        if dir_path:
            for file in os.listdir(dir_path):
                full_file_path = os.path.join(dir_path, file)
                file_name = os.path.basename(full_file_path)
                self.view.listWidget_file.addItem(file_name)
                self.model.file_list.append(full_file_path)
            self.view.update_log_messgae(f"已添加 {dir_path} 成功！")
    
    def add_file_operate(self):
        reply = QMessageBox.question(
            self.view,
            "文件类型选择",
            "确定需要添加文件夹吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.add_folder()
        else:
            self.add_file()


    def del_file_operate(self):
        """
            delete file or folder in ListItem
        """

        selected_indices = self.view.listWidget_file.selectedIndexes()
        if not selected_indices:
            return

        reply = QMessageBox.question(
            self.view,
            "确认删除",
            "确定要删除选定的文件/文件夹吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            for index in selected_indices[::-1]:  # Iterate in reverse to avoid index issues
                self.view.listWidget_file.takeItem(index.row())
                del self.model.file_list[index.row()]
                self.view.update_log_messgae(f"已删除所选文件！")
    
    def zip_files_operate(self):
        self.view.update_log_messgae(f"正在压缩文件...")
        self.model.zip_butt_event()
        self.view.update_log_messgae(f"已压缩成功！")

    def send_files_operate(self):
        self.model.username = self.view.lineEdit_username.text()
        self.model.password = self.view.lineEdit_password.text()
        self.model.transfer_path = self.view.lineEdit_transfer_path.text()
        if self.model.username and \
            self.model.password and \
            self.model.transfer_path:
            self.model.send_butt_event(self.model.avai_ip_list, self.model.file_list)
            self.display_progress_bar_operate(self.model.avai_ip_list)
            self.view.progressBar_transform.setValue(self.view.progressBar_transform.maximum())
            self.view.update_log_messgae(f"已发送完成！")
        else:
            self.view.show_info_message(f"请输入用户名！")

    def scan_ip_list_operate(self):
        self.model.target_ip_subnet = self.view.lineEdit_ip_subnet.text()
        if self.model.target_ip_subnet:
            self.model.scan_ip_event()
            self.view.update_log_messgae(f"已扫描 ip 成功！")
        else:
            self.view.show_info_message(f"请输入 IP 网段！")
        
    def save_ip_list_operate(self):
        if len(self.model.avai_ip_list) > 0 :
            self.model.avai_ip_list = self.view.show_ip_list_dialog(self.model.avai_ip_list)
            self.view.update_log_messgae(f"已保存 ip 列表成功！")
        else:
            self.view.show_info_message(f"请输入 IP 网段或检查网络环境！")

    def display_progress_bar_operate(self, host_list):
        
        # get the length of progress_bar
        bar_length = len(host_list)
        self.view.progressBar_transform.setMaximum(bar_length)

        # calc the value of progress follow the result modify
        progress_value = int((bar_length / bar_length) * 100)
        
        # update the progress value
        self.view.progressBar_transform.setValue(progress_value)