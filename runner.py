#!/usr/bin/env python3

from folderManager import FolderManager
import os
import subprocess


cur_folder = subprocess.check_output('pwd').decode('ascii').strip()
print(cur_folder)
folder_to_edit = FolderManager(cur_folder)