# Import module
import os
import logging
from utils.save_data import save_data
from dotenv import dotenv_values # type: ignore
 
@save_data
def create_item_maps():
    """Create the dict objects that will store the names as keys 
    and a list of all the paths related to it as values.
    For exemples if two files has the same name, their
    paths will be contained in a array which with their name as value.

    Args:
        root (str): starting directory for the creation od the dicts.
    """
    
    configs = dotenv_values('./path.env')
    root = configs["ROOT"] 
    folderMap = {}
    fileMap = {}
    
    def reccur(root):
        """Recursion for the data creation
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
                
                # we remove the extensions
                if item_name.startswith('.'): #special files
                    item_name_= "." + "".join(item_name.split('.')[1])
                else:
                    item_name_= "".join(item_name.split('.')[0])
                
                
                # we store the parent foldr of each file
                if fileMap.get(item_name_):
                    fileMap[item_name_].append(current_item_path[:-len(item_name)-1])
                else:
                    fileMap[item_name_] = [current_item_path[:-len(item_name)-1]]
            
            # it is a directory
            elif folderMap.get(item_name):
                folderMap[item_name].append(current_item_path)
            else:
                folderMap[item_name] = [current_item_path]
            
            # reccursion over all items
            reccur(current_item_path)
        return
       
    reccur(root)
    return folderMap, fileMap

if __name__ == "__main__":
    
    create_item_maps()