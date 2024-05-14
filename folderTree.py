# Import module
import os
import json
import logging
from dotenv import dotenv_values
 
# Assign root
configs = dotenv_values('./path.env')
root = configs["ROOT"]

folderMap = {}
fileMap = {}

def create_item_maps(root : str) -> None:
    """Create the dict objects that will store the names as keys 
    and a list of all the paths related to it as values.
    For exemples if two files has the same name, their
    paths will be contained in a array which with their name as value.

    Args:
        root (str): starting directory for the creation od the dicts.
    """
    
    if os.path.isfile(root):
        return
        
    for item_name in os.listdir(root):
        
        # we don't want .git/* 
        if item_name.startswith('.git') or item_name.startswith('venv'):
            continue
        
        current_item_path = "{0}/{1}".format(root, item_name)
        
        # it is a file
        if os.path.isfile(current_item_path):
            
            if fileMap.get(item_name):
                fileMap[item_name].append(current_item_path)
            else:
                fileMap[item_name] = [current_item_path]
        
        # it is a directory
        elif folderMap.get(item_name):
            folderMap[item_name].append(current_item_path)
        else:
            folderMap[item_name] = [current_item_path]
        
        # reccursion over all items
        create_item_maps(current_item_path)
        
    return

if __name__ == "__main__":
    
    create_item_maps(root)
    with open(configs["FOLDER_DATA_PATH"], 'w') as file:
        json.dump(folderMap, file)
    
    with open(configs["FILE_DATA_PATH"], 'w') as file:
        json.dump(fileMap, file)