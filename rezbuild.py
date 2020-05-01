
import os
import shutil


def build(source_path, build_path, install_path, targets):
    destination_folder = os.path.join(build_path, 'python')

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.copyfile(
        os.path.join(source_path, 'Qt.py'),
        os.path.join(destination_folder, 'Qt.py'))

