# Model (main_model.py)
from functools import partial
import os
from collections import defaultdict
from PySide6.QtCore import (QObject, QRunnable, QThreadPool, Signal)

from models.invoke_func.ip_scp import upload_to_remote_scp
from models.invoke_func.ip_sftp import upload_to_remote_sftp
from models.invoke_func.scan_ip import scan_ip
from models.invoke_func.zip_files import zip_files

class Signals(QObject):
    completed = Signal()

flag = True

class WorkerRunnable(QRunnable):

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.status_signal = kwargs.get('status_signal')
        self.result = None

    def run(self):
        if not self.args:
            self.result = self.func()
        while flag:
            self.result = self.func(*self.args)

    def win_run(self):
        res = self.func(*self.args)
        self.status_signal.emit({'status': res})

class ModelMain(QObject):
    win_status_signal: Signal = Signal(dict)
    
    def __init__(self):
        super().__init__()
        self.thread_pool = QThreadPool()
        self.thread_status_map = defaultdict(bool)

        # var
        self.file_list = []
        self.username = "tianbot"
        self.password = "ros"
        self.transfer_path = "./Desktop"
        self.target_ip_subnet = "192.168.0.1/1"
        self.avai_ip_list = []
        self.send_progress = 0

        # init thread_results
        self.thread_results = {}

    def send_butt_event(self, host_list, local_paths):
        """
            使用线程池向列表中的每个 IP 发送文件
            
            Args:
                host_list: IP 地址列表
                local_path: 本地文件路径
                remote_path: 远程服务器目标路径

            Returns:
                一个列表，包含每个 IP 的发送状态
                a list
        """
        self.thread_pool.setMaxThreadCount(len(host_list))

        results = []

        for host in host_list:
            task = WorkerRunnable(
                upload_to_remote_scp,
                host, 22, self.username, self.password, local_paths, self.transfer_path,
                status_signal=self.win_status_signal
            )

            # 将任务的返回值存储到字典中
            task.status_signal.connect(partial(self.thread_results.__setitem__, host))
            print(f"{host} 任务已添加到线程池")
            print(f"{host} 任务状态：{task.status_signal}")
            print(f"{host} 任务状态：{task.result}")
            self.thread_pool.start(task.win_run)

    def calc_the_progress(self, data):
        """
            calc the progress of the task
        """
        # calc the value of progress follow the result modify

        self.send_progress += 1
    
    def scan_ip_event(self):
        """
            scan all ip in local area
        """

        self.avai_ip_list = scan_ip(self.target_ip_subnet)

    def zip_butt_event(self, local_paths):
        """
            zip files in file_list[]
        """
        zip_files(file_name="001", file_list=local_paths)
