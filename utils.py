#!/usr/bin/env python3

import os
import sys
from subprocess import call
import subprocess
import shlex

def getCommandOutput(comd):
  return subprocess.check_output(shlex.split(comd)).decode('ascii').strip()

def get_files_list_in_directory(folder_path):
  files_list = getCommandOutput(f'ls {folder_path}').split('\n')
  return files_list
  # print(files_list)


# get_files_list_in_directory('/Users/masumrahman/ComputerUtility')