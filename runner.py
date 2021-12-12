#!/usr/bin/env python3

from folderManager import FolderManager
import os
import subprocess


cur_folder = subprocess.check_output('pwd').decode('ascii').strip()
print(cur_folder)
folder_to_edit = FolderManager(cur_folder)

folder_ref = FolderManager(cur_folder+"/Dhaka_Reception")

folder_to_edit.delete_files_except(folder_ref.get_file_list())