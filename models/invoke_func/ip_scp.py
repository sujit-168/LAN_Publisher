import paramiko,os
from scp import SCPClient

def upload_to_remote_scp(host, port, username, password, local_paths, remote_path):
    """
    将文件或文件夹上传到远程服务器

    Args:
        host: 远程服务器 IP 地址
        port: 远程服务器端口号
        username: 远程服务器用户名
        password: 远程服务器密码
        local_path: 本地文件或文件夹路径
        remote_path: 远程服务器目标路径
    """

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_client.connect(host, port, username, password)

        scp_client = SCPClient(ssh_client.get_transport())

        def upload_file(local_path, remote_path):
            if os.path.isfile(local_path):
                scp_client.put(local_path, remote_path)
                print(f"文件 {local_path} 上传成功")
            elif os.path.isdir(local_path):
                scp_client.put(local_path, remote_path, recursive=True)
                print(f"文件夹 {local_path} 上传成功")
            else:
                print(f"{local_path} 不是文件或文件夹")

        if type(local_paths) == list:
                for local_path in local_paths:
                    upload_file(local_path, remote_path)
        else:
            upload_file(local_paths, remote_path)
        return True
    except Exception as e:
        print(f"{local_path} 上传失败：{e}")
        return False
    finally:
        ssh_client.close()


if __name__ == "__main__":
    # 服务器信息
    host = "192.168.0.105"
    port = 22
    username = "tianbot"
    password = "ros"
    local_dirs = []

    # 本地文件/文件夹路径
    local_path = "/home/tianbot/Downloads/dellaert-2021-factor-graphs-exploiting-structure-in-robotics.pdf"
    local_dir = "/home/tianbot/tianbot_ws/src/tianracer/tianracer_gazebo"
    local_dirs.append(local_dir)

    # 远程服务器目标路径
    remote_path = "/home/tianbot/Desktop/dellaert-2021-factor-graphs-exploiting-structure-in-robotics.pdf"
    remote_dir = "/home/tianbot/Desktop/"

    # 上传文件
    upload_to_remote_scp(host, port, username, password, local_path, remote_path)

    # 上传文件夹
    upload_to_remote_scp(host, port, username, password, local_dirs, remote_dir)
