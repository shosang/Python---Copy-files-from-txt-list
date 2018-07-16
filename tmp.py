# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:30:38 2018

@author: SH
"""

import shutil
import os

path = "C:\\path\\"
source = os.listdir(path)
destination = "C:\\new_path\\"      
        
text_file = open("C:\\file_location\\files.txt", "r")
lines = text_file.readlines()
text_file.close()
for line in lines:
    line = line[:-1]
    file = os.path.join(path, line)
    try:
        shutil.copy(file,destination) 
    except EnvironmentError:
        print(line)




