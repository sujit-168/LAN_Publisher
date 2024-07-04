import zipfile
import time, os

def zip_files(file_name, file_list):
    """
        zip the file of file_list with the file_name and timestamp 
    """
    if not file_name:
        return (f"please enter the file name expected!")
    zip_filename = f"{file_name}-{time.strftime('%Y-%m-%d%-H%M%S', time.localtime())}.zip"

    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file_path in file_list:
            if os.path.exists(file_path):
                _add_to_zip(zipf, file_path)
            else:
                return (f"{file_path} does not exist!")
    return (f"{zip_filename} has been created!")


def _add_to_zip(zipf, file_path):
    """
        add the file or folder (recursively) to zipfile
    """
    if os.path.isfile(file_path):
        # if it's a file, not a folder
        zipf.write(file_path, os.path.basename(file_path))
    elif os.path.isdir(file_path):
        # if it's a folder, add its content to zip recursively
        for root, dirs, files in os.walk(file_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.realpath(file_path, file_path))