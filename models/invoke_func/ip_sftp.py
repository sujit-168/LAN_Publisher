import pysftp
import time, os

def upload_to_remote_sftp(host, username, password, local_paths, remote_path):
    """
    使用 pysftp 发送文件夹或文件到目标主机

    Args:
        host: 目标主机的 IP 地址
        username: 目标主机的用户名
        password: 目标主机的密码
        local_path: 要发送的文件夹的本地路径
        remote_path: 要发送的文件夹的目标路径
    """
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  # Disable host key checking (not recommended for production)

    # Retry parameters
    max_retries = 3
    retry_delay = 2

    for attempt in range(0, max_retries + 1):
        try:
            with pysftp.Connection(host, username=username, password=password, cnopts=cnopts, timeout=10) as sftp:
                sftp.chdir(remote_path)

                for local_path in local_paths:
                    if os.path.isfile(local_path):
                        sftp.put(local_path, remotepath=local_path)
                        print(f"文件 {local_path} 上传成功")
                    elif os.path.isdir(local_path):
                        sftp.put(local_path, remotepath=local_path)
                        print(f"文件夹 {local_path} 上传成功")
                    else:
                        print(f"{local_path} 不是文件或文件夹")

            print(f"File uploaded to {host} via SFTP.")
            return True

        except pysftp.ConnectionException as ce:
            print(f"Connection attempt {attempt} failed: {ce}")
            if attempt < max_retries:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                raise ConnectionError("Connection failed after retries.")

        except Exception as e:
            print(f"Error: {e}")
            raise

if __name__ == "__main__":
    host = "192.168.1.100"
    username = "user"
    password = "password"

    # 发送文件
    local_path = "/path/to/file.txt"
    remote_path = "/home/user/file.txt"
    upload_to_remote_sftp(host, username, password, local_path, remote_path)

    # 发送文件夹
    local_path = "/path/to/folder"
    remote_path = "/home/user/folder"
    upload_to_remote_sftp(host, username, password, local_path, remote_path)