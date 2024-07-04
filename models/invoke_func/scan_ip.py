import socket
import threading
import subprocess
from struct import pack, unpack

import ctypes
libgcc_s = ctypes.CDLL('libgcc_s.so.1')

def scan_ip(ip_range):
    """
    扫描指定网段下所有可用 IP 地址

    Args:
        ip_range: 网段地址，例如 "192.168.1.0/24"

    Returns:
        一个列表，包含所有可用 IP 地址
    """


    # 将网段地址转换为 IP 和掩码
    ip, mask = ip_range.split("/")

    # 计算网段内所有 IP 地址的起始 IP 和结束 IP
    start_ip = int(ip.split(".")[-1])
    end_ip = int(mask.split(".")[-1])
    ip_head = ".".join(ip.split(".")[:-1])

    print(f"starting to scan from {ip_head}.{start_ip} to {ip_head}.{mask}!")

    # 创建待检测 IP 地址列表
    ip_list = [f"{ip_head}.{i}" for i in range(start_ip + 1, end_ip + 1)]

    # 使用多线程进行扫描
    available_ips = []
    threads = []
    lock = threading.Lock()

    def scan_thread(ip):
        """
        扫描单个 IP 地址

        Args:
            ip: IP 地址
        """

        try:
            # 使用 ICMP 协议探测 IP 地址是否可用
            response = subprocess.check_output(
                ["ping", "-c", "1", "-W", "3", str(ip)],
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
            if "bytes from" in response:
                with lock:
                    available_ips.append(ip)
        except subprocess.CalledProcessError:
            pass

    for ip in ip_list:
        thread = threading.Thread(target=scan_thread, args=(ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return available_ips

if __name__ == "__main__":
    ip_range = "192.168.0.0/255"
    available_ips = scan_ip(ip_range)
    print(f"available_ips: {available_ips}, \nThe available IP {len(available_ips)} in total!")