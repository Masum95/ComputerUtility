import os
import sys
from subprocess import call
from utils import get_files_list_in_directory


class FolderManager:
    def __init__(self, absolute_path):
        self.absolute_path = absolute_path
        self.files = get_files_list_in_directory(self.absolute_path)
        print(self.absolute_path,  len(self.files))

    def get_file_list(self):
        return self.files
    
    def delete_files(self, lst):
        for fle in lst:
            os.system(f'rm -rf {fle}')
    
    def delete_files_except(self, lst):
        # lst1 = [w.split('.')[0] for w in self.files]
        # lst2 = [w.split('.')[0] for w in lst]

        # files_to_delete = list(set(lst1) - set(lst2))
        # print(lst1, lst2)
        # print(len(files_to_delete))
        # files_to_delete = [w+".jpg" for w in files_to_delete]
        # print(files_to_delete)
        files_to_delete = list(set(self.files) - set(lst))
  
        self.delete_files(files_to_delete)
    
